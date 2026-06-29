import web

db = web.database(dbn='sqlite', db='agenda.db')

class BorrarContacto:
    def GET(self, id_contacto):
        db.delete('contactos', where="id_contacto=$id_contacto", vars=locals())
        raise web.seeother('/contactos')
    
    def POST(self, id_contacto):
        db.delete('contactos', where="id_contacto=$id_contacto", vars=locals())
        raise web.seeother('/contactos')