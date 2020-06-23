from constants import DDLMode
import logging
import os


ddl = DDLMode.NONE
log_level = logging.DEBUG
port_number = 8080

if os.environ.get('docker_build', 'false') is 'true':
    ddl = os.environ.get('ddl', ddl)
    log_level = os.environ.get('log_level', logging.DEBUG)
    port_number = os.environ.get('port_number', port_number)