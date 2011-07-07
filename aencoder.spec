Name:           aencoder           
Version:        0.99.5
Release:        1%{?dist}.R
Summary:        Graphic mencoder frontend for recoding video for Android devices

License:        GPLv2
URL:            http://github.com/goletsa/aEncoder
Source0:        aencoder


Requires:       mencoder
Requires:       tk >= 8.5
Requires:       tcl >= 8.5
Requires:       gpac >= 0.4.4      


BuildArch:      noarch


%description
Graphic mencoder frontend for recoding video for Android devices    


%prep
echo "Nothing to prep"


%build
echo "Nothing to build"


%install
rm -rf $RPM_BUILD_ROOT

# File install
%{__install} -pD -m644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_bindir}/aencoder

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(755,root,root)
%config(noreplace) %{_bindir}/aencoder


%doc


%changelog
* Thu Jul  08 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.99.5-1.R
- initial build
- moved all functionality to one file
