%global tl_name bithesis
%global tl_revision 79190

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.8.12
Release:	%{tl_revision}.1
Summary:	Templates for the Beijing Institute of Technology
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/bithesis
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bithesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bithesis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bithesis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package establishes a simple and easy-to-use LaTeX template for
Beijing Institute of Technology dissertations, including general
undergraduate theses and master theses.

