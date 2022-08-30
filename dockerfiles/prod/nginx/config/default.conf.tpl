server {
    listen 80;

    server_name ${DOMAIN} www.${DOMAIN};

    # server logs
    access_log  /var/log/nginx/access_log.log;
    error_log /var/log/nginx/error_log.log;


    location /.well-known/acme-challenge/ {
        root /vol/www/;
    }


    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
        try_files $uri $uri/ /index.html;
    }
}
