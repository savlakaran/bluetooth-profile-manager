from pystray import Icon as icon, Menu as menu, MenuItem as item
import subprocess
from connected_devices import list_connected_devices
from icon_image import get_tray_image_icon

def make_menu(connected):
    mainMenu = []
    for device in connected:
        menuItem = item(
            device['name'],
            menu(
                item('A2DP', lambda icon, item: switch_profile(device['address'], 'a2dp_sink')),
                item('HSP/HFP', lambda icon, item: switch_profile(device['address'], 'headset_head_unit'))
            )
        )

        mainMenu.append(menuItem)

    icon('BT profile manager', get_tray_image_icon(), menu = menu(*mainMenu)).run()

def switch_profile(device, profile):
    deviceName = prepare_device_name(device)
    subprocess.run(['pactl', 'set-card-profile', deviceName, profile])
    print(deviceName, profile)

def prepare_device_name(device):
    return 'bluez_card.' + device.replace(':', '_')

if __name__ == '__main__':
    connected = list_connected_devices()
    make_menu(connected)