Summary:	java program to preparing presentations using pdf
Summary(pl):	Program w java do przygotowywania prezentacji z u¿yciem pdf
Name:		ppower4
Version:	0.8.4
Release:	1
Group:		Applications/Publishing
Group(de):	Applikationen/Publizieren
Group(pl):	Aplikacje/Publikowanie
License:	GPL
Source0:	http://www-sp.iti.informatik.tu-darmstadt.de/software/ppower4/pp4.jar
Source1:	http://www-sp.iti.informatik.tu-darmstadt.de/software/ppower4/pp4sty.zip
Source2:	http://www-sp.iti.informatik.tu-darmstadt.de/software/ppower4/report.pdf
Source3:	%{name}
URL:		http://www-sp.iti.informatik.tu-darmstadt.de/software/ppower4/
BuildRequires:	unzip
Requires:	java
Requires:	tetex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ppower4 is an java program for prepering profesional presentations
using pdflatex.

%description -l	pl
ppower4 jest programem napisanym w java do przygotowywania
profesjonalnych prezentacji z u¿yciem pdflatex.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{name}
install -d $RPM_BUILD_ROOT%{_bindir}
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{name}
cd $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{name}
unzip %{SOURCE1}
install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/%{name}/
install %{SOURCE2} $RPM_BUILD_ROOT%{_docdir}/%{name}/ 
install %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}

%post -p %{_bindir}/mktexlsr
%postun -p %{_bindir}/mktexlsr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/%{name}/*
%{_datadir}/texmf/tex/latex/%{name}/*
%attr(755,root,root) %{_bindir}/*
%doc %{_docdir}/%{name}/*
