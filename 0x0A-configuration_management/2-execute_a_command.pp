# kills process called killmenow
exec {'killmenow':
  command => 'pkill killmenow'
}
