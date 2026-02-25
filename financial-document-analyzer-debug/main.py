from fastapi import FastAPI, UploadFile, File, Form
from crewai import Crew, Process
import shutil
import os

from agents import financial_analyst
from tasks import analyze_financial_document
from tools import read_financial_document


app = FastAPI()


def run_crew(query: str, file_path: str):
    financial_crew = Crew(
        agents=[financial_analyst],
        tasks=[analyze_financial_document],
        process=Process.sequential,
    )

    result = financial_crew.kickoff({
        "query": query,
        "file_path": file_path
    })

    return result


@app.post("/analyze")
async def analyze_document(
    file: UploadFile = File(...),
    query: str = Form(...)
):
    file_location = f"temp_{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = run_crew(query, file_location)

    os.remove(file_location)

    return {
        "status": "success",
        "analysis": result
    }