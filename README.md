# Download File Manager 🗃️

This tool manages downloaded files automatically in the background.

## Prerequisites

*   Python 3
*   Linux environment (GNOME or XDG-compliant desktop)

## Installation

### 1. Prepare the Script

Ensure the script is in the correct location:
`YOUR_SCRIPT_PATH/download_file_manager.py`

Grant execution permissions:
```bash
chmod +x YOUR_SCRIPT_PATH/download_file_manager.py
```

### 2. Install Desktop Entry (Autostart)

To start the application automatically on login, install the `.desktop` file:

```bash
# Create the autostart directory if it doesn't exist
mkdir -p ~/.config/autostart

# Copy the desktop file
cp YOUR_SCRIPT_PATH/download_file_manager.desktop ~/.config/autostart/
```

### 3. Manual Usage

You can start the manager manually with:
```bash
/usr/bin/python3 YOUR_SCRIPT_PATH/download_file_manager.py start
```
