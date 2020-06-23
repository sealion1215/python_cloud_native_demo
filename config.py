from constants import DDLMode
import logging
import os

db_host = 'localhost'
db_port = 3306
db_user = 'root'
db_password = '1234567'
db_schema = 'python_cloud_native_demo'
ddl = DDLMode.CREATE
log_level = logging.DEBUG
port_number = 8080

if os.environ.get('docker_build', 'false') is 'true':
    db_host = os.environ.get('localhost', db_host)
    db_port = os.environ.get(3306, db_port)
    db_user = os.environ.get('root', db_user)
    db_password = os.environ.get('1234567', db_password)
    ddl = os.environ.get('ddl', ddl)
    log_level = os.environ.get('log_level', logging.DEBUG)
    port_number = os.environ.get('port_number', port_number)