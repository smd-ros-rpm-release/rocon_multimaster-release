Name:           ros-indigo-rocon-hub
Version:        0.7.6
Release:        0%{?dist}
Summary:        ROS rocon_hub package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rocon_hub
Source0:        %{name}-%{version}.tar.gz

Requires:       avahi
Requires:       avahi-tools
Requires:       redis
Requires:       ros-indigo-rocon-console
Requires:       ros-indigo-rocon-gateway
Requires:       ros-indigo-rocon-python-comms
Requires:       ros-indigo-rocon-python-redis
Requires:       ros-indigo-rocon-semantic-version
Requires:       ros-indigo-rosgraph
Requires:       ros-indigo-std-srvs
BuildRequires:  ros-indigo-catkin

%description
A hub acts as a shared key-value store for multiple ros systems (primarily used
by gateways).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Dec 21 2014 Daniel Stonier <d.stonier@gmail.com> - 0.7.6-0
- Autogenerated by Bloom

