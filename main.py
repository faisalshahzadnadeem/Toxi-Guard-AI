from fastapi import FastAPI
from pydantic import BaseModel
from rag_engine import ingest_documents, hybrid_retrieve, generate_explainable_response
from safety_layer import safety_triage

app = FastAPI()

index = None
chunks = None


@app.on_event("startup")
def load_vector_store():
    global index, chunks
    print("Loading toxicology_study.pdf into vector database...")
    index, chunks = ingest_documents()
    print("Vector store loaded successfully.")


class CaseRequest(BaseModel):
    case_description: str


@app.post("/triage")
def triage(request: CaseRequest):

    query = request.case_description

    safety = safety_triage(query)
    retrieved = hybrid_retrieve(query, index, chunks)

    final_response = generate_explainable_response(
        query,
        retrieved,
        safety
    )

    return {
        "risk_level": safety["risk_level"],
        "reason": safety["reason"],
        "recommended_action": safety["action"],
        "explainable_analysis": final_response
    }