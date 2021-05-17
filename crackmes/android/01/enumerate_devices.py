import frida, sys

all_devices = frida.enumerate_devices()
for device in all_devices:
    print(device)

# process = frida.get_usb_device('emulator-5554').attach('com.entebra.crackme0x01')

