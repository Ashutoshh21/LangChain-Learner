import requests
from bs4 import BeautifulSoup
from langchain_core.documents import Document

url = "https://science.nasa.gov/mission/hubble/science/science-behind-the-discoveries/hubble-pulsars/"
response = requests.get(url)

# Parse raw HTML into text strings
soup = BeautifulSoup(response.text, "html.parser")
clean_text = soup.get_text(separator="\n", strip=True)

web_document = Document(page_content=clean_text, metadata={"source": url})

#Now i can also use this clean text directly, or web_document.page_content to pass into prompt input -> Model -> Parser (In short pass into my chain)

print(web_document)