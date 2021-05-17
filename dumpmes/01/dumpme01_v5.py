import os
import pathlib
import frida


process_pid = frida.spawn("dumpme01")
session = frida.attach(process_pid)

script = session.create_script("""
'use strict';

rpc.exports = {
    memoryRanges: function (permission_mask) {
        return Process.enumerateRangesSync(permission_mask);
    },
    extractMemory: function (source_address, size) {
        if(!source_address){
            console.log("NO valid source_address.");
            return null;
        }

        var memoryPage = null;
        try {
            memoryPage = Memory.readByteArray(ptr(source_address), size);
        }
        catch(error){
            return null;
        }

        return memoryPage;
    }
};
""")

script.load()
myagent = script.exports

read_memory_ranges = myagent.memory_ranges('r--')
readwrite_memory_ranges = myagent.memory_ranges('rw-')
execute_memory_ranges = myagent.memory_ranges('--x')


print("[READ] memory blocks:")
counter = 0
for r in read_memory_ranges:
    block = None;
    print("({counter}) [{base}] size: {size}".format(counter=counter,
                                                     base=r['base'],
                                                     size=r['size']))
    try:
        block = myagent.extract_memory(r['base'], r['size'])
    except Exception as e:
        print("Exception when: [{base}] [{size}]".format(base=r['base'], size=r['size']))
        print("E: [%s]" % str(e))
        continue

    if block is None:
        print("    Memory block was NULL/NONE: excepted.")
    counter += 1
