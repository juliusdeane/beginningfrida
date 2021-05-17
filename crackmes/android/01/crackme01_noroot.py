import frida, sys

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

jscode = """
Java.perform(function() {
    Java.use("sg.vantagepoint.uncrackable1.MainActivity").a.implementation = function(s) {
        console.log("SEE IF WE CAN CONTROL THE FUNCTION. Argument=: " + s);
    }
});
"""

device = None
all_devices = frida.enumerate_devices()
for dv in all_devices:
    # Device(id="emulator-5554", name="Android Emulator 5554", type='usb')
    if dv.type != 'usb':
        continue

    if dv.id == "emulator-5554":
        device = dv
        break

if device:
    process_pid = device.spawn(["owasp.mstg.uncrackable1"])
    process = device.attach(process_pid)
    script = process.create_script(jscode)
    script.on('message', on_message)

    print('[*] Hooking crackme 01! Press any key to exit...')
    script.load()
    sys.stdin.read()
else:
    print("No valid device found...")

