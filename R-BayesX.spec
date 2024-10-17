%global packname  BayesX
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          0.2.7
Release:          1
Summary:          R Utilities Accompanying the Software Package BayesX
Group:            Sciences/Mathematics
License:          GPL-2
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/BayesX_0.2-7.tar.gz
Requires:         R-akima R-shapefiles 
Requires:         R-sp R-colorspace R-coda R-splines 
Requires:         R-spdep 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-akima R-shapefiles
BuildRequires:    R-sp R-colorspace R-coda R-splines 
BuildRequires:    R-spdep 

%description
This package provides functionality for exploring and visualising
estimation results obtained with the software package BayesX for
structured additive regression. It also provides functions that allow to
read, write and manipulate map objects that are required in spatial
analyses performed with BayesX, a free software for estimating structured
additive regression models (http://www.stat.uni-muenchen.de/~bayesx).

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/help


%changelog
* Sun Feb 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2_5-1
+ Revision: 777134
- Import R-BayesX
- Import R-BayesX



