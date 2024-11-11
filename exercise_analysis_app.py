# Save this as `exercise_analysis_app.py`

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for seaborn
sns.set(style="whitegrid")

# Title of the Streamlit app
st.title("Exercise Data Analysis Application")

# Upload dataset
st.header("Upload Your Dataset")
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Read dataset
    df = pd.read_csv(uploaded_file)
    
    # Display basic dataset information
    st.subheader("Dataset Overview")
    st.write("Shape of the dataset:", df.shape)
    st.write("Columns in the dataset:", df.columns.tolist())
    
    # Display data sample
    st.subheader("Data Sample")
    st.write(df.head())
    
    # Display summary statistics
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # Visualizations
    st.subheader("Data Visualizations")
    
    # Scatter plot
    st.write("Scatter Plot of [Choose columns]")
    scatter_x = st.selectbox("Select X-axis", df.columns)
    scatter_y = st.selectbox("Select Y-axis", df.columns)
    
    if scatter_x and scatter_y:
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=scatter_x, y=scatter_y, ax=ax)
        st.pyplot(fig)
    
    # Histogram
    st.write("Histogram of Selected Column")
    hist_column = st.selectbox("Select column for histogram", df.columns)
    
    if hist_column:
        fig, ax = plt.subplots()
        sns.histplot(df[hist_column], kde=True, ax=ax)
        st.pyplot(fig)
    
    # Boxplot
    st.write("Box Plot of Selected Column")
    box_column = st.selectbox("Select column for boxplot", df.columns)
    
    if box_column:
        fig, ax = plt.subplots()
        sns.boxplot(x=df[box_column], ax=ax)
        st.pyplot(fig)
    
else:
    st.write("Please upload a CSV file to proceed.")