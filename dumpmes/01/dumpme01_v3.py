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
        return Memory.readByteArray(ptr(source_address), size);
    }
};
""")

script.load()
myagent = script.exports

read_memory_ranges = myagent.memory_ranges('r--')
readwrite_memory_ranges = myagent.memory_ranges('rw-')
execute_memory_ranges = myagent.memory_ranges('--x')

base_path = "./output/dumpme01"

read_base_path = os.path.join(base_path, 'read')
write_base_path = os.path.join(base_path, 'write')
exec_base_path = os.path.join(base_path, 'exec')

pathlib.Path(base_path).mkdir(parents=True,
                              exist_ok=True)

pathlib.Path(read_base_path).mkdir(parents=True,
                                   exist_ok=True)

pathlib.Path(write_base_path).mkdir(parents=True,
                                    exist_ok=True)

pathlib.Path(exec_base_path).mkdir(parents=True,
                                   exist_ok=True)


print("[READ] memory blocks:")
for r in read_memory_ranges:
    output_file = os.path.join(read_base_path, r['base'])
    print("[{base}] size: {size}".format(base=r['base'],
                                         size=r['size']))

    with open(output_file, 'wb') as OUTPUT_FILE:
        OUTPUT_FILE.write(myagent.extract_memory(r['base'], r['size']))

print("[READ/WRITE] memory blocks:")
for r in readwrite_memory_ranges:
    output_file = os.path.join(write_base_path, r['base'])
    print("[{base}] size: {size}".format(base=r['base'],
                                         size=r['size']))

    with open(output_file, 'wb') as OUTPUT_FILE:
        OUTPUT_FILE.write(myagent.extract_memory(r['base'], r['size']))


print("[EXECUTION] memory blocks:")
for r in execute_memory_ranges:
    exec_base_path = os.path.join(base_path, 'exec')
    output_file = os.path.join(exec_base_path, r['base'])
    print("[{base}] size: {size}".format(base=r['base'],
                                         size=r['size']))

    with open(output_file, 'wb') as OUTPUT_FILE:
        OUTPUT_FILE.write(myagent.extract_memory(r['base'], r['size']))
