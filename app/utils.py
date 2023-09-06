import os
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from dotenv import load_dotenv
from st_pages import show_pages_from_config, add_indentation

load_dotenv()

def page_setup():
    hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    hide_footer = st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    
    adjust_whitespace = st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                   
                }
        </style>
        """, unsafe_allow_html=True)

    return show_pages_from_config(), add_indentation()

def metric_card(box_color=(255,255,255), font_color=(0,0,0), font_size=22, fa_icon_name='fa-solid fa-graduation-cap', caption='', metric= int):
    wch_colour_box = (box_color)
    wch_colour_font = (font_color)
    fontsize = font_size
    valign = "left"
    iconname = fa_icon_name
    sline = caption
    lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v6.4.0/css/all.css" crossorigin="anonymous">'
    i = metric

    htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                {wch_colour_box[1]}, 
                                                {wch_colour_box[2]}, 0.9); 
                            color: rgb({wch_colour_font[0]}, 
                                    {wch_colour_font[1]}, 
                                    {wch_colour_font[2]}, 0.9); 
                            font-size: {fontsize}px; 
                            border-radius: 7px; 
                            padding-left: 12px; 
                            padding-top: 18px; 
                            padding-bottom: 18px; 
                            line-height:25px;
                            text-align: left'>
                            <span>{sline} </style></span><i class='{iconname}'></i><BR>{i}
                            </style></p>"""

    return st.markdown(lnk + htmlstr, unsafe_allow_html=True)

def make_grid(cols, rows):
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid

# @st.cache_data
def load_leap_data(school="Landry" or "Behrman"):
    LANDRY_CSV = os.environ.get("LANDRY_CSV")
    BEHRMAN_CSV = os.environ.get("BEHRMAN_CSV")
    try:
        if school == 'Landry':
            df = pd.read_csv(LANDRY_CSV, skipinitialspace=True)
            # Landry-specific csv modifications here
            df_cols = ['AdministrationYear',
                    'AdministrationMonth',
                    'LASID',
                    'LastName',
                    'FirstName',
                    'MiddleInitial',
                    'DOB',
                    'Grade',
                    'Gender',
                    'EthnicityRace',
                    'EducationClassification',
                    'ExceptionalityCode',
                    'EconomicallyDisadvantaged',
                    'EL',
                    'Section504',
                    'CareerDiplomaPathwayTrack',
                    'HomelessFlag',
                    'ALAdministrativeError',
                    'ALTeacherLastName',
                    'ALTeacherFirstName',
                    'ALTestingStatus',
                    'ALVoidFlag',
                    'ALRawScore',
                    'ALScaleScore',
                    'ALAchievementLevel',
                    'ALMajorContentRating',
                    'ALInterpretingFunctionsRating',
                    'ALSolvingAlgebraicallyRating',
                    'ALSolvingGraphicallyRateofChangeRating',
                    'ALAdditionalAndSupportingContentRating',
                    'ALExpressingMathematicalReasoningRating',
                    'ALModelingAndApplicationRating',
                    'E2AdministrativeError',
                    'E2TeacherLastName',
                    'E2TeacherFirstName',
                    'E2TestingStatus',
                    'E2VoidFlag',
                    'E2RawScore',
                    'E2ScaleScore',
                    'E2AchievementLevel',
                    'E2ReadingPerformanceRating',
                    'E2ReadingLiteraryTextRating',
                    'E2ReadingInformationalTextRating',
                    'E2ReadingVocabularyTextRating',
                    'E2WritingPerformanceRating',
                    'E2WrittenExpressionRating',
                    'E2WrittenKnowledgeAndUseofLanguageConventionsRating',
                    'GMAdministrativeError',
                    'GMTeacherLastName',
                    'GMTeacherFirstName',
                    'GMTestingStatus',
                    'GMVoidFlag',
                    'GMRawScore',
                    'GMScaleScore',
                    'GMAchievementLevel',
                    'GMMajorContentRating',
                    'GMCongruenceTransformationsSimilarityRating',
                    'GMSimilarityInTrigonometryModelingAndApplyingRating',
                    'GMAdditionalAndSupportingContentRating',
                    'GMExpressingMathematicalReasoningRating',
                    'GMModelingAndApplicationRating',
                    'E1AdministrativeError',
                    'E1TeacherLastName',
                    'E1TeacherFirstName',
                    'E1TestingStatus',
                    'E1VoidFlag',
                    'E1RawScore',
                    'E1ScaleScore',
                    'E1AchievementLevel',
                    'E1ReadingPerformanceRating',
                    'E1ReadingLiteraryTextRating',
                    'E1ReadingInformationalTextRating',
                    'E1ReadingVocabularyTextRating',
                    'E1WritingPerformanceRating',
                    'E1WrittenExpressionRating',
                    'E1WrittenKnowledgeAndUseofLanguageConventionsRating',
                    'USAdministrativeError',
                    'USTeacherLastName',
                    'USTeacherFirstName',
                    'USTestingStatus',
                    'USVoidFlag',
                    'USRawScore',
                    'USScaleScore',
                    'USAchievementLevel',
                    'USWesternExpansionToProgressivismStandard2Rating',
                    'USIsolationismThroughGreatWarStandard3Rating',
                    'USBecomingWorldPowerThroughWorldWarIIStandard4Rating',
                    'USColdWarEraAndTheModernAgeStandard5and6Rating',
                    'BLAdministrativeError',
                    'BLTeacherLastName',
                    'BLTeacherFirstName',
                    'BLTestingStatus',
                    'BLVoidFlag',
                    'BLRawScore',
                    'BLScaleScore',
                    'BLAchievementLevel',
                    'BLInvestigateRating',
                    'BLEvaluateRating',
                    'BLReasonScientificallyRating',
                    'SchoolYear' 
                    ]
            df = df[df_cols]
            df['SPSYear'] = np.where(df['AdministrationMonth'] != 5, df['AdministrationYear'], df['AdministrationYear'] - 1)
            
        else:
            df = pd.read_csv(BEHRMAN_CSV, skipinitialspace=True)
            # Behrman-specific csv modifications here
            df_cols = [
                'LastName',
                'FirstName',
                'MiddleInitial',
                'LASID',
                'DOB',
                'Grade',
                'Gender',
                'EthnicityRace',
                'EducationClassification',
                'LAP Economically Disadvantaged',
                'EL',
                'Migrant',
                'Section504',
                'HomelessFlag',
                'Military Affiliation',
                'Foster Care',
                'RemediationNeeded',
                'ELARawScore',
                'ELAScaleScore',
                'ELAVoidFlag',
                'ELAAchievementLevel',
                'ELA Reading Performance',
                'ELA Writing Performance',
                'Reading Informational Text',
                'Reading Literary Text',
                'Reading Vocabulary',
                'Written Expression',
                'Written Knowledge & Use of Language Conventions',
                'MathRawScore',
                'MathScaleScore',
                'MathVoidFlag',
                'MathAchievementLevel',
                'Major Content',
                'Products & Quotients_Solve Multiplication & Division Problems',
                'Solve Problems with Any Operation',
                'Fractions as Numbers & Equivalence',
                'Solve Time Area Measurement & Estimation Problems',
                'Compare & Solve Problems with Fractions',
                'Solve Multistep Problems',
                'Multiplicative Comparison & Place Value',
                'Operations with Decimals_Read Write Compare & Decimals',
                'Solve Fraction Problems',
                'Interpret Fractions Place Value & Scaling',
                'Recognize Represent & Determine Volume_Multiply & Divide Whole Numbers',
                'Rational Numbers_Multiply & Divide Fractions',
                'Ratio & Rate',
                'Expressions Inequalities & Equations',
                'Analyze Proportional Relationships & Solve Problems',
                'Operations with Rational Numbers',
                'Radicals Integer Exponents & Scientific Notation',
                'Proportional Relationships Linear Equations & Functions',
                'Solving Linear Equations_Systems of Linear Equations',
                'Congruence & Similarity_Pythagorean Theorem',
                'Additional & Supporting Content',
                'Expressing Mathematical Reasoning',
                'Modeling & Application',
                'SocialRawScore',
                'SocialScaleScore',
                'SocialVoidFlag',
                'SocialAchievementLevel',
                'History',
                'Geography',
                'Civics',
                'Economics',
                'ScienceRawScore',
                'ScienceScaleScore',
                'ScienceVoidFlag',
                'ScienceAchievementLevel',
                'Investigate',
                'Evaluate',
                'Reason Scientifically',
                'ELAOptionalLocalUse',
                'MathOptionalLocalUse',
                'ScienceOptionalLocalUse',
                'SocialOptionalLocalUse',
                'AdministrationDate']
            df = df[df_cols]
            df['SPSYear'] = df['AdministrationDate'].str[:2].astype(int) + 1999
        # Universal CSV mods
        ## If cols need to be included from the origin file add them to the list below
        
        df['SpecialEd'] = np.where(df['EducationClassification'] == 'Special', 'Yes', 'No')
        return df
    except FileNotFoundError as e:
        print(e)
        print("Use either 'Landry' or 'Behrman' as an argument for the ```load_leap_data``` function")
        st.write("Use either 'Landry' or 'Behrman' as an argument for the ```load_leap_data``` function")
        st.write(e)
        st.stop()

def ach_by_yr_line(df, subj: str):
    ach_by_yr = df.groupby('SPSYear')[f'{subj}AchievementLevel'].value_counts()
    ach_by_yr = ach_by_yr.to_frame()
    ach_by_yr.reset_index(inplace=True)
    ach_by_yr['%'] = round(100 * ach_by_yr['count'] / ach_by_yr.groupby('SPSYear')['count'].transform('sum'))
    ach_by_yr['SPSYear'] = pd.to_datetime(ach_by_yr['SPSYear'])
    if len(ach_by_yr['SPSYear'].unique()) != 1:
        fig = px.line(ach_by_yr, x='SPSYear', y='%', color=f'{subj}AchievementLevel', markers=True,
                    color_discrete_map={
                            "Unsatisfactory": "crimson",
                            "Approaching Basic": "orange",
                            "Basic": "green",
                            "Mastery": "lightgreen",
                            "Advanced": "lime"
                        }, template='simple_white')
        fig.update_traces(mode='lines+markers+text',texttemplate="%{y}%", textposition='top center')
        fig.update_xaxes(dtick="M12", tickformat="%Y")
    else:
        fig = px.bar(ach_by_yr, x='SPSYear', y='%', color=f'{subj}AchievementLevel', barmode='relative',
                    color_discrete_map={
                            "Unsatisfactory": "crimson",
                            "Approaching Basic": "orange",
                            "Basic": "green",
                            "Mastery": "lightgreen",
                            "Advanced": "lime"
                        }, template='simple_white')
        fig.update_traces(width=0.1,
                          texttemplate="%{y}%", textposition='outside')
        fig.update_xaxes(dtick="M12", tickformat="%Y")
        
        
    
    return st.plotly_chart(fig, use_container_width=True)

def ach_histogram(df, subj: str):
    df['SPSYear'] = pd.to_datetime(df['SPSYear'], format='%Y')
    df.sort_values([f"{subj}RawScore"], inplace=True)
    subj_ach = f"{subj}AchievementLevel"
    fig = px.histogram(df, x=df['SPSYear'], histfunc="count", barmode='group',color=df[subj_ach], 
                       color_discrete_map={
                           "Unsatisfactory": "crimson",
                           "Approaching Basic": "orange",
                           "Basic": "green",
                           "Mastery": "lightgreen",
                           "Advanced": "lime"
                       }, 
                       template='simple_white'
                       )
    fig.update_xaxes(dtick="M12", tickformat="%Y") ## Nice hack for getting timeseries x axis to look right
    fig.update_layout(showlegend=True)
    fig.update_traces(texttemplate="%{y}", textposition='outside')
    return st.plotly_chart(fig, use_container_width=True)

def scale_score_distrib(df, subj:str):
    subj_ss = f"{subj}ScaleScore"
    fig = px.histogram(df, x=df[subj_ss], histfunc="count", color=df[f"{subj}AchievementLevel"],
                       nbins=40,
                       color_discrete_map={
                           "Unsatisfactory": "crimson",
                           "Approaching Basic": "orange",
                           "Basic": "green",
                           "Mastery": "lightgreen",
                           "Advanced": "lime"
                       } , template='simple_white'
                       )
    fig.update_layout(showlegend=True,
                      bargap=0.1
                      )
    fig.update_traces(texttemplate="%{y}", 
                      textposition='outside')
    return st.plotly_chart(fig, use_container_width=True)

def ss_median_line(df, subj: str):
    median_by_yr = df.groupby('SPSYear')[f'{subj}ScaleScore'].median()
    median_by_yr = median_by_yr.to_frame()
    median_by_yr.reset_index(inplace=True)
    max_value = median_by_yr[f'{subj}ScaleScore'].max()
    if len(median_by_yr['SPSYear']) != 1:
        fig = px.line(median_by_yr, x='SPSYear', y=f'{subj}ScaleScore', markers=True, template='simple_white')
        fig.update_traces(mode='lines+markers+text',texttemplate="%{y}", textposition='top center')
        fig.update_xaxes(dtick="M12", tickformat="%Y")
        
        fig.update_yaxes(range=(649, max_value + 25))
    else:
        fig = px.bar(median_by_yr, x='SPSYear', y=f'{subj}ScaleScore', template='simple_white')
        fig.update_traces(width=0.1,
                          texttemplate="%{y}", textposition='outside')
        fig.update_xaxes(type='category')
        fig.update_yaxes(range=(0, max_value + 100))
        
    return st.plotly_chart(fig, use_container_width=True)

def hs_ai_calc(df, subj:str):
    df = df[df[f"{subj}TestingStatus"] == 'Initial']
    df = df[df[f"{subj}AdministrativeError"] != 'Y']
    df = df[df[f"{subj}VoidFlag"] == 'No']
    ach_levels = df.groupby(['SPSYear', f"{subj}AchievementLevel"])[f"{subj}AchievementLevel"].count()
    ach_levels.index = ach_levels.index.set_names(['Year', 'AchLevel'])
    ach_levels = ach_levels.reset_index()
    ach_levels.columns = ['Year', 'AchLevel', 'Count']
    ach_levels['Year'] = ach_levels['Year'].replace(',','', regex=True)
    num_basic = ach_levels.loc[ach_levels['AchLevel'] == 'Basic'].Count.sum()
    num_mastery = ach_levels.loc[ach_levels['AchLevel'] == 'Mastery'].Count.sum()
    num_adv = ach_levels.loc[ach_levels['AchLevel'] == 'Advanced'].Count.sum()
    total_scores = ach_levels['Count'].sum()
    ai = round(((num_basic * 80) + (num_mastery * 100) + (num_adv * 150)) / total_scores, 1)
    
    return ai
    
def elem_ai_calc(df, subj:str):
    df = df[df[f"{subj}VoidFlag"] == 'No']
    ach_levels = df.groupby(['SPSYear', f"{subj}AchievementLevel"])[f"{subj}AchievementLevel"].count()
    ach_levels.index = ach_levels.index.set_names(['Year', 'AchLevel'])
    ach_levels = ach_levels.reset_index()
    ach_levels.columns = ['Year', 'AchLevel', 'Count']
    ach_levels['Year'] = ach_levels['Year'].replace(',','', regex=True)
    num_basic = ach_levels.loc[ach_levels['AchLevel'] == 'Basic'].Count.sum()
    num_mastery = ach_levels.loc[ach_levels['AchLevel'] == 'Mastery'].Count.sum()
    num_adv = ach_levels.loc[ach_levels['AchLevel'] == 'Advanced'].Count.sum()
    total_scores = ach_levels['Count'].sum()
    ai = round(((num_basic * 80) + (num_mastery * 100) + (num_adv * 150)) / total_scores, 1)
    
    return ai

def ai_by_grade_line(df, subj:str):
    df = df[df[f"{subj}VoidFlag"] == 'No']
    ach_levels = df.groupby(['SPSYear', f'{subj}AchievementLevel', 'Grade'])[f'{subj}AchievementLevel'].count()
    ach_levels.index = ach_levels.index.set_names(['Year', 'AchLevel', 'Grade'])
    ach_levels = ach_levels.reset_index()
    ach_levels.columns = ['Year', 'AchLevel', 'Grade','Count']
    conditions = [
    (ach_levels['AchLevel'] == 'Advanced'),
    (ach_levels['AchLevel'] == 'Mastery'),
    (ach_levels['AchLevel'] == 'Basic')
    ]
    values = [150, 100, 80]
    ach_levels['AIContrib'] = np.select(conditions, values) * ach_levels['Count']
    ach_levels = ach_levels.groupby(['Year','Grade'])[['Count', 'AIContrib']].sum().reset_index()
    ach_levels['AI'] = round(ach_levels['AIContrib'] / ach_levels['Count'], 1)
    
    if len(ach_levels['Year'].unique()) != 1:
        fig = px.line(ach_levels, x='Year', y='AI', facet_col='Grade', facet_col_wrap=3, facet_col_spacing=0.01, markers=True, template='simple_white')
        fig.update_traces(mode='lines+markers+text',texttemplate="%{y}", textposition='top center')
        fig.update_xaxes(dtick="M12", tickformat="%Y")
        fig.update_yaxes(range=(0, 151))
    else:
        fig = px.bar(ach_levels, x='Year', y='AI', facet_col='Grade', facet_col_wrap=3, facet_col_spacing=0.01, template='simple_white')
        fig.update_traces(width=0.1,
                          texttemplate="%{y}", textposition='outside')
        fig.update_yaxes(range=(0,151))
        fig.update_xaxes(type='category')
    
    return st.plotly_chart(fig, use_container_width=True)

def ai_line(df, subj:str):
    df = df[df[f"{subj}VoidFlag"] == 'No']
    ach_levels = df.groupby(['SPSYear', f'{subj}AchievementLevel'])[f'{subj}AchievementLevel'].count()
    ach_levels.index = ach_levels.index.set_names(['Year', 'AchLevel'])
    ach_levels = ach_levels.reset_index()
    ach_levels.columns = ['Year', 'AchLevel','Count']
    conditions = [
    (ach_levels['AchLevel'] == 'Advanced'),
    (ach_levels['AchLevel'] == 'Mastery'),
    (ach_levels['AchLevel'] == 'Basic')
    ]
    values = [150, 100, 80]
    ach_levels['AIContrib'] = np.select(conditions, values) * ach_levels['Count']
    ach_levels = ach_levels.groupby(['Year'])[['Count', 'AIContrib']].sum().reset_index()
    ach_levels['AI'] = round(ach_levels['AIContrib'] / ach_levels['Count'], 1)
    
    if len(ach_levels['Year'].unique()) != 1: 
        fig = px.line(ach_levels, x='Year', y='AI', markers=True, template='simple_white')
        fig.update_traces(mode='lines+markers+text',texttemplate="%{y}", textposition='top center')
        fig.update_xaxes(dtick="M12", tickformat="%Y")
        fig.update_yaxes(range=(0, 151))
    else:
        fig = px.bar(ach_levels, x='Year', y='AI', template='simple_white')
        fig.update_traces(width=0.1,
                          texttemplate="%{y}", textposition='outside')
        fig.update_yaxes(range=(0,151))
        fig.update_xaxes(type='category')
    
    
    return st.plotly_chart(fig, use_container_width=True)

def hs_domain_pie(df, subj:str):
    domains_dict= {
    'AL': ['ALMajorContentRating', 'ALInterpretingFunctionsRating',      'ALSolvingAlgebraicallyRating', 'ALSolvingGraphicallyRateofChangeRating', 'ALAdditionalAndSupportingContentRating', 'ALExpressingMathematicalReasoningRating', 'ALModelingAndApplicationRating'], 
    'E2': ['E2ReadingPerformanceRating', 'E2ReadingLiteraryTextRating', 'E2ReadingInformationalTextRating', 'E2ReadingVocabularyTextRating', 'E2WritingPerformanceRating', 'E2WrittenExpressionRating', 'E2WrittenKnowledgeAndUseofLanguageConventionsRating'], 
    'GM': ['GMMajorContentRating', 'GMCongruenceTransformationsSimilarityRating', 'GMSimilarityInTrigonometryModelingAndApplyingRating', 'GMAdditionalAndSupportingContentRating', 'GMExpressingMathematicalReasoningRating', 'GMModelingAndApplicationRating'], 
    'E1': ['E1ReadingPerformanceRating', 'E1ReadingLiteraryTextRating', 'E1ReadingInformationalTextRating', 'E1ReadingVocabularyTextRating', 'E1WritingPerformanceRating', 'E1WrittenExpressionRating', 'E1WrittenKnowledgeAndUseofLanguageConventionsRating'],
    'US': ['USWesternExpansionToProgressivismStandard2Rating', 'USIsolationismThroughGreatWarStandard3Rating', 'USBecomingWorldPowerThroughWorldWarIIStandard4Rating', 'USColdWarEraAndTheModernAgeStandard5and6Rating'], 
    'BL': ['BLInvestigateRating', 'BLEvaluateRating', 'BLReasonScientificallyRating']
    }
    
    for x in domains_dict[subj]:
        gbdf = df.groupby(['SPSYear', x])[x].count()
        gbdf.index = gbdf.index.set_names(['Year', 'DomainAch'])
        gbdf = gbdf.reset_index()
        gbdf.columns = ['Year', 'DomainAch', 'Count']
        
        fig = px.pie(gbdf, names='DomainAch', values='Count', color='DomainAch', title=x, 
                     color_discrete_map={
                         'Weak':'crimson',
                         'Moderate': 'orange',
                         'Strong': 'green'
                     }, template= 'simple_white')
        
        chart = st.plotly_chart(fig, use_container_width=True)
    
    return chart