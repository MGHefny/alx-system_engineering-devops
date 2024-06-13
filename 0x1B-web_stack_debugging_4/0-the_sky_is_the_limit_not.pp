exec {'max-file-open':
  command => 'sed -i "s/15/10000/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/bin/:/bin/',
}