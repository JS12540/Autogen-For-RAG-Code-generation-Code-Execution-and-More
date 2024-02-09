from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# Set up Selenium options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode

# Set up ChromeDriver service
chrome_service = Service(ChromeDriverManager().install())

# Choose Chrome browser
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Load webpage
driver.get('https://support.photobucket.com/hc/en-us/articles/22633797488788-How-to-Start-a-Free-Trial-if-Your-Account-is-Deactivated')

# Wait for the page to fully render
wait = WebDriverWait(driver, 10)

# Additional wait for specific element(s) to load
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Get the page source
page_source = driver.page_source

# Close the browser
driver.quit()

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find all text data
all_text = soup.find_all(text=True)

# Print the text data
print('Text Data:')
for i, text in enumerate(all_text, 1):
    if not text.parent.name in ['style', 'script', 'head', 'title']:
        print(f'{i}. {text.strip()}')
