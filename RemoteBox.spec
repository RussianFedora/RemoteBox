%define name RemoteBox
%define version 0.5
%define unmangled_version 0.5
%define release 1

Summary:	Open Source VirtualBox Client with Remote Management
Name:		RemoteBox
Version:	0.5
Release:	1%{?dist}

License:	GPLv2 
Group:		Applications/System
Url:		http://remotebox.knobgoblin.org.uk/
Source0:	http://remotebox.knobgoblin.org.uk/downloads/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	remotebox
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch:	noarch
BuildRequires:	desktop-file-utils

Requires:	perl >= 5.8 
Requires:	perl-Gtk2 >= 1.203 
Requires:	perl-SOAP-Lite >= 0.710.10
Requires:	perl-libwww-perl
Requires:	rdesktop

AutoReq:	no

%description
RemoteBox is a graphical (GTK) VirtualBox client, which lets you administer 
guests or virtual machines which reside on a remote server or even your 
local machine if desired.
VirtualBox 3.2.x (not OSE version) installed on the server.


%prep
%setup -q


%build


%install
rm -rf %{buildroot}
install -d %{buildroot}%{_datadir}/%{name}
cp -r share %{buildroot}%{_datadir}/%{name}/
cp remotebox %{buildroot}%{_datadir}/%{name}

install -d %{buildroot}%{_docdir}/%{name}-%{version}
cp docs/* %{buildroot}%{_docdir}/%{name}-%{version}

desktop-file-install --vendor "" \
    --dir %{buildroot}%{_datadir}/applications \
    --add-category Network \
    --add-category X-Fedora \
    %{SOURCE1}

install -d %{buildroot}%{_datadir}/pixmaps
install -m644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

mkdir -p %{buildroot}%{_bindir}
install -m755 %{SOURCE3} %{buildroot}%{_bindir}/remotebox


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%{_docdir}/%{name}-%{version}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/*
%{_bindir}/remotebox


%changelog
* Mon Nov 22 2010 mx < sergey dot mihailov at gmail dot com > - 0.5-1
- Initial package for RPM Fusion
