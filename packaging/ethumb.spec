Name:       ethumb
Summary:    Thumbnail Generator Library
Version:    0.1.1.svn60760
Release:    1
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
Source0:    %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(ecore)
BuildRequires:  pkgconfig(ecore-evas)
BuildRequires:  pkgconfig(ecore-file)
BuildRequires:  pkgconfig(edje)
BuildRequires:  pkgconfig(eina)
BuildRequires:  pkgconfig(evas)
BuildRequires:  pkgconfig(edbus)
BuildRequires:  edje-bin
BuildRequires: pkgconfig(libexif)

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
%{_includedir}/ethumb-0/*.h
%{_libdir}/libethumb*.so
%{_libdir}/pkgconfig/*.pc
