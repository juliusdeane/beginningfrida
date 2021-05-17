rpc.exports = {
  init: function (stage, parameters) {
    console.log('[init]', stage, JSON.stringify(parameters));

    // Interceptor.attach(Module.getExportByName(null, ''), {
    Interceptor.attach(Module.findBaseAddress('crackme02').add(0x1169), {
      onEnter: function (args) {
        console.log(`check_password(format="${args[0].readUtf8String()}") [1]`);
        console.log(`check_password(format="${args[1].readUtf8String()}") [2]`);
      },
      onLeave(retval, state) {
         retval.replace(1);
      }

    });
  },
  dispose: function () {
    console.log('[dispose]');
  }
};
