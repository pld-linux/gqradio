Summary:	X11 tuner radio
Summary(pl):	X11 tuner radiowy
Name:		gqradio
Version:	0.4.1
Release:	1
License:	unknown (probably GPL)
Group:		X11/Applications/Multimedia
Source0:	http://prdownloads.sourceforge.net/gqmpeg/%{name}-%{version}.tar.gz
URL:		http://gqmpeg.sourceforge.net/radio.html
BuildRequires:	autoconf
BuildRequires:	automake=
BuildRequires:	gettext-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gtk+-decel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Gqradio is fine radio tuner working under X11.

%description -l pl
Gqradio jest wspanialym tunerem radiowym pracujacym w srodowisku
graficznym.

%prep
%setup -q

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Multimedia

gzip -9nf AUTHORS NEWS README SKIN-SPECS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Multimedia/*
%{_pixmapsdir}/*
