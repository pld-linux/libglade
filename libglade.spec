#
# Conditional build:
# _without_gnome	- without gnome package (gnome/gnomedb/bonobo libs)
#			  and w/o gnome/gnomedb/bonobo support in libglade-config
#
Summary:	libglade library
Summary(es):	El libglade permite que usted cargue archivos del interfaz del glade
Summary(pl):	Biblioteka do �adowania definicji interfejsu generowanego programem glade
Summary(pt_BR):	Esta biblioteca permite carregar arquivos da interface glade
Summary(ru):	���������� libglade ��� �������� ����������� ������������
Summary(uk):	��̦����� libglade ��� ������������ ��������Ӧ� �����������
Name:		libglade
Version:	0.17
Release:	12
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/libglade/%{name}-%{version}.tar.gz
Patch0:		%{name}-use_AM_GNU_GETTEXT.patch
Patch1:		%{name}-gtkdoc-scanobj-nogtkinit.patch
Patch2:		%{name}-clist-gettext.patch
Patch3:		%{name}-fixquote.patch
Patch4:		%{name}-gnomedb.patch
Patch5:		%{name}-nognome.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
%{!?_without_gnome:BuildRequires:	bonobo-devel >= 0.28}
BuildRequires:	gettext-devel
%{!?_without_gnome:BuildRequires:	gnome-db-devel >= 0.2.96}
%{!?_without_gnome:BuildRequires:	gnome-libs-devel}
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libxml-devel >= 1.7.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_gtkdocdir	%{_defaultdocdir}/gtk-doc/html

%description
The libglade library allows you to load user interfaces which are
stored externally into your program. This allows for alteration of the
interface without recompilation of the program. The interfaces can
also be edited with GLADE. Currently libglade supports all of the
widgets in current releases, keyboard accelerators and automatic
signal connection.

%description -l es
El libglade permite que usted cargue archivos del interfaz del glade
en tiempo de ejecuci�n.

%description -l pl
Biblioteka libglade umo�liwia dynamiczne �adowanie definicji
interfejsu u�ytkownika generowanego za pomoc� programu glade. Taka
separacja definicji interfejsu umo�liwia prac� nad nim bez
konieczno�ci rekompilacji programu.

%description -l pt_BR
O libglade permite carregar, em tempo de execu��o, arquivos da
interface glade. N�o � necess�rio ter o glade instalado, mas esta � a
melhor maneira de criar os arquivos de interface.

%description -l ru
���������� libglade ��������� ��������� � ���� �������� ����������
������������, ���������� �� ������� �����. ��� ��������� ������
��������� ��� �������������� ���������. ���������� ����� �����
��������������� ��� ������ GLADE. ������ libglade ������������ ���
�������, ������������ ������������ � �������������� ����������
����������.

%description -l uk
��̦����� libglade ������Ѥ ������������� � ���� �������� ����������
�����������, �� ���Ҧ������� � ���Φ������ ���̦. �� ������Ѥ
�ͦ������ ��������� ��� �������Ц��æ� ��������. ���������� ������
����� ������������ �� ��������� GLADE. ����ڦ libglade Ц�����դ �Ӧ
צ�����, ���צ����Φ ������������ �� ����������� ��������� �'�������.

%package devel
Summary:	Libraries, includes, etc to develop libglade applications
Summary(es):	Archivos necesarios para el desarrollo de aplicaciones con libglade
Summary(pl):	Biblioteki, pliki nag��wkowe i dokumentacja dla programisty
Summary(pt_BR):	Arquivos necess�rios para o desenvolvimento de aplica��es com a interface glade
Summary(ru):	����� ��� ���������� �������� � �������������� libglade
Summary(uk):	����� ��� �������� ������� � ������������� libglade
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk-doc-common
Requires:	libxml-devel

%description devel
Libraries, include files, etc you can use to develop libglade
applications.

%description devel -l es
Archivos de inclusi�n y bibliotecas necesarias para el desarrollo de
aplicaciones con glade.

%description devel -l pl
Biblioteki, pliki nag��wkowe i dokumentacja dla programisty.

%description devel -l pt_BR
Arquivos de inclus�o e bibliotecas para o desenvolvimento de
aplica��es com a interface glade.

%description devel -l ru
����� libglade-devel �������� �����, ����������� ��� ����������
�������, ������������ libglade.

%description devel -l uk
����� libglade-devel ͦ����� �����, ����Ȧ�Φ ��� �������� �������, ��
�������������� libglade.

%package static
Summary:	Static libglade library
Summary(es):	Archivos est�ticos necesarios para el desarrollo de aplicaciones con libglade
Summary(pl):	Biblioteka statyczna libglade
Summary(pt_BR):	Arquivos est�ticos necess�rios para o desenvolvimento de aplica��es com a interface glade
Summary(ru):	����������� ���������� ��� ���������� ������� � �������������� libglade
Summary(uk):	������Φ ¦�̦����� ��� �������� ������� � ������������� libglade
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libglade library.

%description static -l es
Archivos est�ticos necesarias para el desarrollo de aplicaciones con
glade.

%description static -l pl
Biblioteka statyczna libglade.

%description static -l pt_BR
Bibliotecas est�ticas para o desenvolvimento de aplica��es com a
interface glade.

%description static -l ru
����� libglade-devel-static �������� ����������� ����������, �������
����� ������������ ��� ���������� �������, ��������� libglade.

%description static -l uk
����� libglade-devel-static ͦ����� ������Φ ¦�̦�����, �˦ �����
��������������� ��� �������� �������, �� ���������� libglade.

%package gnome
Summary:	GNOME-dependent libglade libraries
Summary(pl):	Biblioteki libglade zale�ne od GNOME
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description gnome
GNOME-dependent libglade libraries: libglade-gnome, libglade-bonobo,
libglade-gnomedb.

%description gnome -l pl
Biblioteki libglade zale�ne od GNOME: libglade-gnome, libglade-bonobo,
libglade-gnomedb.

%package gnome-devel
Summary:	GNOME-dependent libglade development files
Summary(pl):	Pliki dla programist�w libglade zale�ne od GNOME
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}
Requires:	%{name}-gnome = %{version}
Requires:	bonobo-devel
Requires:	gnome-db-devel
Requires:	gnome-libs-devel

%description gnome-devel
GNOME-dependent libglade development files.

%description gnome-devel -l pl
Pliki dla programist�w libglade zale�ne od GNOME.

%package gnome-static
Summary:	Static GNOME-dependent libglade libraries
Summary(pl):	Statyczne biblioteki libglade zale�ne od GNOME
Group:		X11/Development/Libraries
Requires:	%{name}-gnome-devel = %{version}

%description gnome-static
Static versions of GNOME-dependent libglade libraries: libglade-gnome,
libglade-bonobo, libglade-gnomedb.

%description gnome-static -l pl
Statyczne wersje bibliotek libglade zale�nych od GNOME:
libglade-gnome, libglade-bonobo, libglade-gnomedb.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
touch po/POTFILES.in
aclocal -I macros
%{__autoconf}
%{__automake}
%configure \
	%{!?_without_gnome:--enable-bonobo --enable-gnomedb} \
	%{?_without_gnome:--without-gnome}
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
%attr(755,root,root) %{_libdir}/libglade.la
%{_pkgconfigdir}/libglade.pc
%{_includedir}/libglade-1.0
%{_aclocaldir}/*
%{_gtkdocdir}/*
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libglade.a

%if %{?_without_gnome:0}%{!?_without_gnome:1}
%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglade-*.so.*.*

%files gnome-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglade-*.so
%attr(755,root,root) %{_libdir}/libglade-*.la
# here - because it's for gnome-config and version built with gnome
# is useless when libglade-gnome-devel is not installed
%attr(755,root,root) %{_libdir}/libgladeConf.sh
%{_pkgconfigdir}/libglade-*.pc

%files gnome-static
%defattr(644,root,root,755)
%{_libdir}/libglade-*.a
%endif
