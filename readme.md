# 🧠 TF-IDF Similarity Grouper API

A FastAPI backend that allows users to upload documents (PDF, CSV, TXT), extracts and stores their content in memory, and provides two powerful features:

* 🔍 **Search**: Query the content using TF-IDF + cosine similarity.
* 🧩 **Grouping**: Cluster similar chunks of text from the uploaded document.

---

## 🚀 Features

* Accepts `.pdf`, `.csv`, and `.txt` files
* Automatically extracts and splits content into chunks
* Groups similar text entries using cosine similarity
* Searches content based on TF-IDF relevance
* Easy-to-use FastAPI structure with Swagger docs

---

## 🏗️ Project Structure

```
similarity_app/
├── app/
│   ├── main.py                 # FastAPI app setup
│   ├── api/endpoints.py        # API endpoints
│   ├── core/state.py           # In-memory state store
│   ├── services/
│   │   ├── extractor.py        # File extractors
│   │   └── similarity.py       # TF-IDF & cosine logic
│   ├── models/schemas.py       # Response schemas
│   └── utils/file_helpers.py   # File helpers
├── requirements.txt
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/similarity-app.git
cd similarity-app
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
uvicorn app.main:app --reload
```

* API Base URL: `http://localhost:8000`
* Swagger UI: `http://localhost:8000/docs`

---

## 📤 Upload Endpoint

**POST** `/upload`

Upload a document and receive grouped chunks by similarity.

* Form field: `file`
* Response: List of grouped chunks

**Example cURL:**

```bash
curl -X POST "http://localhost:8000/upload" \
  -F "file=@yourfile.txt"
```

**Response:**

```json
[
  {
    "group": 1,
    "items": [
      "Chunk A",
      "Chunk B"
    ]
  }
]
```

---

## 🔍 Search Endpoint

**GET** `/search?q=your+query`

Search for the most relevant chunks based on your query using TF-IDF.

**Example:**

```bash
curl "http://localhost:8000/search?q=machine+learning"
```

**Response:**

```json
[
  {
    "chunk": "Text about machine learning algorithms...",
    "score": 0.8123
  }
]
```

---

## 🧪 File Handling Rules

| File Type | How It's Processed                   |
| --------- | ------------------------------------ |
| `.pdf`    | Paragraphs per page using PyMuPDF    |
| `.csv`    | Rows combined as strings with pandas |
| `.txt`    | Paragraphs split by double newlines  |

---

## 📚 Use Cases

* Research tools
* Literature reviews
* Text similarity checks
* Auto-clustering content

---

## 🧰 Built With

* [FastAPI](https://fastapi.tiangolo.com/)
* [scikit-learn](https://scikit-learn.org/)
* [pandas](https://pandas.pydata.org/)
* [PyMuPDF](https://pymupdf.readthedocs.io/)
* [Uvicorn](https://www.uvicorn.org/)

---

## 🔮 Coming Soon

* [ ] Redis caching with Upstash
* [ ] Persistent file storage
* [ ] Frontend interface for uploads & search
* [ ] User authentication

---

## 📝 License

MIT © 2025
