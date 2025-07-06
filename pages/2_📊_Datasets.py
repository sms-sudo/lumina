import streamlit as st
import pandas as pd
import os
from pathlib import Path
from io import StringIO

st.set_page_config(page_title="📊 Dataset Explorer", layout="wide")
st.title("📋 Explore Survey Questions by Category")

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

# --- Flat dropdown list with visual headers ---
question_list = [
    "── Health Behaviors ──",
    "    🍻 Alcohol drink", 
    "    🍺 Binge drinkers", 
    "    🍷 Heavy drinkers", 
    "    🍎 Consumed fruit less than one time per day",
    "    🏃 Completed physical activity within past month",
    "    💉 Adults aged 65+ w/ flu shot",
    "    💉 Adults aged 65+ who have ever had a pneumonia vaccination",
    "    ⚕️ Has it been 1 year since last visited a doctor for a routine checkup",

    "── Chronic Health Conditions ──",
    "    🦴 Diagnosed with Arthritis",
    "    😤 Diagnosed with Asthma",
    "    🧠 Diagnosed with Depression",
    "    🩸 Diagnosed with Diabetes",
    "    ❤️ Heart Attack (at least once)",
    "    🧠 Stroke (at least once)",

    "── Health Access / Coverage ──",
    "    💳 Adults who had some form of health insurance",
    "    🚫 Do not have a single personal health care provider",

    "── Demographic Characteristics ──",
    "    💼 Employed",
    "    🧑‍💼 Self-employed",
    "    🚫 Unable to work",
    "    💍 Married Marital Status",
    "    👶 Kids (No kids)",
    "    👶 Kids (1 kid)",
    "    👶 Kids (2 kids)",
    "    🎖️ Veteran Status",

    "── Socioeconomic Indicators ──",
    "    🏠 Home Ownership",
    "    💰 Less than 15k",
    "    💰 15k to 24k",
    "    💰 25k to 34k",
    "    💰 35k to 49k",
    "    💰 50k plus",

    "── Health Status Indicators (Self-Reported Days) ──",
    "    🧠 14 or more days when mental health status not good",
    "    💪 14 or more days when physical health status not good"
]

# --- Map from question display to file base name ---
question_to_filename = {
    "    🍻 Alcohol drink": "alcohol drink/within last 30 days",
    "    🍺 Binge drinkers": "alcohol drink/Binge drinkers (males having five or more drinks on one occasion, females having four or more drinks on one occasion)",
    "    🍷 Heavy drinkers": "alcohol drink/Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week)",
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

# --- Dropdown ---
selected_display = st.sidebar.selectbox("🔽 Choose a question", question_list)

years = st.multiselect("📅 Select Year(s)", [2019, 2020, 2021, 2022, 2023], default=[2023])

# --- Check if it's a data option ---

if selected_display in question_to_filename:
    base_filename = question_to_filename[selected_display]
    st.markdown(f"### 📊 Results for: {selected_display.strip()}")

    if not years:
        st.info("Please select at least one year to view results.")
    else:
        # Automatically sort selected years chronologically
        sorted_years = sorted(years)

        # Create columns side by side
        cols = st.columns(len(sorted_years))

        for i, year in enumerate(sorted_years):
            file_path = Path(__file__).resolve().parents[1] / "pages/data" / f"{base_filename}_{year}.csv"
            with cols[i]:
                st.markdown(f"**{year}**")
                if file_path.exists():
                    df = parse_blocked_education_df(pd.read_csv(file_path))
                    if "n" in df.columns:
                        df = df.drop(columns=["n"])
                    st.dataframe(df, use_container_width=True)
                else:
                    st.error(f"File not found: {file_path.name}")
else:
    st.info("Please select a valid question (not a category heading).")

# --- FOOTER ---
st.markdown("---")
st.caption("M. Abdalla 2025")
