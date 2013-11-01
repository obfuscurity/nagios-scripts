%define ver  0.0.1
%define rel  1

Summary:           Nagios plugin for checking time series data from graphite
Name:              nagios-plugins-graphite
Version:           %{ver}
Release:           %{rel}
License:           MIT
Group:             Applications/System
URL:               https://github.com/obfuscurity/nagios-scripts

BuildArch:         noarch
Source0:           %{name}-%{version}.tar.gz
BuildRoot:         %{_tmppath}/%{name}-%{version}-%{release}-root

Provides:          nagios-plugins-graphite
Requires:          ruby, rubygems, rubygem-json, rubygem-rest-client

%description
A nagios plugin designed to pull time series data from graphite, aggregate the values,
then issue a nagios alert if the aggregate is above thresholds

%prep
%setup

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 check_graphite %{buildroot}%{_libdir}/nagios/plugins/check_graphite

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%dir %{_libdir}/nagios/
%dir %{_libdir}/nagios/plugins/
%{_libdir}/nagios/plugins/check_graphite

%changelog
* Thu Oct 31 2013 Justin La Sotten <justin.lasotten@gmail.com> 0.0.1-1
- Initial build - MIT License.


