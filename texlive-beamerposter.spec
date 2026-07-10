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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
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

