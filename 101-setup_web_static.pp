# sets up web servers for the deployment
exec { 'apt-get -y update && apt-get -y install nginx':
    path => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    user => 'root'
}
-> exec { 'mkdir -p /data/web_static/shared/ /data/web_static/releases/test/':
    path => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    user => 'root'
}
-> file { '/data/web_static/releases/test/index.html':
    ensure  => present,
    content => "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>\n"
}
-> exec { 'ln -sf /data/web_static/releases/test/ /data/web_static/current':
    path => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    user => 'root'
}
-> exec { 'chown -hR ubuntu:ubuntu /data':
    path => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    user => 'root'
}
-> file_line { 'location':
    ensure => present,
    path   => '/etc/nginx/sites-available/default',
    line   => "\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n",
    after  => 'server_name _;'
}
-> exec { 'service nginx restart':
    path => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    user => 'root'
}
