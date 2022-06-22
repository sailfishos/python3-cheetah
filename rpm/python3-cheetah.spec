Name:           python3-cheetah
Version:        3.2.4
Release:        1
Summary:        Template engine and code-generator
License:        MIT
URL:            https://github.com/sailfishos/python3-cheetah
Source:         %{name}-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-markdown
BuildRequires:  python3-pygments
BuildRequires:  python3-setuptools

%description
Cheetah is an open source template engine and code generation tool,
written in Python. It can be used standalone or combined with other
tools and frameworks. Web development is its principle use, but
Cheetah is very flexible and is also being used to generate C++ game
code, Java, sql, form emails and even Python code.

%prep
%setup -q -n %{name}-%{version}/cheetah3

%build
export CHEETAH_USE_SETUPTOOLS=1
%{py3_build}

%install
rm -rf %{buildroot}
export CHEETAH_USE_SETUPTOOLS=1
%{py3_install}

%check
export PATH="%{buildroot}/%{_bindir}:$PATH"
export PYTHONPATH="%{buildroot}/%{python3_sitearch}"
%{buildroot}/%{_bindir}/cheetah test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%license LICENSE
%doc TODO
%{_bindir}/cheetah*
%{python3_sitearch}/Cheetah
%{python3_sitearch}/Cheetah*.egg-info
