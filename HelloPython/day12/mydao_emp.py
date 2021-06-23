import pymysql



class DaoEmp:
    def __init__(self):
        self.db = pymysql.connect(host = 'localhost', user = 'root', password='python', database='pydb', port=3307)
        self.cursor = self.db.cursor()
        print("DaoSample_init__")
    
    def selectList(self):
        ret = []
        query = "SELECT * FROM emp"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        for row in data:
            ret.append({'id' : row[0],'ko_name' : row[1],'en_name' : row[2],'mobile' : row[3],'address' : row[4] })
        return ret    
    
    def update(self, id, ko_name, en_name,mobile,address):
        print(ko_name)
        print(id)
        print(en_name)
        print(mobile)
        print(address)
        query = f"""
        UPDATE emp 
        SET ko_name = '{ko_name}', en_name = '{en_name}', mobile = '{mobile}', address = '{address}' 
        WHERE e_id = {id}"""
        print(query)
        cnt = self.cursor.execute(query)
        self.db.commit()
        return cnt
    
    def delete(self,id):
        query = "delete from emp where e_id = %s"
        cnt = self.cursor.execute(query,(id))
        self.db.commit()
        return cnt
    
    def insert(self,id,ko_name,en_name,mobile,address):
        query = """INSERT INTO emp VALUES(%s,%s,%s,%s,%s)"""
        cnt = self.cursor.execute(query,(id,ko_name,en_name,mobile,address))
        self.db.commit()
        return cnt
    
    
    def __del__(self):
        self.db.close()
        self.cursor.close()
        print("DaoSample_del__")


    
    
    
    
    
    