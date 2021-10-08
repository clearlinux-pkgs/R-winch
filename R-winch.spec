#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-winch
Version  : 0.0.6
Release  : 10
URL      : https://cran.r-project.org/src/contrib/winch_0.0.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/winch_0.0.6.tar.gz
Summary  : Portable Native and Joint Stack Traces
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0
Requires: R-winch-lib = %{version}-%{release}
Requires: R-procmaps
BuildRequires : R-procmaps
BuildRequires : buildreq-R

%description
stack trace for easier debugging of R packages with native code.

%package lib
Summary: lib components for the R-winch package.
Group: Libraries

%description lib
lib components for the R-winch package.


%prep
%setup -q -c -n winch
cd %{_builddir}/winch

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633669417

%install
export SOURCE_DATE_EPOCH=1633669417
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library winch
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library winch
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library winch
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc winch || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/winch/DESCRIPTION
/usr/lib64/R/library/winch/INDEX
/usr/lib64/R/library/winch/Meta/Rd.rds
/usr/lib64/R/library/winch/Meta/features.rds
/usr/lib64/R/library/winch/Meta/hsearch.rds
/usr/lib64/R/library/winch/Meta/links.rds
/usr/lib64/R/library/winch/Meta/nsInfo.rds
/usr/lib64/R/library/winch/Meta/package.rds
/usr/lib64/R/library/winch/Meta/vignette.rds
/usr/lib64/R/library/winch/NAMESPACE
/usr/lib64/R/library/winch/NEWS.md
/usr/lib64/R/library/winch/R/winch
/usr/lib64/R/library/winch/R/winch.rdb
/usr/lib64/R/library/winch/R/winch.rdx
/usr/lib64/R/library/winch/WORDLIST
/usr/lib64/R/library/winch/doc/index.html
/usr/lib64/R/library/winch/doc/report.R
/usr/lib64/R/library/winch/doc/report.Rmd
/usr/lib64/R/library/winch/doc/report.html
/usr/lib64/R/library/winch/help/AnIndex
/usr/lib64/R/library/winch/help/aliases.rds
/usr/lib64/R/library/winch/help/paths.rds
/usr/lib64/R/library/winch/help/winch.rdb
/usr/lib64/R/library/winch/help/winch.rdx
/usr/lib64/R/library/winch/html/00Index.html
/usr/lib64/R/library/winch/html/R.css
/usr/lib64/R/library/winch/tests/example0.R
/usr/lib64/R/library/winch/tests/example1.R
/usr/lib64/R/library/winch/tests/example2.R
/usr/lib64/R/library/winch/tests/example3.R
/usr/lib64/R/library/winch/tests/example4.R
/usr/lib64/R/library/winch/tests/example5.R
/usr/lib64/R/library/winch/tests/example6.R
/usr/lib64/R/library/winch/tests/example7.R
/usr/lib64/R/library/winch/tests/example8.R
/usr/lib64/R/library/winch/tests/testthat.R
/usr/lib64/R/library/winch/tests/testthat/test-add_trace_back.R
/usr/lib64/R/library/winch/tests/testthat/test-stop.R
/usr/lib64/R/library/winch/tests/testthat/test-trace_back.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/winch/libs/winch.so
