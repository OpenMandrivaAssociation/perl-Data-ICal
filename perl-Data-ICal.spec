%define module Data-ICal

Summary:        Generates iCalendar (RFC 2445) calendar files
Name:           perl-%{module}
Version:        0.15
Release:        %mkrel 1
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Data-ICal/
Source:         http://www.cpan.org/modules/by-module/Data/%{module}-%{version}.tar.gz
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
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
A Data::ICal object represents a VCALENDAR object as defined in the
iCalendar protocol (RFC 2445, MIME type "text/calendar"), as implemented in
many popular calendaring programs such as Apple's iCal.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

#make pure_install PERL_INSTALL_ROOT=%{buildroot}

#find %{buildroot} -type f -name .packlist -exec rm -f {} \;
#find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

#chmod -R u+w %{buildroot}/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

