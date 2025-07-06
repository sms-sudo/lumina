import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Bulk Dataset Loader", layout="wide")
st.title("📦 Load and Parse All Survey Files")

# --- Years to load ---
years_to_load = [2019, 2020, 2021, 2022, 2023]

# --- Your provided question_to_filename mapping ---
question_to_filename = {
    "    🍻 Alcohol drink": "alcohol drink/within last 30 days",
    "    🍺 Binge drinkers": "alcohol drink/Binge drinkers (males having five or more drinks on one occasion, females having four or more drinks on one occasion)",
    "    🍷 Heavy drinkers": "alcohol drink/Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week)",
    "    🍎 Consumed fruit at least one time per day": "fruit consumption/Consumed fruit less than one time per day (variable calculated from one or more BRFSS questions)",
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
    "    🎖️ Veteran Status": "veteran/no",  # get reverse percentage

    "    🏠 Home Ownership": "home ownership/do you own your home",
    "    💰 Less than 15k": "household income/less than 15k",
    "    💰 15k to 24k": "household income/15k to 24k",
    "    💰 25k to 34k": "household income/25k to 34k",
    "    💰 35k to 49k": "household income/35k to 49k",
    "    💰 50k plus": "household income/more than 50k",

    "    🧠 14 or more days when mental health status not good": "mental health days/14ormoreDays when mental health status not good (variable calculated from one or more BRFSS questions)",
    "    💪 14 or more days when physical health status not good": "physical health days/14ormoreDays when physical health status not good (variable calculated from one or more BRFSS questions)"
}

# --- Parse function provided ---
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

# --- Main loading logic ---
loading_placeholder = st.empty()
loading_placeholder.info("Loading all files for each question and year...")

base_data_path = Path(__file__).resolve().parents[1] / "pages/data"
loaded_data = {}

for display_name, base_filename in question_to_filename.items():
    question_data = {}
    for year in years_to_load:
        file_path = base_data_path / f"{base_filename}_{year}.csv"
        if file_path.exists():
            try:
                raw_df = pd.read_csv(file_path)
                parsed_df = parse_blocked_education_df(raw_df)
                question_data[year] = parsed_df
            except Exception as e:
                question_data[year] = f"Error parsing file: {str(e)}"
        else:
            question_data[year] = None
    loaded_data[display_name.strip()] = question_data

# --- Summary Display ---
st.success("All available files loaded and parsed.")
loading_placeholder.empty()

with st.expander("📋 Click to expand loaded file summary"):
    for display_name, yearly_data in loaded_data.items():
        st.markdown(f"#### {display_name}")
        for year, data in yearly_data.items():
            if isinstance(data, pd.DataFrame):
                st.markdown(f"- ✅ **{year}**: {len(data)} records")
            elif data is None:
                st.markdown(f"- ❌ **{year}**: File missing")
            else:
                st.markdown(f"- ⚠️ **{year}**: {data}")

# Optional: Store this dict in session state if needed
st.session_state["loaded_data"] = loaded_data

# --- FOOTER ---
st.markdown("---")
st.caption("M. Abdalla 2025")
