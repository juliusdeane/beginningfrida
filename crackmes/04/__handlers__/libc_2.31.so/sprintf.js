{
  onEnter(log, args, state) {
    this.destination_address = args[0];
    log("Format=[" + args[1].readUtf8String() + "]");
    log("Parameter=[" + args[2].readUtf8String() + "]");
  },
  onLeave(log, retval, state) {
    log("sprintf address=[" + this.destination_address + "]");
    log('sprintf result=["' + this.destination_address.readUtf8String() + '"]');
  }
}
