Name:		texlive-l3build
Version:	64987
Release:	2
Summary:	A testing and building system for (La)TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/l3build
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3build.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3build.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3build.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The build system supports testing and building LaTeX3 code, on
Linux, Mac OS X and Windows systems. The package offers: A unit
testing system for (La)TeX code (whether kernel code or
contributed packages); A system for typesetting package
documentation; and An automated process for creating CTAN
releases. The package is essentially independent of other
material released by the LaTeX3 team, and may be updated on a
different schedule.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/texmf-dist/source/latex/l3build
%{_texmfdistdir}/texmf-dist/tex/latex/l3build
%{_texmfdistdir}/texmf-dist/scripts/l3build
%doc %{_texmfdistdir}/texmf-dist/doc/latex/l3build
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/l3build.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/l3build.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
