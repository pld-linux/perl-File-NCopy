#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	NCopy
Summary:	File::NCopy - Copy file, file Copy file[s] | dir[s], dir
Name:		perl-File-NCopy
Version:	0.34
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
# 0.34 not in mirrors.
#Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar
Source0:	http://search.cpan.org/CPAN/authors/id/M/MZ/MZSANFORD/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a2633eb0f3f8a6906303e709a35af26f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::NCopy::copy copies files to directories, or a single file to
another file.  You can also use a reference to a file handle if you wish
whem doing a file to file copy.  The functionality is very similar to
cp.  If the argument is a directory to directory copy and the
recursive flag is set then it is done recursively like cp -R.
In fact it behaves like cp on Unix for the most part.
If called in array context, an array of successful copies is returned,
otherwise the number of succesful copies is returned.  If passed a file
handle, it's difficult to make sure the file we are copying isn't the
same that we are copying to, since by opening the file in write mode it
gets pooched.  To avoid this use file names instead, if at all possible,
especially for the to file.  If passed a file handle, it is not closed
when copy returns, files opened by copy are closed.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/File/*.pm
%{_mandir}/man3/*
