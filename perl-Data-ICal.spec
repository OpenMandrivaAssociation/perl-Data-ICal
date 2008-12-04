Summary:        Generates iCalendar (RFC 2445) calendar files
Name:           perl-Data-ICal
Version:        0.13
Release:        %mkrel 1
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Data-ICal/
Source0:        http://www.cpan.org/authors/id/J/JE/JESSE/Data-ICal-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Class::ReturnValue)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Text::vFile::asData)
# rpm doesn't catch this
Requires:       perl(Class::Accessor)
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A Data::ICal object represents a VCALENDAR object as defined in the
iCalendar protocol (RFC 2445, MIME type "text/calendar"), as implemented in
many popular calendaring programs such as Apple's iCal.

%prep

%setup -q -n Data-ICal-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

