Name:		python-types-python-dateutil
Version:	2.9.0.20241206
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/t/types-python-dateutil/types_python_dateutil-%{version}.tar.gz
Summary:	Typing stubs for python-dateutil
URL:		https://pypi.org/project/types-python-dateutil/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Typing stubs for python-dateutil

%files
%{py_sitedir}/dateutil-stubs
%{py_sitedir}/types_python_dateutil-*.*-info
