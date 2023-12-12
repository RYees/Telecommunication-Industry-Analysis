import pandas.io.sql as sqlio
import psycopg2 as ps
from sqlalchemy import text
# import 
from sqlalchemy import create_engine
import pandas as pd

def db_connection_psycopg():
    # database connection using psycopg2
    pgconn = ps.connect(dbname="slack",
                    user= "postgres",
                    password= "123",
                    host="localhost",
                    port="5432")
    return pgconn

def db_read_table_psycopg(pgconn):
    sql = """ SELECT * FROM public.slack  """
    df = sqlio.read_sql_query(sql, pgconn)
    return df

def db_connection_sqlalchemy():
    engine = create_engine('postgresql+psycopg2://postgres:123@localhost/slack')
    return engine

def db_read_table_sqlalchemy(engine):
    query = 'SELECT * FROM public.xdr_data'
    crypto_data_df = pd.read_sql_query(query , engine)
    return crypto_data_df

def db_filter_table_sqlalchemy(engine):
    query = f"SELECT * FROM slack WHERE reaction_count > 4"
    slack_data_df = pd.read_sql_query(query , engine)
    return slack_data_df