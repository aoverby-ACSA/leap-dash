import streamlit as st
from streamlit_extras.dataframe_explorer import dataframe_explorer
from app.utils import page_setup, metric_card, load_leap_data, ach_histogram, scale_score_distrib, ach_by_yr_line, ss_median_line

st.set_page_config(page_title="Landry LEAP", layout="wide")
page_setup()

st.title("Landry LEAP Results")

landry = load_leap_data("Landry")

## Set filters
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

# Viz Tabs
tab1, tab2, tab3, tab4 = st.tabs(['Achievement Level Summary', 'Achievement Level % Over Time', 'Distribution of Scaled Scores', 'View and Download Data'])

with tab1:
    st.subheader(f"{subj_title} Achievement Level Summary")
    if yr1 == yr2:
        st.markdown(f"##### Date Range: {yr1}")
    else:
        st.markdown(f"##### Date Range: {yr1} - {yr2}")
    with st.expander(label='**Summary Metrics**', expanded=True):
        st.markdown("### Summary Metrics:")
        col1, col2, col3, col4, col5 = st.columns(5)
        tot_testers = int(landry[f"{subj_choice}ScaleScore"].count())
        with col1:
            metric_card(box_color=(255,255,255), metric= tot_testers, caption='Total Testers', fa_icon_name='fa-solid fa-graduation-cap')   
        median = round(landry[f"{subj_choice}ScaleScore"].median())
        with col2:
            metric_card(metric=median, caption='Median SS', fa_icon_name='fa-solid fa-scale-balanced')    
        stdev = round(landry[f"{subj_choice}ScaleScore"].std(ddof=1))
        with col3:
            metric_card(metric=stdev, caption='Std Dev', fa_icon_name='fa-solid fa-arrows-left-right')
        range_high = median + stdev
        with col4:
            metric_card(metric=range_high, caption='SS Range (High)', fa_icon_name='fa-solid fa-arrow-up')   
        range_low = median - stdev
        with col5:
            metric_card(metric=range_low, caption='SS Range (Low)', fa_icon_name='fa-solid fa-arrow-down')
        
        col1, col2, col3, col4, col5 = st.columns(5)
        num_unsat = landry[f"{subj_choice}AchievementLevel"].str.match('Unsatisfactory').sum()
        with col1:
            metric_card(metric=num_unsat, caption="Unsatisfactory", fa_icon_name='', box_color=(220,20,60), font_color=(255,255,255))   
        num_apbasic = landry[f"{subj_choice}AchievementLevel"].str.match('Approaching Basic').sum()     
        with col2:
            metric_card(metric=num_apbasic, caption="App Basic", fa_icon_name='', box_color=(255,165,0), font_color=(255,255,255))   
        num_basic = landry[f"{subj_choice}AchievementLevel"].str.match('Basic').sum()    
        with col3:
            metric_card(metric=num_basic, caption="Basic", fa_icon_name='', box_color=(0,128,0), font_color=(255,255,255))
        num_mastery = landry[f"{subj_choice}AchievementLevel"].str.match('Mastery').sum()    
        with col4:
            metric_card(metric=num_mastery, caption="Mastery", fa_icon_name='', box_color=(144,238,144), font_color=(255,255,255))    
        num_adv = landry[f"{subj_choice}AchievementLevel"].str.match('Advanced').sum()    
        with col5:
            metric_card(metric=num_adv, caption="Advanced", fa_icon_name='', box_color=(0,255,0), font_color=(255,255,255))
            
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('### Median Scale Score')
        if yr1 == yr2:
            st.markdown(f"##### Date Range: {yr1}")
        else:
            st.markdown(f"##### Date Range: {yr1} - {yr2}")
        ss_median_line(landry, subj_choice)
    with col2:
        st.markdown('### Achievement Level Counts')
        if yr1 == yr2:
            st.markdown(f"##### Date Range: {yr1}")
        else:
            st.markdown(f"##### Date Range: {yr1} - {yr2}")
        ach_histogram(landry, subj_choice)
    
    
with tab2:
    st.subheader(f"{subj_title} Achievement Levels as Percentage of Total Results")
    if yr1 == yr2:
        st.markdown(f"##### Date Range: {yr1}")
    else:
        st.markdown(f"##### Date Range: {yr1} - {yr2}")
        
    with st.expander(label='**Summary Metrics**', expanded=False):
        st.markdown("### Summary Metrics:")
        col1, col2, col3, col4, col5 = st.columns(5)
        tot_testers = int(landry[f"{subj_choice}ScaleScore"].count())
        with col1:
            metric_card(box_color=(255,255,255), metric= tot_testers, caption='Total Testers', fa_icon_name='fa-solid fa-graduation-cap')   
        median = round(landry[f"{subj_choice}ScaleScore"].median())
        with col2:
            metric_card(metric=median, caption='Median SS', fa_icon_name='fa-solid fa-scale-balanced')    
        stdev = round(landry[f"{subj_choice}ScaleScore"].std(ddof=1))
        with col3:
            metric_card(metric=stdev, caption='Std Dev', fa_icon_name='fa-solid fa-arrows-left-right')
        range_high = median + stdev
        with col4:
            metric_card(metric=range_high, caption='SS Range (High)', fa_icon_name='fa-solid fa-arrow-up')   
        range_low = median - stdev
        with col5:
            metric_card(metric=range_low, caption='SS Range (Low)', fa_icon_name='fa-solid fa-arrow-down')
        
        col1, col2, col3, col4, col5 = st.columns(5)
        num_unsat = landry[f"{subj_choice}AchievementLevel"].str.match('Unsatisfactory').sum()
        with col1:
            metric_card(metric=num_unsat, caption="Unsatisfactory", fa_icon_name='', box_color=(220,20,60), font_color=(255,255,255))   
        num_apbasic = landry[f"{subj_choice}AchievementLevel"].str.match('Approaching Basic').sum()     
        with col2:
            metric_card(metric=num_apbasic, caption="App Basic", fa_icon_name='', box_color=(255,165,0), font_color=(255,255,255))   
        num_basic = landry[f"{subj_choice}AchievementLevel"].str.match('Basic').sum()    
        with col3:
            metric_card(metric=num_basic, caption="Basic", fa_icon_name='', box_color=(0,128,0), font_color=(255,255,255))
        num_mastery = landry[f"{subj_choice}AchievementLevel"].str.match('Mastery').sum()    
        with col4:
            metric_card(metric=num_mastery, caption="Mastery", fa_icon_name='', box_color=(144,238,144), font_color=(255,255,255))    
        num_adv = landry[f"{subj_choice}AchievementLevel"].str.match('Advanced').sum()    
        with col5:
            metric_card(metric=num_adv, caption="Advanced", fa_icon_name='', box_color=(0,255,0), font_color=(255,255,255))
    
    ach_by_yr_line(landry, subj_choice)
    
with tab3:
    st.subheader(f"{subj_title} Scale Score Distribution")
    if yr1 == yr2:
        st.markdown(f"##### Date Range: {yr1}")
    else:
        st.markdown(f"##### Date Range: {yr1} - {yr2}")
        
    with st.expander(label='**Summary Metrics**', expanded=False):
        st.markdown("### Summary Metrics:")
        col1, col2, col3, col4, col5 = st.columns(5)
        tot_testers = int(landry[f"{subj_choice}ScaleScore"].count())
        with col1:
            metric_card(box_color=(255,255,255), metric= tot_testers, caption='Total Testers', fa_icon_name='fa-solid fa-graduation-cap')   
        median = round(landry[f"{subj_choice}ScaleScore"].median())
        with col2:
            metric_card(metric=median, caption='Median SS', fa_icon_name='fa-solid fa-scale-balanced')    
        stdev = round(landry[f"{subj_choice}ScaleScore"].std(ddof=1))
        with col3:
            metric_card(metric=stdev, caption='Std Dev', fa_icon_name='fa-solid fa-arrows-left-right')
        range_high = median + stdev
        with col4:
            metric_card(metric=range_high, caption='SS Range (High)', fa_icon_name='fa-solid fa-arrow-up')   
        range_low = median - stdev
        with col5:
            metric_card(metric=range_low, caption='SS Range (Low)', fa_icon_name='fa-solid fa-arrow-down')
        
        col1, col2, col3, col4, col5 = st.columns(5)
        num_unsat = landry[f"{subj_choice}AchievementLevel"].str.match('Unsatisfactory').sum()
        with col1:
            metric_card(metric=num_unsat, caption="Unsatisfactory", fa_icon_name='', box_color=(220,20,60), font_color=(255,255,255))   
        num_apbasic = landry[f"{subj_choice}AchievementLevel"].str.match('Approaching Basic').sum()     
        with col2:
            metric_card(metric=num_apbasic, caption="App Basic", fa_icon_name='', box_color=(255,165,0), font_color=(255,255,255))   
        num_basic = landry[f"{subj_choice}AchievementLevel"].str.match('Basic').sum()    
        with col3:
            metric_card(metric=num_basic, caption="Basic", fa_icon_name='', box_color=(0,128,0), font_color=(255,255,255))
        num_mastery = landry[f"{subj_choice}AchievementLevel"].str.match('Mastery').sum()    
        with col4:
            metric_card(metric=num_mastery, caption="Mastery", fa_icon_name='', box_color=(144,238,144), font_color=(255,255,255))    
        num_adv = landry[f"{subj_choice}AchievementLevel"].str.match('Advanced').sum()    
        with col5:
            metric_card(metric=num_adv, caption="Advanced", fa_icon_name='', box_color=(0,255,0), font_color=(255,255,255))
    
    scale_score_distrib(landry, subj_choice)

with tab4:
    landry['SPSYear'] = landry['SPSYear'].dt.year
    cols = ['LastName', 'FirstName', 'Grade', f'{subj_choice}TestingStatus', f'{subj_choice}RawScore', f'{subj_choice}ScaleScore', f'{subj_choice}AchievementLevel', 'SPSYear']
    landry = landry[cols].dropna()
    filtered_df = dataframe_explorer(landry, case=False)
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
    data_as_csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button("Download as CSV ", data=data_as_csv, file_name=f"LandryLEAP{subj_choice}{yr1}.csv", mime="text/csv")
    
    