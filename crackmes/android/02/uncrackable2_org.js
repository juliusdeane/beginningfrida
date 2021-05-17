Java.perform(function(){
  var mainActivity = Java.use("sg.vantagepoint.uncrackable2.MainActivity");
  mainActivity.a.overload("java.lang.String").implementation = function(s) {
    console.log("SEE IF WE CAN CONTROL THE FUNCTION. Argument=: " + s);
  }

  mainActivity.onResume.implementation = function() {
    this.onResume();

    var theMagicWord = "12345678901234567890123";
    const strncmp_ptr = Module.findExportByName('libfoo.so', 'strncmp');
    hook_strncmp(strncmp_ptr, theMagicWord);

    // Find the CodeCheck instance that was created by the app in onCreate()
    // Then call it with the magic word as argument.
    Java.choose("sg.vantagepoint.uncrackable2.CodeCheck", {
      onMatch : function(instance) {
        instance.a(Java.use("java.lang.String").$new(theMagicWord));
        return "stop";
      },
      onComplete:function() {}
    });

    // We've got what we wanted, detach again to prevent multiple attachments
    // to strncmp if onResume is called multiple times.
    Interceptor.detachAll();
  }
});


function hook_strncmp(strncmpAddress, compareTo) {
  Interceptor.attach(strncmpAddress, {
    // strncmp takes 3 arguments, str1, str2, max number of characters to compare
    onEnter: function(args) {
      this.replace_retval = false;

      var len = compareTo.length;
      if (args[2].toInt32() != len) {
        // Definitely comparing something uninteresting, bail.
        return;
      }
      var str1 = args[0].readUtf8String(len)
      var str2 = args[1].readUtf8String(len)
      if (str1 == compareTo || str2 == compareTo) {
        console.log("strncmp(" + str1 + ", " + str2 + ", " + len + ") called");
        this.replace_retval = true;
      }
    },
    onLeave: function(retval) {
      if(this.replace_retval === true){
        retval.replace(0);
      }	    
    }
  });
}
