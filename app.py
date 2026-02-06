import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Student Performance Analysis")

df = pd.read_csv("students.csv")

st.subheader("Dataset")
st.dataframe(df)

st.subheader("Study Hours vs Marks")
fig, ax = plt.subplots()
ax.scatter(df["Hours_Studied"], df["Marks"])
ax.set_xlabel("Hours Studied")
ax.set_ylabel("Marks")
st.pyplot(fig)

st.markdown("### Insight")
st.write("Students who study more hours generally score higher marks.")

