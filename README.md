# sqlsrv_pgsql_no_downtime
Zero / near zero downtime migration from Ms-SQL Server to Postgresql.
In case of production environment, consider readonly mode till pgloader starts moving data. As soon as pgLoader has kickedin, feel free  to change back to read-write.

### Create Debezium container
Navigate to setup folder and create debezium-connect image with the following command before running docker-compose
docker build -t debezium-connect-sql-connector .

### Enable Snapshot Isolation
Navigate to setup folder and run snap_isolation.sql file on SQL Server database