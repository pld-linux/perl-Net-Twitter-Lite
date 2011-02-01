#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Net
%define		pnam	Twitter-Lite
%include	/usr/lib/rpm/macros.perl
Summary:	Net::Twitter::Lite - A perl interface to the Twitter API
#Summary(pl.UTF-8):
Name:		perl-Net-Twitter-Lite
Version:	0.10003
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MM/MMIMS/Net-Twitter-Lite-%{version}.tar.gz
# Source0-md5:	e0d90dfa6b057460164da36f09a6a75d
URL:		http://search.cpan.org/dist/Net-Twitter-Lite/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Crypt-SSLeay >= 0.50
BuildRequires:	perl-Encode
BuildRequires:	perl-JSON-Any >= 1.21
BuildRequires:	perl-Net-OAuth >= 0.25
BuildRequires:	perl-URI
BuildRequires:	perl-libwww >= 2.032
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a perl interface to the Twitter APIs. It uses the
same API definitions as Net::Twitter, but without the extra bells and
whistles and without the additional dependencies. Same great taste,
less filling.

This module is related to, but is not part of the Net::Twitter
distribution. It's API methods and API method documentation are
generated from Net::Twitter's internals. It exists for those who
cannot, or prefer not to install Moose and its dependencies.

You should consider upgrading to Net::Twitter for additional
functionality, finer grained control over features, full backwards
compatibility with older versions of Net::Twitter, and additional
error handling options.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL --skip \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Net/Twitter/*.pm
%dir %{perl_vendorlib}/Net/Twitter/Lite
%{perl_vendorlib}/Net/Twitter/Lite/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
