#
# Conditional build:
%bcond_with	gnome	# gnome packages (gnome/gnomedb/bonobo libs)
#			  and gnome/gnomedb/bonobo support in libglade-config
%bcond_without	bonobo	# bonobo libs
#			  and bonobo support in libglade-config
%bcond_with	gnomedb	# gnomedb libs
#			  and gnomedb support in libglade-config
#
%if !%{with gnome}
%undefine	with_bonobo
%undefine	with_gnomedb
%endif
Summary:	libglade library
Summary(es.UTF-8):	El libglade permite que usted cargue archivos del interfaz del glade
Summary(pl.UTF-8):	Biblioteka do ładowania definicji interfejsu generowanego programem glade
Summary(pt_BR.UTF-8):	Esta biblioteca permite carregar arquivos da interface glade
Summary(ru.UTF-8):	Библиотека libglade для загрузки интерфейсов пользователя
Summary(uk.UTF-8):	Бібліотека libglade для завантаження інтерфейсів користувача
Name:		libglade
Version:	0.17
Release:	23
Epoch:		1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libglade/0.17/%{name}-%{version}.tar.gz
# Source0-md5:	38b2e2cfd813783fe157617813bfe3b3
Patch0:		%{name}-use_AM_GNU_GETTEXT.patch
Patch1:		%{name}-gtkdoc-scanobj-nogtkinit.patch
Patch2:		%{name}-clist-gettext.patch
Patch3:		%{name}-fixquote.patch
Patch4:		%{name}-gnomedb.patch
Patch5:		%{name}-nognome.patch
Patch6:		%{name}-am18.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	bison
%{?with_bonobo:BuildRequires:	bonobo-devel >= 0.28}
BuildRequires:	gettext-devel >= 0.11.5
%{?with_gnomedb:BuildRequires:	gnome-db-devel >= 0.2.96}
%{?with_gnome:BuildRequires:	gnome-libs-devel}
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libxml-devel >= 1.7.2
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libglade library allows you to load user interfaces which are
stored externally into your program. This allows for alteration of the
interface without recompilation of the program. The interfaces can
also be edited with GLADE. Currently libglade supports all of the
widgets in current releases, keyboard accelerators and automatic
signal connection.

%description -l es.UTF-8
El libglade permite que usted cargue archivos del interfaz del glade
en tiempo de ejecución.

%description -l pl.UTF-8
Biblioteka libglade umożliwia dynamiczne ładowanie definicji
interfejsu użytkownika generowanego za pomocą programu glade. Taka
separacja definicji interfejsu umożliwia pracę nad nim bez
konieczności rekompilacji programu.

%description -l pt_BR.UTF-8
O libglade permite carregar, em tempo de execução, arquivos da
interface glade. Não é necessário ter o glade instalado, mas esta é a
melhor maneira de criar os arquivos de interface.

%description -l ru.UTF-8
Библиотека libglade позволяет загружать в вашу програму интерфейсы
пользователя, хранящиеся во внешнем файле. Это позволяет менять
интерфейс без перекомпиляции программы. Интерфейсы могут также
редактироваться при помощи GLADE. Сейчас libglade поддерживает все
виджеты, клавиатурные акселераторы и автоматическое сигнальное
соединение.

%description -l uk.UTF-8
Бібліотека libglade дозволяє завантажувати в вашу програму інтерфейси
користувача, що зберігаються в зовнішньому файлі. Це дозволяє
змінювати інтерфейс без перекомпіляції програми. Інтерфейси можуть
також редагуватися за допомогою GLADE. Наразі libglade підтримує всі
віджети, клавіатурні акселератори та автоматичне сигнальне з'єднання.

%package devel
Summary:	Libraries, includes, etc to develop libglade applications
Summary(es.UTF-8):	Archivos necesarios para el desarrollo de aplicaciones con libglade
Summary(pl.UTF-8):	Biblioteki, pliki nagłówkowe i dokumentacja dla programisty
Summary(pt_BR.UTF-8):	Arquivos necessários para o desenvolvimento de aplicações com a interface glade
Summary(ru.UTF-8):	Файлы для разработки программ с использованием libglade
Summary(uk.UTF-8):	Файли для розробки програм з використанням libglade
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gtk-doc-common
Requires:	libxml-devel

%description devel
Libraries, include files, etc you can use to develop libglade
applications.

%description devel -l es.UTF-8
Archivos de inclusión y bibliotecas necesarias para el desarrollo de
aplicaciones con glade.

%description devel -l pl.UTF-8
Biblioteki, pliki nagłówkowe i dokumentacja dla programisty.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão e bibliotecas para o desenvolvimento de
aplicações com a interface glade.

%description devel -l ru.UTF-8
Пакет libglade-devel содержит файлы, необходимые для разработки
програм, использующих libglade.

%description devel -l uk.UTF-8
Пакет libglade-devel містить файли, необхідні для розробки програм, що
використовують libglade.

%package static
Summary:	Static libglade library
Summary(es.UTF-8):	Archivos estáticos necesarios para el desarrollo de aplicaciones con libglade
Summary(pl.UTF-8):	Biblioteka statyczna libglade
Summary(pt_BR.UTF-8):	Arquivos estáticos necessários para o desenvolvimento de aplicações com a interface glade
Summary(ru.UTF-8):	Статические библиотеки для разработки програм с использованием libglade
Summary(uk.UTF-8):	Статичні бібліотеки для розробки програм з використанням libglade
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libglade library.

%description static -l es.UTF-8
Archivos estáticos necesarias para el desarrollo de aplicaciones con
glade.

%description static -l pl.UTF-8
Biblioteka statyczna libglade.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para o desenvolvimento de aplicações com a
interface glade.

%description static -l ru.UTF-8
Пакет libglade-devel-static содержит статичнские библиотеки, которые
можно использовать для разработки програм, требующих libglade.

%description static -l uk.UTF-8
Пакет libglade-devel-static містить статичні бібліотеки, які можна
використовувати для розробки програм, що потребують libglade.

%package gnome
Summary:	libglade-gnome library
Summary(pl.UTF-8):	Biblioteka libglade-gnome
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnome
libglade-gnome library.

%description gnome -l pl.UTF-8
Biblioteki libglade-gnome.

%package gnome-devel
Summary:	libglade-gnome development files
Summary(pl.UTF-8):	Pliki dla programistów libglade-gnome
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	%{name}-gnome = %{epoch}:%{version}-%{release}
Requires:	gnome-libs-devel

%description gnome-devel
libglade-gnome development files.

%description gnome-devel -l pl.UTF-8
Pliki dla programistów używających libglade-gnome.

%package gnome-static
Summary:	Static libglade-gnome library
Summary(pl.UTF-8):	Statyczna biblioteka libglade-gnome
Group:		X11/Development/Libraries
Requires:	%{name}-gnome-devel = %{epoch}:%{version}-%{release}
Conflicts:	%{name}-static < 1:0.17-10

%description gnome-static
Static version of libglade-gnome library.

%description gnome-static -l pl.UTF-8
Statyczna wersja biblioteki libglade-gnome.

%package gnomedb
Summary:	libglade-gnomedb library
Summary(pl.UTF-8):	Biblioteka libglade-gnomedb
Group:		X11/Libraries
Requires:	%{name}-gnome = %{epoch}:%{version}-%{release}

%description gnomedb
libglade-gnomedb library.

%description gnomedb -l pl.UTF-8
Biblioteka libglade-gnomedb.

%package gnomedb-devel
Summary:	libglade-gnomedb development files
Summary(pl.UTF-8):	Pliki dla programistów libglade-gnomedb
Group:		X11/Development/Libraries
Requires:	%{name}-gnome-devel = %{epoch}:%{version}-%{release}
Requires:	%{name}-gnomedb = %{epoch}:%{version}-%{release}
Requires:	gnome-db-devel

%description gnomedb-devel
libglade-gnomedb development files.

%description gnomedb-devel -l pl.UTF-8
Pliki dla programistów używających libglade-gnomedb.

%package gnomedb-static
Summary:	libglade-gnomedb static library
Summary(pl.UTF-8):	Statyczna biblioteka libglade-gnomedb
Group:		X11/Development/Libraries
Requires:	%{name}-gnomedb-devel = %{epoch}:%{version}-%{release}
Conflicts:	%{name}-gnome-static < 1:0.17-14

%description gnomedb-static
Static version of libglade-gnomedb library.

%description gnomedb-static -l pl.UTF-8
Statyczna wersja biblioteki libglade-gnomedb.

%package bonobo
Summary:	libglade-bonobo library
Summary(pl.UTF-8):	Biblioteka libglade-bonobo
Group:		X11/Libraries
Requires:	%{name}-gnome = %{epoch}:%{version}-%{release}

%description bonobo
libglade-bonobo library.

%description bonobo -l pl.UTF-8
Biblioteka libglade-bonobo.

%package bonobo-devel
Summary:	libglade-bonobo development files
Summary(pl.UTF-8):	Pliki dla programistów libglade-bonobo
Group:		X11/Development/Libraries
Requires:	%{name}-bonobo = %{epoch}:%{version}-%{release}
Requires:	%{name}-gnome-devel = %{epoch}:%{version}-%{release}
Requires:	bonobo-devel

%description bonobo-devel
libglade-bonobo development files.

%description bonobo-devel -l pl.UTF-8
Pliki dla programistów używających libglade-bonobo.

%package bonobo-static
Summary:	libglade-bonobo static library
Summary(pl.UTF-8):	Statyczna biblioteka libglade-bonobo
Group:		X11/Development/Libraries
Requires:	%{name}-bonobo-devel = %{epoch}:%{version}-%{release}
Conflicts:	%{name}-gnome-static < 1:0.17-14

%description bonobo-static
Static version of libglade-bonobo library.

%description bonobo-static -l pl.UTF-8
Statyczna wersja biblioteki libglade-bonobo.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%{__libtoolize}
%{__gettextize}
touch po/POTFILES.in
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	%{?with_bonobo:--enable-bonobo} \
	%{?with_gnomedb:--enable-gnomedb} \
	%{!?with_gnome:--without-gnome}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir} \
	HTML_DIR=%{_gtkdocdir}

install test-libglade.c *.glade $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

mv -f $RPM_BUILD_ROOT%{_gtkdocdir}/{libglade,libglade1}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   gnome -p /sbin/ldconfig
%postun gnome -p /sbin/ldconfig

%post	gnomedb -p /sbin/ldconfig
%postun	gnomedb -p /sbin/ldconfig

%post	bonobo -p /sbin/ldconfig
%postun	bonobo -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libglade.so.*.*

%files devel
%defattr(644,root,root,755)
# libglade-config is different when building with gnome (contains support for
# GNOME-dependent libs), but it doesn't break things like libgladeConf.sh do
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libglade.so
%{_libdir}/libglade.la
%{_pkgconfigdir}/libglade.pc
%{_includedir}/libglade-1.0
%{_aclocaldir}/*
%{_gtkdocdir}/*
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libglade.a

%if %{with gnome}
%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglade-gnome.so.*.*

%files gnome-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglade-gnome.so
%{_libdir}/libglade-gnome.la
# here - because it's for gnome-config and always gives -lglade-gnome
%attr(755,root,root) %{_libdir}/libgladeConf.sh
%{_pkgconfigdir}/libglade-gnome.pc

%files gnome-static
%defattr(644,root,root,755)
%{_libdir}/libglade-gnome.a
%endif

%if %{with bonobo}
%files bonobo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglade-bonobo.so.*.*

%files bonobo-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglade-bonobo.so
%{_libdir}/libglade-bonobo.la
%{_pkgconfigdir}/libglade-bonobo.pc

%files bonobo-static
%defattr(644,root,root,755)
%{_libdir}/libglade-bonobo.a
%endif

%if %{with gnomedb}
%files gnomedb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglade-gnomedb.so.*.*

%files gnomedb-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglade-gnomedb.so
%{_libdir}/libglade-gnomedb.la
%{_pkgconfigdir}/libglade-gnomedb.pc

%files gnomedb-static
%defattr(644,root,root,755)
%{_libdir}/libglade-gnomedb.a
%endif
