Name:       ethumb
Summary:    Thumbnail Generator Library
Version:    1.6.0+svn.75994slp2+build09
Release:    1
Group:      System/Libraries
License:    LGPL-2.1+
URL:        http://www.enlightenment.org/
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
#BuildRequires:  libexif-devel


%description
Enlightenment thumbnailing library Thumbnailing library meant to replace epsilon


%package devel
Summary:    Thumbnail Generator Library (devel)
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}


%description devel
Thumbnailing library meant to replace epsilon (devel)


%package tools
Summary:    Thumbnail Generator Library (tools)
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}
Provides:   %{name}-bin
Obsoletes:  %{name}-bin


%description tools
Thumbnailing library meant to replace epsilon (tools)

%prep
%setup -q


%build
export CFLAGS+=" -fvisibility=hidden -fPIC -Wall"
export LDFLAGS+=" -fvisibility=hidden -Wl,--hash-style=both -Wl,--as-needed"


%autogen --disable-static
make %{?jobs:-j%jobs}


%install
%make_install
mkdir -p %{buildroot}/%{_datadir}/license
cp %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/%{_datadir}/license/%{name}
cp %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/%{_datadir}/license/%{name}-tools


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%{_libdir}/libethumb*.so.*
%{_datadir}/dbus-1/services/org.enlightenment.Ethumb.service
%{_datadir}/ethumb/data/frames/default.edj
%{_bindir}/ethumbd
%{_libexecdir}/ethumbd_slave
%{_datadir}/license/%{name}
%manifest %{name}.manifest


%files devel
%defattr(-,root,root,-)
%{_includedir}/ethumb-1/*.h
%{_libdir}/libethumb*.so
%{_libdir}/pkgconfig/*.pc


%files tools
%{_bindir}/ethumb
%{_bindir}/ethumbd_client
%{_datadir}/license/%{name}-tools
%manifest %{name}-tools.manifest
