# revision 17066
# category Package
# catalog-ctan /macros/latex/contrib/beamerposter
# catalog-date 2010-02-16 13:45:15 +0100
# catalog-license lppl
# catalog-version 1.07
Name:		texlive-beamerposter
Version:	1.07
Release:	1
Summary:	Extend beamer and a0poster for custom sized posters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamerposter
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerposter.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerposter.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/beamerposter/beamerposter.sty
%doc %{_texmfdistdir}/doc/latex/beamerposter/README
%doc %{_texmfdistdir}/doc/latex/beamerposter/beamerposter.pdf
%doc %{_texmfdistdir}/doc/latex/beamerposter/beamerposter.tex
%doc %{_texmfdistdir}/doc/latex/beamerposter/example.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
