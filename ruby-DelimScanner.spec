%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
Summary:	A loose Ruby port of Text::Balanced
Summary(pl):	Swobodny port Text::Balanced dla jêzyka Ruby
Name:		ruby-DelimScanner
Version:	1.2
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://dev.faeriemud.org/~deveiant/RecDescentParser/lib/DelimScanner.rb?dl=1
# NoSource0-md5:	0b117164a34732e950713b60bc4a722e
URL:	http://dev.faeriemud.org/~deveiant/RecDescentParser/lib/DelimScanner.rb
BuildRequires:	ruby
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A derivative of StringScanner that can scan for delimited constructs
in addition to regular expressions. It is a loose port of the
Text::Balanced module for Perl by Damian Conway.

%description -l pl
Pochodna StringScannera potrafi±ca wyszukiwaæ ograniczone konstrukcje
oprócz wyra¿eñ regularnych. Jest to swobodny port modu³u Perla
Text::Balanced Damiana Conwaya.

%prep
%setup -c -T

%build
cp %{SOURCE0} DelimScanner.rb
rdoc -o rdoc DelimScanner.rb
rdoc --ri -o ri DelimScanner.rb

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

install -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{ruby_rubylibdir}/DelimScanner.rb

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
