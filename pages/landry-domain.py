import streamlit as st
from app.utils import page_setup, load_leap_data, hs_domain_pie

st.set_page_config(page_title="Landry LEAP", layout="wide")
page_setup()

st.title("Landry LEAP Results")

landry = load_leap_data("Landry")

# Slider year variables to isolate wanted year range
st.sidebar.subheader("School Year Range")
yr1, yr2 = st.sidebar.slider("*Choose a range of years:*", help="The year selected represents the first year of the school year span. E.g., when you select years 2020-2022 you're selecting school year 2020-2021 through school year 2022-2023", min_value=2017, max_value=2022, value=(2022, 2022), key='date_range')
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

st.subheader(f"{subj_title} Domain Performance")
if yr1 == yr2:
        st.markdown(f"##### Date Range: {yr1}")
else:
    st.markdown(f"##### Date Range: {yr1} - {yr2}")

hs_domain_pie(landry, subj_choice)
    
