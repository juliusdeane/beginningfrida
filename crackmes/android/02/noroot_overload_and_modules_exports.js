Java.perform(function() {
    var mainActivity = Java.use("sg.vantagepoint.uncrackable2.MainActivity");

    mainActivity.a.overload("java.lang.String").implementation = function(s) {
	console.log("SEE IF WE CAN CONTROL THE FUNCTION. Argument=: " + s);
	Process.enumerateModules({
          onMatch: function(module){
		  if(module.name === 'libfoo.so') {
		    console.log("[libfoo.so] FOUND. Export list:");
		    console.log("-------------------------------");
    		    module.enumerateExports().forEach(function(item) {
                      console.log("Export: " + item.name + " (" + item.address + ")" );
                    });
		  }
          },
         onComplete: function(){}
        });
    };
});

