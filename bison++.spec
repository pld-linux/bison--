Summary:	Generate a parser in C or C++ from BNF notation
Summary(pl):	Generowanie parser�w w C lub C++ z notacji BNF
Name:		bison++
Version:	1.21.5
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.iecc.com/pub/file/bison++flex++/b++5.tar.z
# Source0-md5:	482ba52685d2d91bd708a952a1a6e143
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Based on bison version 1.19, compatible with bison but with C++
support. Bison is a general-purpose parser generator that converts a
grammar description for an LALR (BNF-like) context free grammar into a
C/C++ program to parse that grammar. Once you are proficient with
bison++ you can generate a wide range of language parsers, from those
used in simple desk calculators to complex programming languages.

%description -l pl
bison++ jest oparty na bisonie w wersji 1.19, kompatybilny z bisonem,
ale z obs�ug� C++. Bison to generator parser�w og�lnego przeznaczenia,
konwertuj�cy opis gramatyki dla gramatyk bezkontekstowych LALR (w
stylu BNF) na program C/C++ analizuj�cy t� gramatyk�. Po nabraniu
bieg�o�ci w obs�udze bisona++ mo�na generowa� szeroki zakres parser�w
j�zyk�w, od tych u�ywanych w prostych kalkulatorach biurowych, do
z�o�onych j�zyk�w programowania.

%prep
%setup -q -c

%build
%configure

%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall} \
	mandir=$RPM_BUILD_ROOT%{_mandir}/man1 \
	datadir=$RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc REFERENCES ChangeLog
%attr(755,root,root) %{_bindir}/bison++
%{_datadir}/%{name}
%{_mandir}/man?/*
