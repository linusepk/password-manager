# Setup (Debian)
[Certbot](certbot.eef.org)
```shell
$ apt install nginx
$ git clone git@github.com:NanoSwing/password-manager.git
$ cd password-manager/
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ cp password-manager.service /etc/systemd/system/password-manager.service
$ systemctl enable password-manager
$ cp nginx.conf /etc/nginx/nginx.conf
```
