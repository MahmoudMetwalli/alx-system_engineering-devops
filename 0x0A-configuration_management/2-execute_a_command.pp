# kills process called killmenow
exec {'killmenow':
  command => '/usr/bin/pkill killmenow'
}
