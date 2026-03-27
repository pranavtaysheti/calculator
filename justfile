set shell := ["bash", "-cu"]

cc          := "clang"
target      := "x86_64-linux-musl"
musl_include := "/usr/local/musl/include"
musl_lib     := "/usr/local/musl/lib"

lib_dir     := "src/lib"
build_dir   := "build"
lib_archive := "src/lib.a"

# Get the list of source files
sources := `ls src/lib/*.c`

# Use 'replace' to map the directory and extension
# Note: replace(string, old, new)
objects := replace(replace(sources, lib_dir, build_dir), ".c", ".o")

build: build-lib
    {{cc}} --target={{target}} -static -fuse-ld=lld -march=x86-64-v3 -O2 -Wall -Wextra \
        -I {{lib_dir}} -isystem {{musl_include}} \
        -L {{musl_lib}} \
        src/main.c {{lib_archive}} \
        -o calculator.bin

build-lib:
    @mkdir -p {{build_dir}}
    @for src in {{sources}}; do \
        obj="{{build_dir}}/$(basename ${src} .c).o"; \
        echo "Compiling ${src} -> ${obj}"; \
        {{cc}} --target={{target}} -O2 -Wall -Wextra \
            -I {{lib_dir}} -isystem {{musl_include}} \
            -c ${src} -o ${obj}; \
    done
    ar rcs {{lib_archive}} {{objects}}

clean:
    rm -rf {{build_dir}}
    rm -f {{lib_archive}} calculator.bin