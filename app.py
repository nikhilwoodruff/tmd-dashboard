import streamlit as st

import pandas as pd
import numpy as np

st.title("Full comparisons")
st.write(
    "This page shows the full comparisons between the PUF-PE 21, TD 23 and SOI statistics."
)
comparison_df = pd.read_csv("comparisons.csv.gz")

st.dataframe(comparison_df.dropna())

# ST metrics for: number of metrics with relative absolute error > 0.01, > 0.1, > 0.1

_col1, _col2 = st.columns(2)
with _col1:
    st.metric(
        "Number of SOI statistics accounted for",
        comparison_df[~comparison_df["PUF-PE 21"].isna()].shape[0],
    )

with _col2:
    st.metric(
        "Number of SOI statistics not accounted for",
        comparison_df[comparison_df["PUF-PE 21"].isna()].shape[0],
    )

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
        "Absolute error < 5bn",
        comparison_df[comparison_df["PUF-PE 21 - SOI"].abs() < 5].shape[0],
    )

with col2:
    st.metric(
        "Absolute error < 20bn",
        comparison_df[comparison_df["PUF-PE 21 - SOI"].abs() < 20].shape[0],
    )

with col3:
    st.metric(
        "Absolute error > 20bn",
        comparison_df[comparison_df["PUF-PE 21 - SOI"].abs() > 20].shape[0],
    )
