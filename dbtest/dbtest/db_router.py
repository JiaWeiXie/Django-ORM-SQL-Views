from django.conf import settings

class db_Router(object):
    def db_for_read(self, model, **hints):
        return 'mysql'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        db_list = ('default','mysql')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, model):
        if db == 'default':
            return True
        else:
            return False 
        

    def allow_syncdb(self, db, model):
        if db == 'default':
            return True
        else:
            return False
        return None