Name:           oostat
Version:        0.1.0
Release:        1%{?dist}
Summary:        Prints comprehensive file metadata, inode attributes, timestamps, and permissions.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oostat
Source0:        oostat-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oostat is a sovereign, capability-bounded INODE INSPECTOR written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oostat
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oostat-uninstall

%files
/usr/bin/oostat
/usr/bin/oostat-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
