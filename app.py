from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI()

# Database Simulation
nodes_db: Dict[str, dict] = {}
links_db: List[dict] = []

class Node(BaseModel):
    site_id: str
    cpu: int  # Number of CPUs
    mem: int  # Memory in GB
    storage: int  # Storage in GB

class Link(BaseModel):
    source: str
    destination: str
    latency_ms: float  # Latency in milliseconds

@app.post("/nodes/")
def add_node(node: Node):
    if node.site_id in nodes_db:
        raise HTTPException(status_code=400, detail="Node already exists.")
    nodes_db[node.site_id] = node.dict()
    return {"message": "Node added successfully."}

@app.get("/nodes/{site_id}")
def get_node(site_id: str):
    if site_id not in nodes_db:
        raise HTTPException(status_code=404, detail="Node not found.")
    return nodes_db[site_id]

@app.post("/links/")
def add_link(link: Link):
    links_db.append(link.dict())
    return {"message": "Link added successfully."}

@app.get("/links/")
def get_links():
    return links_db

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

