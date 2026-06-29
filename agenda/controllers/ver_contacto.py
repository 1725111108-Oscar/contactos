import web

db = web.database(dbn='sqlite', db='agenda.db')
render = web.template.render('views/', base='layout')

class VerContacto:
    def GET(self, id_contacto):
        try:
            contacto = db.select('contactos', where="id_contacto=$id_contacto", vars=locals())[0]
            return render.ver_contacto(contacto)
        except IndexError:
            raise web.notfound()