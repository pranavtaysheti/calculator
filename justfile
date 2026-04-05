cc := "zig cc -target x86_64-linux-musl -static -O2 -Wall -Wextra"
lib_dir := "src/lib"
build_dir := "build"
sources := `echo src/lib/*.c`
objects := replace(replace(sources, lib_dir, build_dir), ".c", ".o")

build: compile-lib
    {{ cc }} src/main.c {{ objects }} -o calculator.bin

compile-lib:
    @mkdir -p {{ build_dir }}
    @for src in {{ sources }}; do \
    obj="{{ build_dir }}/$(basename ${src} .c).o"; \
    echo "Compiling ${src} -> ${obj}"; \
    {{ cc }} -c ${src} -o ${obj}; \
    done

clean:
    rm -rf {{ build_dir }} calculator.bin
