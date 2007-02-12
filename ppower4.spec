Summary:	Java program to preparing presentations using PDF
Summary(pl.UTF-8):   Program w Javie do przygotowywania prezentacji z użyciem PDF
Name:		ppower4
Version:	0.8.4
Release:	1
Group:		Applications/Publishing
License:	GPL
Source0:	http://www-sp.iti.informatik.tu-darmstadt.de/software/ppower4/pp4.jar
# Source0-md5:	8446628c1cef06ffefbbc7173fab24a0
Source1:	http://www-sp.iti.informatik.tu-darmstadt.de/software/ppower4/pp4sty.zip
# Source1-md5:	593e5d058fe9e3c77548dc7c5b0a37f6
Source2:	http://www-sp.iti.informatik.tu-darmstadt.de/software/ppower4/report.pdf
# Source2-md5:	ab378abdfaf08051e666916a91709aad
Source3:	%{name}
URL:		http://www-sp.iti.informatik.tu-darmstadt.de/software/ppower4/
BuildRequires:	unzip
Requires:	jre
Requires:	tetex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ppower4 is an Java program for prepering profesional presentations
using pdflatex.

%description -l pl.UTF-8
ppower4 jest programem napisanym w Javie do przygotowywania
profesjonalnych prezentacji z użyciem pdflatex.

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p %{_bindir}/mktexlsr
%postun	-p %{_bindir}/mktexlsr

%files
%defattr(644,root,root,755)
%{_datadir}/%{name}
%{_datadir}/texmf/tex/latex/%{name}
%attr(755,root,root) %{_bindir}/*
%doc %{_docdir}/%{name}/*
