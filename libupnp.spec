%define name	libupnp
%define version	1.4.4
%define release %mkrel 1

%define major	0
%define libname %mklibname upnp %major

Name: 	 	%{name}
Summary: 	Library and tools for the UPnP protocol
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/pupnp/%{name}-%{version}.tar.bz2
URL:		http://pupnp.sourceforge.net/
License:	BSD
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
The Linux SDK for UPnP Devices (libupnp) provides developers with an API and
open source code for building control points, devices, and bridges that are
compliant with Version 1.0 of the  Universal Plug and Play Device
Architecture Specification.

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%name-devel

%description -n %{libname}-devel
Libraries and includes files for developing programs based on %name.

%prep
%setup -q

%build
%configure --with-documentation=$RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}-%{version} \
        --enable-tools\
        --enable-sample
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*
%{_defaultdocdir}/%{name}-%{version}/LICENSE
%{_defaultdocdir}/%{name}-%{version}/NEWS
%{_defaultdocdir}/%{name}-%{version}/README
%{_defaultdocdir}/%{name}-%{version}/THANKS
%{_defaultdocdir}/%{name}-%{version}/TODO

%files -n %{libname}-devel
%defattr(-,root,root)
%doc LICENSE README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*pc
%{_defaultdocdir}/%{name}-%{version}/*Prog*
%{_defaultdocdir}/%{name}-%{version}/html
%{_defaultdocdir}/%{name}-%{version}/examples


