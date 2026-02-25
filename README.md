Financial Document Analyzer – Debug Challenge Submission
👩‍💻 Candidate: Vineela Chowdary

AI Internship Assignment – CrewAI Debug Challenge

🚀 Project Overview

This project is a Financial Document Analyzer built using CrewAI and FastAPI.

The original repository contained deterministic runtime bugs and inefficient / unsafe prompt instructions.
This submission fixes all identified issues and improves the system to produce structured, reliable financial analysis.

✅ Bugs Found and How They Were Fixed
1️⃣ Undefined LLM Initialization
Issue

The code contained:

llm = llm

This caused a runtime crash because llm was never defined.

Fix

Initialized the LLM properly using:

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3
)
2️⃣ Missing PDF Loader Import
Issue

Pdf() was used but not imported.

Fix

Replaced it with:

from langchain_community.document_loaders import PyPDFLoader

and implemented a proper PDF reading function.

3️⃣ Improper Tool Implementation
Issues

Incorrect async usage

Incorrect CrewAI tool structure

Dependency errors

Fix

Rewrote tools.py with a clean synchronous function:

def read_financial_document(path: str) -> str:

This properly loads and combines PDF content.

4️⃣ Task and API Naming Conflict
Issue

The FastAPI endpoint function name overwrote the CrewAI task variable.

Fix

Renamed the API endpoint function to:

async def analyze_document(...)

This resolved namespace conflicts.

5️⃣ File Path Not Passed to Crew
Issue

The Crew was not receiving the uploaded file path.

Fix

Updated kickoff call:

result = financial_crew.kickoff({
    "query": query,
    "file_path": file_path
})
6️⃣ Inefficient and Unsafe Prompts
Issues in Original Code

Encouraged hallucinated URLs

Asked to fabricate financial advice

Included contradictory instructions

Unsafe compliance behavior

Fix

Rewritten prompts to:

Use only document-based insights

Avoid fabricated content

Provide structured financial output

Maintain professional standards

🛠️ Tech Stack

Python

CrewAI

LangChain

OpenAI (via langchain-openai)

FastAPI

PyPDF

📂 Project Structure
financial-document-analyzer/
│
├── main.py
├── agents.py
├── tasks.py
├── tools.py
├── requirements.txt
└── README.md
⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone <your-repository-link>
cd financial-document-analyzer
2️⃣ Create Virtual Environment
python -m venv venv
Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Set OpenAI API Key
Windows
set OPENAI_API_KEY=your_api_key_here
Mac/Linux
export OPENAI_API_KEY=your_api_key_here
▶️ Running the Application
uvicorn main:app --reload

Open in browser:

http://127.0.0.1:8000/docs
📌 API Documentation
Endpoint
POST /analyze
Request (Form Data)
Field	Type	Required
file	PDF	Yes
query	Text	Yes
Example Response
{
  "status": "success",
  "analysis": "Structured financial analysis report..."
}
📈 Output Structure

The API returns a structured report including:

Executive Summary

Key Financial Metrics

Growth Trends

Risk Analysis

Investment Insight

Conclusion

All insights are derived strictly from the uploaded document.

🎯 Final Result

The project is now:

Free of deterministic runtime bugs

Free of unsafe prompt instructions

Stable and fully functional

Structured and maintainable

This submission successfully resolves both:

Deterministic Bugs

Inefficient Prompts
