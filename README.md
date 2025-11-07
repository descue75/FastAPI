# FastAPI

Local Requirements: Git, Python

Clone the repository

```
git clone https://github.com/descue75/FastAPI.git
cd FastAPI
```

Create a virtual enironment

```
python -m venv .venv
```

Activate virtual environment

```
On Windows: .venv\Scripts\activate
On macOS / Linux: source .venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run server

```
uvicorn main:app --reload
```

Swagger docs

```
http://127.0.0.1:8000/docs
```
