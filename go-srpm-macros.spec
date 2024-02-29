%global commit		4d469a3d37c21353fbd6bb306ce707dc4151fd1e
%global shortcommit	%(c=%{commit}; echo ${c:0:7})

Name:		go-srpm-macros
Version:	2
Release:	29
Summary:	RPM macros for building Golang packages for various architectures
License:	GPLv3+
Source0:	https://github.com/gofed/go-macros/archive/%{commit}/go-macros-%{shortcommit}.tar.gz
Patch0:		add_all_archs.patch
Patch1:		go-srpm-macros-2-forgemeta.patch
# for install command
BuildRequires:	coreutils

BuildArch:	noarch

%description
The package provides macros for building projects in Go
on various architectures.

%files
%{_rpmconfigdir}/macros.d/macros.go-srpm

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n go-macros-%{commit}

%build
# nothing to build, just for hooks

%install
install -pm 0644 -D rpm/macros.d/macros.go-srpm %{buildroot}%{_rpmconfigdir}/macros.d/macros.go-srpm

