import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Covid India Dashboard", layout="wide")
df = pd.read_csv("Latest Covid-19 India Status.csv")

st.write("<h1 style='text-align: center;'>Covid India Dashboard</h1>", unsafe_allow_html=True)

c1, c2 = st.columns(2)

total_cases_by_states = px.pie(
    df,
    values="Total Cases",
    names="State/UTs",
    template="plotly_white",
    title="<b>Total cases by States/UTs</b>"
)

total_population_by_states = px.pie(
    df,
    values="Population",
    names="State/UTs",
    template="plotly_white",
    title="<b>Total population by States/UTs</b>"
)

c1.plotly_chart(total_cases_by_states, use_container_width=True)
c2.plotly_chart(total_population_by_states, use_container_width=True)

st.markdown("""---""")

below_col_1, below_col_2 = st.columns(2)
fig = px.bar(df,
             x='State/UTs',
             y='Deaths',
             color='State/UTs',
             title='State/UTs Vs No. of Deaths'
             )

below_col_1.plotly_chart(fig)
