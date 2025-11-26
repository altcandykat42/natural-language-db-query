from db import create_tables, add_sample_data
from query import generate_query
from result import get_result
from desc import generate_desc
import streamlit as st
import pandas as pd

def main():
    flag = 0
    if flag == 0:
         create_tables()
         add_sample_data()
         flag += 1
    st.set_page_config(page_title="DB QUERY")
    st.title("DATABASE QUERY AI 🤖")
    table_name = st.selectbox("Select a table to view:", ["Employees", "Departments"])
    r,c = get_result(f"SELECT * FROM {table_name}")
    if st.button("Show Data") and table_name != None:
        st.write(f"### SAMPLE DATABASE {table_name} IN USE: ")
        st.write(pd.DataFrame(r,columns=c))
    # User input for SQL query
    query = st.text_area("Enter SQL Query:", height=100)

    if st.button("Run Query"):
        s_query = generate_query(query)
        rows, columns = get_result(s_query)
        print(s_query)
        print(rows, columns)
        result_desc = generate_desc(query=s_query,result=rows)
        df = pd.DataFrame(rows, columns=columns)
        st.write('### QUERY EXECUTED : ')
        st.write(s_query)
        # st.write(df)
        if rows == []:  # If error message is returned
                st.error(f"Error: NO RESULTS FOUND")
                st.error(result_desc)
        else:
            df = pd.DataFrame(rows, columns=columns)
            st.write("### Query Results:")
            st.dataframe(df)
            st.write('### Summary: ')
            st.write(result_desc)

if __name__ == "__main__":
    main()
