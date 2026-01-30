# Contract Analysis & Risk Assessment Bot

A GenAI-powered web application that helps small and medium businesses (SMEs) analyze contracts, identify potential legal risks, and understand complex legal clauses in simple business language.

This project was built as part of a hackathon to demonstrate the practical use of GenAI and NLP in legal-tech solutions.

---

## Overview

Business contracts often contain complex legal terms that are difficult for non-legal professionals to understand. This application allows users to upload a contract and receive a clause-by-clause analysis with risk levels and simplified explanations, helping them make informed decisions before signing.

---

## Features

- Upload and analyze business contracts  
- Automatic contract type detection  
- Clause-by-clause breakdown  
- Risk classification (Low / Medium / High)  
- Identification of unfavorable clauses  
- Simplified explanations for business users  
- Overall contract risk score  
- Audit logging for each analysis  
- Exportable summary report  
- Local processing to ensure data confidentiality  

---

## Supported Contract Types

- Service Agreements  
- Employment Contracts  
- Vendor Contracts  
- Lease Agreements  
- Partnership Agreements  

---

## Tech Stack

- Python  
- Streamlit (Web UI)  
- NLP techniques (Regex, langdetect)  
- JSON-based local storage for audit logs  

---


## Steps to Run the Project

### Step 1: Install Dependencies

pip install streamlit langdetect

### Step 2: Run the Application

streamlit run app.py

### Step 3: Upload a Contract

- Upload a `.txt` contract file
- The application will automatically analyze the contract

---

## Output

After uploading a contract, the application provides:

- Detected contract type
- Clause-by-clause analysis
- Risk level for each clause (Low / Medium / High)
- Simplified explanation of contract clauses
- Overall contract risk score
- Visual risk indicator
- Downloadable summary report
- Audit log entry for each analysis

---

## Disclaimer

This application is intended to assist users in understanding contracts and identifying potential risks.
It does not replace professional legal advice. Users should consult a qualified legal professional before making any legal decisions.
