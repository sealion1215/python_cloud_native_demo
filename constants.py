from enum import Enum


class DDLMode(Enum):
    CREATE = 'CREATE'
    CREATE_DROP = 'CREATE_DROP'
    NONE = 'NONE'


dateTimeFormat = '%Y-%m-%d %H:%M:%S.%f'
