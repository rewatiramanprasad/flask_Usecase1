from cerberus.validator import Validator
def credential(data):
    schema = {'email': {'type': 'string','required':True},'password': {'type': 'string','required':True}}
    v=Validator(schema)
    if (v.validate(data)):
        return (True,"validation sucessfully")
    else:
        return (False,v.errors)


def validate_2no(data):
    schema = {'num1': {'type': 'integer'},'num2': {'type': 'integer'}}
    v=Validator(schema)
    if (v.validate(data)):
        return (True,"validation sucessfully")
    else:
        return (False,v.errors)

def isvalidquery(query):
    schema = {'query': {'type': 'string'}}
    v=Validator(schema)
    if (v.validate(query)):
        return (True,"validation sucessfully")
    else:
        return (False,v.errors)

def isvalid_departmentid(id):
    schema = {'id': {'type': 'string',
                                'regex':"D{1}[0-9]{3}"}}
    v=Validator(schema)
    if (v.validate(id)):
        return (True,"validation sucessfully")
    else:
        return (False,v.errors)

def isvalid_employee(id):
    schema = {'name': {'type': 'string'},
               'department': {'type': 'string','regex':"D{1}[0-9]{3}"},
               'active': {'type': 'integer','regex':'1|0'},
               'gender': {'type': 'string','regex':'M|F'},
               'role_id': {'type': 'string','regex':"R{1}[0-9]{3}"},}
    v=Validator(schema)
    if (v.validate(id)):
        return (True,"validation sucessfully")
    else:
        return (False,v.errors)


def isvalid_empid(id):
    schema = {'emp_id': {'type': 'string',
                                'regex':"E{1}[0-9]{3}"}}
    v=Validator(schema)
    if (v.validate(id)):
        return (True,"validation sucessfully")
    else:
        return (False,v.errors)


def isvalid_update(data):
    schema = {"column_name":{'type':'string'},
                "new_value":{'type':'string'},
            'emp_id': {'type': 'string','regex':"E{1}[0-9]{3}"}}
    v=Validator(schema)
    if (v.validate(data)):
        return (True,"validation sucessfully")
    else:
        return (False,v.errors)