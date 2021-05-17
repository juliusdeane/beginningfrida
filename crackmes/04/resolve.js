let sprintf_addr = null;
let sprintf_value = null;
const sprintf_ptr = Module.findExportByName('libc-2.31.so', 'sprintf');
const strcmp_ptr = Module.findExportByName('libc-2.31.so', 'strcmp');


function hook(function_ptr, function_actions) {
  Interceptor.attach(function_ptr, function_actions);
}


hook(sprintf_ptr,
{
  onEnter: function(args, state) {
    console.log("sprintf.onEnter:");
    this.destination_address = args[0];
  },
  onLeave:function(retval, state) {
    sprintf_addr = this.destination_address;
    sprintf_value = this.destination_address.readUtf8String();
  }
}
);

hook(strcmp_ptr,
{
    onEnter:function(args, state) {
    console.log('[*] BEFORE MANIPULATING ARGUMENTS');
    console.log(`strcmp(s1="${args[0].readUtf8String()}", s2="${args[1].readUtf8String()}")`);

    console.log('[*] sprintf_value and sprintf_addr:');
    console.log('    sprintf_addr: ' + sprintf_addr);
    console.log('    sprintf_value: ' + sprintf_value);
    args[1] = sprintf_addr;

    console.log('[*] AFTER MANIPULATING ARGUMENTS (with previous value)');
    console.log(`strcmp(s1="${args[0].readUtf8String()}", s2="${args[1].readUtf8String()}")`);
  },
  onLeave:function(retval, state) {
    // Remove the cheat here as must be resolved in OnEnter.
    // retval.replace(0);
  }
}
);
