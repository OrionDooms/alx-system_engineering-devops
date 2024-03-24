#!/usr/bin/pup
class ssh{
  file{'~/.ssh/school':
    passwordAuthentication => 'no',
    notify => Service['ssh']
  }

  service {'ssh':
    ensure => 'running',
    enable => 'true',
  }
}
