exec {'max-file-open':
  command => 'sed -i "s/15/5000/" /etc/default/nginx',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}

exec { 're-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
