%define upstream_name     Data-ICal
%define upstream_version  0.18

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Generates iCalendar (RFC 2445) calendar files
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Data-ICal/
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Class::ReturnValue)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::LongString)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Text::vFile::asData)
BuildArch:	noarch
# rpm doesn't catch this
Requires:	perl(Class::Accessor)

%description
A Data::ICal object represents a VCALENDAR object as defined in the
iCalendar protocol (RFC 2445, MIME type "text/calendar"), as implemented in
many popular calendaring programs such as Apple's iCal.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
sed -i s,"auto_install();",, Makefile.PL
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

