Name:		texlive-bithesis
Version:	65314
Release:	1
Summary:	Templates for the Beijing Institute of Technology
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bithesis
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bithesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bithesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bithesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package establishes a simple and easy-to-use LaTeX
template for Beijing Institute of Technology dissertations,
including general undergraduate theses and master theses.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/bithesis
%{_texmfdistdir}/tex/latex/bithesis
%doc %{_texmfdistdir}/doc/latex/bithesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
