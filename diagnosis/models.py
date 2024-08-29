from django.db import connection

# Create your models here.
def insert_data(arr):
    with connection.cursor() as cursor:
            # Example of an INSERT query
            cursor.execute(f"INSERT INTO tb_diagnostic (dName,dContact,dEmail,dLocation,dPassword) VALUES{arr}")            
            connection.commit()

def select_data():
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT * FROM tb_diagnostic")
        rows = cursor.fetchall()
        return rows
    
def select_centercard_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT * FROM tb_diagnostic WHERE dId = {id}")
        rows = cursor.fetchone()
        return rows
    
def insert_appointment_data(arr):
    with connection.cursor() as cursor:
            # Example of an INSERT query
            cursor.execute(f"INSERT INTO tb_centerappointment (capId,cadId,caDate,caTime) VALUES{arr}")            
            connection.commit()

def select_appointmentpatient_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT caDate,DATE_FORMAT(caTime,'%H:%m %p'),dName,dId FROM tb_centerappointment,tb_diagnostic,tb_prescription,tb_appointment WHERE presaId = aId AND appId = {id} AND caStatus = 1")
        rows = cursor.fetchall()
        return rows
    
def select_appointmentcenter_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT caDate,DATE_FORMAT(caTime,'%H:%m %p'),caStatus,presId,pId,pFname,pLname,caId FROM tb_centerappointment,tb_prescription,tb_appointment,tb_person WHERE presaId = aId AND appId = pId AND cadId = {id}")
        rows = cursor.fetchall()
        return rows
    
def select_appointmentreport_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT caId,dName,pFname,pLname FROM tb_centerappointment,tb_diagnostic,tb_prescription,tb_appointment,tb_person WHERE capId = presId AND presaId = aId AND appId = pId AND cadId = dId AND caId = {id}")
        rows = cursor.fetchone()
        return rows
    
def insert_report_data(arr):
    with connection.cursor() as cursor:
            # Example of an INSERT query
            cursor.execute(f"INSERT INTO tb_report (reportcaId,reportDate,reportTime,reportFile) VALUES{arr}")
            connection.commit()

def select_reportdone_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT reportId,reportDate,DATE_FORMAT(reportTime,'%H:%m %p'),pFname,pLname FROM tb_report,tb_centerappointment,tb_prescription,tb_appointment,tb_person WHERE reportcaId = caId AND reportStatus = 2 AND capId = presId AND presaId = aId AND appId = pId AND cadId = {id}")
        rows = cursor.fetchall()
        return rows
    
def select_reportcard_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT reportId,reportDate,DATE_FORMAT(reportTime,'%H:%m %p'),reportFile,pFname,pLname,dName FROM tb_report,tb_centerappointment,tb_prescription,tb_appointment,tb_person,tb_diagnostic WHERE reportcaId = caId AND reportStatus = 2 AND capId = presId AND presaId = aId AND appId = pId AND cadId = dId AND reportId = {id}")
        rows = cursor.fetchone()
        return rows