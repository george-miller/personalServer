# Personal Server

This site is live here: (http://georgemyersmiller.com)

## Install

Install python and pip (https://pip.pypa.io/en/stable/installing/)

You must create your own log files of the following structure or use the creator script ```source createlogs.sh```. 
```
logs/
├── django_request.log
└── mylog.log
```

* Modify djangoSite/settings.py to connect to your mysql database. Find the part of code that looks like the lines shown below.  Replace the 'NAME' value with your database name, the 'USER' value with your databse user and the 'PASSWORD' value with your database password.  The mysql database is used for the polls app.  If you don't want to use that app, simply comment out the lines below.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'root',
	'USER': 'root',
	'PASSWORD': 'root',
	'HOST': '',
    }
}
```

## Adding in Intellectual Sharing site

* Clone this repo: (https://github.com/george-miller/intellectualSharing) and use a soft link to bring that repo's ```home``` module into this one. ```ln -s  intellectualSharing/home/ personalServer/intellectualSharing``` 

* Follow installation instructions in intellectualSharing/README.md

* Modify personalServer/djangoSite/urls.py and uncomment this line (remove the # symbol from the beginning of the line).
```#    url(r'^is/', include('intellectualSharing.urls', namespace="is"))```.  You must also modify djangoSite/settings.py and uncomment intellectualSharing from the INSTALLED_APPS.

## Adding in regex

* Clone this repo: (https://github.com/george-miller/regex) and use a soft link to bring that repo into this one ```ln -s regex personalServer/regex/lib```

* Uncomment the route in djangoSite/urls.py
