import frida


process_pid = frida.spawn("dumpme01")
session = frida.attach(process_pid)

script = session.create_script("""
'use strict';

rpc.exports = {
    memoryranges: function (permission_mask) {
        return Process.enumerateRangesSync(permission_mask);
    }
};
""")

script.load()
myagent = script.exports

read_memory_ranges = myagent.memoryranges('r--')

for r in read_memory_ranges:
    print("Read memory range: [{base}]".format(base=r['base']))

