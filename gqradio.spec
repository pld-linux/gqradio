Summary:	X11 tuner radio
Summary(pl):	X11 tuner radiowy
Name:		gqradio
Version:	0.4.0
Release:	1
License:	unknown (probably GPL)
Group:		Applications/Mutimedia
######		Unknown group!
BuildRequires:	gettext
BuildRequires:	gettext-devel
Source0:	http://prdownloads.sourceforge.net/gqmpeg/%{name}-%{version}.tar.gz
URL:		http://gqmpeg.sourceforge.net/radio.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


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

%configure -q

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
gzip -9nf TODO README ChangeLog NEWS AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {TODO,README,ChangeLog,NEWS,AUTHORS}.gz
%attr(755,root,root) %{_bindir}/*
