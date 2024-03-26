#!/usr/bin/pup
#show local SSH Client by create a client configuration file

file { 'ect/ssh/ssh_config':
	ensure  => 'present',
	content => 'IdentityFile ~/.ssh/school',
	line => 'passwordAuthentication  no',


}
file {'/etc/ssh/ssh_config':
  ensure => present,
}

file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/ssh_config',
  line   => 'passwordAuthentication no',
}

file_line { 'Declare identity file':
  path   => 'etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}
~  
