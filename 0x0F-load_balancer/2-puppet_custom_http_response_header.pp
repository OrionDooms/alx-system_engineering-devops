#!/usr/bin/pup
#A Puppet script that configures that install and a custom HTTP header.
#Install a nginx package
package { 'nginx':
  ensure  => installed,
}
#Configures a custom HTTP header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "add_header X-Served-By [HOST=${hostname}];",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

#Enabled Nginx
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
