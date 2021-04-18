#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : sqlite-autoconf
Version  : 3.33.0
Release  : 98
URL      : file:///aot/build/clearlinux/packages/sqlite-autoconf/sqlite-autoconf-3.33.0.tar.gz
Source0  : file:///aot/build/clearlinux/packages/sqlite-autoconf/sqlite-autoconf-3.33.0.tar.gz
Summary  : SQL database engine
Group    : Development/Tools
License  : Public-Domain
Requires: sqlite-autoconf-bin = %{version}-%{release}
Requires: sqlite-autoconf-lib = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gcc
BuildRequires : gcc-abi
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gdb-dev
BuildRequires : gettext-bin
BuildRequires : git
BuildRequires : glibc-abi
BuildRequires : glibc-bench
BuildRequires : glibc-bin
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-doc
BuildRequires : glibc-extras
BuildRequires : glibc-lib-avx2
BuildRequires : glibc-libc32
BuildRequires : glibc-locale
BuildRequires : glibc-nscd
BuildRequires : glibc-staticdev
BuildRequires : glibc-utils
BuildRequires : gmp-dev
BuildRequires : gmp-staticdev
BuildRequires : graphviz
BuildRequires : guile
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libstdc++
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libunwind
BuildRequires : libunwind-dev
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : libxslt
BuildRequires : m4
BuildRequires : mpc-dev
BuildRequires : mpfr-dev
BuildRequires : ncurses-dev
BuildRequires : ncurses-dev32
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(tcl)
BuildRequires : procps-ng
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : readline
BuildRequires : readline-dev
BuildRequires : readline-dev32
BuildRequires : tcl
BuildRequires : tcl-dev
BuildRequires : tcl-staticdev
BuildRequires : valgrind
BuildRequires : valgrind-dev
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
BuildRequires : zlib-staticdev

%description
This directory contains an SQLite extension that implements a virtual
table type that allows users to create, query and manipulate r-tree[1]
data structures inside of SQLite databases. Users create, populate
and query r-tree structures using ordinary SQL statements.

%package bin
Summary: bin components for the sqlite-autoconf package.
Group: Binaries

%description bin
bin components for the sqlite-autoconf package.


%package dev
Summary: dev components for the sqlite-autoconf package.
Group: Development
Requires: sqlite-autoconf-lib = %{version}-%{release}
Requires: sqlite-autoconf-bin = %{version}-%{release}
Provides: sqlite-autoconf-devel = %{version}-%{release}
Requires: sqlite-autoconf = %{version}-%{release}

%description dev
dev components for the sqlite-autoconf package.


%package dev32
Summary: dev32 components for the sqlite-autoconf package.
Group: Default
Requires: sqlite-autoconf-lib32 = %{version}-%{release}
Requires: sqlite-autoconf-bin = %{version}-%{release}
Requires: sqlite-autoconf-dev = %{version}-%{release}

%description dev32
dev32 components for the sqlite-autoconf package.


%package lib
Summary: lib components for the sqlite-autoconf package.
Group: Libraries

%description lib
lib components for the sqlite-autoconf package.


%package lib32
Summary: lib32 components for the sqlite-autoconf package.
Group: Default

%description lib32
lib32 components for the sqlite-autoconf package.


%package staticdev
Summary: staticdev components for the sqlite-autoconf package.
Group: Default
Requires: sqlite-autoconf-dev = %{version}-%{release}

%description staticdev
staticdev components for the sqlite-autoconf package.


%package staticdev32
Summary: staticdev32 components for the sqlite-autoconf package.
Group: Default
Requires: sqlite-autoconf-dev32 = %{version}-%{release}

%description staticdev32
staticdev32 components for the sqlite-autoconf package.


%prep
%setup -q -n sqlite-autoconf
cd %{_builddir}/sqlite-autoconf
pushd ..
cp -a sqlite-autoconf build32
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618724162
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate -floop-block
export CPPFLAGS="-DSQLITE_HAVE_ZLIB -DSQLITE_ENABLE_RTREE -DSQLITE_ENABLE_DBSTAT_VTAB -DSQLITE_MAX_WORKER_THREADS=16 -DSQLITE_DEFAULT_WORKER_THREADS=6 -DSQLITE_DEFAULT_PAGE_SIZE=4096 -DSQLITE_TEMP_STORE=2 -DSQLITE_DISABLE_DIRSYNC -DSQLITE_ENABLE_UNLOCK_NOTIFY -DSQLITE_MAX_DEFAULT_PAGE_SIZE=32768 -DSQLITE_DEFAULT_SYNCHRONOUS=1 -DSQLITE_DEFAULT_MMAP_SIZE=268435456 -DSQLITE_ENABLE_COLUMN_METADATA -DSQLITE_DEFAULT_MEMSTATUS=0 -DSQLITE_DEFAULT_WAL_SYNCHRONOUS=1 -DSQLITE_THREADSAFE=2 -DSQLITE_LIKE_DOESNT_MATCH_BLOBS -DSQLITE_MAX_EXPR_DEPTH=0 -DSQLITE_USE_ALLOCA -DSQLITE_ENABLE_MEMSYS5 -DUSE_AMALGAMATION=1 -DUSE_PREAD"
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-correction -fprofile-partial-training"
export CFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fno-math-errno -fomit-frame-pointer -pthread -static-libgcc $PGO_GEN $CPPFLAGS"
export FCFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fno-math-errno -fomit-frame-pointer -pthread -static-libgcc $PGO_GEN $CPPFLAGS"
export FFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -fno-math-errno -fomit-frame-pointer -pthread -static-libgcc $PGO_GEN $CPPFLAGS"
export CXXFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fno-math-errno -fomit-frame-pointer -pthread -static-libgcc $PGO_GEN $CPPFLAGS"
export LDFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fno-math-errno -fomit-frame-pointer -pthread -static-libgcc -Wl,--whole-archive,--as-needed,/usr/lib64/libz.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive $PGO_GEN $CPPFLAGS"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fPIC -fno-math-errno -fvisibility=hidden -flto-partition=none
## gcc: -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fno-math-errno -fomit-frame-pointer -pthread -static-libgcc $PGO_USE $CPPFLAGS"
export FCFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fno-math-errno -fomit-frame-pointer -pthread -static-libgcc $PGO_USE $CPPFLAGS"
export FFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fno-math-errno -fomit-frame-pointer -pthread -static-libgcc $PGO_USE $CPPFLAGS"
export CXXFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fno-math-errno -fomit-frame-pointer -pthread -static-libgcc $PGO_USE $CPPFLAGS"
export LDFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fno-math-errno -fomit-frame-pointer -pthread -static-libgcc -Wl,--whole-archive,--as-needed,/usr/lib64/libz.a,-lpthread,-ldl,-lm,-lmvec,--no-whole-archive $PGO_USE $CPPFLAGS"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
## altflags_pgo end
sd --flags mi '^AC_INIT\((.*\n.*\)|.*\))' '$0\nAM_MAINTAINER_MODE([disable])' configure.ac
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%reconfigure  --enable-shared --enable-static --enable-static-shell --enable-tcl --enable-readline --enable-editline
make %{?_smp_mflags} sqlite3.c  V=1 VERBOSE=1
make %{?_smp_mflags} V=1 VERBOSE=1

#make -j1 test || :
make -j1 quicktest || :
sh tool/run-speed-test.sh trunk1 || :
sh tool/run-speed-test.sh trunk2 --wal || :
sh tool/speed-check.sh trunk3 || :
sh tool/speed-check.sh trunk4 --repeat 30 || :
sh tool/speed-check.sh trunk5 --singlethread || :
sh tool/speed-check.sh trunk6 --multithread --threads 16 || :
sh tool/speed-check.sh trunk7 --multithread --threads 16 --main || :
sh tool/speed-check.sh trunk8 --multithread --threads 16 --cte || :
sh tool/speed-check.sh trunk9 --multithread --threads 16 --rtree || :
sh tool/speed-check.sh trunk10 --multithread --threads 16 --orm || :
sh tool/speed-check.sh trunk11 --multithread --threads 16 --fp || :
sh tool/speed-check.sh trunk12 --multithread --threads 16 --wal || :
sh tool/speed-check.sh trunk13 --multithread --threads 16 --main --wal || :
sh tool/kvtest-speed.sh trunk14 || :
make clean
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%reconfigure  --enable-shared --enable-static --enable-static-shell --enable-tcl --enable-readline --enable-editline
make %{?_smp_mflags} sqlite3.c  V=1 VERBOSE=1
make %{?_smp_mflags} V=1 VERBOSE=1

pushd ../build32/
export CFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export CXXFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export LDFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
sd --flags mi '^AC_INIT\((.*\n.*\)|.*\))' '$0\nAM_MAINTAINER_MODE([disable])' configure.ac
%reconfigure  --enable-shared --enable-static --enable-static-shell --enable-readline --enable-editline --disable-tcl --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make %{?_smp_mflags} V=1 VERBOSE=1
make %{?_smp_mflags} sqlite3.c  V=1 VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1618724162
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
## install_append content
mkdir -p %{buildroot}/usr/src/sqlite3
cp /builddir/build/BUILD/sqlite-autoconf/sqlite3.c %{buildroot}/usr/src/sqlite3/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sqlite3

%files dev
%defattr(-,root,root,-)
/usr/include/sqlite3.h
/usr/include/sqlite3ext.h
/usr/lib/tcl8.6/sqlite3/libtclsqlite3.so
/usr/lib/tcl8.6/sqlite3/pkgIndex.tcl
/usr/lib64/libsqlite3.so
/usr/lib64/pkgconfig/sqlite3.pc
/usr/src/sqlite3/sqlite3.c

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libsqlite3.so
/usr/lib32/pkgconfig/32sqlite3.pc
/usr/lib32/pkgconfig/sqlite3.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsqlite3.so.0
/usr/lib64/libsqlite3.so.0.8.6

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libsqlite3.so.0
/usr/lib32/libsqlite3.so.0.8.6

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libsqlite3.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libsqlite3.a
