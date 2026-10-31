from flask import Flask
app = Flask(__name__)

@app.get("/")
def index(): return "user-service v1\n"
@app.get("/healthz")
def healthz(): return "ok", 200
@app.get("/readyz")
def readyz(): return "ready", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
