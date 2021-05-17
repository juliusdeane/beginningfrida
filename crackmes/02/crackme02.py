import frida


def on_message(message, data):
    print("[on_message] message:", message, "data:", data)


process_pid = frida.spawn("crackme02")
session = frida.attach(process_pid)

script = session.create_script("""
Process.enumerateModules({
    onMatch: function(module){
        console.log('Module name: ' + module.name + " (" + "Base Address: " + module.base.toString() + ")");
    },
    onComplete: function(){}
});
""")

script.on("message", on_message)
script.load()
