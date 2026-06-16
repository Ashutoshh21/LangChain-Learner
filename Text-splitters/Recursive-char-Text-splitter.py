from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Chess is a game of strategy. It requires two players and lots of brainstorming on different move variations.
Football is a game of energy and hyperactivity. There are a total of 11 players per team. It requires enthusiasm and lots of stamina to keep chasing the football.
Volleyball is a game of quick reflexes and jumping ability. It has 6 active players per team with a total of 12 to 14 players per team that can be substituted in-game.
Cricket is a game which is overhyped especially among Indian youth making them blind to other sports.
"""

#create an object of Char-text-splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
)

res = splitter.split_text(text)

print(res)

