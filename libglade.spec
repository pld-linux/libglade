Summary:	libglade library
Name:		libglade
Version:	0.7
Release:	1
Copyright:	LGPL
Group:		X11/Libraries
Source:		ftp://ftp.daa.com.au/pub/james/gnome/%{name}-%{version}.tar.gz
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libxml-devel
BuildRequires:	XFree86-devel
URL:		http://www.gnome.org
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6

Requires: gtk+
Requires: libxml >= 1.3

%description
This library allows you to load user interfaces in your program, which are
stored externally. This allows alteration of the interface without
recompilation of the program.

The interfaces can also be edited with GLADE.

%package devel
Summary:	Libraries, includes, etc to develop libglade applications
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description devel
Libraries, include files, etc you can use to develop libglade applications.

%package static
Summary:	Static libglade library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description static
Static libglade library.

%prep
%setup -q

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=/usr/share/aclocal

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README

install test-libglade.c *.glade $RPM_BUILD_ROOT/usr/src/examples/%{name}

%find_lang %{name}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *gz
%docdir %{_datadir}/gnome/html/libglade
%doc %{_datadir}/gnome/html/libglade/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libgladeConf.sh
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/glade

/usr/share/aclocal/*

/usr/src/examples/%{name}

%files static
%attr(644,root,root) %{_libdir}/lib*.a
