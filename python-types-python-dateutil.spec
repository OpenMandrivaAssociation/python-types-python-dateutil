%define oname types_python_dateutil

Name:		python-types-python-dateutil
Version:	2.9.0.20251115
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/t/%{oname}/%{oname}-%{version}.tar.gz
Summary:	Typing stubs for python-dateutil
URL:		https://pypi.org/project/types-python-dateutil/
License:	Apache-2.0
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Typing stubs for python-dateutil

%prep
%autosetup -n %{oname}-%{version} -p1
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%files
%{python_sitelib}/dateutil-stubs
%{python_sitelib}/%{oname}-%{version}.dist-info
