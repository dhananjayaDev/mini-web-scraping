# Mock Amazon Scraper Project

![Banner](https://github.com/dhananjayaDev/mini-web-scraping/blob/main/web%20scrape%20project%20banner.png)

A modular mini-project that simulates a dynamic e-commerce store and showcases web scraping skills using **BeautifulSoup**, **Selenium**, and **Flask**. Built with recruiter appeal in mind—clean UI, editable data, and live scraping feedback.

---

##  Project Overview

This repo contains two Flask apps:

### 1. `mock_store/` – Editable Mock Amazon Store
- Amazon-style product cards with images, ratings, and delivery info
- Inline price editing for each item
- Bootstrap-styled layout for professional polish

### 2. `scraper_viewer/` – Scraped Product Viewer
- Scrapes the mock store using BeautifulSoup
- Displays products in the same layout, but read-only
- Optionally saves scraped data to `scraped_data.json`

---

##  Folder Structure

```
mock_amazon_scraper/
├── venv/                     # Shared virtual environment
├── mock_store/              # Editable product store
│   ├── app.py
│   └── templates/
│       └── index.html
├── scraper_viewer/          # Scraper + viewer
│   ├── scraper.py
│   ├── scraped_data.json
│   └── templates/
│       └── scraper.html
├── requirements.txt
├── README.md
└── .gitignore
```

---

##  How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/dhananjayaDev/mini-web-scraping.git
cd mock-amazon-scraper
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the mock store
```bash
cd mock_store
python app.py
```

### 5. Start the scraper viewer (in a new terminal)
```bash
cd scraper_viewer
python scraper.py
```

Then open:
- `http://localhost:5000` → Editable store
- `http://localhost:5001` → Scraped viewer

---

##  Features

- ✅ Dynamic price editing in the store
- ✅ Real-time scraping of local site
- ✅ Bootstrap layout mimicking Amazon
- ✅ Modular codebase for easy extension
- ✅ JSON export of scraped data

---

##  Future Enhancements

- Add “Scrape Now” button to viewer
- Persist store data to JSON or SQLite
- Add Streamlit dashboard for price trends
- Dockerize for deployment
- Add unit tests with `pytest`

---

##  Demo Screenshots

> _Coming soon: add screenshots or GIFs here_

---

##  Author

Built by Dhananjaya – just a dev who likes clean code and cooler dashboards.

---

##  License

MIT License

