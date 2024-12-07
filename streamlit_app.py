import streamlit as st

st.title("IRA Risk Scoring")



def get_ira_risk_score(hypotension, age, fevg, diabete, hb, bicar, lactates, efgr):
    score = 0
    score += 5 if hypotension else 0
    score += 4 if age else 0
    score += 3 if fevg else 0
    score += 3 if diabete else 0
    score += 3 if hb else 0
    score += 5 if bicar else 0
    score += 5 if lactates else 0
    score += {
        ">= 60": 0,
        "40 to 60": 2,
        "20 to 40": 4,
        "<20": 6,
    }[efgr]
    return score


col1, col2 = st.columns(2)

with col1:

    hypotension = st.radio("Hypotension", (False, True), horizontal=True)
    age = st.radio("Age > 75", (False, True), horizontal=True)
    fevg = st.radio("FEGV < 30%", (False, True), horizontal=True)
    diabete = st.radio("Diabete", (False, True), horizontal=True)
    hb = st.radio("Hb < 10 g/dl", (False, True), horizontal=True)
    bicar = st.radio("Bicar < 10 mmol/l", (False, True), horizontal=True)
    lactates = st.radio("Lactates > 5 mmol/l", (False, True), horizontal=True)
    efgr = st.selectbox("eGFR (ml/mn/1,73 m2", (">= 60", "40 to 60", "20 to 40", "<20"))

    score = get_ira_risk_score(hypotension, age, fevg, diabete, hb, bicar, lactates, efgr)

with col2:

    st.subheader("Result")
    st.write("IRA Risk Score:", score)