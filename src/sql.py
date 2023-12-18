import pandas.io.sql as sqlio
import psycopg2 as ps
from sqlalchemy import text
from sqlalchemy import create_engine, Column, Integer, String, Float, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

def db_connection_psycopg():    
    # database connection using psycopg2
    try:
        pgconn = ps.connect(dbname="telecom",
                        user= "postgres",
                        password= "123",
                        host="localhost",
                        port="5432")
        return pgconn
    except Exception as e:
        return f'Error: {str(e)}'
    

def db_read_table_psycopg(pgconn) -> None:
    try:
        sql = """ SELECT * FROM public.slack """
        df = sqlio.read_sql_query(sql, pgconn)
        return df
    except Exception as e:
        return f'Error: {str(e)}'
    

def db_connection_sqlalchemy():
    try:
        engine = create_engine('postgresql+psycopg2://postgres:123@localhost/telecom')
        return engine
    except Exception as e:
            return f'Error: {str(e)}'
    

def db_create_table_sqlalchemy(engine, tablename) -> None:
    try:
        meta = MetaData()
        TableCreation = Table(
            tablename, meta
        )
        meta.create_all(engine)
    except Exception as e:
        return f'Error: {str(e)}'
    

def db_table_insert_dataframe_sqlalchemy(df, tablename, engine) -> None:
    try:
        df.to_sql(tablename, engine, if_exists='replace', index=False)
        return 'Successfully Added'
    except Exception as e:
        return f'Error: {str(e)}'
    

def db_read_table_sqlalchemy(engine) -> None:
    try:
        query = 'SELECT * FROM public.xdr_data'
        data_df = pd.read_sql_query(query , engine)
        return data_df
    except Exception as e:
        return f'Error: {str(e)}'
    

def db_filter_table_sqlalchemy(engine) -> None:
    try:
        query = f"SELECT * FROM slack WHERE reaction_count > 4"
        data_df = pd.read_sql_query(query , engine)
        return data_df
    except Exception as e:
        return f'Error: {str(e)}'