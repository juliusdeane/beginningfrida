{
  onEnter(log, args, state) {
    log('[*] BEFORE MANIPULATING ARGUMENTS');
    log(`strcmp(s1="${args[0].readUtf8String()}", s2="${args[1].readUtf8String()}")`);
    args[1] = args[0];

    log('[*] AFTER MANIPULATING ARGUMENTS');
    log(`strcmp(s1="${args[0].readUtf8String()}", s2="${args[1].readUtf8String()}")`);
  },
  onLeave(log, retval, state) {
    // Remove the cheat here as must be resolved in OnEnter.
    // retval.replace(0);
  }
}
