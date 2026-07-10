%global tl_name beamerposter
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.13
Release:	%{tl_revision}.1
Summary:	Extend beamer and a0poster for custom sized posters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamerposter
License:	lppl gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerposter.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerposter.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package enables the user to use beamer style operations on a canvas
of the sizes provided by a0poster; font scaling is available (using
packages such as type1cm if necessary). In addition, the package allows
the user to benefit from the nice colour box handling and alignment
provided by the beamer class (for example, with rounded corners and
shadows). Good looking posters may be created very rapidly. Features
include: scalable fonts using the fp and type1cm packages; posters in
A-series sizes, and custom sizes like double A0 are possible; still
applicable to custom beamer slides, e.g. 16:9 slides for a wide-screen
(i.e. 1.78 aspect ratio); orientation may be portrait or landscape; a
'debug mode' is provided.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamerposter
%dir %{_datadir}/texmf-dist/tex/latex/beamerposter
%doc %{_datadir}/texmf-dist/doc/latex/beamerposter/README
%doc %{_datadir}/texmf-dist/doc/latex/beamerposter/beamerposter.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerposter/beamerposter.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamerposter/example.tex
%{_datadir}/texmf-dist/tex/latex/beamerposter/beamerposter.sty
%{_datadir}/texmf-dist/tex/latex/beamerposter/beamerthemeAachen.sty
%{_datadir}/texmf-dist/tex/latex/beamerposter/beamerthemeI6dv.sty
%{_datadir}/texmf-dist/tex/latex/beamerposter/beamerthemeI6pd.sty
%{_datadir}/texmf-dist/tex/latex/beamerposter/beamerthemeI6pd2.sty
%{_datadir}/texmf-dist/tex/latex/beamerposter/beamerthemeI6td.sty
%{_datadir}/texmf-dist/tex/latex/beamerposter/beamerthemeZH.sty
