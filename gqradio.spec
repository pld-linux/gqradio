Summary:	X11 tuner radio
Summary(pl.UTF-8):	Tuner radiowy dla X11
Name:		gqradio
Version:	1.9.2
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/gqmpeg/%{name}-%{version}.tar.gz
# Source0-md5:	10fded1c080cadd1b260a592772bcbb6
Patch0:		%{name}-desktop.patch
URL:		http://gqmpeg.sourceforge.net/radio.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gqradio is fine radio tuner working under X11.

%description -l pl.UTF-8
Gqradio jest wspaniałym tunerem radiowym pracującym w środowisku
graficznym.

%prep
%setup -q
%patch0 -p1

%build
glib-gettextize -c -f
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
