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
st.write("Dataset preview")
st.dataframe(df.style.highlight_max(axis=0))

st.data_editor(
    df,
    column_config={
        "continent": st.column_config.SelectboxColumn(
            "origin continent",
            help="The category of the app",
            width="medium",
            options=[
                "US.",
                "Europe.",
                "Japan.",
            ],
            required=True,
        )
    },
    hide_index=True,
)
"""# Exploration"""
st.write("Dataset info")
st.write(df.info())
print("---"*40)
st.write("Dataset description", df.describe(include="all"))
print("---"*40)
st.write("Missed values", df.isna().sum())
print("---"*40)
st.write("There are : ", df.duplicated().sum(), " duplicates")
print("---"*40)

"""## Graphiques

"""

fig, ax = plt.subplots(5, 1)

sns.countplot(x='continent', data=df, palette='plasma', ax=ax[0])
ax[0].set_title('Distribution of cars by continent')

sns.violinplot(x='cylinders', y='weightlbs', data=df, palette='plasma', ax=ax[1])
ax[1].set_title('Distribution of cylinders by weight')

sns.violinplot(x='cylinders', y='cubicinches', data=df, palette='plasma', ax=ax[2])
ax[2].set_title("Distribution of cylinders by cubicinches')")

sns.heatmap(df.select_dtypes("number").corr(), annot=True, center=0, cmap='plasma', ax=ax[3])
ax[3].set_title('Heatmap of numerical columns')

sns.pairplot(df.select_dtypes("number"), palette='plasma', ax=ax[4])
ax[4].set_title('Pairplot of numerical columns')
plt.show()

st.pyplot(fig, use_container_width=True)
