# 🚀 Web Scraping Project with Streamlit , BeautifulSoup, Selenium Web Driver 

This is a Python-based web scraping project using `Selenium`, `BeautifulSoup`, and `Streamlit`. The script launches a Chrome browser, loads a website, extracts the page source, and processes the data.

## 🌟 Features
- ✅ Uses Selenium WebDriver to automate browser interactions.
- ✅ Supports proxy configuration for scraping.
- ✅ Extracts page source for further processing.
- ✅ Interactive UI using Streamlit.

## 📌 Prerequisites
Make sure you have the following installed on your system:
- 🐍 Python (>= 3.7)
- 🌍 Google Chrome (Ensure you have the latest version)
- 🔧 ChromeDriver (Version must match your Chrome browser version)

## 🔧 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/web-scraper.git
cd web-scraper
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```
Activate the virtual environment:
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Linux/macOS:**
  ```bash
  source venv/bin/activate
  ```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Download and Setup ChromeDriver
- Find your **Google Chrome version** by visiting:
  ```
  chrome://settings/help
  ```
- Download the matching `chromedriver` from:
  [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)
- Extract and place `chromedriver.exe` inside the `driver/` directory.

📂 **Make sure your project structure looks like this:**
```
web-scraper/
│── ais/                    # Additional project files (if any)
│── driver/                 # Place ChromeDriver here
│   ├── chromedriver.exe    # ChromeDriver binary
│── main.py                 # Main script
│── scrape.py               # Scraping script
│── requirements.txt        # Project dependencies
│── __pycache__/            # Compiled Python files
```

## 🚀 Running the Application
Run the Streamlit app with:
```bash
streamlit run main.py
```

## 🛠 Troubleshooting
1. **WebDriverException: Chrome failed to start**
   - Ensure `chromedriver.exe` is placed inside the `driver/` directory.
   - Check if ChromeDriver matches your Chrome browser version.
2. **Permission Denied Error**
   - Try running the script as an administrator.
3. **Exit Code -1073741510 (0xC000013A)**
   - This error may occur due to missing dependencies or an incorrect WebDriver setup. Ensure all dependencies are correctly installed.

## 🤝 Contributing
Feel free to fork the repository and submit pull requests. Contributions are welcome! 😊

## 📜 License
This project is licensed under the MIT License.

Happy Scraping! 🎉

