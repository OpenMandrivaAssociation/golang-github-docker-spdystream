# http://github.com/docker/spdystream

%global goipath         github.com/docker/spdystream
%global commit          b2c3287865f3ad6aa22821ddb7b4692b896ac207


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.18%{?dist}
Summary:        A multiplexed stream library using spdy
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/gorilla/websocket)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
%gochecks -d . -d ws

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.17.gitb2c3287
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.16.20150615gitb2c3287
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.gitb2c3287
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.gitb2c3287
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.gitb2c3287
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.gitb2c3287
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.gitb2c3287
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.gitb2c3287
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitb2c3287
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.8.gitb2c3287
- Update to spec-2.1
  related: #1214600

* Fri Jul 31 2015 jchaloup <jchaloup@redhat.com> - 0-0.7.gitb2c3287
- Update spec file to spec-2.0
  related: #1214600

* Sat Jul 25 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.gitb2c3287
- Bump to upstream b2c3287865f3ad6aa22821ddb7b4692b896ac207
  resolves: #1246760

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git83ae67e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git83ae67e
- Bump to upstream 83ae67e694a4ab5cbaee4d3126f25118712b26e6
  resolves: #1196363

* Tue Mar 31 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.gite731c8f
- Bump to upstream e731c8f9f19ffd7e51a469a2de1580c1dfbb4fae
  resolves: #1196363

* Tue Mar 03 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.gite9bf991
- Bump to upstream e9bf9912b85eec0ed6aaf317808a0eab25e3ca43
  resolves: #1196363

* Wed Feb 25 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git29e1da2
- First package for Fedora
  resolves: #1196363

