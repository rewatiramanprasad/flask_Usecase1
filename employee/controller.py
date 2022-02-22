from flask import Flask,request
from utility.validation import *
from employee.SQLcontroler import *
from flask_jwt_extended import *



# @error.errorhandler(404)

def sum_2no():
    flag=True
    message=None
    value=None
    data =request.get_json()
    valid=validate_2no(data)
    if (valid[0]):
        # try:
        value=data["num1"]+data["num2"]
        status_code=200
        message="successful execution"
        # except Exception as e:
        #     message=str(e)
        #     flag=False
        #     status_code=400
    else:
        message=valid[1]
        status_code=400

    response={
    "sucess":flag,
    "data":value,
    "message":message
    }
    return response,status_code


    

def any_query():
    value=None
    message=None
    flag=True
    data=request.get_json()
    valid=isvalidquery(data)

    if (valid[0]): 
        # try:
        q=data["query"]
        value=query(q)
        message=str(len(value))+" rows fetched"
        status_code=200
        # except Exception as e:
        #     flag=False
        #     message=str(e)
        #     status_code=400
    else:
        message=valid[1]
        status_code=400

    response={
    "sucess":flag,
    "data":value,
    "message":message
    }
    return response,status_code


def get_all_data():
    flag=True
    value=None
    # try:
    value=select()
    message=str(len(value))+" row fetched"
    status_code=200
    # except Exception as e :
        
    #     flag=False
    #     message=str(e)
    #     status_code=400

    response={
    "sucess":flag,
    "data":value,
    "message":message
    }
    
    return response,status_code


def getdata_byid():
    flag=True
    message=None
    value=None
    data=request.get_json()
    valid=isvalid_departmentid(data)
    if(valid[0]):
        # try:
        value=select_id(data["id"])
        message=str(len(value))+" row fetched"
        status_code=200
        # except Exception as e:
        #     message=str(e)
        #     flag=False
        #     status_code=400
    else:
        message=valid[1]
        status_code=400

    
    response={
    "sucess":flag,
    "data":value,
    "message":message
    }
    return response,status_code
@jwt_required(optional=True)
def insert_data():
    value=None
    message=None
    flag=True
    data=request.get_json()
    valid=isvalid_employee(data)
    if valid[0]:

        # try:
        value=insert(data["name"],data["department"],data["active"],data["gender"],data["role_id"])
        message=str(len(value))+" row fetched"
        status_code=200
        # except Exception as e:
        #     message=str(e)
        #     flag=False
        #     status_code=400
    else:
        message=valid[1]
        status_code=400

    response={
    "sucess":flag,
    "data":value,
    "message":message
    }
    return response,status_code
@jwt_required(optional=True)
def delete_data():
    value=None
    message=None
    flag=True
    data=request.get_json()
    valid=isvalid_empid(data)
    if valid[0]:
        # try:
        data=request.get_json()
        value=delete(data["emp_id"])
        message="deleted successfully"
        status_code=200
        # except Exception as e:
        #     message=str(e)
        #     flag=False
        #     status_code=400
    else:
        message=valid[1]
        status_code=400


    response={
    "sucess":flag,
    "data":value,
    "message":message
    }

    return response,status_code

@jwt_required(optional=True)
def update_data():
    value=None
    message=None
    flag=True
    data=request.get_json()
    valid=isvalid_update(data)
    if valid[0]:
        # try:
            
        value=update(data["column_name"],data["new_value"],data["emp_id"])
        message="sucessfully update"
        status_code=200
        # except Exception as e:
        #     message=str(e)
        #     flag=False
        #     status_code=400
            
    else:
        message=valid[1]
        status_code=400

    response={
    "sucess":flag,
    "data":value,
    "message":message
    }
    
    return response,status_code
