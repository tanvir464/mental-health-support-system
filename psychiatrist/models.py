from django.db import connection

# Create your models here.
def insert_data(arr):
    with connection.cursor() as cursor:
            # Example of an INSERT query
            cursor.execute(f"INSERT INTO tb_person (pFname,pLname,pGender,pContact,pEmail,pDOB,pBlood,pCountry,pPassword,pProfile,pAccType) VALUES{arr}")
            cursor.execute(f"SELECT pId FROM tb_person WHERE pContact={arr[3]}")
            read = cursor.fetchone()            
            cursor.execute(f"INSERT INTO tb_psychiatrist (pchipId) VALUES({read[0]})")
            connection.commit()

def select_data():
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute("SELECT * FROM tb_person, tb_psychiatrist WHERE pAccType = 2 AND pAccStatus = 1 AND pId = pchipId")
        rows = cursor.fetchall()
        return rows

def select_psychiatristcard_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT * FROM tb_person, tb_psychiatrist WHERE pId = pchipId AND pId = {id}")
        rows = cursor.fetchone()
        return rows
    
def select_psychiatristappointment_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT pId,pFname,pLname,pGender,pDOB, aId,adate,atime,aStatus FROM tb_person, tb_appointment WHERE aspId = {id} AND appId = pId")
        rows = cursor.fetchall()
        return rows 
    
def select_user_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT pId, pFname, pLname, pchipExpertise, pchipRating FROM tb_person, tb_psychiatrist WHERE pId = {id}")
        rows = cursor.fetchone()
        return rows