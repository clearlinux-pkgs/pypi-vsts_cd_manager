#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-vsts_cd_manager
Version  : 1.0.2
Release  : 18
URL      : https://files.pythonhosted.org/packages/fc/cd/29c798a92d5f7a718711e4beace03612c93ad7ec2121aea606d8abae38ee/vsts-cd-manager-1.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/fc/cd/29c798a92d5f7a718711e4beace03612c93ad7ec2121aea606d8abae38ee/vsts-cd-manager-1.0.2.tar.gz
Summary  : Python wrapper around some of the VSTS APIs
Group    : Development/Tools
License  : MIT
Requires: pypi-vsts_cd_manager-python = %{version}-%{release}
Requires: pypi-vsts_cd_manager-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(mock)
BuildRequires : pypi(msrest)

%description
Visual Studio Team Services Continuous Delivery Manager
=======================================================

%package python
Summary: python components for the pypi-vsts_cd_manager package.
Group: Default
Requires: pypi-vsts_cd_manager-python3 = %{version}-%{release}

%description python
python components for the pypi-vsts_cd_manager package.


%package python3
Summary: python3 components for the pypi-vsts_cd_manager package.
Group: Default
Requires: python3-core
Provides: pypi(vsts_cd_manager)
Requires: pypi(mock)
Requires: pypi(msrest)

%description python3
python3 components for the pypi-vsts_cd_manager package.


%prep
%setup -q -n vsts-cd-manager-1.0.2
cd %{_builddir}/vsts-cd-manager-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649793933
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*