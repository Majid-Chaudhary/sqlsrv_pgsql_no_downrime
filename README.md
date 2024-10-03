# sqlsrv_pgsql_no_downtime
Zero / near zero downtime migration from Ms-SQL Server to Postgresql.<br>
In case of production environment, consider readonly mode till pgloader starts moving data. As soon as pgLoader kicks in, feel free  to change back to read-write.

### Create Debezium Image
Navigate to setup folder and create debezium-connect image with the following command before running docker-compose:<br>
docker build -t debezium-connect-sql-connector .

### Enable Snapshot Isolation
Navigate to setup folder and run snap_isolation.sql file on SQL Server database

### CDC Test
You can test CDC using cdc_test.py file from cdc_test folder. Setting up pyodbc for SQL Server does require some tinkering.<br>
This script will insert a record per second into SQL Server's actor table, you can change it if required.