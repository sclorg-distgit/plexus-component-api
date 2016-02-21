%global pkg_name plexus-component-api
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%define project_version 1.0-alpha-15

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.0
Release:        0.16.alpha15.12%{?dist}
Summary:        Plexus Component API

License:        ASL 2.0
URL:            http://svn.codehaus.org/plexus/plexus-containers/tags/plexus-containers-1.0-alpha-15/plexus-component-api/
#svn export http://svn.codehaus.org/plexus/plexus-containers/tags/plexus-containers-1.0-alpha-15/plexus-component-api/ plexus-component-api-1.0-alpha-15
#tar zcf plexus-component-api-1.0-alpha-15.tar.gz plexus-component-api-1.0-alpha-15/
Source0:        plexus-component-api-1.0-alpha-15.tar.gz

BuildArch: noarch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix}maven-assembly-plugin
BuildRequires:  %{?scl_prefix}maven-resources-plugin
BuildRequires:  %{?scl_prefix}maven-site-plugin
BuildRequires:  %{?scl_prefix}maven-plugin-plugin
BuildRequires:  %{?scl_prefix}plexus-classworlds
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
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%files javadoc -f .mfiles-javadoc

%changelog
* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 1.0-0.16.alpha15.12
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.0-0.16.alpha15.11
- maven33 rebuild

* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 1.0-0.16.alpha15.10
- Fix directory ownership

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.16.alpha15.9
- Rebuild to fix provides

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.0-0.16.alpha15.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.0-0.16.alpha15.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.16.alpha15.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.16.alpha15.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.16.alpha15.4
- Mass rebuild 2014-02-18

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.16.alpha15.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.16.alpha15.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.16.alpha15.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0-0.16.alpha15
- Mass rebuild 2013-12-27

* Fri Jul 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.15.alpha15
- Remove workaround for rpm bug #646523
- Add BR on plexus-containers

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.14.alpha15
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

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
