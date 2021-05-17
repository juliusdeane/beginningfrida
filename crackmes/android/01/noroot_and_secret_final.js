Java.perform(function() {
    // cut&paste from stackoverflow:
    // https://stackoverflow.com/questions/3195865/converting-byte-array-to-string-in-javascript
    // now added some changes:
    // result += (String.fromCharCode(converted_array[i] & 0xff));
    function bin2String(array) {
        var result = "";
        for(var i = 0; i < array.length; ++i){
          result += (String.fromCharCode(array[i] & 0xff));
        }
        return result;
    }

    var mainActivity = Java.use("sg.vantagepoint.uncrackable1.MainActivity");

    mainActivity.a.implementation = function(s) {
	console.log("SEE IF WE CAN CONTROL THE FUNCTION. Argument=[" + s + "]\n");
    }

    var base_class_secret = Java.use("sg.vantagepoint.a.a");
    console.log("[base_class_secret] " + base_class_secret);

    var original_function = base_class_secret.a;
    console.log("[base_class_secret.a] " + original_function);

    base_class_secret.a.implementation = function(str1, str2) {
        // return this.a(str1, str2);
        var retval = this.a(str1, str2);
	console.log("[BEGIN] retval");
	console.log(retval);
	console.log(JSON.stringify(retval));
	console.log("=== convert retval to string ===");
	console.log("The secret was: " + bin2String(retval));
	console.log("[END] retval");
	return retval;
    }
});

