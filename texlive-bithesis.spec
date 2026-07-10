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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package establishes a simple and easy-to-use LaTeX template for
Beijing Institute of Technology dissertations, including general
undergraduate theses and master theses.

%prep
%setup -q -c -a1 -a2
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
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bithesis
%dir %{_datadir}/texmf-dist/source/latex/bithesis
%dir %{_datadir}/texmf-dist/tex/latex/bithesis
%doc %{_datadir}/texmf-dist/doc/latex/bithesis/README.md
%doc %{_datadir}/texmf-dist/doc/latex/bithesis/bithesis-doc-src.zip
%doc %{_datadir}/texmf-dist/doc/latex/bithesis/bithesis-handbook-graduate.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bithesis/bithesis-handbook-undergraduate.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bithesis/bithesis.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bithesis/contributing-zh.md
%doc %{_datadir}/texmf-dist/doc/latex/bithesis/contributing.md
%doc %{_datadir}/texmf-dist/doc/latex/bithesis/dtx-style.sty
%doc %{_datadir}/texmf-dist/source/latex/bithesis/bithesis-beamer.dtx
%doc %{_datadir}/texmf-dist/source/latex/bithesis/bithesis-doc-style.dtx
%doc %{_datadir}/texmf-dist/source/latex/bithesis/bithesis-finale.dtx
%doc %{_datadir}/texmf-dist/source/latex/bithesis/bithesis-report.dtx
%doc %{_datadir}/texmf-dist/source/latex/bithesis/bithesis-thesis-exports.dtx
%doc %{_datadir}/texmf-dist/source/latex/bithesis/bithesis-thesis.dtx
%doc %{_datadir}/texmf-dist/source/latex/bithesis/bithesis.dtx
%doc %{_datadir}/texmf-dist/source/latex/bithesis/bithesis.ins
%{_datadir}/texmf-dist/tex/latex/bithesis/bitbeamer.cls
%{_datadir}/texmf-dist/tex/latex/bithesis/bithesis.cls
%{_datadir}/texmf-dist/tex/latex/bithesis/bitreport.cls
