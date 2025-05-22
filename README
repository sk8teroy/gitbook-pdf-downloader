# 🧾 GitBook Documentation PDF Downloader

This Python script automates the process of downloading and merging all pages from a GitBook-style documentation website into a single PDF file using Selenium and PyPDF2.

## ✅ Features

* Automatically extracts sidebar links from GitBook-style documentation
* Saves each page as a high-quality PDF
* Merges all individual PDFs into one complete document
* Runs headlessly using Chrome

## 📦 Requirements

* Python 3.8+
* Google Chrome
* ChromeDriver (compatible with your Chrome version)
* Python packages:

  * `selenium`
  * `PyPDF2`

You can install the required packages using:

```bash
pip install selenium PyPDF2
```

## 🚀 How to Use

1. Clone or download this repository:

```bash
git clone https://github.com/sk8teroy/gitbook-pdf-downloader.git
cd gitbook-pdf-downloader
```

2. Run the script:

```bash
python gitbook.py
```

3. When prompted, enter the base URL of the documentation site.
   Example:

```
Enter the base URL of the documentation site: https://docs.example.com
```

4. Wait while the script:

   * Loads all sidebar links
   * Saves each page as a PDF
   * Merges all pages into `merged_docs.pdf`

## 📂 Output

* Individual PDFs will be saved in the `pdf_pages/` directory.
* The final merged PDF will be saved as `merged_docs.pdf` in the current directory.

## 🛠 Troubleshooting

* **Chrome not found?** Make sure Chrome is installed and `chromedriver` is in your system's PATH.

## 📝 Notes

* This script is designed for **GitBook-style documentation** that uses an `<aside>` element with `<a href>` links in the sidebar.
* Some dynamic or heavily JavaScript-based sites may require additional wait times or logic tweaks.

## 📄 License

MIT License. Free to use and modify.
