import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)


# Load the Iris dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")


st.title("Exploratory Data Analysis of Iris dataset in streamlit web")
st.header("This app create simple interactive dashboard to explore iris dataset")

#visualise the data in a table
st.subheader("1. dataframe or tabular presentation of the dataset")
st.dataframe(df)

# Create a dropdown menu to select the X and Y columns
x_column = st.sidebar.selectbox("X Column", df.columns)
y_column = st.sidebar.selectbox("Y Column", df.columns)

#create a histogram
selected_column = st.sidebar.selectbox("or select a class to visualise", df.columns)
st.subheader("2. Histoplot view")
sns.histplot(df[selected_column])
st.pyplot()

# Create a plot using Plotly Express
st.subheader("3. Scatter view of species")
fig = px.scatter(df, x=x_column, y=y_column, color="species")

# Use Seaborn to create a pairplot
st.subheader("4. Pairplot visualising the species")
sns.pairplot(df, hue="species")

# Display the plot and the pairplot in the Streamlit app
st.plotly_chart(fig)
st.pyplot()

# Display summary statistics
st.subheader("5. Summary Statistics or description of data")
st.write(df.describe())

# Create a bar plot
st.subheader("6. Bar Plot")
fig = px.bar(df, x="species", y=y_column)
st.plotly_chart(fig)

# Create a heatmap
st.subheader("Heatmap")
sns.heatmap(df.corr(), annot=True)
st.pyplot()



# Swarm plot
st.subheader('7. Swarm plot')
sns.swarmplot(x='species', y='petal_length', data=df)
st.pyplot()


# Show or hide Violin plot
if st.sidebar.checkbox('Show Violin plot'):
    st.subheader('8. Violin plot')
    sns.violinplot(x='species', y='petal_length', data=df)
    st.pyplot()

# Show or hide Box plot
if st.sidebar.checkbox('Show Box plot'):
    st.subheader('9. Box plot')
    sns.boxplot(x='species', y='petal_length', data=df)
    st.pyplot()







