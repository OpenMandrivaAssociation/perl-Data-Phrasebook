# $Id: perl-Data-Phrasebook.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Barbie <barbie$cpan,org>

%define upstream_name Data-Phrasebook

Summary:	Base class for Phrasebook Models
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.34
Release:	1
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Data-Phrasebook/
Source:		http://www.cpan.org/modules/by-module/Data/Data-Phrasebook-0.34.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More) >= 0.47
BuildArch:	noarch

%description
Base class for Phrasebook Models.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%make

%install
make pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%files
%defattr(-, root, root, 0755)
%doc Artistic COPYING ChangeLog Changes INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Data::Phrasebook.3pm*
%doc %{_mandir}/man3/Data::Phrasebook::*.3pm*
%dir %{perl_vendorlib}/Data/
%{perl_vendorlib}/Data/Phrasebook/
%{perl_vendorlib}/Data/Phrasebook.pm

%changelog
* Tue Sep 27 2011 Leonardo Coelho <leonardoc@mandriva.com> 0.29-1mdv2012.0
+ Revision: 701500
- first mandriva version
- Created package structure for 'perl-Data-Phrasebook'.


