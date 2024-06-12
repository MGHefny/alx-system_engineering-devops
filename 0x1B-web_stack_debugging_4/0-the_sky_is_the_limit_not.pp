exec {'max-file-open':
  command => 'sed -i "s/15/2000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

exec { 're-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
