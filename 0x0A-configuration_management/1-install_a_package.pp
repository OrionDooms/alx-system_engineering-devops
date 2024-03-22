#!/usr/bin/pup
#Install a flask version 2.1.0 package using puppet
package { 'flask':
  ensure => '2.1.0',
  name   => 'flask',
provider => 'pip3',
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
