Name:          xmms-mplayer
Summary:       MPlayer plugin for XMMS
Version:       0.5
Release:       15%{?dist}
License:       GPL+
Group:         Applications/Multimedia
URL:           http://xmmsmplayer.sourceforge.net
Source:        http://downloads.sourceforge.net/xmmsmplayer/xmmsmplayer-%{version}.tar.gz

BuildRequires: libtool 
BuildRequires: xmms-devel
Requires:      mplayer
Requires:      xmms

%description
Xmms-MPlayer is an input plugin for XMMS that allows you to play all audio and
video files in XMMS. Thus, allowing you to use XMMS as a playlist frontend for
MPlayer. This project aims at merely being a connecting link between XMMS and 
MPlayer. It does not intend to get involved into any processing of video files,
all that is left to MPlayer.

%prep
%setup -q -n xmmsmplayer-%{version}

# To compile the shared version of the library:
sed -i 's|XMMS_LIBS=\(.*\)|XMMS_LIBS="-L%{_libdir} \1"|' aclocal.m4
cat /dev/null > acinclude.m4
aclocal
autoconf
libtoolize --force
automake --add-missing

%build
%configure 
%make_build

%install
%make_install

# Kill .la files
rm -f %{buildroot}%{_libdir}/xmms/Input/*.la

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/xmms/Input/libxmmsmplayer.*

%changelog
* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.5-13
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.5-10
- Fix build issue

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 03 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.5-7
- Fix F22 FTBFS rhbz#3620

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon May 27 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.5-5
- Rebuilt for x264/FFmpeg

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.5-4
- Mass rebuilt for Fedora 19 Features

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu May 21 2009 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.5-2
- Use "install -p".
- Add [ -s NEWS ] && exit 1

* Thu Apr 02 2009 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.5-1
- Initial build.
