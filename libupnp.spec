%define major 6
%define minor 2
%define libname %mklibname upnp %{major}
%define develname %mklibname upnp -d

Summary:	Library and tools for the UPnP protocol
Name:		libupnp
Version:	1.6.14
Release:	1
License:	BSD
Group:		System/Libraries
URL:		http://pupnp.sourceforge.net/
Source:		http://downloads.sourceforge.net/pupnp/%{name}-%{version}.tar.bz2

%description
The Linux SDK for UPnP Devices (libupnp) provides developers with an API and
open source code for building control points, devices, and bridges that are
compliant with Version 1.0 of the Universal Plug and Play Device
Architecture Specification.

%package -n %{libname}
Summary:        Library and tools for the UPnP protocol
Group:          System/Libraries
Obsoletes:	%mklibname upnp 0

%description -n %{libname}
The Linux SDK for UPnP Devices (libupnp) provides developers with an API and
open source code for building control points, devices, and bridges that are
compliant with Version 1.0 of the Universal Plug and Play Device
Architecture Specification.

%package -n %{develname}
Summary:	Header files and static libraries from %name
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname upnp 0 -d} < 1.6.6
Provides:	%mklibname upnp 0 -d

%description -n %{develname}
Libraries and includes files for developing programs based on %name.

%prep
%setup -q

%build
%configure2_5x \
	--with-documentation=%{_docdir}/%{name} \
        --enable-tools \
        --enable-sample
%make
								
%install
%makeinstall_std

%files -n %{libname}
%doc LICENSE NEWS README THANKS TODO
%{_libdir}/*upnp.so.%{major}*
%{_libdir}/*.so.%{minor}*
%{_libdir}/libthreadutil.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*pc
%{_docdir}/%{name}
