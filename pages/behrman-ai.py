import streamlit as st
import numpy as np
from app.utils import page_setup, metric_card, load_leap_data, elem_ai_calc

st.set_page_config(page_title="Behrman LEAP", layout="wide")
page_setup()

st.title("Behrman LEAP Results")

behrman = load_leap_data("Behrman")

## Set filters
# Year Select
years = sorted(behrman['SPSYear'].unique())
st.sidebar.subheader("Select School Year", help="The year selected represents the first year of the school year span. E.g., when you select year 2022 you're selecting school year 2022-2023")
yr_choice = st.sidebar.selectbox("*Choose a School Year*", options=years, index=(len(behrman['SPSYear'].unique())-1))
behrman = behrman[behrman['SPSYear'] == yr_choice]

# Display AI 
ela_ai = elem_ai_calc(behrman, 'ELA')
math_ai = elem_ai_calc(behrman, 'Math')
social_ai = elem_ai_calc(behrman, 'Social')
sci_ai = elem_ai_calc(behrman, 'Science')

ass_indices = [ela_ai, ela_ai, math_ai, math_ai, social_ai, sci_ai]

overall_ass_index = round(np.nanmean(ass_indices), 1)

with st.expander(label="Summary Metrics", expanded=True):
    st.subheader(f"Overall Assessment Index {yr_choice}-{yr_choice + 1}")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        metric_card(metric=overall_ass_index, caption="Overall AI", fa_icon_name="")

    st.subheader(f"Assessment Index by Subject {yr_choice}-{yr_choice + 1}")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        metric_card(metric=ela_ai, caption="ELA", fa_icon_name="fa-solid fa-book-open")
    with col2:
        metric_card(metric=math_ai, caption="Math", fa_icon_name="fa-solid fa-square-root-variable")
    with col3:
        metric_card(metric=social_ai, caption="Social Studies", fa_icon_name="fa-solid fa-landmark")
    with col4:
        metric_card(metric=sci_ai, caption="Science", fa_icon_name="fa-solid fa-flask")
   
