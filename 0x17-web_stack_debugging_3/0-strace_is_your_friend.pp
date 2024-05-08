# fix the extension error in the wp-settings.php

$file_path = '/var/www/html/wp-settings.php'

exec { 'fix_extension' :
        command => "sed -i 's/\\.phpp/\\.php/g' ${file_path}",
        path    => '/usr/bin:/bin',
}
