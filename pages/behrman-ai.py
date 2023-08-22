import streamlit as st
import numpy as np
from app.utils import page_setup, metric_card, load_leap_data, elem_ai_calc, ai_by_grade_line, ai_line

st.set_page_config(page_title="Behrman LEAP", layout="wide")
page_setup()

st.title("Behrman LEAP Results")

behrman = load_leap_data("Behrman")
## Set filters
# Slider year variables to isolate wanted year range
st.sidebar.subheader("School Year Range")
yr1, yr2 = st.sidebar.slider("*Choose a range of years:*", help="The year selected represents the first year of the school year span. E.g., when you select years 2020-2022 you're selecting school year 2020-2021 through school year 2022-2023", min_value=2017, max_value=2022, value=(2020, 2022), key='date_range')
behrman = behrman[(behrman['SPSYear'] >= yr1) & (behrman['SPSYear'] <= yr2)]

# # Grade Level Filter
# st.sidebar.subheader("Grade Level Selection")
# grade_choices = {'All Grades':'All Grades', 3:'3rd Grade', 4:'4th Grade', 5:'5th Grade', 6:'6th Grade', 7:'7th Grade', 8:'8th Grade'}
# grade_choice = st.sidebar.selectbox("*Choose a grade level*", options=grade_choices, format_func=grade_choices.get)
# if grade_choice != 'All Grades':
#     behrman = behrman[behrman['Grade'] == grade_choice]
# else:
#     pass

# Subject select variables
subjs = {'ELA':'ELA', 'Math':'Math', 'Social':'Social Studies', 'Science':'Science'}
st.sidebar.subheader("Subject Selection")
subj_choice = st.sidebar.selectbox("*Choose a subject:*", options=subjs, format_func=subjs.get)
def return_value(key):
    subjs = {'ELA':'ELA', 'Math':'Math', 'Social':'Social Studies', 'Science':'Science'}
    return str(subjs.get(key))
subj_title = return_value(subj_choice)

# Subgroup filter
subgroups = {'None':'None','SpecialEd': 'Special Ed', 'Section504':'504', 'EL':'English Learners', 'HomelessFlag': 'Homeless'}
st.sidebar.subheader("Subgroup Selection")
subgroup_choice = st.sidebar.selectbox("*Choose a subgroup:*", options=subgroups, format_func=subgroups.get)
if subgroup_choice != 'None':
    behrman = behrman[behrman[subgroup_choice] == 'Yes']
else:
    pass


st.subheader(f"{subj_title} Assessment Index")
if yr1 == yr2:
        st.markdown(f"##### Date Range: {yr1}")
else:
    st.markdown(f"##### Date Range: {yr1} - {yr2}")

st.subheader(f"Overall {subj_title} Assessment Index")
ai_line(behrman, subj_choice)

st.subheader(f"{subj_title} Assessment Index by Grade")
ai_by_grade_line(behrman, subj_choice)
   

    
    
# # Display AI 
# ela_ai = elem_ai_calc(behrman, 'ELA')
# math_ai = elem_ai_calc(behrman, 'Math')
# social_ai = elem_ai_calc(behrman, 'Social')
# sci_ai = elem_ai_calc(behrman, 'Science')

# ass_indices = [ela_ai, ela_ai, math_ai, math_ai, social_ai, sci_ai]

# overall_ass_index = round(np.nanmean(ass_indices), 1)

# with st.expander(label="Summary Metrics", expanded=True):
#     st.subheader(f"Overall Assessment Index {yr_choice}-{yr_choice + 1}")
#     col1, col2, col3, col4, col5, col6 = st.columns(6)
#     with col1:
#         metric_card(metric=overall_ass_index, caption="Overall AI", fa_icon_name="")

#     st.subheader(f"Assessment Index by Subject {yr_choice}-{yr_choice + 1}")
#     col1, col2, col3, col4 = st.columns(4)
#     with col1:
#         metric_card(metric=ela_ai, caption="ELA", fa_icon_name="fa-solid fa-book-open")
#     with col2:
#         metric_card(metric=math_ai, caption="Math", fa_icon_name="fa-solid fa-square-root-variable")
#     with col3:
#         metric_card(metric=social_ai, caption="Social Studies", fa_icon_name="fa-solid fa-landmark")
#     with col4:
#         metric_card(metric=sci_ai, caption="Science", fa_icon_name="fa-solid fa-flask")