# coding=UTF-8

import cherrypy
import os, os.path
import codecs
from Cheetah.Template import Template
import mysql.connector
import hashlib

def template_render(fname, params):
    page = os.path.join('html', fname)
    f = codecs.open(page, encoding='utf-8')
    temp = f.read()
    rend = Template(temp)
    for key, value in params.iteritems():
        setattr(rend, key, value)
    return unicode(rend)    

def execute_query(query, params):
    cnx = mysql.connector.connect(user='root',
                                          password='master',
                                          host='127.0.0.1',
                                          database='markbook')
    cursor = cnx.cursor()
    cursor.execute(query, params)
    try:
        rows = cursor.fetchall()
    except:
        rows = None
        cnx.commit()
    return rows
    
def login_page(message):
    return template_render('login.html', {'message': message})

class Root(object):
    @cherrypy.expose
    def checklogin(self, username, passwd, action):
        try:
            query = "SELECT password, id FROM markbook.users WHERE login = %s "
            rows = execute_query(query, [username])
            if len(rows) > 0:
                if (rows[0][0].lower() == hashlib.md5(passwd).hexdigest().lower()):
                    cherrypy.session['sid'] = cherrypy.session.id
                    cherrypy.session['user_id'] = str(rows[0][1])
                    raise cherrypy.HTTPRedirect("/user?id=" + str(rows[0][1]))
                else:
                    return login_page("Отказано в доступе!")
            else:
                return login_page("Отказано в доступе!! ")
        except cherrypy.HTTPRedirect:
            raise
        except Exception, e:
            return login_page("Отказано в доступе!!!"+e.message)

    @cherrypy.expose
    def index(self):
        if 'sid' not in cherrypy.session:
            return login_page("init")
        else:
            try:
                return template_render('chess.html', {})
            except Exception, e:
                cherrypy.log("Root. Template Render Failure!", traceback=True)
                return error_page(str(e))

    @cherrypy.expose
    def logout(self):
        cherrypy.session.delete()
        return login_page("init")

    @cherrypy.expose
    def user(self, id):
        if 'sid' not in cherrypy.session:
            return login_page("init")
        
        if cherrypy.session['user_id'] != id:
            return login_page("init")
        query = "SELECT name FROM markbook.users WHERE id = %s "
        rows = execute_query(query, [id]) 
            
        if not rows:
            pass
            
        user_name = rows[0][0]
        
        has_photo = os.path.isfile("./public/user_photos/" + id + ".jpg")
        photo = id + ".jpg"
    
        query = "SELECT id, name FROM markbook.courses WHERE id_instructor = %s "
        rows = execute_query(query, [id])
        list = [{"id":i[0],"name":i[1]} for i in rows]
        
        return template_render('user_page.html', {'user_name' : user_name, 'has_photo' : has_photo, 'photo' : photo, 'id' : id, 'courses': list})

    @cherrypy.expose
    def upload(self, id, ufile):
        upload_path = "./public/user_photos/"
        upload_filename = str(id) + ".jpg"
        upload_file = os.path.join(upload_path, upload_filename)
        size = 0
        with open(upload_file, 'wb') as out:
            while True:
                data = ufile.file.read(8192)
                if not data:
                    break
                out.write(data)
                size += len(data)

        raise cherrypy.HTTPRedirect("/user?id=" + id)  
        
    @cherrypy.expose
    def registration(self):
        return template_render('user_edit.html',{})
        
    @cherrypy.expose
    def login_exists(self, login):
        query = "Select id from markbook.users where login = %s"
        rows = execute_query(query, [login])
        return str(len(rows))
        
    @cherrypy.expose
    def add_user(self, login, password, name, comment):
        query = "Insert into markbook.users (name, comment, login, password) values (%s, %s, %s, %s)"
        rows = execute_query(query, [name, comment, login, hashlib.md5(password).hexdigest().lower()])
        return login_page("init")
        
    @cherrypy.expose
    def course_registration(self):
        query = "Select id, name, login from markbook.users"
        rows = execute_query(query, [])
        list = [{"id" : i[0], "name" : i[1], "login" : i[2]} for i in rows]
        return template_render('course_edit.html',{"users" : list})    
        
    @cherrypy.expose
    def add_course(self, name, instructor):
        query = "Insert into markbook.courses (name, id_instructor) values (%s, %s)"
        rows = execute_query(query, [name, instructor])
        return "ok";
        
cherrypy.quickstart(Root(), '/', "app.conf")
