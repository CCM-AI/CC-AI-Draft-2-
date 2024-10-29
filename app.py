import streamlit as st
from datetime import datetime

# Placeholder functions for risk algorithms
def calculate_cardio_risk(age, systolic_bp, smoker, cholesterol):
    risk_score = (age * 0.1) + (systolic_bp * 0.05) + (10 if smoker else 0) + (cholesterol * 0.02)
    if risk_score > 15:
        return "High"
    elif risk_score > 10:
        return "Moderate"
    else:
        return "Low"

def calculate_diabetes_risk(bmi, age, family_history, fasting_glucose):
    risk_score = (bmi * 0.3) + (age * 0.1) + (10 if family_history else 0) + (fasting_glucose * 0.02)
    if risk_score > 20:
        return "High"
    elif risk_score > 15:
        return "Moderate"
    else:
        return "Low"

def calculate_copd_risk(smoking_years, age, fev1):
    risk_score = (smoking_years * 0.5) + (age * 0.2) - (fev1 * 0.1)
    if risk_score > 25:
        return "High"
    elif risk_score > 15:
        return "Moderate"
    else:
        return "Low"

# Streamlit App Layout
st.title("Chronic Condition Risk Stratification and Personalized Care Plan")
st.write("This application stratifies risk for chronic conditions and provides a personalized care plan according to evidence-based guidelines.")

# Define tabs for each condition
tab1, tab2, tab3, tab4 = st.tabs(["Cardiovascular Risk", "Diabetes Risk", "COPD Risk", "Personalized Care Plan"])

# Results dictionary to store risk levels for each condition
results = {}

# Cardiovascular Risk Tab
with tab1:
    st.header("Cardiovascular Risk Assessment")
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    systolic_bp = st.slider("Systolic Blood Pressure (mmHg)", 90, 200, 120)
    cholesterol = st.slider("Total Cholesterol (mg/dL)", 100, 300, 180)
    smoker = st.radio("Smoking Status", options=["Non-smoker", "Current smoker"])

    if st.button("Calculate Cardiovascular Risk"):
        cardio_risk = calculate_cardio_risk(age, systolic_bp, smoker == "Current smoker", cholesterol)
        st.write(f"**Cardiovascular Risk Level**: {cardio_risk}")
        results["Cardiovascular"] = cardio_risk

# Diabetes Risk Tab
with tab2:
    st.header("Diabetes Risk Assessment")
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)
    family_history = st.radio("Family History of Diabetes", options=["Yes", "No"])
    fasting_glucose = st.number_input("Fasting Glucose (mg/dL)", min_value=50, max_value=300, value=90)

    if st.button("Calculate Diabetes Risk"):
        diabetes_risk = calculate_diabetes_risk(bmi, age, family_history == "Yes", fasting_glucose)
        st.write(f"**Diabetes Risk Level**: {diabetes_risk}")
        results["Diabetes"] = diabetes_risk

# COPD Risk Tab
with tab3:
    st.header("COPD Risk Assessment")
    smoking_years = st.number_input("Years of Smoking (if applicable)", min_value=0, max_value=60, value=0)
    fev1 = st.number_input("FEV1 (%)", min_value=20, max_value=100, value=80)

    if st.button("Calculate COPD Risk"):
        copd_risk = calculate_copd_risk(smoking_years, age, fev1)
        st.write(f"**COPD Risk Level**: {copd_risk}")
        results["COPD"] = copd_risk

# Personalized Care Plan Tab
with tab4:
    st.header("Personalized Care Plan")
    for condition, risk in results.items():
        st.subheader(f"{condition} Risk: {risk}")

        # Define the care plan based on the risk level
        if risk == "High":
            st.error(f"{condition} Risk is High.")
            st.write("### Recommended Care Plan:")
            st.write("- **Self-management support**: Comprehensive lifestyle modifications including diet and physical activity with regular health education.")
            st.write("- **Monitoring**: Monthly check-ups, regular lab tests (e.g., blood pressure for cardiovascular, A1C for diabetes, spirometry for COPD).")
            st.write("- **Follow-up**: Schedule follow-up visits every 1-3 months with healthcare provider.")
            st.write("- **Outcome evaluation**: Assess improvement in risk factors every 3 months and adjust treatment accordingly.")
            
        elif risk == "Moderate":
            st.warning(f"{condition} Risk is Moderate.")
            st.write("### Recommended Care Plan:")
            st.write("- **Self-management support**: Lifestyle advice with moderate modifications such as balanced diet, reduced smoking exposure, and increased exercise.")
            st.write("- **Monitoring**: Check-ups every 3-6 months with relevant tests.")
            st.write("- **Follow-up**: Regular follow-up every 3-6 months to assess risk factors and track progress.")
            st.write("- **Outcome evaluation**: Semi-annual outcome evaluation to ensure risk factors are improving.")

        else:  # Low Risk
            st.success(f"{condition} Risk is Low.")
            st.write("### Recommended Care Plan:")
            st.write("- **Self-management support**: Encourage a healthy lifestyle and preventive practices.")
            st.write("- **Monitoring**: Annual check-ups are sufficient.")
            st.write("- **Follow-up**: Yearly follow-up with healthcare provider to maintain health.")
            st.write("- **Outcome evaluation**: Annual review of health metrics to ensure stable condition.")

# Display Date and Time of Assessment
st.write("Assessment Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
