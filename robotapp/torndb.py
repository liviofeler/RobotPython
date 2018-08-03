from torndb import Connection

from .views import app

app.config.from_object('config')

db = Connection ('127.0.0.1', app.config['DATABASE_NAME'],app.config['DATABASE_USER'], app.config['DATABASE_PASS'] )
