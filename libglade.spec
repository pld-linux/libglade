Summary:	libglade library
Summary(pl):	Biblioteka do ³adowania definicji interfejsu generowanego programem glade
Name:		libglade
Version:	0.11
Release:	1
License:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://ftp.daa.com.au/pub/james/gnome/%{name}-%{version}.tar.gz
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libxml-devel >= 1.7.2
BuildRequires:	XFree86-devel
URL:		http://www.gnome.org/
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6

%description
This library allows you to load user interfaces in your program, which are
stored externally. This allows alteration of the interface without
recompilation of the program. The interfaces can also be edited with
GLADE.

%description -l pl
Biblioteka libglade umo¿liwia dynamiczne ³adowanie definicji interfejsu
u¿ytkownika generowanego za pomoc± programu glade. Taka separacja definicji
interfrejsu umozliwia placê nad nim bez konieczno¶ci rekompilacji programu.

%package devel
Summary:	Libraries, includes, etc to develop libglade applications
Summary(pl):	Biblioteki, pliki nag³ówkowe i dokumentacja dla programisty
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Libraries, include files, etc you can use to develop libglade applications.

%description -l pl devel
Biblioteki, pliki nag³ówkowe i dokumentacja dla programisty.

%package static
Summary:	Static libglade library
Summary(pl):	Biblioteka statyczna libglade
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description static
Static libglade library.

%description -l pl static
Biblioteka statyczna libglade.

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
	m4datadir=%{_datadir}/aclocal

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

%{_datadir}/aclocal/*

/usr/src/examples/%{name}

%files static
%attr(644,root,root) %{_libdir}/lib*.a
