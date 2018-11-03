=====
Http451
=====

Http451 is a simple Django app that implements http451 on django. It implements the following IEFT RFC:

https://tools.ietf.org/html/rfc7725

https://tools.ietf.org/id/draft-sahib-451-new-protocol-elements-03.txt

Quick start
-----------

1. Install http451 via pip :

`pip install django-http-451`

2. Add 'http451' to your INSTALLED_APPS settings like:

INSTALLED_APPS = [
        ...

        'http451',
    ]

3. Add the following in your middleware

MIDDLEWARE = [
    ...

    'http451.middleware.http451Middleware',
]

4. Run `python manage.py migrate` to create the http451 models.
5. Start the development server and visit the admin page
6. Block a resource add it through the admin page http451 section
