const m = Process.enumerateModules()[0];
console.log(JSON.stringify(m));

const pattern = "62 75 73 69 6e 65 73 73";

var results = Memory.scanSync(m.base, m.size, pattern);

console.log('[Memory.scan().onMatch] match: addr=' + m.base + " / size=" + m.size);
results.forEach( (item) => {
    console.log('  [Memory.scanSync()]: match: addr=' + item.address + " / size=" + item.size);
});
