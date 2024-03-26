#!/usr/bin/pup
#show local SSH Client by create a client configuration file
<<<<<<< HEAD
=======
class ssh {
  file {'~/.ssh/school':
    path                   => 'ect/ssh/ssh_config',
    line                   => 'IdentityFile ~/.ssh/school',
    passwordAuthentication => 'no',
    notify                 => Service['ssh']
  }
>>>>>>> 96972039eec1a43694e634aae153b458c7a9020d

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
