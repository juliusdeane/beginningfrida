import frida

session = frida.attach("simple3")

# The invented struct we want to build:
# typedef struct my_INVENTED_STRUCT {
#     USHORT    counter;
#     ULONG    starCount;
#     ULONG    blackholeCount;
# } INVENTED_STRUCT, *INVENTED_HEADER;
script = session.create_script("""
    const INVENTED_STRUCT_SIZE = 10;
    var myStruct = Memory.alloc(INVENTED_STRUCT_SIZE);

    console.log('[myStruct] BASE address: ' + myStruct);

    myStruct.writeU16(0x0000);
    var mystruct_plus_2 = myStruct.add(0x02);
    console.log('[myStruct] BASE address: ' + mystruct_plus_2 + ' +2 bytes');

    mystruct_plus_2.writeU32(0xFE00FE00);
    var mystruct_plus_2_plus_4 = mystruct_plus_2.add(0x04);
    console.log('[myStruct] BASE address: ' + mystruct_plus_2_plus_4 + ' +6 bytes');

    mystruct_plus_2_plus_4.writeU32(0x000000fe);

    // Now read:
    var buffer_read = Memory.readByteArray(myStruct, INVENTED_STRUCT_SIZE);
    console.log(hexdump(buffer_read, {
        offset: 0,
        length: INVENTED_STRUCT_SIZE,
        header: true,
        ansi: false
    }));
""")

script.load()
session.detach()

