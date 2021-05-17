const m = Process.enumerateModules()[0];
console.log(JSON.stringify(m));

const pattern = "62 75 73 69 6e 65 73 73";

Memory.scan(m.base, m.size, pattern, {
  onMatch(address, size) {
    console.log('[Memory.scan().onMatch] match: addr=' + address + " / size=" + size);

    // if we want only the first match, just issue a return here.
    return true;
  },
  onComplete() {
    console.log('Memory.scan() complete');
  }
});
