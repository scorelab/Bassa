#!/bin/bash

SCHEMA_DIR=/tmp/schema

mysql_exec=( mysql -uroot -p${MYSQL_ROOT_PASSWORD} )

if [[-z "$BASSA_DB_NAME" ]]
    echo "BASSA_DB_NAME is not defined."
    exit 1
fi

echo "Creating database ${BASSA_DB_NAME}..."
echo "DROP DATABASE IF EXISTS ${BASSA_DB_NAME}; CREATE DATABASE ${BASSA_DB_NAME};" | "${mysql_exec[@]}" &> /dev/null

mysql_exec_in_db=("${mysql_exec[@]}" "${BASSA_DB_NAME}")

for sql_file in $SCHEMA_DIR/*
do
    sql_file_name=$(basename $sql_file)
    echo "Dumping file ${sql_file_name} to ${BASSA_DB_NAME}..."
    "${mysql_exec_in_db[@]}" < ${sql_file} &> /dev/null
done

echo "Initial schema created!"
