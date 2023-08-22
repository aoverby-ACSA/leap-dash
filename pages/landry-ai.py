import streamlit as st
import numpy as np
from app.utils import page_setup, metric_card, load_leap_data, hs_ai_calc, ai_line

st.set_page_config(page_title="Landry LEAP", layout="wide")
page_setup()

st.title("Landry LEAP Results")

landry = load_leap_data("Landry")

# Slider year variables to isolate wanted year range
st.sidebar.subheader("School Year Range")
yr1, yr2 = st.sidebar.slider("*Choose a range of years:*", help="The year selected represents the first year of the school year span. E.g., when you select years 2020-2022 you're selecting school year 2020-2021 through school year 2022-2023", min_value=2017, max_value=2022, value=(2020, 2022), key='date_range')
landry = landry[(landry['SPSYear'] >= yr1) & (landry['SPSYear'] <= yr2)]

# Subject select variables
subjs = {'AL':'Algebra I', 'GM':'Geometry', 'E1':'English I', 'E2':'English II', 'BL':'Biology','US':'US History'}
st.sidebar.subheader("Subject Selection")
subj_choice = st.sidebar.selectbox("*Choose a subject:*", options=subjs, format_func=subjs.get)
def return_value(key):
    subjs = {'AL':'Algebra I', 'GM':'Geometry', 'E1':'English I', 'E2':'English II', 'BL':'Biology','US':'US History'}
    return str(subjs.get(key))
subj_title = return_value(subj_choice)

# Subgroup filter
subgroups = {'None':'None','SpecialEd': 'Special Ed', 'Section504':'504', 'EL':'English Learners', 'HomelessFlag': 'Homeless'}
st.sidebar.subheader("Subgroup Selection")
subgroup_choice = st.sidebar.selectbox("*Choose a subgroup:*", options=subgroups, format_func=subgroups.get)
if subgroup_choice != 'None':
    landry = landry[landry[subgroup_choice] == 'Yes']
else:
    pass


st.subheader(f"{subj_title} Assessment Index")
if yr1 == yr2:
        st.markdown(f"##### Date Range: {yr1}")
else:
    st.markdown(f"##### Date Range: {yr1} - {yr2}")

st.subheader(f"Overall {subj_title} Assessment Index")
ai_line(landry, subj_choice)

# ## Set filters
# # Year Select
# years = sorted(landry['SPSYear'].unique())
# st.sidebar.subheader("Select School Year", help="The year selected represents the first year of the school year span. E.g., when you select year 2022 you're selecting school year 2022-2023")
# yr_choice = st.sidebar.selectbox("*Choose a School Year*", options=years, index=(len(landry['SPSYear'].unique())-2))
# landry = landry[landry['SPSYear'] == yr_choice]

# # Display AI 
# al_ai = hs_ai_calc(landry, 'AL')
# gm_ai = hs_ai_calc(landry, 'GM')
# e1_ai = hs_ai_calc(landry, 'E1')
# e2_ai = hs_ai_calc(landry, 'E2')
# bl_ai = hs_ai_calc(landry, 'BL')
# us_ai = hs_ai_calc(landry, 'US')

# ass_indices = [al_ai, gm_ai, e1_ai, e2_ai, bl_ai, us_ai]

# overall_ass_index = round(np.nanmean(ass_indices), 1)

# with st.expander(label="Summary Metrics", expanded=True):
#     st.subheader(f"Overall Assessment Index {yr_choice}-{yr_choice + 1}")
#     col1, col2, col3, col4, col5, col6 = st.columns(6)
#     with col1:
#         metric_card(metric=overall_ass_index, caption="Overall AI", fa_icon_name="")

#     st.subheader(f"Assessment Index by Subject {yr_choice}-{yr_choice + 1}")
#     col1, col2, col3, col4, col5, col6 = st.columns(6)
#     with col1:
#         metric_card(metric=al_ai, caption="Algebra I", fa_icon_name="fa-solid fa-square-root-variable")
#     with col2:
#         metric_card(metric=gm_ai, caption="Geometry", fa_icon_name="fa-solid fa-shapes")
#     with col3:
#         metric_card(metric=e1_ai, caption="English I", fa_icon_name="fa-solid fa-book-open")
#     with col4:
#         metric_card(metric=e2_ai, caption="English II", fa_icon_name="fa-solid fa-book")
#     with col5:
#         metric_card(metric=bl_ai, caption="Biology", fa_icon_name="fa-solid fa-dna")
#     with col6:
#         metric_card(metric=us_ai, caption="US History", fa_icon_name="fa-solid fa-monument")

