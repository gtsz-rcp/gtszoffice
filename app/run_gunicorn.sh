#!/bin/bash
# to run this script as service, change permission to 744 with `chmod 744 rungunicorn.sh`
# ExecStart={absolute_path}/rungunicon.sh
# systemctl daemon-reload
# systemctl enable gtszapp
# systemctl start gtszapp
# check log with tail -f /var/log/syslog

/home/gtszoffice/gtszoffice/app/is_docker_already_up.sh && /home/gtszoffice/gtszoffice/app/env/bin/gunicorn -c /home/gtszoffice/gtszoffice/app/gunicorn.conf -b 0.0.0.0:5000 gunicorn_app:app;
