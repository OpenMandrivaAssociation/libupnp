%define major 6
%define ixmlmaj 2
%define libname %mklibname upnp %{major}
%define libthreadutil %mklibname threadutil %{major}
%define libixml %mklibname ixml %{ixmlmaj}
%define devname %mklibname upnp -d

Summary:	Library and tools for the UPnP protocol
Name:		libupnp
Version:	1.6.18
Release:	13
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

%package -n %{libthreadutil}
Summary:	Library and tools for the UPnP protocol
Group:		System/Libraries
Conflicts:	%{_lib}upnp6 < 1.6.18-2

%description -n %{libthreadutil}
This package contains a shared library for %{name}.

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
Requires:	%{libthreadutil} >= %{version}-%{release}
Requires:	%{libixml} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package includes the development files for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libupnp.so.%{major}*

%files -n %{libixml}
%{_libdir}/libixml.so.%{ixmlmaj}*

%files -n %{libthreadutil}
%{_libdir}/libthreadutil.so.%{major}*

%files -n %{devname}
%doc LICENSE NEWS README THANKS TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*pc

