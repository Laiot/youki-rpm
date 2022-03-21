Name: youki
Version: 0.0.2
Release:        1%{?dist}
Summary: A container runtime in Rust

License: Apache-2.0 License
URL: https://github.com/containers/youki
Source0: https://github.com/containers/youki

BuildRequires: rust-packaging


ExclusiveArch: %{rust_arches}

%description


%prep
%autosetup
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%configure
%make_build


%install
%make_install


%check


%files
%license
%doc


%changelog

