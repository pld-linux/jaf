# NOTE:
#   - The JavaBeans Activation Framework 1.1.1 final release is included with the
#     Java SE 6 release and is also available separately.
#   - There is an alternative, free implementation of java-activation. See
#     java-gnu-activation.spec
%include	/usr/lib/rpm/macros.java
Summary:	JavaBeans (tm) Activation Framework
Summary(pl.UTF-8):	Środowisko aktywacyjne JavaBeans(tm)
Name:		jaf
Version:	1.1.1
Release:	1
License:	restricted (see LICENSE.txt)
Group:		Development/Languages/Java
# download through forms from http://java.sun.com/products/javabeans/jaf/downloads/index.html#download
Source0:	%{name}-%(echo %{version} | tr . _).zip
# NoSource0-md5:	e55a9e5a44eb55fa588d1020544226f1
NoSource:	0
URL:		http://java.sun.com/products/javabeans/jaf/index.jsp
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	jpackage-utils
Provides:	java-activation
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package javadoc
Summary:	Online manual for %{name}
Summary(pl.UTF-8):	Dokumentacja online do %{name}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for %{name}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{name}.

%description javadoc -l fr.UTF-8
Javadoc pour %{name}.

%package demo
Summary:	Demo for %{name}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu %{name}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%description demo -l pl.UTF-8
Pliki demonstracyjne i przykłady dla pakietu %{name}.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
install activation.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/activation.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jaf.jar

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a docs/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt RELNOTES.txt README.txt distributionREADME.txt
%{_javadir}/activation.jar
%{_javadir}/jaf.jar
%{_javadir}/jaf-%{version}.jar

%files doc
%defattr(644,root,root,755)
%doc docs/JAF-*

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
