# -*- coding: utf-8 -*-
"""Valerie_Streamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16Yja0i261NvG04O6L2rvl456GpDBLGia

# Data extraction
"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

st.title("Cars dataset exploration")
url = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(url)
st.write(df.head())

"""# Exploration"""
st.write(df.info())
print("---"*40)
st.write("Dataset description", df.describe(include="all"))
print("---"*40)
st.write("Missed values", df.isna().sum())
print("---"*40)
st.write(df.duplicated().sum())
print("---"*40)

"""## Graphiques

"""

plt.title('Distribution of cars by continent')
countplot = sns.countplot(x='continent', data=df, palette='plasma')
st.pyplot(countplot.figure)

plt.title('Distribution of cylinders by weight')
violinplot1 = sns.violinplot(x='cylinders', y='weightlbs', data=df, palette='plasma')
st.pyplot(violinplot1.figure)

plt.title('Distribution of cylinders by cubicinches')
violinplot2 = sns.violinplot(x='cylinders', y='cubicinches', data=df, palette='plasma')
st.pyplot(violinplot2.figure)

plt.title('Heatmap of correlation')
heatmap = sns.heatmap(df.select_dtypes("number").corr(), annot=True, center=0, cmap='plasma')
st.pyplot(heatmap.figure)

plt.title('Pairplot of numerical columns')
pairplot = sns.pairplot(df.select_dtypes("number"), palette='plasma')
st.pyplot(pairplot.figure)
