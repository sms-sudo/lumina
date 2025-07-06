import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

st.set_page_config(page_title="Visualizations (Comparison)", layout="wide")
st.title("📅 Visualizations (Comparison)")

loaded_data = st.session_state["loaded_data"]

# --- Sidebar for options ---
st.sidebar.header("🔧 Visualization Settings")

# --- Select Multiple Questions ---
selected_questions = st.sidebar.multiselect("📋 Data Categories", list(loaded_data.keys()), default=[list(loaded_data.keys())[0]])

# --- Select Years (multiple) ---
available_years = sorted(
    list({year for q in selected_questions for year in loaded_data[q].keys() if isinstance(loaded_data[q][year], pd.DataFrame)}),
    reverse=True
)
selected_years = st.sidebar.multiselect("📅 Choose Year(s)", available_years, default=[available_years[0]])

# --- Select Chart Type ---
chart_type = st.sidebar.selectbox("📊 Choose Chart Type", ["Bar", "Line", "Scatter"])

# --- Load and combine data for selected questions and years ---
df_list = []
for question in selected_questions:
    for year in selected_years:
        if year in loaded_data[question]:
            df = loaded_data[question][year].copy()
            df["Year"] = year
            df["Question"] = question
            df_list.append(df)
if not df_list:
    st.warning("No data available for the selected questions and years.")
    st.stop()

df = pd.concat(df_list, ignore_index=True)

# --- Optional filters ---
all_states = sorted(df["State"].unique())
all_edu_levels = sorted(df["Education Level"].unique())

selected_states = st.sidebar.multiselect("🌎 Filter by States", all_states, default=all_states)
selected_edu_levels = st.sidebar.multiselect("🎓 Filter by Education Level", all_edu_levels, default=all_edu_levels)

# --- Color picker for each (Question, Year, Education Level) combination ---
default_colors = px.colors.qualitative.Plotly
color_map = {}

st.sidebar.markdown("### 🎨 Pick colors for each Question-Year-Education combination")

# Create a combined column for coloring
df["ColorKey"] = df["Question"] + " | " + df["Year"].astype(str) + " - " + df["Education Level"]

# Get unique combinations in filtered data
unique_combinations = df[
    df["State"].isin(selected_states) &
    df["Education Level"].isin(selected_edu_levels)
]["ColorKey"].unique()

for i, combo in enumerate(sorted(unique_combinations)):
    default_color = default_colors[i % len(default_colors)]
    color_map[combo] = st.sidebar.color_picker(f"{combo}", default_color, key=f"color_{combo}")

# --- Axis selectors ---
axis_x = st.sidebar.selectbox("📊 X-Axis", ["State", "Percentage", "Year", "Education Level"])
axis_y = st.sidebar.selectbox("📈 Y-Axis", ["Percentage", "State", "Year", "Education Level"])

# --- Filter Data ---
filtered_df = df[
    df["State"].isin(selected_states) &
    df["Education Level"].isin(selected_edu_levels)
].copy()

if filtered_df.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

# --- Plot chart ---
years_str = ", ".join(str(y) for y in selected_years)
questions_str = ", ".join(selected_questions)
st.subheader(f"{questions_str} ({years_str})")
chart_title = f"{axis_y} by {axis_x}"

# Plot using ColorKey (Question + Year + Education Level)
if chart_type == "Bar":
    fig = px.bar(
        filtered_df,
        x=axis_x,
        y=axis_y,
        color="ColorKey",
        color_discrete_map=color_map,
        hover_data=["Question", "State", "Education Level", "Year", "Percentage"],
        barmode='group',
        title=chart_title
    )
elif chart_type == "Line":
    fig = px.line(
        filtered_df,
        x=axis_x,
        y=axis_y,
        color="ColorKey",
        color_discrete_map=color_map,
        markers=True,
        hover_data=["Question", "State", "Education Level", "Year", "Percentage"],
        title=chart_title
    )
elif chart_type == "Scatter":
    fig = px.scatter(
        filtered_df,
        x=axis_x,
        y=axis_y,
        color="ColorKey",
        color_discrete_map=color_map,
        hover_data=["Question", "State", "Education Level", "Year", "Percentage"],
        title=chart_title
    )
else:
    st.error("Unsupported chart type selected.")
    st.stop()

fig.update_layout(xaxis_title=axis_x, yaxis_title=axis_y)
st.plotly_chart(fig, use_container_width=True)

# --- Optional data preview ---
with st.expander("📄 Show Table"):
    preview_df = filtered_df.drop(columns=["n"], errors="ignore").copy()
    # Move 'Year' and 'Question' to the front
    cols = preview_df.columns.tolist()
    for col in ["Question", "Year"]:
        if col in cols:
            cols.insert(0, cols.pop(cols.index(col)))
    preview_df = preview_df[cols]
    st.dataframe(preview_df, use_container_width=True)

# --- FOOTER ---
st.markdown("---")
st.caption("M. Abdalla 2025")
