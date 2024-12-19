task 0
How does the function work?

    the loop itreates over each field name in the fields list
    => fields = ["password", "date_of_birth"]
    why ? -- To process and obfuscate each specified field one by one.

    message = re.sub(field + "=.*?" + separator,
                         field + "=" + redaction + separator,
                         message)

    lets breakdown >>

    field + "=.*?" + separator
     => matches the fieldName followed by an "=" and matches any character up to the next occurrence of the seprator ";"
    field + "=" + redaction + separator
     => matches the fieldName and "=" as `email=` and replace the original field value with the redaction  string "xxx" followed by the seprator.

    why ? To obfuscate the value of the specified field in the message.
=====================================
task 1
    How does the class's Format Method work?
    
    def format(self, record: logging.LogRecord) -> str:
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)

    => This method overrides the format method of the logging.Formatter class
    to customize how log records are formatted
     -- How does the formatting method work?
        ``` 
            def format(self, record):
            """
            Format the specified record as text.

            :param record: The log record to be formatted
            :type record: logging.LogRecord
            :return: The formatted log message
            :rtype: str
            """
            # Define the format string
            format_str = '%(asctime)s - %(levelname)s - %(message)s'
            
            # Perform substitution
            formatted_message = format_str % {
                'asctime': self.formatTime(record),
                'levelname': record.levelname,
                'message': record.getMessage(),
            }
            
            return formatted_message
        ```
        The format method is flexible, allowing you to customize the log message format according to your requirements. It's a fundamental part of Python's logging system and provides a powerful way to control how log messages are presented.

        detailed :
        --> Calls the format method of the superclass (logging.Formatter), which formats the log record into a string based on the format specified ([HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s).

    -- filter_datum() => calls the function to obfuscate sensitive information in log message to apply redaction to specified fields in the log message before formatting and returning the final log record string.

    super().format(record) => Calls the format method of the superclass (logging.Formatter) to format the log record.

================================
task 2
How does the function work?
    
    -- Logger
        =>This logger is used to capture and manage log messages related to user data operations.

    -- Logger Level
        => This ensures that log messages with severity 'INFO'.

    -- Propagation
        ---- logger.propagate = False
        => Ensures that log messages are only handled by this specific logger and not passed up to ancestor loggers.

    -- StramHandler
        => To send log message to the console, stream handler is responsible for outputting log messages to the console.
    
    -- Formatter
        => Formats the log messages according to the specified format and redacts PII fields before outputting.

    -- logger.addHandler(stramHandle)
        => Ensures that log messages captured by the 'user_data' logger are processed by the StreamHandler and outputted to the console.

====================================
task 3
How does the function work?

    The get_db function establishes and returns a connection to a MySQL database using the mysql.connector library. It retrieves connection parameters from environment variables for flexibility and security.

    Returns:

        mysql.connector.connection.MySQLConnection: A connection object representing a connection to the MySQL database.

==============================
task 4
How does function work ?

    This function ensures that each row from the users table is logged in a filtered format, as specified by the logger's setup. It encapsulates the process of fetching data from the database and logging it, providing a clear and modular approach to database interaction and logging within the application.

    -- Database Connection and Cursor Setup:
        database = get_db()
        => Obtain a database connection using get_db().
        cursor = database.cursor()
        => Create a cursor object to execute SQL queries.

    -- Execute SQL Query:
        cursor.execute("SELECT * FROM users;")
        => This query selects all rows (*) from the users table 
        in the connected database.
        => Execute a SELECT query to fetch all rows from the users table.
        fields = [i[0] for i in cursor.description]
        => Retrieve column names from the cursor description.
    
    -- Logger Setup:
        Initialize a logger using get_logger().
    
    --Logging Rows:
        Iterate over each row fetched from the database.
        Format each row into a string representation using a list comprehension.
        Log each formatted row using the log.info() method.

        for row in cursor
         => This loop iterates over each row fetched from the database using the cursor.

        str_row = ''.join(f'{f}={str(r)}; ' for r, f in zip(row, fields))
        => zip(row, fields) pairs each value in the row with its corresponding field name
        => {f}={str(r)}; formats each field name and its corresponding value as a string and concatenates them together.

        log.info(str_row.strip())
        => info() method is used to log an informational message.
        => removes any leading or trailing whitespace characters from the formatted row string before logging it.

    -- Close Cursor and Database Connection:
        Close the cursor to release resources.
        Close the database connection.
