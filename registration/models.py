from django.db import connection

# Create your models here.
def select_login_data(contact,password):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT pId, pAccType, pAccStatus, pContact FROM tb_person WHERE pContact = '{contact}' OR pEmail = '{contact}' AND pPassword = '{password}'")
        rows = cursor.fetchone()
        return rows
    
def select_adminlogin_data(contact,password):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT auId FROM tb_admin WHERE auId = '{contact}' AND auPassword = '{password}'")
        rows = cursor.fetchone()
        return rows
    
def select_organizationlogin_data(contact,password):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT orgId FROM tb_organization WHERE orgEmail = '{contact}' AND orgPassword = '{password}'")
        rows = cursor.fetchone()
        return rows

def select_diagnosislogin_data(contact,password):
    with connection.cursor() as cursor:
        # Example of a SELECT query
        cursor.execute(f"SELECT dId FROM tb_diagnostic WHERE dEmail = '{contact}' AND dPassword = '{password}'")
        rows = cursor.fetchone()
        return rows

def select_loginuser_data(id) :
    with connection.cursor() as cursor:
        # Example of a SELECT query
        if id == "admin" :
            return "admin"
        cursor.execute(f"SELECT pId, pAccType FROM tb_person WHERE pId = {id}")
        rows = cursor.fetchone()
        if rows != None :
            rows = list(rows)
            rows.append("person")
        else :
            cursor.execute(f"SELECT orgId FROM tb_organization WHERE orgId = {id}")
            rows = cursor.fetchone()
            if rows!= None :
                rows = list(rows)
                rows.append("organization")
            else :
                cursor.execute(f"SELECT dId FROM tb_diagnostic WHERE dId = {id}")
                rows = cursor.fetchone()
            if rows!= None :
                rows = list(rows)
                rows.append("diagnosis")

        return rows