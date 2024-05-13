# A web stack debugging task. Testing the web server setup under pressure.
# Getting a huge amount of failed requests. Making 2000 requests to a server,
# with 100 request at a time. This script would change the value of ULIMIT from
# 15 to 4096.

exec { 'fix_nginx' :
provider => shell,
command  => 'sudo sed -i "s/15/4096/" /etc/default/nginx',
}
exec {'nginx_restart':
command  => 'sudo service nginx restart',
provider => shell,
}
