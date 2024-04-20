from typing import List
from together import Together
import tomllib


with open("../secrets.toml", "rb") as f:
    data = tomllib.load(f)

client = Together(api_key = data["together"]["KEY"])

def get_embeddings(texts: List[str], model: str) -> List[List[float]]:
    texts = [text.replace("\n", " ") for text in texts]
    outputs = client.embeddings.create(model=model, input=texts)
    return [outputs.data[i].embedding for i in range(len(texts))]

input_texts = ['Our solar system orbits the Milky Way galaxy at about 515,000 mph']
embeddings = get_embeddings(input_texts, model='togethercomputer/m2-bert-80M-8k-retrieval')

print(embeddings)

