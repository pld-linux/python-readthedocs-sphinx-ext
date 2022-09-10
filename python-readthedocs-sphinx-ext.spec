#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx extension for Read the Docs overrides
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do modyfikacji Read the Docs
Name:		python-readthedocs-sphinx-ext
Version:	2.1.8
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/readthedocs-sphinx-ext/
Source0:	https://files.pythonhosted.org/packages/source/r/readthedocs-sphinx-ext/readthedocs-sphinx-ext-%{version}.tar.gz
# Source0-md5:	ecaaee440cb231bab66328c09b120567
URL:		https://pypi.org/project/readthedocs-sphinx-ext/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Sphinx
BuildRequires:	python-jinja2 >= 2.9
BuildRequires:	python-requests
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-jinja2 >= 2.9
BuildRequires:	python3-requests
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module adds extensions that make Sphinx easier to use.

%description -l pl.UTF-8
Ten moduł dodaje rozszerzenia ułatwiające używanie Sphinksa.

%package -n python3-readthedocs-sphinx-ext
Summary:	Sphinx extension for Read the Docs overrides
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do modyfikacji Read the Docs
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-readthedocs-sphinx-ext
This module adds extensions that make Sphinx easier to use.

%description -n python3-readthedocs-sphinx-ext -l pl.UTF-8
Ten moduł dodaje rozszerzenia ułatwiające używanie Sphinksa.

%prep
%setup -q -n readthedocs-sphinx-ext-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/readthedocs_ext
%{py_sitescriptdir}/readthedocs_sphinx_ext-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-readthedocs-sphinx-ext
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/readthedocs_ext
%{py3_sitescriptdir}/readthedocs_sphinx_ext-%{version}-py*.egg-info
%endif
