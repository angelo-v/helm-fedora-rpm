# Helm RPM Package

This repository provides a specfile to build a Fedora RPM package for Kubernetes Helm.

# Prerequisites 

    dnf install fedora-packager fedora-review

# Build

To build the RPM run

    ./build.sh

## Install Helm

To install the RPM run

    dnf install x86_64/helm-*.rpm

# Clean up

To delete all build artefacts run

    ./clean.sh
