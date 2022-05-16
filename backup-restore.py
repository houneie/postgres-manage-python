from manage_postgres_db import *


DUMB_FILE = "backup"
#Src DB 
src_host = 
src_database_name
src_port
src_user
src_password

#Dest DB
dst_db_host
dst_db
dst_port
dst_user
dst_password

print("====>BackingUp<====")
backup_postgres_db(src_host, src_database_name, src_port, src_user, src_password, DUMB_FILE, True)
print("====>Restoring<====")
restore_postgres_db(dst_db_host, dst_db, dst_port, dst_user, dst_password, DUMB_FILE, True)