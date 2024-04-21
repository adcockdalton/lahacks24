import chromadb
import chromadb.db.base
from chromadb import QueryResult


class VectorDB:
    def __init__(self, *, local: bool):
        if local:
            self._chroma_client = chromadb.PersistentClient(path = "./vdb/events")
        else:
            self._chroma_client = chromadb.Client()

        try:
            self._top_grouping = self._chroma_client.create_collection(name="top_grouping")
        except chromadb.db.base.UniqueConstraintError:
            self._top_grouping = self._chroma_client.get_collection(name="top_grouping")

    def add(self, embeddings: list[list[float]], documents: list[str], metadatas: list[dict], ids: list[str]):
        self._top_grouping.add(
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )

        # documents can be the document detail
        # metadata can be the UUID

    def query(self, query_embeddings: list[float], n_results: int) -> QueryResult:
        return self._top_grouping.query(
            query_embeddings = query_embeddings,
            n_results = n_results,
        )

# ADD COUNTY INFORMATION IN THE VECTOR EMBEDDING
# STORE EVENTS IN RELATIONAL

if __name__ == '__main__':
    pass

