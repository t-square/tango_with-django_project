import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page
def populate():
    python_pages = [
        {'title': 'Official Python Tutorial', 'views': 22,
            'url':'http://docs.python.org/3/tutorial/'},
        {'title':'How to Think like a Computer Scientist', 'views': 55,
            'url':'http://www.greenteapress.com/thinkpython/'},
        {'title':'Learn Python in 10 Minutes', 'views': 33,
            'url':'http://www.korokithakis.net/tutorials/python/'} ]

    django_pages = [
        {'title':'Official Django Tutorial', 'views': 4,
            'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title':'Django Rocks', 'views': 5,
            'url':'http://www.djangorocks.com/'},
        {'title':'How to Tango with Django', 'views': 5,
            'url':'http://www.tangowithdjango.com/'} ]

    other_pages = [
        {'title':'Bottle', 'views': 6,
            'url':'http://bottlepy.org/docs/dev/'},
        {'title':'Flask', 'views': 7,
            'url':'http://flask.pocoo.org'} ]

    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes':16}   }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['views'], p['url'])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_page(cat, title, v, u):
    p = Page.objects.get_or_create(category=cat, title=title, views=v, url=u)[0]
    p.save()
    return p

def add_cat(name, v, l):
    c = Category.objects.get_or_create(name=name, views=v, likes=l)[0]
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
