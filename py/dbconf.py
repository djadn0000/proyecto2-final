from logging import exception
import pymysql
from pymysql.cursors import Cursor

class DataBase:
    def __init__(self) :
        self.connection = pymysql.connect(
            host='proyectoadrianitt.ddns.net',
            user='jose',
            password='j2b1l',
            db='Proyecto'
        )
        self.cursor =self.connection.cursor()
 #seleccion por id  
    #seleccionar usuari@ por id
    def select_user(self,id):
        sql = 'SELECT * from users WHERE id = {}'.format(id)
       
        try:
         self.cursor.execute(sql)
         user = self.cursor.fetchone()

         print ('Id:{}'.format(user[0]))
         print ('Name:{}'.format(user[1])) 
         print ('Email:{}'.format(user[2]))
         print ('Pass:{}'.format(user[3]))

         return user

         
        except Exception as e:
            print("No se pudo conectar la base de datos")
            pass
            
    #seleccionar roles por id
    def select_roles(self,id):
        sql = 'SELECT * from roles WHERE id = {}'.format(id)
       
        try:
         self.cursor.execute(sql)
         role= self.cursor.fetchone()
         return role

         
        except Exception as e:
            print("No se pudo encontrar el rol solicitado")
            pass
    
    #seleccionar malware por id
    def select_malware(self,id):
        sql = 'SELECT * from malwares WHERE id = {}'.format(id)
       
        try:
         self.cursor.execute(sql)
         malware= self.cursor.fetchone()
         return malware
         
        except Exception as e:
            print("No se pudo encontrar el malware solicitado")
            pass

    #seleccionar blacklist por id
    def select_blacklist_by_id(self,id):
        sql = 'SELECT * from blacklists WHERE id = {}'.format(id)
       
        try:
         self.cursor.execute(sql)
         blacklist = self.cursor.fetchone()
         return blacklist
         
        except Exception as e:
            print("No se pudo encontrar el link solicitado/n {}".format(str(e)))
            print("************ERROR*********************")

    #seleccionar toda la blacklist 
    def select_all_blacklist(self):
        sql = 'SELECT url from blacklists'
       
        try:
         self.cursor.execute(sql)
         blacklist = self.cursor.fetchall()
         return blacklist
         
        except Exception as e:
            print("No se pudo encontrar el link solicitado/n {}".format(str(e)))
            print("************ERROR*********************")

    #seleccionar toda las ip de blacklist 
    def select_allip_blacklist(self):
        sql = 'SELECT ip from blacklists'
       
        try:
         self.cursor.execute(sql)
         blacklist = self.cursor.fetchall()
         return blacklist
         
        except Exception as e:
            print("No se pudo encontrar el link solicitado/n {}".format(str(e)))
            print("************ERROR*********************")


    #seleccionar user_blacklist por id
    def select_user_blacklist(self,id):
        
        sql = 'SELECT * from blacklist_user WHERE id = {}'.format(id)
       
        try:
         self.cursor.execute(sql)
         blackuser= self.cursor.fetchone()

         return blackuser
 
        except Exception as e:
            print("No se pudo encontrar el usuario de la lista negra solicitado")
            
    #seleccionar migration por id
    def select_migration_by_id(self,id):
        sql = 'SELECT * from migrations WHERE id = {}'.format(id)
       
        try:
         self.cursor.execute(sql)
         role= self.cursor.fetchone()
         return role
         
        except Exception as e:
            print("No se pudo completar su solicitud")
            pass

    #existencia de dominio
    def domainblocked(self,url):
       sql= 'SELECT COUNT(*) FROM blacklists WHERE url = "{}"'.format(url)

       try:
           self.cursor.execute(sql)
           a = self.cursor.fetchone()
            
           bol= False
           if a[0] > 0 :
               bol = True
               print('hay almenos un resultado\n')
               return bol
           else :
               print('No hay resultado')
               return 

       except Exception as e:  
           print('Hubo un error en su querry \n\n {}'.format(e))
           pass       

    def ipdomainblocked(self,ip):
       sql= 'SELECT COUNT(*) FROM blacklists WHERE ip = "{}"'.format(ip)

       try:
           self.cursor.execute(sql)
           a = self.cursor.fetchone()
            
           bol= False
           if a[0] > 0 :
               bol = True
               print('hay almenos un resultado\n')
               return bol
           else :
               print('No hay resultado')
               return 

       except Exception as e:  
           print('Hubo un error en su querry \n\n {}'.format(e))
           pass       


    
#eliminar por id
    # eliminar usuario por id
    def delete_user(self,id):
        sql = 'DELETE FROM users WHERE id = {}'.format(id)
       
        try:
         self.cursor.execute(sql)
                  
        except Exception as e:
            pass

    # eliminar roles por id
    def delete_role(self,id):
        sql = 'DELETE FROM roles WHERE id = {}'.format(id)
       
        try:
         self.cursor.execute(sql)
                  
        except Exception as e:
            pass
   
    # eliminar migration por id
    def delete_migration(self,id):
        sql = 'DELETE FROM migradions WHERE id = {}'.format(id)
       
        try:
         self.cursor.execute(sql)
                  
        except Exception as e:
            pass
    
    # eliminar roles por id
    
    # eliminar malware por id
    def delete_malware(self,id):
        sql = 'DELETE FROM malwares WHERE id = {}'.format(id)
       
        try:
         self.cursor.execute(sql)
                  
        except Exception as e:
            pass

    # eliminar blacklist_user por id
    def delete_blacklist_user(self,id):
        sql = 'DELETE FROM blacklist_user WHERE id = {}'.format(id)
       
        try:
         self.cursor.execute(sql)
                  
        except Exception as e:
            pass

    # eliminar blacklistpor id
    def delete_blacklist_user(self,id):
        sql = 'DELETE FROM blacklist WHERE id = {}'.format(id)
       
        try:
         self.cursor.execute(sql)
                  
        except Exception as e:
            pass
 
 #editar por id
   #user:
    #editar todo user por id:
    def  edit_alluser(self,id,name,email,password):
        sql='UPDATE users SET name ={},email={},password={} WHERE id={}'.format(name,email,password,id)
        try:
         self.cursor.execute(sql)
                  
        except Exception as e:
            pass
    
    #editar nombre del user por id:
    def  edit_nameuser(self,id,name):
        sql='UPDATE users SET name ={} WHERE id={}'.format(name,id)
        try:
         self.cursor.execute(sql)
                  
        except Exception as e:
            pass

    #editar Email del user por id:
    def  edit_emailuser(self,id,email):
        sql='UPDATE users SET email={} WHERE id={}'.format(email,id)
        try:
         self.cursor.execute(sql)
                  
        except Exception as e:
            pass

    #editar pass del user por id:
    def  edit_passworduser(self,id,password):
        sql='UPDATE users SET name ={},password={} WHERE id={}'.format(password,id)
        
        try:
         self.cursor.execute(sql)
                  
        except Exception as e:
            pass
   
   #roles:
    #editar todo roles por id
        def  edit_allrole(self,id,name,description):
            sql='UPDATE roles SET name={}, description = {} WHERE id={}'.format(name,description,id)
            
            try:
                self.cursor.execute(sql)                  
            except Exception as e:
                pass

    #editar nombre del roles por id
        def  edit_namerole(self,id,name):
            sql='UPDATE roles SET name={} WHERE id={}'.format(name,id)
            
            try:
                self.cursor.execute(sql)                  
            except Exception as e:
                pass

    #editar todo roles por id
        def  edit_descriptionrole(self,id,name,description):
            sql='UPDATE roles SET  description = {} WHERE id={}'.format(description,id)
            
            try:
                self.cursor.execute(sql)                  
            except Exception as e:
                pass
'''
pepe= DataBase()
p= pepe.select_user(1)
'''