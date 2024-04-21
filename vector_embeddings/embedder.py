from typing import List
from together import Together
import tomllib


class EventEmbedder:
    def __init__(self):
        with open("../secrets.toml", "rb") as f:
            data = tomllib.load(f)

        self._client = Together(api_key = data["together"]["KEY"])

    def get_embeddings(self, texts: List[str]) -> List[List[float]]:
        texts = [text.replace("\n", " ") for text in texts]
        outputs = self._client.embeddings.create(model='togethercomputer/m2-bert-80M-8k-retrieval', input=texts)
        return [outputs.data[i].embedding for i in range(len(texts))]

if __name__ == '__main__':
    eb = EventEmbedder()

    input_texts = ['Our solar system orbits the Milky Way galaxy at about 515,000 mph', "Their solar system orbits the Andromeda galaxy at about 0 mph"]
    embeddings = eb.get_embeddings(input_texts)

    for embedding in embeddings:
        print(embedding)

