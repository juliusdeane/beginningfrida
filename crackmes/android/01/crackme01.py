import frida, sys

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

jscode = """
Java.perform(function () {
  // owasp.mstg.uncrackable1:
  // p000sg.vantagepoint.uncrackable1.MainActivity is the entry point to the application.
  // we hook it.
  console.log("[Java.perform] Going to use MainActivity.");
  var mainActivity_hook = Java.use('p000sg.vantagepoint.uncrackable1.MainActivity');

  if(!mainActivity_hook) {
    console.log("[Java.perform] ERROR: we *do not* have MainActivity hook.:");
    throw "MainActivity not available here. ERROR.";
  }

  console.log("[Java.perform] We have MainActivity hook. Watch onCreate:");
  var onCreate = mainActivity_hook.onCreate;

  if(!onCreate) {
    console.log("[Java.perform] ERROR: we *do not have* onCreate.");
    throw "ERROR: no onCreate found.";
  }

  onCreate.implementation = function(v) {
    // console.log("[.onCreate] BEGIN");

    // console.log(v);

    // console.log("[.onCreate] END (call real handler)");
    onCreate.call(this, v);
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
else:
    print("No valid device found...")
