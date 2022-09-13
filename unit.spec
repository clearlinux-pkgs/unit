#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : unit
Version  : 1.28.0.1
Release  : 17
URL      : https://github.com/nginx/unit/archive/1.28.0-1/unit-1.28.0.1.tar.gz
Source0  : https://github.com/nginx/unit/archive/1.28.0-1/unit-1.28.0.1.tar.gz
Source1  : unitd.service
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: unit-bin = %{version}-%{release}
Requires: unit-lib = %{version}-%{release}
Requires: unit-license = %{version}-%{release}
Requires: unit-man = %{version}-%{release}
Requires: unit-services = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : openssl-dev
BuildRequires : pcre2-dev
BuildRequires : python3-dev
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

%description services
services components for the unit package.


%prep
%setup -q -n unit-1.28.0-1
cd %{_builddir}/unit-1.28.0-1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663084909
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static --openssl \
--modules=/usr/lib64/unit \
--state=/var/lib/unit
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1663084909
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/unit
cp %{_builddir}/unit-1.28.0-1/LICENSE %{buildroot}/usr/share/package-licenses/unit/04319952ed7b0f3b3a70ae4d5d9f954317b8f970 || :
cp %{_builddir}/unit-1.28.0-1/NOTICE %{buildroot}/usr/share/package-licenses/unit/7fdaf3c362e55e747c97f5d87d60b0299f574f59 || :
cp %{_builddir}/unit-1.28.0-1/pkg/deb/debian/copyright %{buildroot}/usr/share/package-licenses/unit/cc015eb51347c7dcf3f6d886f7a1c426b988198c || :
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
