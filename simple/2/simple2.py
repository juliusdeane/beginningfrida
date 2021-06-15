import frida
import sys
import readchar


session = frida.attach("simple2")


script = session.create_script("""
Interceptor.attach(ptr("%s"), {
    onLeave: function(retval) {
        retval.replace(1);
    }
});
""" % sys.argv[1])
def on_message(message, data):
    print(message)
script.on('message', on_message)
script.load()

print("Press a key to detach...")
readchar.readkey()

session.detach()
print("Detached.")

