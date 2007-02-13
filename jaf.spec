Summary:	JavaBeans (tm) Activation Framework
Summary(pl.UTF-8):	Środowisko aktywacyjne JavaBeans(tm)
Name:		jaf
Version:	1.1
Release:	1
License:	restricted (see LICENSE.txt)
Group:		Development/Languages/Java
# download through froms from URL
Source0:	%{name}-%(echo %{version} | tr . _)-fr.zip
# NoSource0-md5:	7423eb6831ba82e7d1f10956eb2bd0d3
NoSource:	0
URL:		http://java.sun.com/products/javabeans/glasgow/jaf.html
Requires:	jre >= 1.1.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
JavaBeans (tm) Activation Framework.

%description -l pl.UTF-8
Środowisko aktywacyjne JavaBeans(tm) Activation Framework.

%package doc
Summary:	JavaBeans (tm) Activation Framework documentation
Summary(pl.UTF-8):	Dokumentacja do JavaBeans(tm) Activation Framework
Group:		Development/Languages/Java

%description doc
JavaBeans (tm) Activation Framework documentation.

%description doc -l pl.UTF-8
Dokumentacja do środowiska JavaBeans(tm) Activation Framework.

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
