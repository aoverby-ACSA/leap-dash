import streamlit as st
from app.utils import page_setup, metric_card, load_leap_data, ach_histogram, scale_score_distrib, ach_by_yr_line, ss_median_line

st.set_page_config(page_title="Behrman LEAP", layout="wide")
page_setup()

st.title("Behrman LEAP Results")

behrman = load_leap_data("Behrman")

## Set filters
# Slider year variables to isolate wanted year range
st.sidebar.subheader("School Year Range")
yr1, yr2 = st.sidebar.slider("*Choose a range of years:*", help="The year selected represents the first year of the school year span. E.g., when you select years 2020-2022 you're selecting school year 2020-2021 through school year 2022-2023", min_value=2017, max_value=2022, value=(2020, 2022), key='date_range')
behrman = behrman[(behrman['SPSYear'] >= yr1) & (behrman['SPSYear'] <= yr2)]

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

tab1, tab2, tab3 = st.tabs(['Achievement Level Summary', 'Achievement Level % Over Time', 'Distribution of Scaled Scores'])

with tab1:
    st.subheader(f"{subj_title} Achievement Level Summary")
    if yr1 == yr2:
        st.markdown(f"##### Date Range: {yr1}")
    else:
        st.markdown(f"##### Date Range: {yr1} - {yr2}")
    with st.expander(label='**Summary Metrics**', expanded=True):
        st.markdown("### Summary Metrics:")
        col1, col2, col3, col4, col5 = st.columns(5)
        tot_testers = int(behrman[f"{subj_choice}ScaleScore"].count())
        with col1:
            metric_card(box_color=(255,255,255), metric= tot_testers, caption='Total Testers', fa_icon_name='fa-solid fa-graduation-cap')   
        median = round(behrman[f"{subj_choice}ScaleScore"].median())
        with col2:
            metric_card(metric=median, caption='Median SS', fa_icon_name='fa-solid fa-scale-balanced')    
        stdev = round(behrman[f"{subj_choice}ScaleScore"].std(ddof=1))
        with col3:
            metric_card(metric=stdev, caption='Std Dev', fa_icon_name='fa-solid fa-arrows-left-right')
        range_high = median + stdev
        with col4:
            metric_card(metric=range_high, caption='SS Range (High)', fa_icon_name='fa-solid fa-arrow-up')   
        range_low = median - stdev
        with col5:
            metric_card(metric=range_low, caption='SS Range (Low)', fa_icon_name='fa-solid fa-arrow-down')
            
        col1, col2, col3, col4, col5 = st.columns(5)
        num_unsat = behrman[f"{subj_choice}AchievementLevel"].str.match('Unsatisfactory').sum()
        with col1:
            metric_card(metric=num_unsat, caption="Unsatisfactory", fa_icon_name='', box_color=(220,20,60), font_color=(255,255,255))   
        num_apbasic = behrman[f"{subj_choice}AchievementLevel"].str.match('Approaching Basic').sum()     
        with col2:
            metric_card(metric=num_apbasic, caption="App Basic", fa_icon_name='', box_color=(255,165,0), font_color=(255,255,255))   
        num_basic = behrman[f"{subj_choice}AchievementLevel"].str.match('Basic').sum()    
        with col3:
            metric_card(metric=num_basic, caption="Basic", fa_icon_name='', box_color=(0,128,0), font_color=(255,255,255))
        num_mastery = behrman[f"{subj_choice}AchievementLevel"].str.match('Mastery').sum()    
        with col4:
            metric_card(metric=num_mastery, caption="Mastery", fa_icon_name='', box_color=(144,238,144), font_color=(255,255,255))    
        num_adv = behrman[f"{subj_choice}AchievementLevel"].str.match('Advanced').sum()    
        with col5:
            metric_card(metric=num_adv, caption="Advanced", fa_icon_name='', box_color=(0,255,0), font_color=(255,255,255))
    
    with st.expander(label='**View Data**'):
        st.dataframe(data=behrman, use_container_width=True, hide_index=True)
        
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('### Median Scale Score')
        if yr1 == yr2:
            st.markdown(f"##### Date Range: {yr1}")
        else:
            st.markdown(f"##### Date Range: {yr1} - {yr2}")
        ss_median_line(behrman, subj_choice)
    with col2:
        st.markdown('### Achievement Level Counts')
        if yr1 == yr2:
            st.markdown(f"##### Date Range: {yr1}")
        else:
            st.markdown(f"##### Date Range: {yr1} - {yr2}")
        ach_histogram(behrman, subj_choice)
        
with tab2:
    st.subheader(f"{subj_title} Achievement Levels as Percentage of Total Results")
    if yr1 == yr2:
        st.markdown(f"##### Date Range: {yr1}")
    else:
        st.markdown(f"##### Date Range: {yr1} - {yr2}")
    ach_by_yr_line(behrman, subj_choice)
    
with tab3:
    st.subheader(f"{subj_title} Scale Score Distribution")
    if yr1 == yr2:
        st.markdown(f"##### Date Range: {yr1}")
    else:
        st.markdown(f"##### Date Range: {yr1} - {yr2}")
    scale_score_distrib(behrman, subj_choice)
