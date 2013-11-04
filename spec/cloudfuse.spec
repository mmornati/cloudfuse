Name:           cloudfuse 
Version:        1.0
Release:        1%{?dist}
Summary:        Cloudfuse is a FUSE application which provides access to Rackspace's Cloud Files (or any installation of Swift).

Group:          Application
License:        GPLv3
URL:            https://github.com/redbo/cloudfuse
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc make fuse-devel curl-devel libxml2-devel openssl-devel
#Requires:       
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}.

%prep
%setup -n %{name}


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/bin/cloudfuse
%doc


%changelog
