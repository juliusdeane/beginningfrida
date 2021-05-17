import frida


process_pid = frida.spawn("dumpme01")
session = frida.attach(process_pid)

script = session.create_script("""
'use strict';

rpc.exports = {
    printme: function () {
        console.log("PRINT ME: dumpme01");
    },
    printAgain: function(with_name) {
        console.log("PRINT ME: dumpme01 (" + with_name + ")");
    }
};
""")

script.load()
myagent = script.exports
myagent.printme()

# Now, with parameter.
myagent.print_again("Julie")

