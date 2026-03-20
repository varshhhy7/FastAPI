from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

ideas: list[dict] = [
    {
        "id": 1,
        "creator": "Varshith",
        "title": "AI Personal CFO",
        "description": "An AI agent that manages your finances, predicts expenses, and gives smart insights.",
        "status": "prototype",
        "created_on": "March 2026"
    },
    {
        "id": 2,
        "creator": "Varshith",
        "title": "Infilo - Smart File System",
        "description": "An intelligent file system that organizes files using AI and allows natural language search.",
        "status": "building",
        "created_on": "March 2026"
    },
    {
        "id": 3,
        "creator": "Varshith",
        "title": "BizOS",
        "description": "Operating system for small businesses to automate clients, payments, and workflows.",
        "status": "idea",
        "created_on": "March 2026"
    }
]

@app.get("/" , response_class=HTMLResponse, include_in_schema=False)
@app.get("/ideas" , response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1> {ideas[0]['title']}</h1>"
@app.get("/api/ideas")
def get_ideas():
    return ideas
