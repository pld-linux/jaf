Summary: 	JavaBeans (tm) Activation Framework
Summary(pl):	¦rodowisko aktywacyjne JavaBeans(tm)
Name:		jaf
Version:	1.0.1
Release:	1
License:	Read LICENSE.txt!
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Source0:	jaf1_0_1.zip
URL:		http://java.sun.com/products/javabeans/glasgow/jaf.html
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
JavaBeans (tm) Activation Framework.

%description -l pl
¦rodowisko aktywacyjne JavaBeans(tm) Activation Framework.

%package doc
Summary:	JavaBeans (tm) Activation Framework documentation
Summary(pl):	Dokumentacja do JavaBeans(tm) Activation Framework
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java

%description doc
JavaBeans (tm) Activation Framework documentation.

%description doc -l pl
Dokumentacja do ¶rodowiska JavaBeans(tm) Activation Framework.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
install *.jar $RPM_BUILD_ROOT%{_javalibdir}

gzip -9nf LICENSE.txt RELNOTES.txt README.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{_javalibdir}
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc demo docs
