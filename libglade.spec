Summary:	libglade library
Summary(es):	El libglade permite que usted cargue archivos del interfaz del glade
Summary(pl):	Biblioteka do ≥adowania definicji interfejsu generowanego programem glade
Summary(pt_BR):	Esta biblioteca permite carregar arquivos da interface glade
Name:		libglade
Version:	0.17
Release:	2
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/‚…¬Ã…œ‘≈À…
Group(uk):	X11/‚¶¬Ã¶œ‘≈À…
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/libglade/%{name}-%{version}.tar.gz
Patch0:		%{name}-use_AM_GNU_GETTEXT.patch
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
en tiempo de ejecuciÛn.

%description -l pl
Biblioteka libglade umoøliwia dynamiczne ≥adowanie definicji
interfejsu uøytkownika generowanego za pomoc± programu glade. Taka
separacja definicji interfrejsu umozliwia placÍ nad nim bez
konieczno∂ci rekompilacji programu.

%description -l pt_BR
O libglade permite carregar, em tempo de execuÁ„o, arquivos da
interface glade. N„o È necess·rio ter o glade instalado, mas esta È a
melhor maneira de criar os arquivos de interface.

%package devel
Summary:	Libraries, includes, etc to develop libglade applications
Summary(es):	Archivos necesarios para el desarrollo de aplicaciones con libglade
Summary(pl):	Biblioteki, pliki nag≥Ûwkowe i dokumentacja dla programisty
Summary(pt_BR):	Arquivos necess·rios para o desenvolvimento de aplicaÁıes com a interface glade
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Libraries, include files, etc you can use to develop libglade
applications.

%description -l es devel
Archivos de inclusiÛn y bibliotecas necesarias para el desarrollo de
aplicaciones con glade.

%description -l pl devel
Biblioteki, pliki nag≥Ûwkowe i dokumentacja dla programisty.

%description -l pt_BR devel
Arquivos de inclus„o e bibliotecas para o desenvolvimento de
aplicaÁıes com a interface glade.

%package static
Summary:	Static libglade library
Summary(es):	Archivos est·ticos necesarios para el desarrollo de aplicaciones con libglade
Summary(pl):	Biblioteka statyczna libglade
Summary(pt_BR):	Arquivos est·ticos necess·rios para o desenvolvimento de aplicaÁıes com a interface glade
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description static
Static libglade library.

%description -l es static
Archivos est·ticos necesarias para el desarrollo de aplicaciones con
glade.

%description -l pl static
Biblioteka statyczna libglade.

%description -l pt_BR static
Bibliotecas est·ticas para o desenvolvimento de aplicaÁıes com a
interface glade.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
libtoolize --copy --force
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c
%configure \
	--enable-bonobo
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
%{_includedir}/glade
%{_aclocaldir}/*

/usr/src/examples/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
