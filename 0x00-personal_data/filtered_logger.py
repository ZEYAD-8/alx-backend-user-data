#!/usr/bin/env python3
"""
 -- first task : 0. Regex-ing: filter_datum
"""
from typing import List
import re
import logging
import mysql.connector
import os


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''
    Regex-ing - Write a function called filter_datum that
        returns the log message obfuscated:

    Arguments:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character
        is separating all fields in the log line

    Returns:
        a new string where all occurrences of each field in fields
        are replaced by redaction
    '''
    for field in fields:
        '''
        The re.sub function is used to search for a
        pattern in the message and
        replace it with a new string.
        '''
        message = re.sub(field + "=.*?" + separator,
                         field + "=" + redaction + separator,
                         message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''filter values in incoming log records using filter_datum'''
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    '''get_logger - returns a logging.Logger object'''
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stramHandle = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stramHandle.setFormatter(formatter)
    logger.addHandler(stramHandle)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    '''
    you will connect to a secure holberton database
    to read a users table. The database is protected
    by a username and password that are set as
    environment variables on the server named
    PERSONAL_DATA_DB_USERNAME (set the default as “root”),
    PERSONAL_DATA_DB_PASSWORD (set the default as an empty string)
    and PERSONAL_DATA_DB_HOST (set the default as “localhost”).

    Returns:
         A connector to the database
         mysql.connector.connection.MySQLConnection object.
    '''
    return mysql.connector.connection.MySQLConnection(
        host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        database=os.getenv('PERSONAL_DATA_DB_NAME'))


def main():
    '''
    The function will obtain a database connection
    using get_db and retrieve all rows in the users
    table and display each row under a filtered format.
    '''
    database = get_db()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = [i[0] for i in cursor.description]

    log = get_logger()

    for row in cursor:
        # Format each row into a string representation
        str_row = ''.join(f'{f}={str(r)};' for r, f in zip(row, fields))
        # Log the formatted row
        log.info(str_row.strip())

    cursor.close()
    database.close()


if __name__ == '__main__':
    main()
