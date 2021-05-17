import frida


process_pid = frida.spawn("dumpme01")
session = frida.attach(process_pid)

script = session.create_script("""
'use strict';

function printme() {
    console.log("PRINT ME: dumpme01");
}

rpc.exports = {
    printme: printme,
    printAgain: function(with_name) {
        console.log("PRINT ME: dumpme01 (" + with_name + ")");
    },
    printAgainAndagain: function(with_name) {
        console.log("PRINT ME (dup): dumpme01 (" + with_name + ")");
    }
};
""")

script.load()
myagent = script.exports
myagent.printme()

# Now, with parameter.
myagent.print_again("Julie")

# See convention in <lower>_
myagent.print_again_andagain("Deane")

