#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	NCopy
Summary:	File::NCopy - Copy file, file Copy file[s] | dir[s], dir
Summary(pl.UTF-8):   File::NCopy - kopiowanie pliku do pliku lub plików do katalogów
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
another file. You can also use a reference to a file handle if you
wish when doing a file to file copy. The functionality is very similar
to cp. If the argument is a directory to directory copy and the
recursive flag is set then it is done recursively like cp -R. In fact
it behaves like cp on Unix for the most part. If called in array
context, an array of successful copies is returned, otherwise the
number of succesful copies is returned. If passed a file handle, it's
difficult to make sure the file we are copying isn't the same that we
are copying to, since by opening the file in write mode it gets
pooched. To avoid this use file names instead, if at all possible,
especially for the to file. If passed a file handle, it is not closed
when copy returns, files opened by copy are closed.

%description -l pl.UTF-8
File::NCopy::copy kopiuje pliki do katalogów lub pojedynczy plik do
innego pliku. Można także używać referencji do uchwytu pliku przy
tworzeniu kopii pliku. Funkcjonalność jest bardzo podobna do cp. Jeśli
argumentem jest kopiowanie katalogu do katalogu i ustawiona jest flaga
rekurencji, kopiowanie jest rekurencyjne podobnie jak przy cp -R. W
rzeczywistości moduł zachowuje się w większości jak uniksowe cp. Przy
wywołaniu w kontekście tablicy zwracana jest tablica pomyślnie
wykonanych kopii, a w przeciwnym wypadku - ich liczba. Jeśli podano
uchwyt pliku, trudno się upewnić, że plik do którego kopiujemy nie
jest tym samym, jako że przy otwarciu pliku w trybie zapisu jest on
nadpisywany. Aby tego uniknąć, należy używać nazw plików, w
szczególności dla pliku docelowego. Jeśli podano uchwyt pliku, nie
jest on zamykany, natomiast zamykane są pliki otwierane przy
kopiowaniu.

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
