import streamlit as st
# from streamlit.logger import get_logger
import matplotlib.pyplot as plt
import connection.connsql as con 
import plotly.express as px
import pandas as pd
import os
import plotly.figure_factory as ff
import warnings
warnings.filterwarnings('ignore')


def run():
    custom_css = """
        body {
            background-color: #333;
        }
        .header {
            margin-top: 9rem;
            font-size: 3rem;
        }
    """
      # Apply the custom CSS
    st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)    

    column_names, rows = con.run_query("SELECT * from cleaned_telecom")
    data_frame = pd.DataFrame(rows, columns=column_names)
    # st.write(data_frame['Bearer Id'][0])

    data_frame["Handset Type"].value_counts()

    col1, col2 = st.columns((2))
    with col1:
        st.markdown('<div class=""><h5>The top most 5 devices used by users</h5></div>', unsafe_allow_html=True)
        value_counts = data_frame["Handset Type"].value_counts()

        # Convert the value counts to a DataFrame
        value_counts_df = value_counts[:5].reset_index()
        value_counts_df.columns = ["Handset Type", "Count"]
        # Create a bar chart using Plotly
        fig = px.bar(
            value_counts_df,
            x="Handset Type",
            y="Count",
            text=value_counts_df["Count"],
            template="seaborn"
        )

        # Remove the y-axis label
        fig.update_yaxes(showticklabels=False)

        # Remove the grid lines
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)

        # Set chart height and display on Streamlit
        st.plotly_chart(fig, use_container_width=True, height = 200)
    
    # Apply the custom CSS
    # st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class=""><h5>The least 5 devices used by users</h5></div>', unsafe_allow_html=True)
        value_counts = data_frame["Handset Type"].value_counts()

        # Get the last 5 devices with the smallest count
        last_5_smallest = value_counts.nsmallest(5)

        # Convert the value counts to a DataFrame
        value_counts_df = last_5_smallest.reset_index()
        value_counts_df.columns = ["Handset Type", "Count"]

        fig = px.bar(
            value_counts_df,
            x="Handset Type",
            y="Count",
            text=value_counts_df["Count"],
            template="seaborn"
        )
        # Remove the y-axis label
        fig.update_yaxes(showticklabels=False)

        # Remove the grid lines
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)

        # Set chart height and display on Streamlit
        st.plotly_chart(fig, use_container_width=True)

    
    col1, col2 = st.columns((2))
    with col1:
        st.markdown('<div class="header">The top most 3 manufactures</div>', unsafe_allow_html=True)      

    with col2:
        #st.markdown('<div class="header"><h6>The top most 3 manufactures</h6></div>', unsafe_allow_html=True)
        value_counts = data_frame["Handset Manufacturer"].value_counts()
        # Get the last 5 devices with the largest count
        top_5_largest = value_counts.nlargest(3)
        # Convert the value counts to a DataFrame
        value_counts_df = top_5_largest.reset_index()
        value_counts_df.columns = ["Handset Manufacturer", "Count"]
        # Create a line chart using Plotly
        fig = px.line(
            value_counts_df,
            x="Handset Manufacturer",
            y="Count",
            text=value_counts_df["Count"],
            template="seaborn",
        )
        # Remove the axis label
        #fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False) 
        # Remove the grid lines
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        # Set chart height and display on Streamlit
        st.plotly_chart(fig, use_container_width=True, height=200)



    apple_data = con.fetch_table('SELECT * from "Apple_handsets"')
    apple_data = pd.DataFrame(apple_data)
    #print(apple_data.head(1))
    huawei_data = con.fetch_table('SELECT * from "Huawei_handsets"')
    huawei_data = pd.DataFrame(huawei_data)
    #print(apple_data.head(1))
    samsung_data = con.fetch_table('SELECT * from "Samsung_handsets"')
    samsung_data = pd.DataFrame(samsung_data)
    #print(apple_data.head(1))

    
    st.subheader(":point_down: Manufacturers vs Users Summary")
    col1, col2, col3 = st.columns((3))  
    with col1:
        st.markdown("Apple Manufacturer")
        df_sample = apple_data.loc[:3, ["Handset Type", "Count"]]
        df_sample = df_sample.rename(columns={"Count": "users"})
        fig = ff.create_table(df_sample, colorscale = "Cividis")
        st.plotly_chart(fig, use_container_width=True, width=200)
    with col2:
        st.markdown("Huawei Manufacturer")
        df_sample = huawei_data.loc[:3, ["Handset Type", "Count"]]
        df_sample = df_sample.rename(columns={"Count": "users"})
        fig = ff.create_table(df_sample, colorscale = "Cividis")
        st.plotly_chart(fig, use_container_width=True, width=200)

    with col3:
        st.markdown("Samsung Manufacturer")
        df_sample = samsung_data.loc[:3, ["Handset Type", "Count"]]
        df_sample = df_sample.rename(columns={"Count": "users"})
        fig = ff.create_table(df_sample, colorscale = "Cividis")
        st.plotly_chart(fig, use_container_width=True, width=200)
  


if __name__ == "__main__":
    run()

