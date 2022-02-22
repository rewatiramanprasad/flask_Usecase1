from utility.db import execute,execute_fetchall

def checking_credential(email,password_md5):
    count=execute_fetchall("select * from empuser where email='{}'and password_md5='{}'".format(email,password_md5))
    if len(count)==1:
        return True
    return False


def query(query):
    return execute_fetchall("select row_to_json(row) from ({}) row ".format(query))
    


def select():
    rows=execute_fetchall('select row_to_json(row) from (select * from employee) row ')
    return rows
    


def select_id(ID):
    rows=execute_fetchall("select row_to_json(row) from (select * from employee where department='{}') row".format(ID) )
    return rows
    
    
def insert(name,department,active,gender,role_id,):
    
    data1=execute_fetchall("select count(*) from employee")
    data=data1[0][0]
    emp_id="E0"+str(data+46)
    # print(emp_id)
    execute("insert into employee(id,name,department,active,gender,role_id) values(\'{}\',\'{}\',\'{}\',{},\'{}\',\'{}\')".format(emp_id,name,department,active,gender,role_id))
    rows=execute_fetchall("select row_to_json(row) from (select * from employee where department='{}') row".format(emp_id))
    return rows
    
    
    

def update(column_name,new_value,emp_id):
    #print("1. name \n2. department \n3. active \n3. gender\n4. role_id ")
    
    if(column_name=='name'):
        execute("update employee set name='{}' where id='{}';".format(new_value,emp_id))
    elif(column_name=="department"):
        execute("update employee set department='{}' where id='{}';".format(new_value,emp_id))
    elif(column_name=="gender"):
        execute("update employee set gender='{}' where id='{}';".format(new_value,emp_id))
    elif(column_name=="role_id"):
        execute("update employee set role_id='{}' where id='{}';".format(new_value,emp_id))
    elif(column_name=="active"):
        execute("update employee set active={} where id='{}';".format(new_value,emp_id))
    
    rows=execute_fetchall("select row_to_json(row) from (select * from employee where department='{}') row".format(emp_id))
    return rows
    


def delete(ID):
    execute("DELETE FROM employee WHERE id='{}'".format(ID))
    return 0
    
    