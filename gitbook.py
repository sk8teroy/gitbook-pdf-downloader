import os
import time
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.print_page_options import PrintOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = input("Enter the base URL of the documentation site: ").strip()
TEMP_DIR = "pdf_pages"
OUTPUT_PDF = "merged_docs.pdf"

os.makedirs(TEMP_DIR, exist_ok=True)

def get_driver():
    options = Options()
    options.add_argument("--headless=new")  # New headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280x1696")
    options.add_experimental_option("prefs", {
        "printing.print_preview_sticky_settings.appState": '{"recentDestinations":[{"id":"Save as PDF","origin":"local"}],"selectedDestinationId":"Save as PDF","version":2}',
        "savefile.default_directory": os.path.abspath(TEMP_DIR),
    })
    options.add_argument("--kiosk-printing")
    return webdriver.Chrome(options=options)

def get_sidebar_links(driver, base_url):
    print("[*] Loading the documentation site...")
    driver.get(base_url)

    try:
        # Wait up to 20 seconds for any link inside an <aside>
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "aside a[href]"))
        )
    except Exception:
        print("[-] Timeout waiting for sidebar links.")
        return []

    anchors = driver.find_elements(By.CSS_SELECTOR, "aside a[href]")
    links = []
    for a in anchors:
        href = a.get_attribute("href")
        if href and href.startswith(base_url) and href not in links:
            links.append(href)

    print(f"[+] Found {len(links)} pages.")
    return links

def save_pages_as_pdf(driver, links):
    print("[*] Saving pages as PDFs...")
    filenames = []

    for i, url in enumerate(links):
        print(f"[*] Processing page {i+1}/{len(links)}: {url}")
        driver.get(url)
        time.sleep(2)  # Wait for the page to fully load

        pdf_data = driver.print_page(PrintOptions())
        
        # pdf_data might be a base64-encoded string, decode it
        if isinstance(pdf_data, str):
            pdf_data = base64.b64decode(pdf_data)
        
        filename = os.path.join(TEMP_DIR, f"page_{i:03}.pdf")
        with open(filename, "wb") as f:
            f.write(pdf_data)

        print(f"Saved: {filename}")
        filenames.append(filename)

    return filenames

def merge_pdfs(pdf_files, output_file):
    from PyPDF2 import PdfMerger
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write(output_file)
    merger.close()
    print(f"[+] Final merged PDF saved as: {output_file}")

def main():
    driver = get_driver()
    try:
        links = get_sidebar_links(driver, BASE_URL)
        if not links:
            print("No pages found. Exiting.")
            return
        pdfs = save_pages_as_pdf(driver, links)
        merge_pdfs(pdfs, OUTPUT_PDF)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
