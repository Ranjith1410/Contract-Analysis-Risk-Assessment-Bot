# ================================
# Contract Analysis & Risk Assessment Bot
# Tech Stack: Streamlit + spaCy + GPT-style prompting (mocked)
# =================================

import streamlit as st
import json
import re
from datetime import datetime
from langdetect import detect

# -------------------------------
# Utility Functions
# -------------------------------

def extract_text(file):
    if file.type == "text/plain":
        return file.read().decode("utf-8")
    else:
        return "PDF/DOC parsing placeholder (text-based assumed)"


def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"


def classify_contract(text):
    keywords = {
        "Employment": ["employee", "salary", "termination"],
        "Service": ["services", "deliverables", "payment"],
        "Vendor": ["vendor", "purchase", "supply"],
        "Lease": ["lease", "rent", "premises"],
        "Partnership": ["partner", "profit", "loss"]
    }
    for k, v in keywords.items():
        for word in v:
            if word.lower() in text.lower():
                return k
    return "Unknown"


def extract_clauses(text):
    clauses = re.split(r"\n\s*(?=\d+\.)", text)
    return clauses


def risk_score_clause(clause):
    risk = 0
    triggers = {
        "penalty": 3,
        "indemnity": 4,
        "terminate at any time": 4,
        "exclusive": 2,
        "non-compete": 3,
        "jurisdiction": 2
    }
    for k, v in triggers.items():
        if k in clause.lower():
            risk += v
    if risk >= 6:
        return "High"
    elif risk >= 3:
        return "Medium"
    return "Low"


def simple_explanation(clause):
    return f"This clause means: {clause[:120]}..."


def generate_audit_log(data):
    with open("audit_log.json", "a") as f:
        f.write(json.dumps(data) + "\n")

# -------------------------------
# Streamlit UI
# -------------------------------

st.set_page_config(page_title="Contract Risk Analyzer", layout="wide")

st.title("📄 Contract Analysis & Risk Assessment Bot")
st.write("Helping Indian SMEs understand contracts in simple language")

uploaded_file = st.file_uploader("Upload Contract (PDF, DOCX, TXT)", type=["txt", "pdf", "docx"])

if uploaded_file:
    text = extract_text(uploaded_file)
    language = detect_language(text)
    contract_type = classify_contract(text)
    clauses = extract_clauses(text)

    st.subheader("📌 Contract Overview")
    st.write(f"**Detected Language:** {language}")
    st.write(f"**Contract Type:** {contract_type}")

    total_risk = 0
    st.subheader("📑 Clause-by-Clause Analysis")

    for i, clause in enumerate(clauses[:10]):
        risk = risk_score_clause(clause)
        if risk == "High": total_risk += 3
        elif risk == "Medium": total_risk += 2
        else: total_risk += 1

        with st.expander(f"Clause {i+1} - Risk: {risk}"):
            st.write("**Original Clause:**")
            st.write(clause)
            st.write("**Simple Explanation:**")
            st.write(simple_explanation(clause))
            if risk == "High":
                st.warning("Unfavorable clause detected. Consider renegotiation.")

    st.subheader("⚠️ Overall Risk Assessment")
    st.progress(min(total_risk / 30, 1.0))
    st.write(f"**Composite Risk Score:** {total_risk} / 30")

    audit = {
        "timestamp": str(datetime.now()),
        "contract_type": contract_type,
        "risk_score": total_risk
    }
    generate_audit_log(audit)

    if st.button("📄 Export Summary"):
        summary = {
            "contract_type": contract_type,
            "language": language,
            "risk_score": total_risk
        }
        st.download_button("Download JSON", json.dumps(summary, indent=2), file_name="contract_summary.json")

st.markdown("---")
st.caption("⚖️ This tool assists understanding and does not replace legal advice")
