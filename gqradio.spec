Summary:	X11 tuner radio
Summary(pl):	X11 tuner radiowy
Name:		gqradio
Version:	0.6.0
Release:	1
License:	GPL (?)
Group:		X11/Applications/Sound
Source0:	http://prdownloads.sourceforge.net/gqmpeg/%{name}-%{version}.tar.gz
URL:		http://gqmpeg.sourceforge.net/radio.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Gqradio is fine radio tuner working under X11.

%description -l pl
Gqradio jest wspaniałym tunerem radiowym pracującym w środowisku
graficznym.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Multimedia \
	desktop_DATA=gqradio.desktop \
	icondir=%{_pixmapsdir} \
	icon_DATA=gqradio.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README SKIN-SPECS TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Multimedia/*
%{_pixmapsdir}/*
%{_datadir}/*
