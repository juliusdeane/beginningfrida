Java.perform(function() {
    var mainActivity = Java.use("sg.vantagepoint.uncrackable2.MainActivity");

    mainActivity.a.overload("java.lang.String").implementation = function(s) {
	console.log("SEE IF WE CAN CONTROL THE FUNCTION. Argument=: " + s);
	Process.enumerateModules({
          onMatch: function(module){
		  if(module.name === 'libfoo.so') {
		    console.log("[libfoo.so] FOUND.");
		    console.log("[libfoo.so] Export list:");
		    console.log("-------------------------------");
    		    module.enumerateExports().forEach(function(item) {
                      console.log("Export: " + item.name + " (" + item.address + ")" );
                    });

		    console.log("[libfoo.so] Import list:");
		    console.log("-------------------------------");
    		    module.enumerateImports().forEach(function(item) {
                      console.log("Import: " + item.name + " (" + item.address + ")" );
                    });

		    console.log("[libfoo.so] Symbols list:");
		    console.log("-------------------------------");
    		    module.enumerateSymbols().forEach(function(item) {
                      console.log("Symbol: " + item.name + " (" + item.address + ")" );
                    });
		  }
          },
         onComplete: function(){}
        });
    };
});

