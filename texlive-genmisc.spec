# revision 27208
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-genmisc
Version:	20120807
Release:	8
Summary:	TeXLive genmisc package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/genmisc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive genmisc package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/genmisc/anti.tex
%{_texmfdistdir}/tex/generic/genmisc/apldef.tex
%{_texmfdistdir}/tex/generic/genmisc/arabic.tex
%{_texmfdistdir}/tex/generic/genmisc/backgrnd.tex
%{_texmfdistdir}/tex/generic/genmisc/balancedquotes.sty
%{_texmfdistdir}/tex/generic/genmisc/chessmin.tex
%{_texmfdistdir}/tex/generic/genmisc/compare.tex
%{_texmfdistdir}/tex/generic/genmisc/cropmark.sty
%{_texmfdistdir}/tex/generic/genmisc/cropmark.tex
%{_texmfdistdir}/tex/generic/genmisc/croptest.tex
%{_texmfdistdir}/tex/generic/genmisc/dayofweek.tex
%{_texmfdistdir}/tex/generic/genmisc/daytime.sty
%{_texmfdistdir}/tex/generic/genmisc/default.sty
%{_texmfdistdir}/tex/generic/genmisc/dow.tex
%{_texmfdistdir}/tex/generic/genmisc/emtrees.tex
%{_texmfdistdir}/tex/generic/genmisc/endnote.tex
%{_texmfdistdir}/tex/generic/genmisc/fakebold.tex
%{_texmfdistdir}/tex/generic/genmisc/hep.tex
%{_texmfdistdir}/tex/generic/genmisc/inscrutable.tex
%{_texmfdistdir}/tex/generic/genmisc/laps.tex
%{_texmfdistdir}/tex/generic/genmisc/letterspacing.tex
%{_texmfdistdir}/tex/generic/genmisc/longdiv.tex
%{_texmfdistdir}/tex/generic/genmisc/mandel.tex
%{_texmfdistdir}/tex/generic/genmisc/mathlig.tex
%{_texmfdistdir}/tex/generic/genmisc/nth.sty
%{_texmfdistdir}/tex/generic/genmisc/outerhbox.sty
%{_texmfdistdir}/tex/generic/genmisc/pagereference.tex
%{_texmfdistdir}/tex/generic/genmisc/quotation.tex
%{_texmfdistdir}/tex/generic/genmisc/ragged.sty
%{_texmfdistdir}/tex/generic/genmisc/random.tex
%{_texmfdistdir}/tex/generic/genmisc/ruler.tex
%{_texmfdistdir}/tex/generic/genmisc/selectpage.tex
%{_texmfdistdir}/tex/generic/genmisc/shadebox.tex
%{_texmfdistdir}/tex/generic/genmisc/swrule.sty
%{_texmfdistdir}/tex/generic/genmisc/underlin.tex
%{_texmfdistdir}/tex/generic/genmisc/undertilde.tex
%{_texmfdistdir}/tex/generic/genmisc/verbatim.tex
%{_texmfdistdir}/tex/generic/genmisc/weekday.sty
%{_texmfdistdir}/tex/generic/genmisc/wiggly.tex
%{_texmfdistdir}/tex/generic/genmisc/zip.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120807-1
+ Revision: 812271
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 752240
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718531
- texlive-genmisc
- texlive-genmisc
- texlive-genmisc
- texlive-genmisc

