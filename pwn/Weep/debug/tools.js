function prettyPrint(addr, num) {
	var b = []
	for(var i=addr/4; i<addr/4+num; i+=1){
		b.push("0x"+HEAP32[i].toString(16))
	}
	return b
}
function printHeap() {
	HEAP_START = 0x10568-4
	HEAP_MAX = 0x12000
	cur = HEAP_START
	while(cur < HEAP_MAX) {
		size = HEAP32[cur/4]&0xfffffffc
		console.log("Address: 0x" + cur.toString(16) + " Size: 0x" + size.toString(16))
		console.log(prettyPrint(cur, Math.min(10, size/4)).join(' '))
		cur += size
		if(size == 0) break;
	}
}
function grep(addr) {
	var b = []
	for(var i=0; i<HEAP32.length; i+=1){
		if(HEAP32[i] == addr) b.push(i*4)
	}
	return b
}
