Java.perform(function() {
    var mainActivity = Java.use("sg.vantagepoint.uncrackable2.MainActivity");

    mainActivity.a.implementation = function(s) {
	console.log("SEE IF WE CAN CONTROL THE FUNCTION. Argument=: " + s);
    }
});

