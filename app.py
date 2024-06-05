import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.title("2015 PUF replication of SOI targets")

st.write("This dashboard shows replication accuracy of the 2015 IRS SOI statistics from the 2015 PUF, in order to assess the 'best-possible' accuracy that PUF-deriving tax microdata can achieve.")

df = pd.read_csv("comparisons_puf.csv.gz")

st.dataframe(df)

st.subheader("Error quantiles")

fig = px.bar(
    df["Relative absolute difference"].quantile(np.linspace(0, 1, 100)),
    title="Relative absolute difference quantiles between PUF and SOI",
    labels={"index": "Percentile", "value": "Relative absolute difference"},
    log_y=True,
).update_layout(
    yaxis_tickformat=".2%",
    showlegend=False,
)

st.plotly_chart(fig)

is_large = (df.Count & (df["Value (SOI)"] > 10e6)) | (~df.Count & (df["Value (SOI)"] > 10e9))

fig_2 = px.bar(
    df[is_large]["Relative absolute difference"].quantile(np.linspace(0, 1, 100)),
    title="Relative absolute difference quantiles between PUF and SOI on large targets",
    labels={"index": "Percentile", "value": "Relative absolute difference"},
    log_y=True,
).update_layout(
    yaxis_tickformat=".2%",
    showlegend=False,
)

st.write("Large is defined as a count greater than 10 million or a value greater than 10 billion.")

st.plotly_chart(fig_2)