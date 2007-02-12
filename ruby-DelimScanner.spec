Summary:	A loose Ruby port of Text::Balanced
Summary(pl.UTF-8):   Swobodny port Text::Balanced dla języka Ruby
Name:		ruby-DelimScanner
Version:	1.2
Release:	2
License:	GPL
Group:		Development/Libraries
Source0:	http://dev.faeriemud.org/~deveiant/RecDescentParser/lib/DelimScanner.rb?dl=1
# NoSource0-md5:	0b117164a34732e950713b60bc4a722e
NoSource:	0
URL:		http://dev.faeriemud.org/~deveiant/RecDescentParser/lib/DelimScanner.rb
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby
#BuildArch:	noarch
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A derivative of StringScanner that can scan for delimited constructs
in addition to regular expressions. It is a loose port of the
Text::Balanced module for Perl by Damian Conway.

%description -l pl.UTF-8
Pochodna StringScannera potrafiąca wyszukiwać ograniczone konstrukcje
oprócz wyrażeń regularnych. Jest to swobodny port modułu Perla
Text::Balanced Damiana Conwaya.

%prep
%setup -q -cT
cp %{SOURCE0} DelimScanner.rb

%build
rdoc -o rdoc DelimScanner.rb
rdoc --ri -o ri DelimScanner.rb

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

install %{SOURCE0} $RPM_BUILD_ROOT%{ruby_rubylibdir}/DelimScanner.rb

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/DelimScanner.rb
%{ruby_ridir}/DelimScanner
%{ruby_ridir}/String/interpolate-i.yaml
%{ruby_ridir}/String/to_re-i.yaml
