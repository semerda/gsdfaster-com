# Website GSDfaster.com

**[GSDfaster.com](https://www.gsdfaster.com/) is a Website for the GSDfaster app. GSDfaster is an app for your iPhone, iPad and Watch to help you Get Stuff Done Faster & Be More Productive. The goal is for GSDfaster to be your distributed cognition tool which you can trust to empty your mind, gain control & stay focused.

> "Most productive people are those with nothing in their head."
*David Allen Do Lectures, Getting Things Done*

## How to get the apps

* [GSDfaster: https://itunes.apple.com/us/app/gsdfaster-gtd-todo-lists-pomodoro/id488633128?mt=8](https://itunes.apple.com/us/app/gsdfaster-gtd-todo-lists-pomodoro/id488633128?mt=8) on iTunes
* [GSDfaster.com Website](https://www.gsdfaster.com/) - with The GTD Knowledge Center

[![Watch GSDfaster Intro Video](https://img.youtube.com/vi/cth-5fM-2Vg/0.jpg)](https://www.youtube.com/watch?v=cth-5fM-2Vg)

## Notes

If you are using the Apache webserver, consider using mod_wsgi.
http://flask.pocoo.org/docs/0.11/deploying/mod_wsgi/

Deployment Options
http://flask.pocoo.org/docs/0.11/deploying/

LOCAL DEV

```
python app.py runserver -d
```

APACHE CONF

```
cd /etc/apache2/sites-available/
sudo nano gsdfaster_com.conf
```

```
sudo a2ensite gsdfaster_com.conf
sudo service apache2 reload
```

DEBIAN / UBUNTU

1. Installation

```
apt-get install libapache2-mod-wsgi
```

```
sudo pip install virtualenv
sudo virtualenv gsdfaster_com
source gsdfaster_com/bin/activate # deactivate
```

```
sudo pip install Flask
sudo apt-get install libapache2-mod-wsgi
sudo a2enmod wsgi
```

1.1 User for .conf (see WSGIDaemonProcess)

create a new user without a home directory:
```
sudo useradd -M flask
```

remove shell:
```
sudo usermod -s /bin/false flask
```

Finally, lock the account to prevent logging in:
```
sudo usermod -L flask
```

I also added the user to the Apache www-data group. This makes it easier to work with file permissions later as I can keep ownership of them with my own user, but allow the www-data group access.
```
sudo adduser flask www-data
```

2. Make sure wsgi is copied / edited:
```
cp gsdfaster_com.conf /etc/apache2/sites-available/gsdfaster_com.conf
```

3. Finalize
```
sudo a2ensite gsdfaster_com
sudo service apache2 restart
```

## TODO

1. Add Fabric to auto build box
2. Run in a VirtualEnv -- or
3. Run on Google App Engine -- then VirtualEnv not required?
4. Add Cache: https://github.com/thadeusb/flask-cache
