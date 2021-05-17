Process.enumerateModules({
    onMatch: function(module){
        console.log('Module name: ' + module.name + " (" + "Base Address: " + module.base.toString() + ")");
	module.enumerateExports().forEach(function(item) {
		console.log("(" + module.name + ") export: " + item.name + " (" + item.address + ")" );
	});
    },
    onComplete: function(){}
});
