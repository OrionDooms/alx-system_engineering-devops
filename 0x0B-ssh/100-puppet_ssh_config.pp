#!/usr/bin/pup
#show local SSH Client by create a client configuration file
class ssh_config {
file_line { 'Turn off passwd auth':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => 'passwordAuthentication no',
  }

file_line { 'Declare identity file':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => 'IdentityFile ~/.ssh/school',
  }
}
include ssh_config
