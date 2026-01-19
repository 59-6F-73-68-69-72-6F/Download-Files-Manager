import os
import sys
import time
import shutil
import datetime

from daemonizer import Daemon

MIN: int = 60
DIRECTORY: str = "Downloads"
LOGFILE: str = "download_files.log"
PATH: str = os.path.expanduser(f"~/{DIRECTORY}")

DIR_TYPES: dict = {
    "Images": (".jpg", ".bmp", "JPG", ".jpeg", ".png", ".gif", ".webp", ".svg", ".tiff", ".ico"),
    "Documents": (".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".pptx", ".odt", ".rtf", ".tex", ".wpd", ".wps"),
    "Archives": (".zip", ".rar", ".7z", ".tar", ".gz", ".iso", ".img"),
    "Setup_Files": (".exe", ".msi", ".deb", ".sh", ".AppImage", ".apk", ".dmg"),
    "Videos": (".mp4", ".mkv", ".avi", ".mov", ".flv", ".webm", ".mpeg", ".3gp", ".vob", ".wmv", ".m4v"),
    "Music": (".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".aiff", ".alac", ".midi"),
    "Code_Files": (".py", "pypi", ".java", ".cpp", ".html", ".css", ".php", ".js", "json", "c", "h", "cpp", "xml")
}


class DownloadManager(Daemon):
    def run(self):
        """
        This method will be called after the process has been daemonized by start() or restart().
        It contains the main logic of the download manager.
        """
        counter = 0
        while True:
            if os.path.exists(PATH):
                with os.scandir(PATH) as entries:
                    for entry in entries:
                        if not entry.is_file() or entry.name == LOGFILE:  # ignore LOGFILE and Directories
                            continue
                        for folder, ext_list in DIR_TYPES.items():
                            if entry.name.endswith(ext_list):
                                counter += 1
                                target_dir = f"{PATH}/{folder}"
                                if not os.path.exists(target_dir):  # if target Directory doesn't exist, create it
                                    os.makedirs(target_dir, exist_ok=True)
                                try:
                                    shutil.move(entry.path, f"{target_dir}/{entry.name}")
                                    with open(f"{PATH}/{LOGFILE}", "a") as f:
                                        f.write(f"{counter} - {entry.name} -  /{folder}/  -  {str(datetime.datetime.now())[:22]} \n")
                                except Exception:
                                    pass
            time.sleep(3 * MIN)


if __name__ == "__main__":
    daemon = DownloadManager('/tmp/daemon-download_manager.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print(f"usage: {sys.argv[0]} start|stop|restart")
        sys.exit(2)
