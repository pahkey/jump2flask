#!/bin/bash

# Prepare log files and start outputting logs to stdout
# tail -n 0 -f /root/wikidocs/logs/gunicorn*.log &

# flask run --host 0.0.0.0 --port 8000

exec gunicorn "pybo:create_app()" \
  --reload \
  --name mysite \
  --bind unix:/root/myproject/sock/gunicorn.sock \
  --workers 1 \
  --log-level=debug \
  --log-config /root/myproject/gunicorn_log.ini &

