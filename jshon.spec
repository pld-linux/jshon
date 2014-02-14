Summary:	Jshon is a JSON parser designed for maximum convenience within the shell
Name:		jshon
Version:	20131105
Release:	1
License:	MIT
Group:		Applications/System
URL:		http://kmkeen.com/jshon/
Source0:	http://kmkeen.com/%{name}/jshon.tar.gz
# Source0-md5:	4b1cae2237db068ee4738789286a0409
BuildRequires:	jansson
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jshon is a JSON parser designed for maximum convenience within the
shell

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}
%{_mandir}/man1/jshon.1*
