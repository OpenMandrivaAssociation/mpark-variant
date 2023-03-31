%global debug_package %{nil}
 
Name: mpark-variant
Summary: C++17 std::variant for C++11/14/17
Version: 1.4.0
Release: 2
Group:   System/Libraries
License: Boost
URL: https://github.com/mpark/variant
Source0: https://github.com/mpark/variant/archive/v%{version}/variant-%{version}.tar.gz
 
BuildRequires: cmake
 
%description
Header-only %{summary}.
 
%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
 
%description devel
%{summary}.
 
%prep
%autosetup -n variant-%{version} -p1
sed -i 's@lib/@%{_libdir}/@g' CMakeLists.txt
 
%build
%cmake \
        -DCMAKE_BUILD_TYPE=Release

%make_build

%install
%make_install -C build

%files devel
%doc README.md
%license LICENSE.md
%{_includedir}/mpark
%{_libdir}/cmake/mpark_variant
