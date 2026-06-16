from langchain_text_splitters import CharacterTextSplitter

text = """
Chess is a game of strategy. It requires two players and lots of brainstorming on different move variations.
Football is a game of energy and hyperactivity. There are a total of 11 players per team. It requires enthusiasm and lots of stamina to keep chasing the football.
Volleyball is a game of quick reflexes and jumping ability. It has 6 active players per team with a total of 12 to 14 players per team that can be substituted in-game.
Cricket is a game which is overhyped especially among Indian youth making them blind to other sports.
"""

#create an object of Char-text-splitter
splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=' '
)

res = splitter.split_text(text)

print(res)


#using list of document objects []
from langchain_core.documents import Document
from pypdf import PdfReader


reader = PdfReader('../Document-Loaders/example.pdf')
documents = []

for page_num, page in enumerate(reader.pages, start= 1):
    text = page.extract_text()

    #skip empty pages
    if text.strip():
        doc = Document(page_content=text, metadata = {'source' : 'example.pdf', 'page' : page_num})
        documents.append(doc)

result = splitter.split_documents(documents)

print(result) #one document object splitted into multiple seperate doc objects acc. to chunk_size, 
              #each havin a page_content and metadata