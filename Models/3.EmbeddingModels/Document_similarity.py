from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

documents = [
    'Chess is a game of strategy. It requires two players and lots of brainstorming on different move variations',
    'Football is a game of energy and hyperactivity. There are a total of 11 players per team. It requires enthusiasm and lots of stamina to keep chasing the football',
    'Volleyball is a game of quick reflexes and jumping ability. It has 6 active players per team with a total of 12 to 14 players per team that can be substituted in-game.',
    'Cricket is a game which is overhyped especially among Indian youth making them blind to other sports.'
]

my_query = 'which game requires lots of energy and enthusiasm?'

document_embd = embeddings.embed_documents(documents) #only done once, then stored into vector databases
query_embd = embeddings.embed_query(my_query)

result_vector = cosine_similarity([query_embd], document_embd)[0] #accessing [0] since it'll return a 2d vector scoring each of left 2d vector's row similarity with each of right ones

index, score = sorted(list(enumerate(result_vector)), key = lambda x: x[1])[-1]

print("\n\n", my_query)
print(documents[index])
print(f'The similarity score is : {score}')
