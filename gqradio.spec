Summary:	X11 tuner radio
Summary(pl):	Tuner radiowy dla X11
Name:		gqradio
Version:	1.9.1
Release:	3
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/gqmpeg/%{name}-%{version}.tar.gz
# Source0-md5:	88a8cea682ff2c597d41eb21e9a4534d
Patch0:		%{name}-desktop.patch
URL:		http://gqmpeg.sourceforge.net/radio.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gqradio is fine radio tuner working under X11.

%description -l pl
Gqradio jest wspania³ym tunerem radiowym pracuj±cym w ¶rodowisku
graficznym.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README SKIN-SPECS TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_datadir}/gqradio
