import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(layout="wide")

def parse_blocked_education_df(raw_df):
    records = []
    current_state = None

    for _, row in raw_df.iterrows():
        if pd.isna(row["n"]) and pd.isna(row["Percentage"]):
            current_state = row["Location"].strip()
        elif current_state and not pd.isna(row["Percentage"]):
            records.append({
                "State": current_state,
                "Education Level": row["Location"],
                "n": row["n"],
                "Percentage": row["Percentage"],
                "CI": row["95% CI"]
            })
    return pd.DataFrame(records)

# Simulated loading function — replace with your real loading logic
@st.cache_data
def load_data():
    dfs = {}
    for year in range(2019, 2024):  # Adjust range as needed
        df = parse_blocked_education_df(pd.read_csv(f"pages/data/overall education/education level_{year}.csv"))
        df['Year'] = year
        dfs[year] = df
    return dfs

@st.cache_data
def load_health_stat(filename, year):
    full_path = os.path.join("pages/data/", filename + f"_{year}.csv")
    df = parse_blocked_education_df(pd.read_csv(full_path))
    df['State'] = df['State'].str.strip()
    df['Percentage'] = pd.to_numeric(df['Percentage'], errors='coerce')
    return df
    
# Map state names to abbreviations for choropleth map
us_state_abbrev = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
    'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
    'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
    'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
    'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH',
    'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
    'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
    'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN',
    'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
    'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY', 'District of Columbia': 'DC'
}

question_to_filename = {
    "    🍻 Alcohol drink within past 30 days": "alcohol drink/within last 30 days",
    "    🍺 Binge drinkers (M 5+, F 4+ on one occasion)": "alcohol drink/Binge drinkers (males having five or more drinks on one occasion, females having four or more drinks on one occasion)",
    "    🍷 Heavy drinkers (M 14+, F 7+ in one week)": "alcohol drink/Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week)",
    "    🍎 Consumed fruit less than one time per day": "fruit consumption/Consumed fruit less than one time per day (variable calculated from one or more BRFSS questions)",
    "    🏃 Completed physical activity within past month": "physical activity/physical activity within past month",
    "    💉 Adults aged 65+ w/ flu shot": "flu shot/Adults aged 65+ who have had a flu shot within the past year (variable calculated from one or more BRFSS questions)",
    "    💉 Adults aged 65+ who have ever had a pneumonia vaccination": "pneumonia vaccination/Adults aged 65+ who have ever had a pneumonia vaccination (variable calculated from one or more BRFSS questions)",
    "    ⚕️ Has it been 1 year since last visited a doctor for a routine checkup": "last physical checkup/1year since you last visited a doctor for a routine checkup",

    "    🦴 Diagnosed with Arthritis": "chronic health indicators/arthritis",
    "    😤 Diagnosed with Asthma": "chronic health indicators/asthma",
    "    🧠 Diagnosed with Depression": "chronic health indicators/depression",
    "    🩸 Diagnosed with Diabetes": "chronic health indicators/diabetes",
    "    ❤️ Heart Attack (at least once)": "chronic health indicators/heart attack at least once",
    "    🧠 Stroke (at least once)": "chronic health indicators/stroke at least once",

    "    💳 Adults who had some form of health insurance": "health care insurance/Adults who had some form of health insurance (variable calculated from one or more BRFSS questions)",
    "    🚫 Do not have a single personal health care provider": "personal health care provider/do not have a single personal health care provider",

    "    💼 Employed": "employment status/employed",
    "    🧑‍💼 Self-employed": "employment status/selfemployed",
    "    🚫 Unable to work": "employment status/unable to work",
    "    💍 Married Marital Status": "martial status/married",
    "    👶 Kids (No kids)": "number of kids/no kids",
    "    👶 Kids (1 kid)": "number of kids/one kid",
    "    👶 Kids (2 kids)": "number of kids/two kid",
    "    🎖️ Veteran Status": "veteran/no", #get reverse percentage

    "    🏠 Home Ownership": "home ownership/do you own your home",
    "    💰 Less than 15k": "household income/less than 15k",
    "    💰 15k to 24k": "household income/15k to 24k",
    "    💰 25k to 34k": "household income/25k to 34k",
    "    💰 35k to 49k": "household income/35k to 49k",
    "    💰 50k plus": "household income/more than 50k",

    "    🧠 14 or more days when mental health status not good": "mental health days/14ormoreDays when mental health status not good (variable calculated from one or more BRFSS questions)",
    "    💪 14 or more days when physical health status not good": "physical health days/14ormoreDays when physical health status not good (variable calculated from one or more BRFSS questions)"
}

# Load all 5 dataframes at the beginning
all_data = load_data()

st.title("📊 Visualization Levels by State")
selected_year = st.selectbox("Select Year", sorted(all_data.keys()))

# Layout: left spacer, right main panel
left, right = st.columns([3, 3])

with left:

    selected_question = st.selectbox("Select Health/Lifestyle Indicator", list(question_to_filename.keys()))
    filename = question_to_filename[selected_question]

    df_health = load_health_stat(filename, selected_year)
    df_health['Abbrev'] = df_health['State'].map(us_state_abbrev)
    df_health = df_health.dropna(subset=['Abbrev', 'Percentage'])

    fig_left = px.choropleth(
        df_health,
        locations='Abbrev',
        locationmode='USA-states',
        color='Percentage',
        color_continuous_scale='Viridis',
        scope='usa',
        labels={'Percentage': '%'},
        hover_name='State',
        title=selected_question.strip(),
    )

    fig_left.update_layout(
        height=800,
        margin={"r":0,"t":60,"l":0,"b":0}
    )

    st.plotly_chart(fig_left, use_container_width=True)

with right:
    # User selects year and education group
    edu_group = st.selectbox("Select Education Group", ["College+", "Less than College"])

    # Filter to selected year
    df_selected = all_data[selected_year].copy()
    df_selected['State'] = df_selected['State'].str.strip()
    df_selected['Education Level'] = df_selected['Education Level'].str.strip()
    df_selected['Percentage'] = pd.to_numeric(df_selected['Percentage'], errors='coerce')

    if edu_group == "College+":
        df_edu = df_selected[df_selected['Education Level'] == "College+"].copy()
    else:
        # Sum of the three "less than college" levels per state
        df_less = df_selected[df_selected['Education Level'].isin([
            "Less than H.S.", "H.S. or G.E.D.", "Some post-H.S."
        ])].copy()

        df_edu = df_less.groupby("State", as_index=False)['Percentage'].sum()
        df_edu['Education Level'] = "Less than College"

    # Add abbreviations
    df_edu['Abbrev'] = df_edu['State'].map(us_state_abbrev)
    df_edu = df_edu.dropna(subset=['Abbrev', 'Percentage'])

    # Plot heatmap
    fig = px.choropleth(
        df_edu,
        locations='Abbrev',
        locationmode='USA-states',
        color='Percentage',
        color_continuous_scale='YlOrRd',
        scope='usa',
        labels={'Percentage': f'% {edu_group}'},
        hover_name='State',
        title=f"{edu_group} Attainment in {selected_year}",
        height=800,
        width=1000
    )

    st.plotly_chart(fig, use_container_width=True)

with st.container():
    st.header("📉 Relationship Between Indicator and Education Level")

    df_combined = pd.merge(df_health, df_edu, on="State")
    df_combined = df_combined.rename(columns={
        'Percentage_x': 'Health_Percentage',
        'Percentage_y': 'Education_Percentage'
    })

    # Scatter plot
    fig_combined = px.scatter(
        df_combined,
        x="Health_Percentage",
        y="Education_Percentage",
        hover_name="State",
        labels={
            "Health_Percentage": selected_question.strip(),
            "Education_Percentage": f"% {edu_group}"
        },
        title=f"Correlation between '{selected_question.strip()}' and Education in {selected_year}",
        trendline="ols"
    )

    fig_combined.update_traces(marker=dict(size=12, color="blue"))
    fig_combined.update_layout(height=600)
    st.plotly_chart(fig_combined)
