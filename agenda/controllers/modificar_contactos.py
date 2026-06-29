import web

db = web.database(dbn='sqlite', db='agenda.db')
render = web.template.render('views/', base='layout')

class ModificarContacto:
    def GET(self, id_contacto):
        try:
            contacto = db.select('contactos', where="id_contacto=$id_contacto", vars=locals())[0]
            return render.modificar_contacto(contacto)
        except IndexError:
            raise web.notfound()

    def POST(self, id_contacto):
        form = web.input()
        db.update('contactos', 
                  where="id_contacto=$id_contacto", 
                  vars=locals(),
                  nombre=form.nombre, 
                  telefono=form.telefono, 
                  email=form.email)
        raise web.seeother('/contactos')