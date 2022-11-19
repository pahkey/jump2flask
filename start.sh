#!/bin/bash

# Prepare log files and start outputting logs to stdout
# tail -n 0 -f /root/wikidocs/logs/gunicorn*.log &

exec gunicorn "pybo:create_app()" \
  --reload \
  --name mysite \
  --bind unix:/root/myproject/sock/gunicorn.sock \
  --workers 1 \
  --log-level=debug \
  --log-config /root/myproject/gunicorn_log.ini &

