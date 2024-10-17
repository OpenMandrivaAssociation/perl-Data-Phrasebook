# $Id: perl-Data-Phrasebook.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Barbie <barbie$cpan,org>

%define upstream_name Data-Phrasebook
%define upstream_version 0.34

Summary:	Base class for Phrasebook Models
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
License:	Artistic/GPL
Group:		Development/Perl
URL:		https://search.cpan.org/dist/Data-Phrasebook/
Source:		http://www.cpan.org/modules/by-module/Data/Data-Phrasebook-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl(JSON::PP) >= 2.272
BuildArch:	noarch

%description
Base class for Phrasebook Models.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%make

%install
make pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%files
%defattr(-, root, root, 0755)
%doc ChangeLog Changes INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Data::Phrasebook.3pm*
%doc %{_mandir}/man3/Data::Phrasebook::*.3pm*
%dir %{perl_vendorlib}/Data/
%{perl_vendorlib}/Data/Phrasebook/
%{perl_vendorlib}/Data/Phrasebook.pm
