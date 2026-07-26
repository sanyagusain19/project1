# Project1 🚀

A comprehensive full-stack web application built with Flask that integrates multiple APIs and web scrapers to provide dynamic data visualization and interactive dashboards.

## 📋 Overview

Project1 is a feature-rich Flask application that combines real-time data fetching from various APIs with web scraping capabilities. It includes web-based dashboards for exploring music, movies, anime, companies, and more, along with integrated ML models for predictive analytics.

## 🎯 Features

### 🌐 Web Scraping Modules
- **Spotify Scraper** - Extract trending Spotify data
- **Anime Scraper** - Scrape anime information
- **Steam Games Scraper** - Collect gaming data from Steam
- **Top Companies Scraper** - Gather company information from various sources
- **Goodreads Scraper** - Extract book quotes and reviews
- **Movie Scraper** - Fetch movie data

### 📡 API Integrations
- **Plants API** - Search plant information
- **Movies API** - Query movie details
- **Weather API** - Real-time weather data
- **Pokemon API** - Pokémon information lookup
- **Products API** - Product catalog browsing

### 📊 Dynamic Data Feeds
- **Top Charts** - Trending movies across platforms
- **Startups Feed** - Latest startup news and data
- **Hacker News** - Tech news aggregation
- **Top Songs** - Music charts and rankings
- **Disasters** - Real-time disaster information

### 🤖 ML Features
- **Churn Prediction Model** - ML-based customer churn prediction with pre-trained model
- **Data Scaling** - Integrated scikit-learn scaler for model preprocessing

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | HTML (37.7%), CSS (48.9%), JavaScript (2.4%) |
| **Backend** | Python (6.2%), Flask |
| **ML/Data** | Jupyter Notebook (4.8%), scikit-learn, pandas |
| **Web Scraping** | BeautifulSoup, Selenium |
| **Server** | Gunicorn |

## 📦 Dependencies

```
Flask           # Web framework
gunicorn        # Production server
requests        # HTTP library
beautifulsoup4  # Web scraping
selenium        # Browser automation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/sanyagusain19/project1.git
cd project1
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

The application will start on `http://0.0.0.0:5000`

## 📂 Project Structure

```
project1/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── companies_data.json       # Cached company data
├── model_columns.json        # ML model columns config
├── churn_model.pkl          # Pre-trained churn prediction model
├── scaler.pkl               # Data scaler for ML preprocessing
├── scrape_and_save.py       # Data collection script
│
├── scraper/                 # Web scraping modules
│   ├── spotify.py           # Spotify scraper
│   ├── animescraper.py      # Anime scraper
│   ├── streamgames.py       # Steam games scraper
│   ├── topcompanies.py      # Companies scraper
│   ├── goodreadsscraper.py  # Goodreads scraper
│   ├── movies.py            # Movie scraper
│
├── api/                     # API integration modules
│   ├── plants.py            # Plants API
│   ├── weather.py           # Weather API
│   ├── pokemon.py           # Pokemon API
│   ├── product.py           # Products API
│
├── dynamic/                 # Dynamic data feeds
│   ├── topcharts.py         # Movie charts
│   ├── startup.py           # Startup feed
│   ├── hackernews.py        # Hacker News feed
│   ├── top_songs.py         # Music charts
│   ├── disasters.py         # Disaster alerts
│
├── templates/               # HTML templates
│   ├── home.html            # Homepage
│   ├── about.html           # About page
│   ├── projects.html        # Projects showcase
│   ├── webscraping.html     # Web scraping page
│   ├── apis.html            # API showcase
│   ├── dynamic_scraper.html # Dynamic data page
│   ├── minor/               # Minor projects
│   └── ...                  # Other templates
│
├── static/                  # CSS, JS, images
│   └── ...                  # Static assets
│
└── one.ipynb               # Jupyter notebooks for analysis
```

## 🌐 Application Routes

| Route | Feature |
|-------|---------|
| `/` | Homepage |
| `/about` | About page |
| `/journey` | User journey |
| `/projects` | Projects showcase |
| `/webscraping` | Web scraping demo |
| `/animescraper` | Anime data |
| `/spotifyscraper` | Spotify trends |
| `/steamgamesscraper` | Steam games |
| `/topcompaniesscraper` | Top companies |
| `/goodquotesscraper` | Book quotes |
| `/apis` | API integrations |
| `/plants?q=query` | Plant search |
| `/movies?q=query` | Movie search |
| `/weather` | Weather info |
| `/pokemon?name=name` | Pokemon lookup |
| `/products` | Product catalog |
| `/dynamic/topcharts` | Trending movies |
| `/startup` | Startup news |
| `/hackernews` | Tech news |
| `/topS` | Top songs |
| `/disasters` | Disaster alerts |
| `/minor/churn` | Churn prediction |

## 🤖 ML Model

The project includes a pre-trained customer churn prediction model:
- **Model File**: `churn_model.pkl`
- **Scaler File**: `scaler.pkl`
- **Configuration**: `model_columns.json`
- **Accessible at**: `/minor/churn`

## 📊 Data Files

- `companies_data.json` - Pre-scraped company database
- `model_columns.json` - Feature configuration for ML predictions
- `one.ipynb` - Jupyter notebook with analysis and data exploration

## 🔧 Configuration

The Flask app runs with:
- **Host**: 0.0.0.0 (accessible from any interface)
- **Port**: 5000
- **Debug Mode**: True (for development)

For production, modify `app.py` line 207:
```python
app.run(host="0.0.0.0", port=5000, debug=False)  # Set debug=False
```

## 📥 Deployment

Using Gunicorn (recommended for production):
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Sanya Gusain**
- GitHub: [@sanyagusain19](https://github.com/sanyagusain19)

## 🔗 Links

- Repository: https://github.com/sanyagusain19/project1
- Issues: https://github.com/sanyagusain19/project1/issues

## 📚 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [BeautifulSoup4 Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [scikit-learn Documentation](https://scikit-learn.org/)

---

**Last Updated**: July 26, 2026
