import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Public Returns to Postsecondary Education",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- REPORT PAGE ---
st.title("🎓 Quantifying the Public Returns to Postsecondary Education in the United States")
st.markdown("##### A data-driven exploration of higher education's societal benefits")
st.markdown("---")


# --- TABLE OF CONTENTS ---
st.markdown("### 🔗 Jump to Section")
st.markdown("""
- [📌 Executive Summary](#dc16351e)
- [🎯 Introduction: Defining the Public Value of Postsecondary Education](#introduction-defining-the-public-value-of-postsecondary-education)
- [🔍 Purpose and Objectives of the Report](#purpose-and-objectives-of-the-report)
- [🧭 Overview of Existing Frameworks](#overview-of-existing-frameworks)
- [🧮 Health, Demographic, and Socioeconomic Variables](#health-demographic-and-socioeconomic-variables)
""", unsafe_allow_html=True)

st.markdown("---")

# --- SECTION: Executive Summary ---
st.markdown("## 📌 Executive Summary")
st.write("""
This report systematically quantifies the public returns to postsecondary education in the United States by leveraging existing national datasets. 
It proposes a multi-dimensional framework that extends beyond traditional individual economic gains, encompassing broader societal benefits across 
economic well-being, public health, community vitality, and public safety.

The findings underscore that higher educational attainment is consistently associated with a more robust economy, improved public health outcomes, 
enhanced civic engagement and social mobility, and a safer society.
""")

# --- SECTION: Introduction ---
st.markdown("## 🎯 Introduction: Defining the Public Value of Postsecondary Education")
with st.expander("📘 Beyond Private Gains: Conceptualizing Societal Benefits", expanded=True):
    st.write("""
    The discourse surrounding postsecondary education often centers on private benefits like increased earnings. However, this report emphasizes 
    broader public value—benefits such as improved health, reduced crime, and stronger civic participation. These interconnected outcomes 
    collectively amplify the public return on investment in higher education.
    """)

# --- SECTION: Purpose and Objectives ---
st.markdown("## 🔍 Purpose and Objectives of the Report")
with st.expander("📈 Identifying metrics", expanded=True):
    st.write("""
    The goal is to identify U.S. metrics and datasets that quantify the public returns to postsecondary education. Key criteria include the ability to 
    disaggregate by educational attainment and region. The report provides a foundation for researchers and policymakers to understand the collective 
    value of higher education using nationally representative data.
    """)

# --- SECTION: Existing Frameworks ---
st.markdown("## 🧭 Overview of Existing Frameworks")
with st.expander("PostsecondaryValue.org", expanded=True):
    st.write("""
    Uses College Scorecard, IPEDS, and ACS data to assess economic value across demographics, fields of study, institutional missions, and more.
    Limitations include lack of earnings disaggregation by race/ethnicity.
    """)

with st.expander("Lumina Foundation", expanded=True):
    st.write("""
    Focuses on metrics tied to completion, enrollment, and equity. Promotes the Public Value Metric concept and uses data for targeting interventions, 
    particularly for underserved groups. Also highlights a rising skepticism toward higher education.
    """)

with st.expander("Key Data Challenges", expanded=True):
    st.write("""
    - Lack of disaggregated data (e.g., race, military status)
    - Difficulty capturing short-term credentials
    - Need for more detailed microdata (e.g., PUMS, IPUMS)
    """)

# --- SECTION: Categorized Variables ---
st.markdown("## 🧮 Health, Demographic, and Socioeconomic Variables")
st.caption("These categories are used to analyze broader social outcomes associated with educational attainment.")

with st.expander("🍎 Health Behaviours", expanded=False):
    st.markdown("""
    - **Alcohol consumption**
        - Alcohol drink  
        - Binge drinkers  
        - Heavy drinkers  
        - Within last 30 days  
    - **Fruit and diet**
        - Fruit consumption  
            - Consumed fruit less than one time per day  
    - **Physical activity**
        - Physical activity  
    - **Vaccinations**
        - Flu shot  
            - Adults aged 65+ w/ flu shot  
        - Pneumonia vaccination  
    - **Health checkups**
        - Last physical checkup  
    """)

with st.expander("🩺 Chronic Health Conditions", expanded=False):
    st.markdown("""
    - Arthritis  
    - Asthma  
    - Depression  
    - Diabetes  
    - Heart attack at least once  
    - Stroke at least once  
    """)

with st.expander("💳 Health Access / Coverage", expanded=False):
    st.markdown("""
    - Health care coverage  
    - Health care insurance  
    - Personal health care provider  
    """)

with st.expander("🧍️ Demographic Characteristics", expanded=False):
    st.markdown("""
    - Employment status  
        - Employed  
        - Self-employed  
        - Unable to work  
    - Marital status  
    - Number of kids  
        - No kids  
        - One kid  
        - Two kids  
    - Veteran  
    """)

with st.expander("💰 Socioeconomic Indicators", expanded=False):
    st.markdown("""
    - Home ownership  
    - Household income  
        - Less than 15k  
        - 15 to 24k  
        - 25 to 34k  
        - 35 to 49k  
        - 50k plus  
    """)

with st.expander("📅 Health Status Indicators (Self-Reported Days)", expanded=False):
    st.markdown("""
    - Mental health days  
    - Physical health days  
    """)

# --- FOOTER ---
st.markdown("---")
st.caption("M. Abdalla 2025")
