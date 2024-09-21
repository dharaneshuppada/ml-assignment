import streamlit as st
import pandas as pd

# Streamlit App Title
st.title("Time-Wasters on Social Media Data Viewer")

# Upload file section
uploaded_file = st.file_uploader("Time-Wasters on Social Media.csv", type=["csv"])

# If a file is uploaded, read and display it
if uploaded_file is not None:
    # Read the uploaded CSV
    df = pd.read_csv("Time-Wasters on Social Media.csv")
    
    # Display the dataframe
    st.write("Here is your data:")
    st.dataframe(df)
    
    # Show basic statistics
    st.write("Basic Statistics:")
    st.write(df.describe())

    # Additional exploration options
    if st.checkbox("Show column names"):
        st.write(df.columns)
    
    if st.checkbox("Show data types"):
        st.write(df.dtypes)
    
    # Filter by column
    if st.checkbox("Filter by a specific column"):
        column = st.selectbox("Choose a column to filter", df.columns)
        unique_values = df[column].unique()
        selected_value = st.selectbox(f"Filter by {column}", unique_values)
        filtered_data = df[df[column] == selected_value]
        st.write(f"Data filtered by {column} = {selected_value}")
        st.dataframe(filtered_data)

# Add more functionalities here as per your dataset and requirements
