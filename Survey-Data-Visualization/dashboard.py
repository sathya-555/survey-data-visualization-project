import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("data/survey_data.csv")

# Bar Chart – Learning Mode
fig1 = px.bar(
    df,
    x="Learning_Mode",
    title="Preferred Learning Mode",
    labels={"Learning_Mode": "Learning Mode"}
)

# Pie Chart – Gender
fig2 = px.pie(
    df,
    names="Gender",
    title="Gender Distribution",
    hole=0.3
)

# Box Plot – Satisfaction Rating
fig3 = px.box(
    df,
    x="Learning_Mode",
    y="Satisfaction",
    title="Satisfaction Rating by Learning Mode"
)

# Heatmap – Correlation
fig4 = px.imshow(
    df[["Satisfaction", "Internship_Rating"]].corr(),
    text_auto=True,
    title="Correlation Heatmap"
)

# Show dashboard charts
fig1.show()
fig2.show()
fig3.show()
fig4.show()
