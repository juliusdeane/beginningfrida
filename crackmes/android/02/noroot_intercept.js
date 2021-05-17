Java.perform(function(){
  var mainActivity = Java.use("sg.vantagepoint.uncrackable2.MainActivity");

  // Firts, bypass the root check. This is trivial for us now...
  mainActivity.a.overload("java.lang.String").implementation = function(s) {
    console.log("SEE IF WE CAN CONTROL THE FUNCTION. Argument=: " + s);
  }

  // We will hook on onResume.
  mainActivity.onResume.implementation = function() {
    // Always remember to call the original function.
    // There are many ways to do so, but using this.onResumen()
    // is the simplest.
    this.onResume();

    // We already know libfoo.so and strncmp will be available.
    const strncmp_ptr = Module.findExportByName('libfoo.so', 'strncmp');
    // Important: we are starting to separate functions and code blocks
    // that we use more than once. Here we create a "hook" just passing
    // the _ptr.
    // In the next version we will make it even more general.
    hook_strncmp(strncmp_ptr);

    // For the future...
    // Interceptor.detachAll();
  }
});


// Our hooking function. Just pass the _ptr
// and we will call the Interceptor.
function hook_strncmp(strncmp_address) {
  Interceptor.attach(strncmp_address, {
    onEnter: function(args) {
      var str1 = null;
      var str2 = null;
      // Get the size passed on the call.
      var argument_size = args[2].toInt32();

      // We already know the secret and its lenght.
      // This is just to reduce overhead and exit early
      // if calling makes no sense.
      if(argument_size != 23) { 
        return;
      }

      // Just to make sure str1|2 will not break execution flow.
      try{
        str1 = args[0].readUtf8String(argument_size)
      } catch(error) {
        return;
      }

      try{
        str2 = args[1].readUtf8String(argument_size)
      } catch(error) {
        return;
      }

      this.please_replace_retval = false;

      if (str1.includes("Julius Deane") ) {
        console.log('[strncmp.onEnter] BEGIN');
        console.log('    strncmp("' + str1 + '", "' + str2 + '", ' + argument_size + ');');
        console.log('[strncmp.onEnter] END');

	this.please_replace_retval = true;
      }
    },
    onLeave: function(retval) {
      if(this.please_replace_retval === true) {
        retval.replace(0);
      }
    }
  });
}
