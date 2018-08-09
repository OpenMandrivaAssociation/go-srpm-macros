%global commit        4d469a3d37c21353fbd6bb306ce707dc4151fd1e
%global shortcommit   %(c=%{commit}; echo ${c:0:7})

Name:           go-srpm-macros
Version:        2
Release:        18%{?dist}
Summary:        RPM macros for building Golang packages for various architectures
Group:          Development/Libraries
License:        GPLv3+
Source0:	https://raw.githubusercontent.com/gofed/go-macros/master/rpm/macros.d/macros.go-srpm
BuildArch:      noarch
# for install command
BuildRequires:  coreutils

%description
The package provides macros for building projects in Go
on various architectures.

%prep

%build
# nothing to build, just for hooks

%install
install -m 644 -D %{SOURCE0} %{buildroot}%{_rpmconfigdir}/macros.d/macros.go-srpm

%files
%{_rpmconfigdir}/macros.d/macros.go-srpm
