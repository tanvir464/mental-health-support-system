from django.db import connection

# Create your models here.
def insert_data(arr):
    with connection.cursor() as cursor:
            # Example of an INSERT query
            cursor.execute(f"INSERT INTO tb_organization (orgName,orgContact,orgEmail,orgAddress,orgDate,orgType,orgPassword,orgPhoto) VALUES{arr}")            
            connection.commit()

def select_data():
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT orgId, orgName, orgType, orgContact,orgEmail FROM tb_organization")
        rows = cursor.fetchall()
        return rows

def select_user_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT orgId, orgName, orgType, orgRating FROM tb_organization WHERE orgId = {id}")
        rows = cursor.fetchone()
        return rows

def select_card_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT * FROM tb_organization WHERE orgId = {id}")
        rows = cursor.fetchone()
        return rows
    
def insert_event_data(arr):
    with connection.cursor() as cursor:
            # Example of an INSERT query
            cursor.execute(f"INSERT INTO tb_event (eOrgId,eTopic,eType,eMode,eDate,etTime,eLocation,eDescription,eDuration) VALUES{arr}")            
            id = cursor.lastrowid
            print(id)
            print(type(arr[2]))
            if arr[2] == "1" :
                cursor.execute(f"INSERT INTO tb_eworkshop (ewId) VALUES ({id})")
            elif arr[2] == "2" :
                cursor.execute(f"INSERT INTO tb_eseminar (esId) VALUES ({id})")
            connection.commit()

def select_allevent_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT eId,eTopic,eType,eMode,eDate,DATE_FORMAT(etTime, '%H:%m %p'),eDuration,eStatus FROM tb_event WHERE eOrgId = {id}")
        rows = cursor.fetchall()
        return rows

def select_workshopevent_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT eId,eTopic,eType,eMode,eDate,DATE_FORMAT(etTime, '%H:%m %p'),eDuration,eStatus,eLocation,ewActivities,ewFollow,ewPrerequisite,ewMaterial,ewFacilitatorId FROM tb_event,tb_eworkshop WHERE eId = {id} AND ewId=eId")
        rows = cursor.fetchone()
        
        if rows[13] != None :
            cursor.execute(f"SELECT pId,pFname,pLname,pAccType FROM tb_person WHERE pId={rows[13]}")
            fac = cursor.fetchone()
        else :
            fac = None
        return rows,fac


def select_facilitator_data():
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT pId,pFname,pLname,pAccType FROM tb_person WHERE pAccStatus = {1} AND pAccType = 2 OR pAccType = 3")
        rows = cursor.fetchall()
        return rows
    
def select_seminarevent_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT eId,eTopic,eType,eMode,eDate,DATE_FORMAT(etTime, '%H:%m %p'),eDuration,eStatus,eLocation,esSponsor,esAgenda,esSlide,esNote FROM tb_event,tb_eseminar WHERE eId = {id} AND esId=eId")
        rows = cursor.fetchone()
        cursor.execute(f"SELECT * FROM tb_espeaker WHERE eeId = {id}")
        speaker = cursor.fetchall()
        return rows,speaker
    
def insert_seminarspeaker_data(arr):
    with connection.cursor() as cursor:
            # Example of an INSERT query
            cursor.execute(f"INSERT INTO tb_espeaker (eeId,esId) VALUES{arr}")            
            connection.commit()


def select_eventcard_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT eId,eTopic,eType,eMode,eDate,DATE_FORMAT(etTime, '%H:%m %p'),eDuration,eLocation,eDescription,eStatus,eOrgId FROM tb_event WHERE eId = {id}")
        rows = cursor.fetchone()

        cursor.execute(f"SELECT orgName,orgType FROM tb_organization WHERE orgId = {rows[10]}")
        org = cursor.fetchone()

        if rows[2] == 1 :
            cursor.execute(f"SELECT ewActivities,ewFollow,ewPrerequisite,ewMaterial,ewFacilitatorId FROM tb_eworkshop where ewId = {rows[0]}")
            event = cursor.fetchone()
            print(event)
            if event[4] != None :
                cursor.execute(f"SELECT pId,pFname,pLname,pAccType FROM tb_person WHERE pId={event[4]}")
                fac = cursor.fetchone()            
        elif rows[2] == 2 :
            cursor.execute(f"SELECT esId,esSponsor,esAgenda,esSlide,esNote FROM tb_eseminar where esId = {rows[0]}")
            event = cursor.fetchone()
            
            cursor.execute(f"SELECT pId,pFname,pLname,pContact,pEmail,pAccType FROM tb_person, tb_espeaker where esId = pId AND eeId = {id}")
            fac = cursor.fetchall()
        return rows,event,fac,org
    
def insert_participant_data(arr):
    with connection.cursor() as cursor:
            # Example of an INSERT query
            cursor.execute(f"INSERT INTO tb_eparticipant (eeId,epId) VALUES{arr}")            
            connection.commit()

def select_eventparticipant_data(id):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT pId,pFname,pLname,pContact,pEmail,epStatus FROM tb_person,tb_eparticipant WHERE eeId = {id} AND epId = pId")
        rows = cursor.fetchall()
        return rows
