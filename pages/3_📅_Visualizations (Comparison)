import streamlit as st
import pandas as pd
import plotly.express as px
import os

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

def load_and_clean_csv(filepath, year):
    df = pd.read_csv(filepath, header=None, names=["Location", "n", "Percentage", "95% CI"])
    df["Location"] = df["Location"].astype(str).str.strip()
    state_mask = df["n"].isna() & df["Percentage"].isna() & df["95% CI"].isna()
    df.loc[state_mask, "State"] = df.loc[state_mask, "Location"]
    df["State"] = df["State"].ffill()
    df = df[~state_mask].copy()
    df.rename(columns={"Location": "Education Level"}, inplace=True)
    df["n"] = pd.to_numeric(df["n"], errors='coerce')
    df["Percentage"] = pd.to_numeric(df["Percentage"], errors='coerce')
    df.reset_index(drop=True, inplace=True)
    df["Year"] = year  # add the year column
    return df

@st.cache_data
def load_data(selected_factors, selected_years):
    combined_df = pd.DataFrame()
    base_dir = "./pages/data/"

    for factor in selected_factors:
        relative_path = question_to_filename.get(factor)
        if not relative_path:
            st.warning(f"No filepath found for factor: {factor}")
            continue
        
        for year in selected_years:
            # Assuming files are named like "<relative_path>_<year>.csv"
            # Adjust this if your file naming differs
            filename = f"{relative_path}_{year}.csv"
            full_path = os.path.join(base_dir, filename)
            
            if not os.path.exists(full_path):
                st.warning(f"File not found: {full_path}")
                continue
            
            df = load_and_clean_csv(full_path, year)
            df["Factor"] = factor.strip()
            combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df

st.title("Interactive Visualization")

# Step 1: Factor selection
selected_factors = st.multiselect("Select Factor(s)", options=list(question_to_filename.keys()))

# Step 2: Year selection (example years 2018-2023)
available_years = list(range(2019, 2024))
selected_years = st.multiselect("Select Year(s)", options=available_years, default=available_years)

if selected_factors and selected_years:
    df = load_data(selected_factors, selected_years)
    
    # Sidebar filters - update options only if df is not empty
    if not df.empty:
        selected_factors_filter = st.sidebar.multiselect("Filter Factors", options=df["Factor"].unique(), default=df["Factor"].unique())
        selected_states = st.sidebar.multiselect("Filter States", options=df["State"].unique(), default=df["State"].unique())
        selected_education = st.sidebar.multiselect("Filter Education Levels", options=df["Education Level"].unique(), default=df["Education Level"].unique())
        selected_year_filter = st.sidebar.multiselect("Filter Years", options=df["Year"].unique(), default=df["Year"].unique())

        filtered_df = df[
            (df["Factor"].isin(selected_factors_filter)) &
            (df["State"].isin(selected_states)) &
            (df["Education Level"].isin(selected_education)) &
            (df["Year"].isin(selected_year_filter))
        ]

        numeric_cols = filtered_df.select_dtypes(include=["number"]).columns.tolist()

        col1, col2 = st.columns(2)
        with col1:
            x_axis = st.selectbox("Select X axis", options=numeric_cols, index=0)
        with col2:
            y_axis = st.selectbox("Select Y axis", options=numeric_cols, index=1 if len(numeric_cols) > 1 else 0)

        if st.button("Swap X and Y"):
            x_axis, y_axis = y_axis, x_axis

        if filtered_df.empty:
            st.warning("No data to display with the current filters.")
        else:
            fig = px.scatter(
                filtered_df, x=x_axis, y=y_axis,
                color="Factor", symbol="State",
                title=f"Scatter plot of {y_axis} vs {x_axis}",
                hover_data=["Factor", "State", "Education Level", "Year"]
            )
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data loaded for the selected factors and years.")
else:
    st.info("Please select at least one factor and one year.")
