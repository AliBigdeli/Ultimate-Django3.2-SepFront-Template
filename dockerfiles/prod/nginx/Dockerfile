FROM nginx:alpine

COPY ./dockerfiles/prod/nginx/config/* /etc/nginx/
COPY ./dockerfiles/prod/nginx/entrypoint.sh /entrypoint.sh

USER root

RUN apk add --no-cache openssl bash
RUN chmod +x /entrypoint.sh


CMD ["/entrypoint.sh"]