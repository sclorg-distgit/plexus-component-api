%{?scl:%scl_package plexus-component-api}
%{!?scl:%global pkg_name %{name}}

%define project_version 1.0-alpha-15

Name:           %{?scl_prefix}plexus-component-api
Version:        1.0
Release:        0.22.alpha15.1%{?dist}
Summary:        Plexus Component API

License:        ASL 2.0
URL:            http://svn.codehaus.org/plexus/plexus-containers/tags/plexus-containers-1.0-alpha-15/plexus-component-api/
#svn export http://svn.codehaus.org/plexus/plexus-containers/tags/plexus-containers-1.0-alpha-15/plexus-component-api/ plexus-component-api-1.0-alpha-15
#tar zcf plexus-component-api-1.0-alpha-15.tar.gz plexus-component-api-1.0-alpha-15/
Source0:        %{pkg_name}-%{project_version}.tar.gz

BuildArch: noarch

BuildRequires:  java-devel >= 1:1.6.0
BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}maven-assembly-plugin
BuildRequires:  %{?scl_prefix}maven-resources-plugin
BuildRequires:  %{?scl_prefix}maven-plugin-plugin
BuildRequires:  %{?scl_prefix}plexus-classworlds
# requires as parent pom
BuildRequires:  %{?scl_prefix}plexus-containers

%description
Plexus Component API

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{project_version}

%build
%mvn_build

%install
%mvn_install

%pre javadoc
# workaround for rpm bug, can be removed in F-20
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{pkg_name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{pkg_name}) %{_javadocdir}/%{pkg_name} || :

%files -f .mfiles
%dir %{_javadir}/%{pkg_name}

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 1.0-0.22.alpha15.1
- Automated package import and SCL-ization

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.22.alpha15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Michael Simacek <msimacek@redhat.com> - 1.0-0.21.alpha15
- Remove BR on site-plugin

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.20.alpha15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.19.alpha15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.18.alpha15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-0.17.alpha15
- Use Requires: java-headless rebuild (#1067528)

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.16.alpha15
- Fix unowned directory

* Mon Aug 12 2013 gil cattaneo <puntogil@libero.it> 1.0-0.15.alpha15
- fix rhbz#992803
- add missing BR plexus-containers

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.14.alpha15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 20 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-0.13.alpha15
- Update to latest guidelines

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.12.alpha15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-0.11.alpha15
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Aug  7 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-0.10.alpha15
- Move jar to original name format to improve compatibility

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.9.alpha15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-0.8.alpha15
- Cleanup spec
- Use maven-3.x to build

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.7.alpha15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.alpha15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed May 26 2010 Yong Yang <yyang@redhat.com> - 0:1.0-0.5.alpha15
- Add R: plexus-digest

* Thu May 20 2010 Yong Yang <yyang@redhat.com> - 0:1.0-0.4.alpha15
- Fix JPP pom name

* Thu May 20 2010 Yong Yang <yyang@redhat.com> - 0:1.0-0.3.alpha15
- Add BR:  plexus-digest

* Thu May 20 2010 Yong Yang <yyang@redhat.com> - 0:1.0-0.2.alpha15
- Change JPP pom name to prefix JPP-

* Tue May 04 2010 Yong Yang <yyang@redhat.com> - 0:1.0-0.1.alpha15
- Initial build
