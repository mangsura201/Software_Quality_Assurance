from .settings import *
<<<<<<< HEAD
DATABASES={
"default":{
"ENGINE":"django.db.backends.sqlite3",
"NAME":":memory",
}
} 
EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'
=======

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory",
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
>>>>>>> 62615bc1b85e5176a07671444b0786e27d168e66
