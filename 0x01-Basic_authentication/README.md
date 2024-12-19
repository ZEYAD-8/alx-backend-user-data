### 1. Obfuscating Data in Logs

Use the `filter_datum` function to obfuscate specific fields in a log message. Here's how to use it in your Python code:

```python
from filtered_logger import filter_datum

fields = ["password", "date_of_birth"]
message = "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;"
obfuscated_message = filter_datum(fields, 'xxx', message, ';')
print(obfuscated_message)
```

### 2. Logging with Redacted PII

To create a logger that automatically redacts specified PII fields, use the `RedactingFormatter` class:

```python
import logging
from filtered_logger import get_logger

logger = get_logger()
logger.info("User login: email=bob@dylan.com; password=verysecret;")
```

### 3. Secure Database Connection

To connect to a database securely, use the `get_db` function. Ensure you have set the required environment variables (`PERSONAL_DATA_DB_USERNAME`, `PERSONAL_DATA_DB_PASSWORD`, `PERSONAL_DATA_DB_HOST`, and `PERSONAL_DATA_DB_NAME`):

```python
from filtered_logger import get_db

db_connection = get_db()
# Use db_connection as needed
```

### 4. Password Hashing and Verification

To hash and verify passwords securely, use the `hash_password` and `is_valid` functions:

```python
from encrypt_password import hash_password, is_valid

password = "MyAmazingPassw0rd"
hashed_password = hash_password(password)

# Verify the password
print(is_valid(hashed_password, password))
```

## Contributing

Contributions to this project are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

 All rights reserved to ALX
