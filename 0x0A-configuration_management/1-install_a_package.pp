#!/usr/bin/pup
##Install a flask version 2.1.0 package using puppet
package {'install flask':
ensure   => '2.1.0',
name     => 'flask',
provider => 'pip3',
}
