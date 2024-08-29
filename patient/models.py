from django.db import connection

# Create your models here.
def insert_data(arr):
    with connection.cursor() as cursor:
            # Example of an INSERT query
            cursor.execute(f"INSERT INTO tb_person (pFname,pLname,pGender,pContact,pEmail,pDOB,pBlood,pCountry,pPassword,pProfile,pAccType) VALUES{arr}")
            cursor.execute(f"SELECT pId FROM tb_person WHERE pContact={arr[3]}")
            read = cursor.fetchone()            
            cursor.execute(f"INSERT INTO tb_patient (ppId) VALUES({read[0]})")
            connection.commit()

def select_data():
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute("SELECT * FROM tb_person WHERE pAccType = 1 AND pAccStatus = 1")
        rows = cursor.fetchall()
        return rows

def select_pending_data():
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute("SELECT * FROM tb_person WHERE pAccType = 1 AND pAccStatus = 2")
        rows = cursor.fetchall()
        return rows
    
def insert_appointment_data(arr):
    with connection.cursor() as cursor:
            # Example of an INSERT query
            cursor.execute(f"INSERT INTO tb_appointment (appId,aspId,adate,atime) VALUES{arr}")                      
            connection.commit()

def select_readforappointment_data():
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute("SELECT * FROM tb_person WHERE (pAccType = 2 OR pAccType = 3) AND pAccStatus = 1")
        rows = cursor.fetchall()
        return rows

def select_appointment_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT pFname, pLname, pAccType, adate, atime, aStatus, aId FROM tb_appointment, tb_person WHERE appId = {id} AND aspId = pId")
        rows = cursor.fetchall()
        return rows
    
def select_user_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT pId, pFname, pLname FROM tb_person WHERE pId = {id}")
        rows = cursor.fetchone()
        return rows

def select_patientcard_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT * FROM tb_person, tb_patient WHERE pId = {id}")
        rows = cursor.fetchone()
        return rows
    

def insert_prescription_data(arr):
    with connection.cursor() as cursor:
            # Example of an INSERT query
            cursor.execute(f"INSERT INTO tb_prescription (presaId,presTest,presMedicine,presAdvice,presDate) VALUES{arr}")                      
            connection.commit()

def select_prescription_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT presId, adate, pFname, pLname, pAccType FROM tb_prescription, tb_appointment, tb_person  WHERE aId = presaId AND appId = {id} AND aspId = pId")
        rows = cursor.fetchall()
        return rows

def select_prescriptioncard_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT * FROM tb_prescription WHERE presaId = {id}")
        pres = cursor.fetchone()
        cursor.execute(f"SELECT pId,pFname,pLname,pAccType FROM tb_person,tb_appointment WHERE aId = {pres[1]} AND aspId = pId")
        spe = cursor.fetchone()
        cursor.execute(f"SELECT pId,pFname,pLname,pAccType,pDOB FROM tb_person,tb_appointment WHERE aId = {pres[1]} AND appId = pId")
        patient = cursor.fetchone()
        return pres,spe,patient

def select_report_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT reportId,reportDate,reportFile,dName FROM tb_report,tb_centerappointment,tb_diagnostic,tb_prescription,tb_appointment,tb_person WHERE reportStatus = 2 AND reportcaId = caId AND cadId = dId AND capId = presId AND presaId = aId AND appId = pId AND appId = {id}")
        rows = cursor.fetchall()
        return rows
    
def select_profile_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT * FROM tb_person, tb_patient  WHERE pId = {id} AND ppId = pId")
        rows = cursor.fetchone()
        return rows

def appointment_chart_data():
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute("SELECT aId, aDate, pFname, pLname, pAccType FROM mhm_system_db.tb_appointment, mhm_system_db.tb_person where appId = 7 AND aspId = pId")
        rows = cursor.fetchall()
        return rows