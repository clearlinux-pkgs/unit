#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v2
# autospec commit: f032afc
#
Name     : unit
Version  : 1.29.0.1
Release  : 21
URL      : https://github.com/nginx/unit/archive/1.29.0-1/unit-1.29.0.1.tar.gz
Source0  : https://github.com/nginx/unit/archive/1.29.0-1/unit-1.29.0.1.tar.gz
Source1  : unitd.service
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: unit-bin = %{version}-%{release}
Requires: unit-lib = %{version}-%{release}
Requires: unit-license = %{version}-%{release}
Requires: unit-man = %{version}-%{release}
Requires: unit-services = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : buildreq-php
BuildRequires : openssl-dev
BuildRequires : pcre2-dev
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Ignore-ignorant-exit-code.patch

%description
# NGINX Unit
## Universal Web App Server
![NGINX Unit Logo](docs/unitlogo.svg)
NGINX Unit is a lightweight and versatile open-source server that has
three core capabilities:

%package bin
Summary: bin components for the unit package.
Group: Binaries
Requires: unit-license = %{version}-%{release}
Requires: unit-services = %{version}-%{release}

%description bin
bin components for the unit package.


%package lib
Summary: lib components for the unit package.
Group: Libraries
Requires: unit-license = %{version}-%{release}

%description lib
lib components for the unit package.


%package license
Summary: license components for the unit package.
Group: Default

%description license
license components for the unit package.


%package man
Summary: man components for the unit package.
Group: Default

%description man
man components for the unit package.


%package services
Summary: services components for the unit package.
Group: Systemd services
Requires: systemd

%description services
services components for the unit package.


%prep
%setup -q -n unit-1.29.0-1
cd %{_builddir}/unit-1.29.0-1
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697570053
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static --openssl \
--modules=/usr/lib64/unit \
--state=/var/lib/unit
make  %{?_smp_mflags}

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1697570053
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/unit
cp %{_builddir}/unit-1.29.0-1/LICENSE %{buildroot}/usr/share/package-licenses/unit/04319952ed7b0f3b3a70ae4d5d9f954317b8f970 || :
cp %{_builddir}/unit-1.29.0-1/NOTICE %{buildroot}/usr/share/package-licenses/unit/7fdaf3c362e55e747c97f5d87d60b0299f574f59 || :
cp %{_builddir}/unit-1.29.0-1/pkg/deb/debian/copyright %{buildroot}/usr/share/package-licenses/unit/cc015eb51347c7dcf3f6d886f7a1c426b988198c || :
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/unitd.service
## install_append content
./configure python --config=python3-config
./configure php --config=php-config
make DESTDIR=%{buildroot} python3-install
make DESTDIR=%{buildroot} php-install
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/unitd

%files lib
%defattr(-,root,root,-)
/usr/lib64/unit/php.unit.so
/usr/lib64/unit/python3.unit.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/unit/04319952ed7b0f3b3a70ae4d5d9f954317b8f970
/usr/share/package-licenses/unit/7fdaf3c362e55e747c97f5d87d60b0299f574f59
/usr/share/package-licenses/unit/cc015eb51347c7dcf3f6d886f7a1c426b988198c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/unitd.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/unitd.service
