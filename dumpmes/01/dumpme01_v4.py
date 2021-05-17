import time
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
    showMe: function () {
        return Process.enumerateModules()[0];
    }
};
""")

script.load()
myagent = script.exports

read_memory_ranges = myagent.memory_ranges('r--')

print("(1) [READ] memory blocks:")
print("    [BASE] -> " + myagent.show_me()['base'])
for r in read_memory_ranges:
    print("[{base}] size: {size}".format(base=r['base'],
                                         size=r['size']))

time.sleep(10)

read_memory_ranges = myagent.memory_ranges('r--')
print("(2) [READ] memory blocks:")
print("    [BASE] -> " + myagent.show_me()['base'])
for r in read_memory_ranges:
    print("[{base}] size: {size}".format(base=r['base'],
                                         size=r['size']))

time.sleep(10)

read_memory_ranges = myagent.memory_ranges('r--')
print("(3) [READ] memory blocks:")
print("    [BASE] -> " + myagent.show_me()['base'])
for r in read_memory_ranges:
    print("[{base}] size: {size}".format(base=r['base'],
                                         size=r['size']))


