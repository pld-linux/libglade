Summary:	libglade library
Summary(es):	El libglade permite que usted cargue archivos del interfaz del glade
Summary(pl):	Biblioteka do Ёadowania definicji interfejsu generowanego programem glade
Summary(pt_BR):	Esta biblioteca permite carregar arquivos da interface glade
Summary(ru):	Библиотека libglade для загрузки интерфейсов пользователя
Summary(uk):	Б╕бл╕отека libglade для завантаження ╕нтерфейс╕в користувача
Name:		libglade
Version:	0.17
Release:	7
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/libglade/%{name}-%{version}.tar.gz
Patch0:		%{name}-use_AM_GNU_GETTEXT.patch
Patch1:		%{name}-gtkdoc-scanobj-nogtkinit.patch
Patch2:		%{name}-clist-gettext.patch
Patch3:		%{name}-fixquote.patch
Patch4:		%{name}-gnomedb.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	bison
BuildRequires:	bonobo-devel >= 0.28
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libxml-devel >= 1.7.2
BuildRequires:	gnome-db-devel >= 0.2.96
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
The libglade library allows you to load user interfaces which are
stored externally into your program. This allows for alteration of the
interface without recompilation of the program. The interfaces can
also be edited with GLADE. Currently libglade supports all of the
widgets in current releases, keyboard accelerators and automatic
signal connection.

%description -l es
El libglade permite que usted cargue archivos del interfaz del glade
en tiempo de ejecuciСn.

%description -l pl
Biblioteka libglade umo©liwia dynamiczne Ёadowanie definicji
interfejsu u©ytkownika generowanego za pomoc╠ programu glade. Taka
separacja definicji interfejsu umo©liwia pracЙ nad nim bez
konieczno╤ci rekompilacji programu.

%description -l pt_BR
O libglade permite carregar, em tempo de execuГЦo, arquivos da
interface glade. NЦo И necessАrio ter o glade instalado, mas esta И a
melhor maneira de criar os arquivos de interface.

%description -l ru
Библиотека libglade позволяет загружать в вашу програму интерфейсы
пользователя, хранящиеся во внешнем файле. Это позволяет менять
интерфейс без перекомпиляции программы. Интерфейсы могут также
редактироваться при помощи GLADE. Сейчас libglade поддерживает все
виджеты, клавиатурные акселераторы и автоматическое сигнальное
соединение.

%description -l uk
Б╕бл╕отека libglade дозволя╓ завантажувати в вашу програму ╕нтерфейси
користувача, що збер╕гаються в зовн╕шньому файл╕. Це дозволя╓
зм╕нювати ╕нтерфейс без перекомп╕ляц╕╖ програми. ╤нтерфейси можуть
також редагуватися за допомогою GLADE. Нараз╕ libglade п╕дтриму╓ вс╕
в╕джети, клав╕атурн╕ акселератори та автоматичне сигнальне з'╓днання.

%package devel
Summary:	Libraries, includes, etc to develop libglade applications
Summary(es):	Archivos necesarios para el desarrollo de aplicaciones con libglade
Summary(pl):	Biblioteki, pliki nagЁСwkowe i dokumentacja dla programisty
Summary(pt_BR):	Arquivos necessАrios para o desenvolvimento de aplicaГУes com a interface glade
Summary(ru):	Файлы для разработки программ с использованием libglade
Summary(uk):	Файли для розробки програм з використанням libglade
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Libraries, include files, etc you can use to develop libglade
applications.

%description devel -l es
Archivos de inclusiСn y bibliotecas necesarias para el desarrollo de
aplicaciones con glade.

%description devel -l pl
Biblioteki, pliki nagЁСwkowe i dokumentacja dla programisty.

%description devel -l pt_BR
Arquivos de inclusЦo e bibliotecas para o desenvolvimento de
aplicaГУes com a interface glade.

%description devel -l ru
Пакет libglade-devel содержит файлы, необходимые для разработки
програм, использующих libglade.

%description devel -l uk
Пакет libglade-devel м╕стить файли, необх╕дн╕ для розробки програм, що
використовують libglade.

%package static
Summary:	Static libglade library
Summary(es):	Archivos estАticos necesarios para el desarrollo de aplicaciones con libglade
Summary(pl):	Biblioteka statyczna libglade
Summary(pt_BR):	Arquivos estАticos necessАrios para o desenvolvimento de aplicaГУes com a interface glade
Summary(ru):	Статические библиотеки для разработки програм с использованием libglade
Summary(uk):	Статичн╕ б╕бл╕отеки для розробки програм з використанням libglade
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libglade library.

%description static -l es
Archivos estАticos necesarias para el desarrollo de aplicaciones con
glade.

%description static -l pl
Biblioteka statyczna libglade.

%description static -l pt_BR
Bibliotecas estАticas para o desenvolvimento de aplicaГУes com a
interface glade.

%description static -l ru
Пакет libglade-devel-static содержит статичнские библиотеки, которые
можно использовать для разработки програм, требующих libglade.

%description static -l uk
Пакет libglade-devel-static м╕стить статичн╕ б╕бл╕отеки, як╕ можна
використовувати для розробки програм, що потребують libglade.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
rm -f missing
libtoolize --copy --force
gettextize --copy --force
aclocal -I macros
%{__autoconf}
%{__automake}
%configure \
	--enable-bonobo \
	--enable-gnomedb
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

install test-libglade.c *.glade $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%docdir %{_datadir}/gnome/html/libglade
%doc %{_datadir}/gnome/html/libglade/*
%doc %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libgladeConf.sh
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_pkgconfigdir}/*
%{_includedir}/libglade-1.0
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
