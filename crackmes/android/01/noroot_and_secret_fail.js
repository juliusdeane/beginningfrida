Java.perform(function() {
    var mainActivity = Java.use("sg.vantagepoint.uncrackable1.MainActivity");

    mainActivity.a.implementation = function(s) {
	console.log("SEE IF WE CAN CONTROL THE FUNCTION. Argument=[" + s + "]\n");
    }

    var base_class_secret = Java.use("sg.vantagepoint.a.a");
    console.log("[base_class_secret] " + base_class_secret);

    var original_function = base_class_secret.a;
    console.log("[base_class_secret.a] " + original_function);

    base_class_secret.a.implementation = function(str1, str2) {
        return this.a(str1, str2);
    }
});

