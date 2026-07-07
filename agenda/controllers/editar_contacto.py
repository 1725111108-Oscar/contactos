import web
import sqlite3
import os

render = web.template.render('views', base='layout')

class EditarContacto:
    
    def conectar_db(self):
        if os.path.exists('sql/agenda.db'):
            return sqlite3.connect('sql/agenda.db')
        elif os.path.exists('agenda.db'):
            return sqlite3.connect('agenda.db')
        else:
            raise FileNotFoundError("No se pudo localizar el archivo agenda.db")

    def GET(self, id_contacto):
        conn = None
        try:
            conn = self.conectar_db()
            cursor = conn.cursor()
            query = "SELECT id_contacto, nombre, primer_apellido, segundo_apellido, email, telefono FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (int(id_contacto),))
            row = cursor.fetchone()
            
            if row:
                contacto = {
                    'id_contacto': int(row[0]) if row[0] is not None else id_contacto,
                    'nombre': str(row[1]) if row[1] is not None else "",
                    'primer_apellido': str(row[2]) if row[2] is not None else "",
                    'segundo_apellido': str(row[3]) if row[3] is not None else "",
                    'email': str(row[4]) if row[4] is not None else "",
                    'telefono': str(row[5]) if row[5] is not None else ""
                }
                return render.editar_contacto(contacto)
            else:
                return "Error: El contacto no existe."
        except Exception as e:
            return f"Error en GET: {str(e)}"
        finally:
            if conn:
                conn.close()

    def POST(self, id_contacto):
        data = web.input()

        nombre = data.nombre if 'nombre' in data else ""
        primer_apellido = data.primer_apellido if 'primer_apellido' in data else ""
        segundo_apellido = data.segundo_apellido if 'segundo_apellido' in data else ""
        email = data.email if 'email' in data else ""
        telefono = data.telefono if 'telefono' in data else ""

        conn = None
        try:
            conn = self.conectar_db()
            cursor = conn.cursor()
            
            query = """
                UPDATE contactos 
                SET nombre = ?, primer_apellido = ?, segundo_apellido = ?, email = ?, telefono = ? 
                WHERE id_contacto = ?
            """
            cursor.execute(query, (
                nombre, 
                primer_apellido, 
                segundo_apellido, 
                email, 
                telefono, 
                int(id_contacto)
            ))
            conn.commit()
            print(f"¡Contacto {id_contacto} actualizado correctamente!")
        except Exception as e:
            print(f"Error al guardar los datos en POST: {e}")
        finally:
            if conn:
                conn.close()
                
        raise web.seeother('/contactos')