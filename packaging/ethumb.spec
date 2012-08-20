#sbs-git:slp/pkgs/e/ethumb ethumb 1.0.0+svn.68464slp2+build01 eee5311dd71f4fde48a4838412f70490e5d70c0b

Name:       ethumb
Summary:    Thumbnail Generator Library
Version:    1.6.0+svn.73539slp2+build01
Release:    1
Group:      System/Libraries
License:    LGPLv2.1
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  eina-devel
BuildRequires:  evas-devel
BuildRequires:  ecore-devel
BuildRequires:  edje-devel
BuildRequires:  eet-devel
BuildRequires:  edje-bin
BuildRequires:  edbus-devel
BuildRequires:  libexif-devel

%description
Enlightenment thumbnailing library Thumbnailing library meant to replace epsilon

%package devel
Summary:    Thumbnail Generator Library (devel)
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Thumbnailing library meant to replace epsilon (devel)

%prep
%setup -q

%build
export CFLAGS+=" -fPIC"
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed"

%autogen --disable-static
%configure --disable-static
make %{?jobs:-j%jobs}

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libethumb*.so.*
/usr/share/dbus-1/services/org.enlightenment.Ethumb.service
/usr/share/ethumb/data/frames/default.edj
/usr/bin/ethumb
/usr/bin/ethumbd
/usr/bin/ethumbd_client
/usr/libexec/ethumbd_slave

%files devel
%defattr(-,root,root,-)
%{_includedir}/ethumb-1/*.h
%{_libdir}/libethumb*.so
%{_libdir}/pkgconfig/*.pc
