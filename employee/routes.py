from flask import Blueprint
from employee.controller import *
from utility.auth import *

flask_blue=Blueprint('routes',__name__)

flask_blue.add_url_rule("/sum/","sum",sum_2no,methods=['GET'])
flask_blue.add_url_rule("/query/","query",any_query,methods=['GET'])
flask_blue.add_url_rule("/all_record/","all_record",get_all_data,methods=['GET'])
flask_blue.add_url_rule("/record_id/","record_id",getdata_byid,methods=['POST'])
flask_blue.add_url_rule("/insert_data/","insert_data",insert_data,methods=['POST'])
flask_blue.add_url_rule("/delete_data/","delete_data",delete_data,methods=['DELETE'])
flask_blue.add_url_rule("/update_data/","update_data",update_data,methods=['PUT'])
flask_blue.add_url_rule("/authentication/","authentication",authentication,methods=['POST'])
flask_blue.add_url_rule("/protection/","protection",protected,methods=['GET'])


