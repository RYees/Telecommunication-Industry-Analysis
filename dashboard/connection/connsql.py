import streamlit as st
#pip install psycopg2
import psycopg2
import pandas as pd
import pandas.io.sql as sqlio


# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.cache_data    
def fetch_table(query) -> None:
    try:
        df = sqlio.read_sql_query(query, conn)
        return df
    except Exception as e:
        return f'Error: {str(e)}'
    
    
@st.cache_data(ttl=600)
def run_query(query):
    column_names = ['Bearer Id', 'Start', 'Start ms', 'End', 'End ms', 'Dur. (ms)',
       'MSISDN/Number', 'Last Location Name', 'Avg RTT DL (ms)',
       'Avg RTT UL (ms)', 'Avg Bearer TP DL (kbps)', 'Avg Bearer TP UL (kbps)',
       'TCP DL Retrans. Vol (Bytes)', 'TCP UL Retrans. Vol (Bytes)',
       'DL TP < 50 Kbps (%)', '50 Kbps < DL TP < 250 Kbps (%)',
       '250 Kbps < DL TP < 1 Mbps (%)', 'DL TP > 1 Mbps (%)',
       'UL TP < 10 Kbps (%)', '10 Kbps < UL TP < 50 Kbps (%)',
       '50 Kbps < UL TP < 300 Kbps (%)', 'UL TP > 300 Kbps (%)',
       'Activity Duration DL (ms)', 'Activity Duration UL (ms)', 'Dur. (ms).1',
       'Handset Manufacturer', 'Handset Type', 'Nb of sec with Vol DL < 6250B',
       'Nb of sec with Vol UL < 1250B', 'Social Media DL (Bytes)',
       'Social Media UL (Bytes)', 'Google DL (Bytes)', 'Google UL (Bytes)',
       'Email DL (Bytes)', 'Email UL (Bytes)', 'Youtube DL (Bytes)',
       'Youtube UL (Bytes)', 'Netflix DL (Bytes)', 'Netflix UL (Bytes)',
       'Gaming DL (Bytes)', 'Gaming UL (Bytes)', 'Other DL (Bytes)',
       'Other UL (Bytes)', 'Total UL (Bytes)', 'Total DL (Bytes)',
       'Sessions Frequency', 'Session Duration', 'Sessions Total Traffic',
       'Normalized Sessions Frequency', 'Normalized Session Duration',
       'Normalized Sessions Total Traffic', 'Engagement Group',
       'Normalized Session Frequency', 'Average TCP retransmission',
       'Average RTT', 'Average throughput', 'Experience Group', 'Cluster']
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()
        return column_names, rows

    
