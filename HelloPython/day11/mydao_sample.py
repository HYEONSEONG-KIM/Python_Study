import pymysql



class DaoSample:
    def __init__(self):
        self.db = pymysql.connect(host = 'localhost', user = 'root', password='python', database='pydb', port=3307)
        self.cursor = self.db.cursor()
        print("DaoSample_init__")
    
    def selectList(self):
        ret = []
        query = "SELECT * FROM sample"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        for row in data:
            ret.append({'col01' : row[0],'col02' : row[1],'col03' : row[2]})
        return ret    
    
    def update(self,col01,col02,col03):
        query = f"""
        UPDATE SAMPLE 
        SET COL02 = {col02}, COL03 = {col03}
         WHERE COL01 = {col01}"""
        cnt = self.cursor.execute(query)
        self.db.commit()
        return cnt
    
    def delete(self,col01):
        query = "delete from sample where col01 = %s"
        cnt = self.cursor.execute(query,(col01))
        self.db.commit()
        return cnt
    
    def insert(self,col01,col02,col03):
        query = """INSERT INTO SAMPLE VALUES(%s,%s,%s)"""
        cnt = self.cursor.execute(query,(col01,col02,col03))
        self.db.commit()
        return cnt
    
    
    def __del__(self):
        self.db.close()
        self.cursor.close()
        print("DaoSample_del__")

if __name__ == '__main__':
    ds = DaoSample()
    cntUp = ds.update(6,2,2)
    print(cntUp)
    arr = ds.selectList()
    print(arr)
    # cnt = ds.insert(14, 24, 14)
    # print(cnt)
    
    
    
    
    
    
    