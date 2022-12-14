from mysql.connector import pooling
from dotenv import load_dotenv
import os

load_dotenv()

def db_conn():
    conn = pooling.MySQLConnectionPool(pool_name=os.getenv('pool_name'),
                                                pool_size= int(os.getenv('pool_size')),
                                                # pool_reset_session=os.getenv('reset_session'),
                                                host=os.getenv('pool_host'),
                                                database=os.getenv('pool_database'),
                                                user=os.getenv('pool_user'),
                                                password=os.getenv('pool_password'),
                                                port=int(os.getenv('pool_port')),
                                                auth_plugin=os.getenv("pool_auth_plugin"))  

    conn_object = conn.get_connection()

    return conn_object
        

db_conn()
