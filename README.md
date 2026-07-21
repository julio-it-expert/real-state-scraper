# Real Estate Data Pipeline 🚀

An enterprise-grade, modular web scraping architecture engineered in Python. This system parses complex DOM structures and automates data extraction pipelines using Pandas.

## 🛠️ Key Technical Features

* **Anti-Blocking System:** Simulates human behavior with randomized micro-delays (`time.sleep`) and dynamic HTTP header rotation using automated User-Agents.
* **Resilient Architecture:** Implements standalone components for networking, parsing, and data processing.
* **Pandas Data Pipeline:** Features advanced data cleansing, handles missing financial fields safely without crashing, and executes concurrent data persistence into Excel (`.xlsx`) and `.csv` formats.

## 📁 Project Structure

```text
├── core/
│   ├── network.py   # Handles secure HTTP requests and proxy/agent rotation
│   ├── parser.py    # Extracts real estate fields from target DOM text
│   └── pipeline.py  # Pandas transformations and analytical file exporting
├── data/            # Local directory for structured file persistence
├── main.py          # Orchestrates the execution logs
└── README.md
```
⚙️ Installation & Usage
1. Clone this repository.

2. Ensure you have requirements installed: pip install pandas beautifulsoup4 requests openpyxl.

3. Run the central orchestrator:

Bash
python main.py