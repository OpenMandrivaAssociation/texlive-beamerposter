Name:		texlive-beamerposter
Version:	54512
Release:	2
Summary:	Extend beamer and a0poster for custom sized posters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamerposter
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerposter.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerposter.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables the user to use beamer style operations on
a canvas of the sizes provided by a0poster; font scaling is
available (using packages such as type1cm if necessary). In
addition, the package allows the user to benefit from the nice
colour box handling and alignment provided by the beamer class
(for example, with rounded corners and shadows). Good looking
posters may be created very rapidly. Features include: -
scalable fonts using the fp and type1cm packages; - posters in
A-series sizes, and custom sizes like double A0 are possible; -
still applicable to custom beamer slides, e.g. 16:9 slides for
a wide-screen (i.e. 1.78 aspect ratio); - orientation may be
portrait or landscape; - a 'debug mode' is provided.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/beamerposter
%doc %{_texmfdistdir}/doc/latex/beamerposter

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
