from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import os
import uvicorn

app = FastAPI()

# Health check endpoint
@app.get("/ping")
async def health_check():
    return {"status": "healthy"}

# Serve an HTML form
@app.get("/", response_class=HTMLResponse)
async def form():
    return """
    <html>
      <head>
        <title>Simple Input Form</title>
      </head>
      <body>
        <h1>Submit Text</h1>
        <form action="/submit" method="post">
          <input type="text" name="input_text" placeholder="Enter some text" />
          <button type="submit">Submit</button>
        </form>
        <p>Check health: <a href="/ping">/ping</a></p>
      </body>
    </html>
    """

# Process form input
@app.post("/submit", response_class=HTMLResponse)
async def submit(input_text: str = Form(...)):
    return f"""
    <html>
      <head>
        <title>Submission Result</title>
      </head>
      <body>
        <h1>You submitted:</h1>
        <p>{input_text}</p>
        <a href="/">Go back</a>
        <p>Check health: <a href="/ping">/ping</a></p>
      </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.getenv("PORT", "80"))
    uvicorn.run(app, host="0.0.0.0", port=port)
