%global tl_name l3build
%global tl_revision 79643

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A testing and building system for (La)TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/l3build
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/l3build.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/l3build.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/l3build.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(l3build.bin)
Requires:	texlive(luatex)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The build system supports testing and building LaTeX3 code, on Linux,
Mac OS X and Windows systems. The package offers: A unit testing system
for (La)TeX code (whether kernel code or contributed packages); A system
for typesetting package documentation; and An automated process for
creating CTAN releases. The package is essentially independent of other
material released by the LaTeX3 team, and may be updated on a different
schedule.

