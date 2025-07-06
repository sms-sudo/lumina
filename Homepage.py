import streamlit as st

st.set_page_config(page_title="Lumina Challenge Submission", layout="wide")

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
- [🔍 Purpose and Objectives of the Report](#8e24fac5)
- [🧭 Overview of Existing Frameworks](#6649edcc)
- [🧮 Health, Demographic, and Socioeconomic Variables](#21042c9)
""", unsafe_allow_html=True)

st.markdown("---")

# --- SECTION: Executive Summary ---
st.markdown("## 📌 Executive Summary")
st.write("""
This report systematically quantifies the public returns to postsecondary education in the United States by leveraging existing national datasets. It proposes a multidimensional framework that extends beyond traditional individual economic gains, encompassing broader societal benefits across economic well-being, public health, community vitality, and public safety. The analysis identifies key metrics and their associated national datasets, emphasizing their disaggregation capabilities at educational and regional levels. The findings underscore that higher educational attainment is consistently associated with a more robust economy, improved public health outcomes, enhanced civic engagement and social mobility, and a safer society.
While acknowledging current data limitations, particularly regarding granular disaggregation for certain outcomes, this report provides a comprehensive, data-driven foundation for understanding and articulating the profound collective benefits of investing in postsecondary education.

An interactive digital version of this report, featuring a live dashboard with expanded variables and analyses, is accessible at: https://luminachallenge.streamlit.app/
""")

# --- SECTION: Introduction ---
st.markdown("## 🎯 Introduction: Defining the Public Value of Postsecondary Education")
with st.expander("📘 Beyond Private Gains: Conceptualizing Societal Benefits", expanded=True):
    st.write("""
    The discourse surrounding postsecondary education often centers on its private benefits, such as increased individual earnings and improved employment prospects. However, a comprehensive understanding of higher education's impact necessitates a shift in focus to its broader public value—the collective societal benefits that accrue from an educated populace. Postsecondary education contributes to a more informed and engaged citizenry, fosters improved public health, correlates with reduced crime rates, stimulates innovation, and enhances overall civic participation. These multifaceted contributions collectively enrich the public good, extending far beyond the direct advantages experienced by credential holders. 
    
    The various dimensions of public value are not isolated but rather interconnected and mutually reinforcing. For instance, enhanced health outcomes, a key public health metric, can directly contribute to greater community participation and social capital by fostering a more active, resilient, and productive population. Similarly, increased civic engagement, a metric of community vitality, can strengthen the social fabric, potentially influencing public safety and overall community well-being. This interconnectedness suggests that improvements in one area, driven by educational attainment, can cascade into positive effects across other domains, thereby amplifying the overall public return on investment in higher education.""")

# --- SECTION: Purpose and Objectives ---
st.markdown("## 🔍 Purpose and Objectives of the Report")
with st.expander("📈 Identifying metrics", expanded=True):
    st.write("""
    The primary objective of this report is to identify and detail reliable, nationally representative U.S. metrics and datasets capable of quantifying the public returns to postsecondary education. A critical requirement is the ability to disaggregate these data by educational attainment levels (e.g., certificates, associate's, bachelor's, master's, doctoral degrees) and various regional levels (e.g., states, counties, metropolitan areas, school districts). By systematically cataloging these resources, this report aims to provide a robust, data-driven foundation for policymakers, researchers, and the public to better understand and articulate the societal dividendsof postsecondary education.""")

# --- SECTION: Existing Frameworks ---
st.markdown("## 🧭 Overview of Existing Frameworks")
with st.expander("PostsecondaryValue.org", expanded=True):
    st.write("""
    Several organizations are actively engaged in defining and measuring the public value of higher education, providing crucial context for this report's framework. PostsecondaryValue.org, through its Equitable Value Explorer, offers an innovative diagnostic tool built upon publicly available data from sources such as the College Scorecard, the Integrated Postsecondary Education Data System (IPEDS), and the U.S. Census Bureau's American Community Survey (ACS). This tool aims to assess the economic value delivered to students and, where data permits, how this value is distributed across various demographic groups. It also incorporates contextual factors like institutional mission, state policy, local labor market conditions, student enrollment, graduation rates, STEM field participation, cohort default rates, instructional expenditures, and minority-serving institution designations.""")

with st.expander("Lumina Foundation", expanded=True):
    st.write("""
    The Lumina Foundation, the host of this challenge, is actively seeking to develop a "Public Value Metric" that outlines the societal benefits of increased educational attainment across communities. 3 Their research focuses on critical areas such as enrollment, persistence, and completion in postsecondary education, particularly for adult learners and individuals from underrepresented racial and ethnic groups. Lumina's own work uses data to discern effective strategies for different populations and conditions, striving towards a quantifiable goal of 60% of American adults holding a quality post-high school credential by 2025. Their studies also highlight a growing public skepticism towards higher education, even as the perceived value of a college degree persists.""")

with st.expander("Key Data Challenges", expanded=True):
    st.write("""
    A significant challenge acknowledged by both PostsecondaryValue.org and more broadly, the Lumina Foundation is the incompleteness of available data, particularly concerning granular disaggregation. For instance, the College Scorecard currently lacks disaggregated earnings data by race and ethnicity, which impedes the precise calculation of equitable value metrics such as the Economic Value Index (EVI) and Economic Value Contribution (EVC) for specific student subgroups. Similarly, the Lumina Foundation emphasizes the need for more robust data sources on short-term credentials and comprehensive data systems that capture diverse student characteristics (e.g., race, age, caregiving status, military service, prior college experience) to accurately assess persistence and completion gaps. These data limitations underscore the critical importance of leveraging microdata, such as ACS Public Use Microdata Sample (PUMS) files and IPUMS datasets, which allow for custom analyses and more granular disaggregation than pre-tabulated aggregate tables can provide. """)
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
            - Consumed fruit at least than one time per day  
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
