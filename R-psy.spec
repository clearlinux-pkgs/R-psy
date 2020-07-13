#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-psy
Version  : 1.1
Release  : 18
URL      : https://cran.r-project.org/src/contrib/psy_1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/psy_1.1.tar.gz
Summary  : Various procedures used in psychometry
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n psy
cd %{_builddir}/psy

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589537672

%install
export SOURCE_DATE_EPOCH=1589537672
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library psy
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library psy
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library psy
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc psy || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/psy/DESCRIPTION
/usr/lib64/R/library/psy/INDEX
/usr/lib64/R/library/psy/Meta/Rd.rds
/usr/lib64/R/library/psy/Meta/data.rds
/usr/lib64/R/library/psy/Meta/features.rds
/usr/lib64/R/library/psy/Meta/hsearch.rds
/usr/lib64/R/library/psy/Meta/links.rds
/usr/lib64/R/library/psy/Meta/nsInfo.rds
/usr/lib64/R/library/psy/Meta/package.rds
/usr/lib64/R/library/psy/NAMESPACE
/usr/lib64/R/library/psy/R/psy
/usr/lib64/R/library/psy/R/psy.rdb
/usr/lib64/R/library/psy/R/psy.rdx
/usr/lib64/R/library/psy/data/ehd.rda
/usr/lib64/R/library/psy/data/expsy.rda
/usr/lib64/R/library/psy/data/sleep.rda
/usr/lib64/R/library/psy/help/AnIndex
/usr/lib64/R/library/psy/help/aliases.rds
/usr/lib64/R/library/psy/help/paths.rds
/usr/lib64/R/library/psy/help/psy.rdb
/usr/lib64/R/library/psy/help/psy.rdx
/usr/lib64/R/library/psy/html/00Index.html
/usr/lib64/R/library/psy/html/R.css
