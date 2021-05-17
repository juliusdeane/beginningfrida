function string2pattern(search_string) {
    var pattern = [];
    for (var n = 0, l = search_string.length; n < l; n ++) {
        var hex_char = Number(search_string.charCodeAt(n)).toString(16);
        pattern.push(hex_char);
    }
    return pattern.join(' ');
}

const m = Process.enumerateModules()[0];
console.log(JSON.stringify(m));

const search_string = "business";
// const pattern = "62 75 73 69 6e 65 73 73";
const pattern = string2pattern(search_string);
console.log('String=[' + search_string + '] Pattern=[' + pattern + ']');

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
