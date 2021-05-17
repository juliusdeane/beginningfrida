Java.perform(function () {
  var MainActivity = Java.use('com.entebra.crackme0x01.MainActivity');
  var onClick = MainActivity.onClick;
  onClick.implementation = function (v) {
    send('[onClick] entered.');
    onClick.call(this, v);

    this.m.value = 0;
    this.n.value = 1;
    this.cnt.value = 999;

    // Log to the console that it's done, and we should have the flag!
    console.log('Done:' + JSON.stringify(this.cnt));
  };
});
