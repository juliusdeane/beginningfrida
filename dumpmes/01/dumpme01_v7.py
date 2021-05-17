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

counter = 0
for r in read_memory_ranges:
    print("({counter}) Read memory range: [{base}] size: [{size}] perms: [{perms}]".format(counter=counter,
                                                                                           base=r['base'],
                                                                                           size=r['size'],
                                                                                           perms=r['protection']))
    counter += 1

