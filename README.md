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

* Modify djangoSite/settings.py to connect to your database. Find the part of code that looks like this: Replace the 'NAME' value with your database name, the 'USER' value with your databse user and the 'PASSWORD' value with your database password. 
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

* Clone this repo: (https://github.com/george-miller/intellectualSharing) and use a soft link to bring that repo into this one. ```ln -s  intellectualSharing/ personalServer/``` 

* Follow installation instructions in intellectualSharing/README.md

* Modify personalServer/djangoSite/urls.py and uncomment this line (remove the # symbol from the beginning of the line).
```#    url(r'^is/', include('intellectualSharing.urls', namespace="is"))```

