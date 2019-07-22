%define major 13
%define ixmlmaj 10
%define libname %mklibname upnp %{major}
%define libixml %mklibname ixml %{ixmlmaj}
%define devname %mklibname upnp -d

Summary:	Library and tools for the UPnP protocol
Name:		libupnp
Version:	1.8.4
Release:	1
License:	BSD
Group:		System/Libraries
Url:		http://pupnp.sourceforge.net/
Source0:	http://downloads.sourceforge.net/pupnp/%{name}-%{version}.tar.bz2

%description
The Linux SDK for UPnP Devices (libupnp) provides developers with an API and
open source code for building control points, devices, and bridges that are
compliant with Version 1.0 of the Universal Plug and Play Device
Architecture Specification.

%package -n %{libname}
Summary:	Library and tools for the UPnP protocol
Group:		System/Libraries

%description -n %{libname}
The Linux SDK for UPnP Devices (libupnp) provides developers with an API and
open source code for building control points, devices, and bridges that are
compliant with Version 1.0 of the Universal Plug and Play Device
Architecture Specification.

%package -n %{libixml}
Summary:	Library and tools for the UPnP protocol
Group:		System/Libraries
Conflicts:	%{_lib}upnp6 < 1.6.18-2

%description -n %{libixml}
This package contains a shared library for %{name}.

%package -n %{devname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Requires:	%{libixml} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package includes the development files for %{name}.

%prep
%autosetup -p1

%build
%configure \
	--disable-static

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libupnp.so.%{major}*

%files -n %{libixml}
%{_libdir}/libixml.so.%{ixmlmaj}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*pc

