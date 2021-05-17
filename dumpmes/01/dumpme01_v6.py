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
            console.log("memoryPage was read! (compare with python context)");
        }
        catch(error){
            console.log("Catched error: " + error);
            console.log("  ***> try to protect and set READ permission.");

            var protect_result = Memory.protect(ptr(source_address), size, 'r--');
            if(protect_result === true){
                console.log("Memory.protect->read successful. Do read.");

                try{
                    memoryPage = Memory.readByteArray(ptr(source_address), size);
                }
                catch(second_error) {
                    memoryPage = null;
                }

                if(!memoryPage) {
                    console.log("memoryPage: is null again?.");
                }
                else {
                    console.log("memoryPage: is NOT null.");
                }

                return memoryPage;
            }
            else {
                console.log("Memory.protect->read ERROR (" + protect_result + "). Skip.");
                memoryPage = null;
            }
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
