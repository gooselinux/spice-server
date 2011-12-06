
%define tarname spice-server
%define tarversion 0.4.2

%define patchid 15
Name:           spice-server
Version:        0.4.2
Release:        %{patchid}%{?dist}
Summary:        Implements the server side of the SPICE protocol
Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://www.spice-space.org/
Source0:        %{tarname}-%{tarversion}.tar.bz2
patch1:         spice-server-1-avoid-video-streaming-of-small-images.patch
patch2:         spice-server-2-new-api-alloc-init-free.patch
patch3:         spice-server-3-new-api-configure-port-ticket.patch
patch4:         spice-server-4-new-api-zap-function-pointer-indirection.patch
patch5:         spice-server-5-new-api-configure-tls.patch
patch6:         spice-server-6-new-api-configure-listen-addr.patch
patch7:         spice-server-7-new-api-public-image_compression_t.patch
patch8:         spice-server-8-new-api-add-get-set-image-compression.patch
patch9:         spice-server-9-new-api-public-spice_channel_t.patch
patch10:        spice-server-10-new-api-add-secure-channels.patch
patch11:        spice-server-11-new-api-add-absolute-mouse.patch
patch12:        spice-server-12-new-api-add_renderer.patch
patch13:        spice-server-13-new-api-add-get-sock-peer-info.patch
patch14:        spice-server-14-new-migration-process.patch
patch15:        spice-server-15-more-permissive-video-identification.patch
patch16:        spice-server-16-fix-wrong-access-to-ring-item.patch
patch17:        spice-server-17-renaming-library-and-includedir.patch
patch18:        spice-server-18-renaming-library-Makefile.in-changes.patch
patch19:        spice-server-19-new-api-move-STREAM_VIDEO-enum.patch
patch20:        spice-server-20-new-api-add-get-set-streaming-video.patch
patch21:        spice-server-21-new-api-add-get-set-agent-mouse.patch
patch22:        spice-server-22-new-api-add-get-set-playback_compression.patch
patch23:        spice-server-23-make-opengl-optional-disabled-by-default.patch
patch24:        spice-server-24-disable-open-gl-2.patch
patch25:        spice-server-25-disable-open-gl-3.patch
patch26:        spice-server-26-fix-unsafe-guest-host-data-handling.patch
patch27:        spice-server-27-fix-unsafe-free.patch
patch28:        spice-server-28-fix-unsafe-cursor-handling.patch
patch29:        spice-server-29-add-missing-overflow-check.patch

BuildRoot:      %{_tmppath}/%{tarname}-%{version}-%{release}-root-%(%{__id_u} -n)

ExclusiveArch:  x86_64

BuildRequires:  pkgconfig
BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel
BuildRequires:  libpng-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXext-devel
BuildRequires:  openssl-devel
BuildRequires:  celt051-devel
BuildRequires:  cairo-spice-devel >= 1.4.6
BuildRequires:  ffmpeg-spice-devel
BuildRequires:  spice-common-devel >= 0.4.2-7

BuildRequires:  autoconf automake libtool

Requires:  pkgconfig

%package devel
Summary:        Header files, libraries and development documentation for %{name}
Group:          Development/Libraries

Requires:       %{name} = %{version}-%{release}
Requires:       alsa-lib-devel
Requires:       libpng-devel
Requires:       libXrandr-devel
Requires:       libXext-devel
Requires:       openssl-devel
Requires:       celt051-devel
Requires:       cairo-spice-devel >= 1.4.6
Requires:       ffmpeg-spice-devel


%description
The Simple Protocol for Independent Computing Environments (SPICE) is
a remote display system built for virtual environments which allows
you to view a computing 'desktop' environment not only on the machine
where it is running, but from anywhere on the Internet and from a wide
variety of machine architectures.

This package contains the runtime libraries for any application that wishes
to be a SPICE server.

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs
using %{name},you will need to install %{name}-devel.

%prep
%setup -q -n %{tarname}-%{tarversion}

# Note that "patch -p2" is used, as patches are against spice and
# not spice/server.
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p2
%patch5 -p2
%patch6 -p2
%patch7 -p2
%patch8 -p2
%patch9 -p2
%patch10 -p2
%patch11 -p2
%patch12 -p2
%patch13 -p2
%patch14 -p2
%patch15 -p2
%patch16 -p2
%patch17 -p2
%patch18 -p2
%patch19 -p2
%patch20 -p2
%patch21 -p2
%patch22 -p2
%patch23 -p2
%patch24 -p2
%patch25 -p2
%patch26 -p2
%patch27 -p2
%patch28 -p2
%patch29 -p2


%build
autoreconf -i -f
CFLAGS="%{optflags}"; CFLAGS="${CFLAGS/-Wall/}"; export CFLAGS;
CXXFLAGS="%{optflags}"; CXXFLAGS="${CXXFLAGS/-Wall/}"; export CXXFLAGS;
FFLAGS="%{optflags}"; FFLAGS="${FFLAGS/-Wall/}"; export FFLAGS;
%configure PATCHID=%{patchid} DISTRIBUTION=%{?dist} --with-spice-common
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_libdir}/libspice-server.so.*

%files devel
%defattr(-, root, root, 0755)
%doc COPYING README
%{_includedir}/spice-server/
%{_libdir}/libspice-server.so
%{_libdir}/pkgconfig/spice-server.pc
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%changelog
* Fri Jul 30 2010 Uri Lublin <uril@redhat.com> - 0.4.2-15
 - Fix unsafe accesses
  + fix unsafe guest data accessing.
  + fix unsafe free() call.
  + fix unsafe cursor items handling.
  + add missing overflow check.
Resolves: #568811

* Wed Jun 30 2010 Uri Lublin <uril@redhat.com> - 0.4.2-14
- make opengl optional - add a missing patch
  ifdef out some opengl calls.
Resolves: #482556

* Wed Jun 30 2010 Uri Lublin <uril@redhat.com> - 0.4.2-13
- remove Requires and BuildRequires mesa-libGLU-devel
  + open-gl is now disabled.
- bumped release to -13 due to tag issue
Related: #482556

* Wed Jun 30 2010 Uri Lublin <uril@redhat.com> - 0.4.2-11
- make opengl optional, disabled by default (2 patches)
Resolves: #482556

* Thu Apr 22 2010 Uri Lublin <uril@redhat.com> - 0.4.2-10
- spice: server: new-api (4 more patches)
     + streaming-video, agent-mouse, playback-compression.
Related: #571286

* Sun Apr  4 2010 Uri Lublin <uril@redhat.com> - 0.4.2-9
 - generate auto* generated files (e.g. Makefile.in)
Resolves: #579329

* Tue Mar 23 2010 Uri Lublin <uril@redhat.com> - 0.4.2-8
 - spice server: renaming library and includedir
Resolves: #573349

* Tue Mar 23 2010 Uri Lublin <uril@redhat.com> - 0.4.2-7
 - fix wrong access to ring item
Resolves: #575556

* Tue Mar 23 2010 Uri Lublin <uril@redhat.com> - 0.4.2-6
 - more permissive video identification
Resolves: #575576

* Tue Mar 23 2010 Uri Lublin <uril@redhat.com> - 0.4.2-5
 - new migration process
Resolves: #576029

* Wed Mar 17 2010 Uri Lublin <uril@redhat.com> - 0.4.2-4
- spice: server: new-api (2 more patches)
Related: #571286

* Mon Mar  7 2010 Uri Lublin <uril@redhat.com> - 0.4.2-3
 - Use default configure macro (remove _prefix and _libdir)
Related: #543948

* Sun Mar 07 2010 Uri Lublin <uril@redhat.com> - 0.4.2-2
- spice: server: new-api (10 patches)
Related: #571286

* Sun Mar 07 2010 Uri Lublin <uril@redhat.com> - 0.4.2-1
- spice: server: avoid video streaming of small images
Resolves: #571283

* Mon Jan 11 2009 Uri Lublin <uril@redhat.com> - 0.4.2-0
 - first spec for 0.4.2
Related: #549807
