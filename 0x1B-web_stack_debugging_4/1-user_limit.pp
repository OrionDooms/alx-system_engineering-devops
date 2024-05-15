#Change the OS configuration so that it is possible to login with the holberton 


exec {'fix_Holberton_hard_user_limit':
command => "sed -i 's/^holberton hard nofile 5/holberton hard nofile 10000/' /etc/security/limits.conf",
path    => '/user/bin:/bin',
}

exec {'fix_Holberton_soft_user_limit':
command => "sed -i 's/^holberton soft nofile 4/holberton soft nofile 10000/' /etc/security/limits.conf",
path    => '/user/bin:/bin',
}
