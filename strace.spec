%include	/usr/lib/rpm/macros.perl

Summary:	prints system call strace of a running process
Name:		strace
Version:	4.7
Release:	1
License:	BSD-like
Group:		Development/Debuggers
Source0:	http://downloads.sourceforge.net/strace/%{name}-%{version}.tar.xz
# Source0-md5:	6054c3880a00c6703f83b57f15e04642
URL:		http://sourceforge.net/projects/strace/
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Strace prints a record of each system call another program makes,
including all of the arguments passed to it and the system call's
return value.

%package graph
Summary:	strace graph
Group:		Development/Debuggers
# NOTE: doesn't require directly strace binary.

%description graph
strace-graph script processes strace -f output. It displays a graph of
invoked subprocesses, and is useful for finding out what complex
commands do.

The script can also handle the output with strace -t, -tt, or -ttt.
It will add elapsed time for each process in that case.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT CREDITS ChangeLog NEWS README-linux
%attr(755,root,root) %{_bindir}/strace
%attr(755,root,root) %{_bindir}/strace-log-merge
%{_mandir}/man1/*

%files graph
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/strace-graph

