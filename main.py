import logging
from phue import Bridge
import keyboard
import sys

# Configuration variables
BRIDGE_IP = "192.168.50.197"
HOTKEY_UP = 'ctrl+up'
HOTKEY_DOWN = 'ctrl+down'
EXIT_HOTKEY = 'ctrl+alt+shift+e'
DIM_STEP = 20

# Setup logging
logging.basicConfig(filename='hue_light_control.log', level=logging.INFO,
                    format='%(asctime)s %(message)s')
logging.info('Script started')

try:
    # Connect to the Hue bridge
    b = Bridge(BRIDGE_IP)

    # Connect to the bridge
    b.connect()

    # Get the list of lights
    lights = b.get_light_objects('name')
    logging.info(f"Lights connected: {lights.keys()}")

    def on_hotkey_pressed(direction):
        if direction == 'up':
            for light_name, light in lights.items():
                if not light.on:
                    light.on = True
                if light.brightness < 254:
                    light.brightness += DIM_STEP
        elif direction == 'down':
            for light_name, light in lights.items():
                if light.brightness > DIM_STEP:
                    light.brightness -= DIM_STEP
                else:
                    light.on = False  # Turn off the light if brightness is too low

    def exit_program():
        logging.info("Exiting program.")
        sys.exit(0)

    # Register the hotkeys
    keyboard.add_hotkey(HOTKEY_UP, lambda: on_hotkey_pressed('up'))
    keyboard.add_hotkey(HOTKEY_DOWN, lambda: on_hotkey_pressed('down'))

    # Register the exit hotkey
    keyboard.add_hotkey(EXIT_HOTKEY, exit_program)

    logging.info("Hotkey listener started. Press Ctrl + Up Arrow or Ctrl + Down Arrow to adjust brightness.")
    logging.info("Press Ctrl + Alt + Shift + E to exit.")

    # Keep the script running to listen for the hotkey
    keyboard.wait()  # Wait for any hotkey to be pressed

except Exception as e:
    logging.error(f"An error occurred: {e}")
    sys.exit(1)
