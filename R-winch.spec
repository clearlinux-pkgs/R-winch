#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-winch
Version  : 0.0.9
Release  : 20
URL      : https://cran.r-project.org/src/contrib/winch_0.0.9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/winch_0.0.9.tar.gz
Summary  : Portable Native and Joint Stack Traces
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0
Requires: R-winch-lib = %{version}-%{release}
Requires: R-winch-license = %{version}-%{release}
Requires: R-procmaps
BuildRequires : R-procmaps
BuildRequires : buildreq-R

%description
stack trace for easier debugging of R packages with native code.

%package lib
Summary: lib components for the R-winch package.
Group: Libraries
Requires: R-winch-license = %{version}-%{release}

%description lib
lib components for the R-winch package.


%package license
Summary: license components for the R-winch package.
Group: Default

%description license
license components for the R-winch package.


%prep
%setup -q -n winch
cd %{_builddir}/winch

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1662051462

%install
export SOURCE_DATE_EPOCH=1662051462
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-winch
cp %{_builddir}/winch/src/vendor/libbacktrace/LICENSE %{buildroot}/usr/share/package-licenses/R-winch/555657fe7ff5be9969fa3387d8e465e0a1afa2f4 || :
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/winch/tests/testthat/_snaps/add_trace_back.md
/usr/lib64/R/library/winch/tests/testthat/test-add_trace_back.R
/usr/lib64/R/library/winch/tests/testthat/test-stop.R
/usr/lib64/R/library/winch/tests/testthat/test-trace_back.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/winch/libs/winch.so
/usr/lib64/R/library/winch/libs/winch.so.avx2
/usr/lib64/R/library/winch/libs/winch.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-winch/555657fe7ff5be9969fa3387d8e465e0a1afa2f4
