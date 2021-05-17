import frida


process_pid = frida.spawn("dumpme01")
session = frida.attach(process_pid)

script = session.create_script("""
'use strict';

rpc.exports = {
    printme: function () {
        console.log("PRINT ME: dumpme01");
    }
};
""")

script.load()
myagent = script.exports
myagent.printme()

