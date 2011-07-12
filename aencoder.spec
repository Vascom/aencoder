Name:           aencoder           
Version:        0.99.5
Release:        2%{?dist}.R
Summary:        Graphic mencoder frontend for recoding video for Android devices

License:        GPLv2
URL:            http://github.com/goletsa/aEncoder
Source0:        https://github.com/downloads/goletsa/aEncoder/aEncoder_%{version}_linux.tar.gz
Patch00:        simple.patch


Requires:       mencoder
Requires:       tk >= 8.5
Requires:       tcl >= 8.5
Requires:       gpac >= 0.4.4      


BuildArch:      noarch


%description
Graphic mencoder frontend for recoding video for Android devices    


%prep
%setup -q -n aEncoder_%{version}_linux
%patch00 -p1


%build
echo "Nothing to build"


%install
rm -rf $RPM_BUILD_ROOT

# File install
%{__install} -pD -m644 %{_builddir}/aEncoder_%{version}_linux/aEncoder.tcl \
    $RPM_BUILD_ROOT%{_bindir}/aencoder

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(755,root,root)
%config(noreplace) %{_bindir}/aencoder


%doc


%changelog
* Tue Jul  12 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.99.5-2.R
- using original archive and add patch to it

* Thu Jul  08 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.99.5-1.R
- initial build
- moved all functionality to one file
