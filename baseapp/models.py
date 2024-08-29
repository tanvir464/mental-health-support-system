from django.db import connection

# Create your models here.

def update_pendinguser_data(id):
    with connection.cursor() as cursor:
        # Example of an UPDATE query
        cursor.execute(f"UPDATE tb_person SET pAccStatus = 1 WHERE pId = {id}")

# specialist appointment accept reject start
def update_specialistacceptappointment_data(id):
    with connection.cursor() as cursor:
        # Example of an UPDATE query
        cursor.execute(f"UPDATE tb_appointment SET aStatus = 2 WHERE aId = {id}")

def update_specialistrejectappointment_data(id):
    with connection.cursor() as cursor:
        # Example of an UPDATE query
        cursor.execute(f"UPDATE tb_appointment SET aStatus = 0 WHERE aId = {id}")
# specialist appointment accept reject end
def update_workshopevent_data(arr):
    with connection.cursor() as cursor:
        # Example of an UPDATE query
        cursor.execute(f"UPDATE tb_eworkshop SET ewActivities = '{arr[0]}',ewFollow = '{arr[1]}',ewPrerequisite = '{arr[2]}',ewFacilitatorId = {arr[3]} WHERE ewId = {arr[4]}")

def update_eventparticipant_data(arr):
    with connection.cursor() as cursor:
        # Example of an UPDATE query        
        cursor.execute(f"UPDATE tb_eparticipant SET epStatus = {arr[2]} WHERE eeId = {arr[0]} AND epId = {arr[1]}")

def update_patientprofile_data(arr):
    with connection.cursor() as cursor:
        # Example of an UPDATE query
        cursor.execute(f"SELECT pPassword FROM tb_person WHERE pId = {arr[11]}")
        password = cursor.fetchone()
        if password[0] == arr[10]:
            cursor.execute(f"UPDATE tb_person SET pFname ='{arr[0]}',pLname='{arr[1]}',pProfile='{arr[2]}',pHouse='{arr[3]}',pRoad='{arr[4]}',pArea='{arr[5]}',pDistrict='{arr[6]}',pCountry='{arr[7]}' WHERE pId={arr[11]}")
            cursor.execute(f"UPDATE tb_patient SET ppEducation='{arr[8]}',ppEmployment='{arr[9]}' WHERE ppId = {arr[11]}")

def update_centerappointment_data(id):
    with connection.cursor() as cursor:
        # Example of an UPDATE query        
        cursor.execute(f"UPDATE tb_centerappointment SET caStatus = 2 WHERE caId = {id}")

def update_reportdone_data(id):
    with connection.cursor() as cursor:
        # Example of an UPDATE query                
        cursor.execute(f"UPDATE tb_report SET reportStatus = 2 WHERE reportcaId = {id}")
        cursor.execute(f"UPDATE tb_centerappointment SET caStatus = 0 WHERE caId = {id}")


# admin db control

def select_patientappointment_data():
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT pFname, pLname, pAccType, adate, atime, aStatus, aId FROM tb_appointment, tb_person WHERE aspId = pId")
        rows = cursor.fetchall()
        return rows
    
def select_centerappointmentpatient_data():
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT caDate,DATE_FORMAT(caTime,'%H:%m %p'),dName,dId FROM tb_centerappointment,tb_diagnostic,tb_prescription,tb_appointment WHERE presaId = aId AND caStatus = 1")
        rows = cursor.fetchall()
        return rows
    
def select_patientprescription_data():
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT presId, adate, pFname, pLname, pAccType FROM tb_prescription, tb_appointment, tb_person  WHERE aId = presaId AND aspId = pId")
        rows = cursor.fetchall()
        return rows
    
def select_patientreport_data():
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT reportId,reportDate,reportFile,dName FROM tb_report,tb_centerappointment,tb_diagnostic,tb_prescription,tb_appointment,tb_person WHERE reportStatus = 2 AND reportcaId = caId AND cadId = dId AND capId = presId AND presaId = aId AND appId = pId")
        rows = cursor.fetchall()
        return rows
    
def select_psychiatristappointment_data():
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT pId,pFname,pLname,pGender,pDOB, aId,adate,atime,aStatus FROM tb_person, tb_appointment WHERE appId = pId")
        rows = cursor.fetchall()
        return rows 
    
def select_psychologistappointment_data():
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT pId,pFname,pLname,pGender,pDOB, aId,adate,atime,aStatus FROM tb_person, tb_appointment WHERE appId = pId")
        rows = cursor.fetchall()
        return rows 