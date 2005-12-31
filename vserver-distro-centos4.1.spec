Summary:	VServer build template for CentOS 4.1
Summary(pl):	Szablon budowania VServera dla CentOS 4.1
Name:		vserver-distro-centos4.1
Version:	1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	%{name}.tar.gz
# Source0-md5:	47e4ea8f73434e6800562d7bb6c67302
URL:		http://linux-vserver.org/CentOS_HowTo
BuildRequires:	rpmbuild(macros) >= 1.213
Requires:	util-vserver-build
Requires:	yum
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VServer build template for CentOS 4.1.

%description -l pl
Szablon budowania VServera dla CentOS 4.1.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT
tar xzf %{SOURCE0}
%if "%{_lib}" != "lib"
mv usr/lib usr/%{_lib}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/util-vserver/distributions/centos4.1
%{_sysconfdir}/vservers/.distributions/centos4.1
