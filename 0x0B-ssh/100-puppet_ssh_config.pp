#!/usr/bin/pup
#show local SSH Client by create a client configuration file
class ssh {
  file {'~/.ssh/school':
    passwordAuthentication => 'no',
    notify                 => Service['ssh']
  }

  service {'ssh':
    ensure => 'running',
    enable => 'true',
  }
}
