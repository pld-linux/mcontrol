Summary:	ALSA MIDI sequencer client
Summary(pl.UTF-8):	Klient sekwencera ALSA MIDI
Name:		mcontrol
Version:	0.1.03
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://personal.telefonica.terra.es/web/soudfontcombi/%{name}-%{version}.tar.gz
# Source0-md5:	e64081cf0fa19bccd74c2efdc5922a2f
URL:		http://personal.telefonica.terra.es/web/soudfontcombi/mcontrol.html
BuildRequires:	alsa-lib-devel
BuildRequires:	fltk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mcontrol is a ALSA MIDI sequencer client and brings the possibility to
assign up to twelve "simultaneous" MIDI control messages for each
controller in your MIDI keyboard (Modulation Wheel, Breath Controller,
Foot Controller, Pitch Bend and After Touch).

%description -l pl.UTF-8
Mcontrol to klient sekwencera ALSA MIDI dający możliwość jednoczesnego
przypisania do dwunastu rozkazów MIDI dla każdego kontrolera twojej
klawiatury MIDI.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mcontrol
%dir %{_datadir}/mcontrol
%{_datadir}/mcontrol/*
