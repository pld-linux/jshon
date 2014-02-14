Summary:	Jshon is a JSON parser designed for maximum convenience within the shell
Name:		jshon
Version:	20131010
Release:	1
License:	MIT
Group:		Applications/System
URL:		http://kmkeen.com/jshon/
# Source0:	http://kmkeen.com/%{name}/jshon.tar.gz
Source0:	ftp://ftp.debian.org/debian/pool/main/j/jshon/jshon_20131010.orig.tar.gz
# Source0-md5:	f939755699cd152379f97a8a9e2fe7c4
BuildRequires:	jansson
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jshon is a JSON parser designed for maximum convenience within the
shell

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

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
