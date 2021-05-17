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
        return Memory.readByteArray(ptr(source_address), size);
    }
};
""")

script.load()
myagent = script.exports

read_memory_ranges = myagent.memory_ranges('r--')
readwrite_memory_ranges = myagent.memory_ranges('rw-')
execute_memory_ranges = myagent.memory_ranges('--x')

print("[READ] memory blocks:")
for r in read_memory_ranges:
    print("[{base}] size: {size}".format(base=r['base'],
                                         size=r['size']))

print("[READ/WRITE] memory blocks:")
for r in readwrite_memory_ranges:
    print("[{base}] size: {size}".format(base=r['base'],
                                         size=r['size']))

print("[EXECUTION] memory blocks:")
for r in execute_memory_ranges:
    print("[{base}] size: {size}".format(base=r['base'],
                                         size=r['size']))


