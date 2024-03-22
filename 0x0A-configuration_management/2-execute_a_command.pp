#Execute a command that kills a process
exec {'kill_process':
command  => 'pkill killmenow',
provider => 'shell',
}
