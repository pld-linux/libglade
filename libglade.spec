# Note that this is NOT a relocatable package
%define name	libglade
%define ver	0.3
%define RELEASE 1
%define rel     %{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}
%define prefix	/usr

Summary: libglade library
Name: %name
Version: %ver
Release: %rel
Copyright: LGPL
Group: X11/Libraries
Source: ftp://ftp.daa.com.au/pub/james/gnome/libglade-%{ver}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Packager: James Henstridge
URL: http://www.gnome.org
Docdir: %{prefix}/doc

Requires: gtk+
Requires: libxml >= 1.3

%description
This library allows you to load user interfaces in your program, which are
stored externally.  This allows alteration of the interface without
recompilation of the program.

The interfaces can also be edited with GLADE.

%package devel
Summary: Libraries, includes, etc to develop libglade applications
Group: X11/libraries
Requires: libglade gtk+-devel libxml-devel

%description devel
Libraries, include files, etc you can use to develop libglade applications.


%changelog

* Sun Nov  1 1998 James Henstridge <james@daa.com.au>

- Updated the dependencies of the devel package, so users must have gtk+-devel.

* Sun Oct 25 1998 James Henstridge <james@daa.com.au>

- Initial release 0.0.1

%prep
%setup

%build
# Needed for snapshot releases.
if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=%prefix 
else
  CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix 
fi

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install


%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog NEWS README COPYING
%{prefix}/lib/lib*.so.*

%files devel
%defattr(-, root, root)

%{prefix}/bin/*
%{prefix}/lib/lib*.so
%{prefix}/lib/*a
%{prefix}/include/glade/*
%{prefix}/share/aclocal/*
%{prefix}/lib/libgladeConf.sh

%doc test-libglade.c
%doc *.glade
%doc %{prefix}/share/gnome/html/libglade/*
