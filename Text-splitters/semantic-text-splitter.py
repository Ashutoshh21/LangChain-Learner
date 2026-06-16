from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

text_splitter = SemanticChunker(
    embedding,
    breakpoint_threshold_type = 'standard_deviation',
    breakpoint_threshold_amount = 0.3 #difference of 1 point from std results in new chunk
                                    #std is taken among each difference or similarity scores (depending on choice) between two adjacent sentences' embd. vectors
)

text = """
Chess is a game of strategy. It requires two players and lots of brainstorming on different move variations.
Football is a game of energy and hyperactivity. There are a total of 11 players per team. It requires enthusiasm and lots of stamina to keep chasing the football.
Volleyball is a game of quick reflexes and jumping ability. It has 6 active players per team with a total of 12 to 14 players per team that can be substituted in-game.
Cricket is a game which is overhyped especially among Indian youth making them blind to other sports.
Modi ji is the longest serving Prime Minister of India. Our Indian constitution is outdated thus people exploit it heavily.
The biggest plannet in our solar system is jupiter. Naruto is one of the most prominent anime all over the world.
"""

doc= text_splitter.create_documents([text])

print(doc)