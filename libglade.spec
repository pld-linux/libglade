Summary:	libglade library
Summary(es):	El libglade permite que usted cargue archivos del interfaz del glade
Summary(pl):	Biblioteka do ³adowania definicji interfejsu generowanego programem glade
Summary(pt_BR):	Esta biblioteca permite carregar arquivos da interface glade
Name:		libglade
Version:	1.99.12
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:        ftp://ftp.gnome.org/pub/GNOME/earthquake/sources/libglade/%{name}-%{version}.tar.bz2
Patch1:		%{name}-gtkdoc-scanobj-nogtkinit.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	bison
BuildRequires:	bonobo-devel >= 0.28
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libxml-devel >= 1.7.2
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This library allows you to load user interfaces in your program, which
are stored externally. This allows alteration of the interface without
recompilation of the program. The interfaces can also be edited with
GLADE.

%description -l es
El libglade permite que usted cargue archivos del interfaz del glade
en tiempo de ejecución.

%description -l pl
Biblioteka libglade umo¿liwia dynamiczne ³adowanie definicji
interfejsu u¿ytkownika generowanego za pomoc± programu glade. Taka
separacja definicji interfejsu umo¿liwia pracê nad nim bez
konieczno¶ci rekompilacji programu.

%description -l pt_BR
O libglade permite carregar, em tempo de execução, arquivos da
interface glade. Não é necessário ter o glade instalado, mas esta é a
melhor maneira de criar os arquivos de interface.

%package devel
Summary:	Libraries, includes, etc to develop libglade applications
Summary(es):	Archivos necesarios para el desarrollo de aplicaciones con libglade
Summary(pl):	Biblioteki, pliki nag³ówkowe i dokumentacja dla programisty
Summary(pt_BR):	Arquivos necessários para o desenvolvimento de aplicações com a interface glade
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Libraries, include files, etc you can use to develop libglade
applications.

%description devel -l es
Archivos de inclusión y bibliotecas necesarias para el desarrollo de
aplicaciones con glade.

%description devel -l pl
Biblioteki, pliki nag³ówkowe i dokumentacja dla programisty.

%description devel -l pt_BR
Arquivos de inclusão e bibliotecas para o desenvolvimento de
aplicações com a interface glade.

%package static
Summary:	Static libglade library
Summary(es):	Archivos estáticos necesarios para el desarrollo de aplicaciones con libglade
Summary(pl):	Biblioteka statyczna libglade
Summary(pt_BR):	Arquivos estáticos necessários para o desenvolvimento de aplicações com a interface glade
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libglade library.

%description static -l es
Archivos estáticos necesarias para el desarrollo de aplicaciones con
glade.

%description static -l pl
Biblioteka statyczna libglade.

%description static -l pt_BR
Bibliotecas estáticas para o desenvolvimento de aplicações com a
interface glade.

%prep
%setup -q
%patch1 -p1

%build
rm -f missing
libtoolize --copy --force
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c -f
%configure \
	--enable-bonobo \
	--disable-gnomedb
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

gzip -9nf AUTHORS ChangeLog NEWS README

install test-libglade.c *.glade $RPM_BUILD_ROOT/usr/src/examples/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
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
%{_pkgconfigdir}/*
%{_includedir}/libglade-1.0
%{_aclocaldir}/*

/usr/src/examples/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
