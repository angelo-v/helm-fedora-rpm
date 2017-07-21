Name:    helm
Version: 2.5.0
Release: 1%{?dist}
Summary: The Kubernetes Package Manager 

URL: https://helm.sh
License: ASL 2.0
Source0: https://storage.googleapis.com/kubernetes-helm/helm-v%{version}-linux-amd64.tar.gz 

%description
Helm helps you manage Kubernetes applications — Helm Charts helps you define, install, and upgrade even the most complex Kubernetes application.

%prep
%autosetup -n linux-amd64

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 helm %{buildroot}/%{_bindir}

%files
%{_bindir}/helm

%changelog
