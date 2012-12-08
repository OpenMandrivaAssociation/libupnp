%define major 6
%define minor 2
%define libname %mklibname upnp %{major}
%define develname %mklibname upnp -d
%define develnamest %mklibname upnp -d -s

Summary:	Library and tools for the UPnP protocol
Name:		libupnp
Version:	1.6.17
Release:	2
License:	BSD
Group:		System/Libraries
URL:		http://pupnp.sourceforge.net/
Source0:	http://downloads.sourceforge.net/pupnp/%{name}-%{version}.tar.bz2

%description
The Linux SDK for UPnP Devices (libupnp) provides developers with an API and
open source code for building control points, devices, and bridges that are
compliant with Version 1.0 of the Universal Plug and Play Device
Architecture Specification.

%package -n %{libname}
Summary:	Library and tools for the UPnP protocol
Group:		System/Libraries
Obsoletes:	%{mklibname upnp 0} < 1.6.6
Obsoletes:	%{mklibname upnp 3} < 1.6.17

%description -n %{libname}
The Linux SDK for UPnP Devices (libupnp) provides developers with an API and
open source code for building control points, devices, and bridges that are
compliant with Version 1.0 of the Universal Plug and Play Device
Architecture Specification.

%package -n %{develname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname upnp 0 -d} < 1.6.6

%description -n %{develname}
Libraries and includes static files for developing programs based on %{name}.

%package -n %{develnamest}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel-static = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname upnp 0 -d -s} < 1.6.6

%description -n %{develnamest}
Libraries and includes static files for developing programs based on %{name}.

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
%{_libdir}/pkgconfig/*pc
%{_docdir}/%{name}

%files -n %{develnamest}
%{_libdir}/*.a


%changelog
* Tue Jun 19 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.6.17-1
+ Revision: 806209
- version update 1.6.17

* Fri Dec 16 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.6.14-1
+ Revision: 741700
- la files removed
- version update 1.6.14

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6.6-3mdv2011.0
+ Revision: 620234
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.6.6-2mdv2010.0
+ Revision: 429844
- rebuild

* Tue Jun 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.6.6-1mdv2009.0
+ Revision: 228472
- update to new version 1.6.6

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Apr 25 2008 Götz Waschk <waschk@mandriva.org> 1.6.5-2mdv2009.0
+ Revision: 197464
- fix obsoletes

* Thu Apr 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.6.5-1mdv2009.0
+ Revision: 195343
- new version
- new development library policy
- bump major
- fix descriptions
- spec file clean

* Sat Jan 26 2008 Erwan Velu <erwan@mandriva.org> 1.6.3-1mdv2008.1
+ Revision: 158259
- 1.6.3
- 1.6.3

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 07 2007 Erwan Velu <erwan@mandriva.org> 1.6.0-1mdv2008.0
+ Revision: 59908
- 1.6.0

* Mon Apr 23 2007 Erwan Velu <erwan@mandriva.org> 1.4.4-1mdv2008.0
+ Revision: 17464
- 1.4.4

