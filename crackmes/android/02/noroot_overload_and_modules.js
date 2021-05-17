Java.perform(function() {
    var mainActivity = Java.use("sg.vantagepoint.uncrackable2.MainActivity");

    mainActivity.a.overload("java.lang.String").implementation = function(s) {
	console.log("SEE IF WE CAN CONTROL THE FUNCTION. Argument=: " + s);
	Process.enumerateModules({
          onMatch: function(module){
            console.log('Module name: ' + module.name + " (" + "Base Address: " + module.base.toString() + ")");
          },
         onComplete: function(){}
        });
    };
});

