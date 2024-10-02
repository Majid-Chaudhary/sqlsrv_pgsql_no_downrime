# sqlsrv_pgsql_no_downtime
Zero downtime migration from Ms-SQL Server to Postgresql

## Navigate to setup folder and create debezium-connect image with the following command before running docker-compose
docker build -t debezium-connect-sql-connector .