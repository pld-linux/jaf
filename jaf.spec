Summary:	JavaBeans (tm) Activation Framework
Summary(pl):	¦rodowisko aktywacyjne JavaBeans(tm)
Name:		jaf
Version:	1.0.2
Release:	1
License:	restricted (see LICENSE.txt)
Group:		Development/Languages/Java
Source0:	%{name}-1_0_2.zip
NoSource:	0
URL:		http://java.sun.com/products/javabeans/glasgow/jaf.html
Requires:	jre >= 1.1.6
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt RELNOTES.txt README.txt
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc demo docs
