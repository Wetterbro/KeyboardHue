# Philips Hue Light Control with Keyboard Shortcuts

This project allows you to control the brightness of your Philips Hue lights using keyboard shortcuts. The script listens for specific hotkeys and adjusts the brightness of the lights accordingly.

## Features

- Increase brightness with `Ctrl + Up Arrow`
- Decrease brightness with `Ctrl + Down Arrow`
- Automatically turn on lights when increasing brightness
- Automatically turn off lights when brightness is too low
- Exit the script with `Ctrl + Alt + Shift + E`

## Requirements

- Python 3.x
- `phue` library
- `keyboard` library

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/hue-light-control.git
    cd hue-light-control
    ```

2. **Install the required Python packages:**

    ```sh
    pip install phue keyboard
    ```

## Configuration

1. **Update the configuration variables:**

    Open `hue_light_control.py` and modify the following variables as needed:

    ```python
    BRIDGE_IP = "192.168.50.197"  # IP address of your Philips Hue bridge
    HOTKEY_UP = 'ctrl+up'         # Hotkey to increase brightness
    HOTKEY_DOWN = 'ctrl+down'     # Hotkey to decrease brightness
    EXIT_HOTKEY = 'ctrl+alt+shift+e'  # Hotkey to exit the program
    DIM_STEP = 20                 # Step to adjust the brightness
    ```

2. **Press the button on your Philips Hue bridge:**

    Before running the script for the first time, press the physical button on your Philips Hue bridge to authorize the connection.

3. **Run the script:**

    ```sh
    python hue_light_control.py
    ```

## Logging

The script logs its activity to `hue_light_control.log`. This is useful for diagnosing any issues that occur while the script is running.

## Running at Startup

### Windows

1. **Create a Shortcut:**
   - Right-click on the `hue_light_control.py` file and select "Create shortcut."
   - Move the shortcut to the "Startup" folder. You can access this folder by pressing `Win + R`, typing `shell:startup`, and hitting Enter.

2. **Edit the Shortcut:**
   - Right-click the shortcut in the "Startup" folder and select "Properties."
   - In the "Target" field, add the path to your Python executable and the path to your script. It should look something like this:
     ```
     "C:\Path\To\Python\python.exe" "C:\Path\To\Your\Script\hue_light_control.py"
     ```
   - Click "OK" to save the changes.

### macOS

1. **Create a Launch Agent:**
   - Open the Terminal and create a `.plist` file in the LaunchAgents directory:
     ```sh
     nano ~/Library/LaunchAgents/com.yourusername.huelightcontrol.plist
     ```
   - Add the following content to the file, replacing the paths with the appropriate paths to your Python executable and script:
     ```xml
     <?xml version="1.0" encoding="UTF-8"?>
     <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
     <plist version="1.0">
       <dict>
         <key>Label</key>
         <string>com.yourusername.huelightcontrol</string>
         <key>ProgramArguments</key>
         <array>
           <string>/usr/local/bin/python3</string>
           <string>/path/to/your/hue_light_control.py</string>
         </array>
         <key>RunAtLoad</key>
         <true/>
         <key>KeepAlive</key>
         <false/>
       </dict>
     </plist>
     ```
   - Save the file by pressing `Ctrl + X`, then `Y`, and then `Enter`.

2. **Load the Launch Agent:**
   - Still in the Terminal, load the new Launch Agent:
     ```sh
     launchctl load ~/Library/LaunchAgents/com.yourusername.huelightcontrol.plist
     ```

### Linux

1. **Create a Systemd Service (for systemd-based distributions):**
   - Open a terminal and create a new service file:
     ```sh
     sudo nano /etc/systemd/system/hue_light_control.service
     ```
   - Add the following content to the file, replacing the paths with the appropriate paths to your Python executable and script:
     ```ini
     [Unit]
     Description=Hue Light Control Script

     [Service]
     ExecStart=/usr/bin/python3 /path/to/your/hue_light_control.py
     Restart=always
     User=yourusername
     Environment=DISPLAY=:0

     [Install]
     WantedBy=default.target
     ```
   - Save the file by pressing `Ctrl + X`, then `Y`, and then `Enter`.

2. **Enable and Start the Service:**
   - Enable the service to start at boot:
     ```sh
     sudo systemctl enable hue_light_control.service
     ```
   - Start the service immediately:
     ```sh
     sudo systemctl start hue_light_control.service
     ```

## Usage

- **Increase brightness:** Press `Ctrl + Up Arrow`
- **Decrease brightness:** Press `Ctrl + Down Arrow`
- **Exit the script:** Press `Ctrl + Alt + Shift + E`

## Example

Here's a brief example of what you should see when running the script:

```sh
$ python hue_light_control.py
Lights connected: dict_keys(['Living Room', 'Bedroom', 'Kitchen'])
Hotkey listener started. Press Ctrl + Up Arrow or Ctrl + Down Arrow to adjust brightness.
Press Ctrl + Alt + Shift + E to exit.
