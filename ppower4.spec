Summary:	java program to preparing presentations using pdf.
Name:		ppower4	
Version:	0.8.4
Release:	1
Group:		Applications/Publishing/	
Copyright:	GPL
Vendor:         PLD
Source0:	http://www-sp.iti.informatik.tu-darmstadt.de/software/ppower4/pp4.jar
Source1:	http://www-sp.iti.informatik.tu-darmstadt.de/software/ppower4/pp4sty.zip
Source2:	http://www-sp.iti.informatik.tu-darmstadt.de/software/ppower4/report.pdf
Source3:	ppower4
URL:		http://www-sp.iti.informatik.tu-darmstadt.de/software/ppower4/
BuildPrereq:	unzip
Requires:	java	
Prereq:         tetex
Prereq:         /usr/bin/mktexlsr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ppower4 is an java program for prepering profesional presentations using pdflatex.

%prep
%build
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

%post
/usr/bin/mktexlsr

%postun
/usr/bin/mktexlsr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/%{name}/*
%{_datadir}/texmf/tex/latex/%{name}/*
%attr(755,root,root) %{_bindir}/*

%doc %{_docdir}/%{name}/*



%changelog
