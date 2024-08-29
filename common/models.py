from django.db import connection

# Create your models here.
def insert_resource_data(arr):
    with connection.cursor() as cursor:
            # Example of an INSERT query
            cursor.execute(f"INSERT INTO tb_resource (repId,reTitle,reType,reDes,reResource,reDate) VALUES{arr}")
            connection.commit()

def select_resource_data():
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT reId,repId,reTitle,reType,reDate,pFname,pLname FROM tb_resource, tb_person WHERE repId = pId")
        rows = cursor.fetchall()
        return rows

def select_resourcecard_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT reId,repId,reTitle,reType,reDate,reDes,pFname,pLname,pAccType FROM tb_resource, tb_person WHERE repId = pId AND reId = {id}")
        rows = cursor.fetchone()
        return rows

def select_pending_data(contact):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT pFname,pLname,pAccType FROM tb_person WHERE pContact = '{contact}' OR pEmail = '{contact}'")
        rows = cursor.fetchone()
        return rows
    
def select_pendingspecialist_data():
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT * FROM tb_person WHERE pAccStatus = 2 AND pAccType != 1")
        rows = cursor.fetchall()
        return rows
    
def select_appointmentcard_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT * FROM tb_appointment WHERE aId = {id}")
        rows = cursor.fetchone()
        cursor.execute(f"SELECT pId,pFname,pLname,pContact,pEmail,pAccType,pDOB FROM tb_person WHERE pId = {rows[1]} AND pAccType = 1")
        patient = cursor.fetchone()
        cursor.execute(f"SELECT pId,pFname,pLname,pContact,pEmail,pAccType FROM tb_person WHERE pId = {rows[2]}")        
        specialist = cursor.fetchone()
        if specialist[5] == 2 :
             cursor.execute(f"SELECT pchiFee FROM tb_psychiatrist WHERE pchipId = {rows[2]}")
             fee = cursor.fetchone()
        elif specialist[5] == 3 :
             cursor.execute(f"SELECT pchoFee FROM tb_psychologist WHERE pchopId = {rows[2]}")
             fee = cursor.fetchone()      
        return (rows,patient,specialist,fee)

def select_allevent_data():
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT eId,eTopic,eType,eMode,eDate,DATE_FORMAT(etTime, '%H:%m %p'),eDuration,eStatus FROM tb_event WHERE eStatus = 1")
        rows = cursor.fetchall()
        return rows
    
def select_event_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT orgName,orgType,eId,eTopic,eType,eMode,eDate,DATE_FORMAT(etTime,'%H:%m %p'),eDuration,eLocation,eDescription,eStatus FROM tb_organization, tb_event, tb_eparticipant WHERE epId = {id} AND eeId = eId AND eOrgId = orgId AND epStatus = 1")
        rows = cursor.fetchall()
        return rows

