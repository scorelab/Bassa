There is already `db.config.json` file at `/components/core` setting up default values for database connection. If you want to override any of the key, just make a `user.db.config.json` file in directory same as of `db.config.json` with keys you want to override. <br>

Template for `user.db.config.json` file:
```json
{
    "BASSA_DB_NAME": "Bassa",
    "BASSA_HOST": "localhost",
    "BASSA_DB_USERNAME": "root",
    "BASSA_DB_PASSWORD": ""
}
```

