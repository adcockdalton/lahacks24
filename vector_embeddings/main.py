from vector_embeddings.embedder import EventEmbedder
from vector_embeddings.vector_db import VectorDB


events = [
    {
        "title": "Physics Symposium",
        "texts": "Join us for an exciting discussion on the latest advancements in the field of Physics.",
        "metadatas": {
            "county": "Orange County"
        },
        "ids": "ID1"
    },
    {
        "title": "Mathematics Conference",
        "texts": "Explore the fascinating world of Mathematics with leading experts in the field.",
        "metadatas": {
            "county": "LA County"
        },
        "ids": "ID2"
    },
    {
        "title": "Literature Lecture",
        "texts": "Learn about the history and development of Literature from renowned scholars.",
        "metadatas": {
            "county": "San Francisco County"
        },
        "ids": "ID3"
    },
    {
        "title": "Computer Science Workshop",
        "texts": "Discover the intersection of technology and Computer Science in this hands-on workshop.",
        "metadatas": {
            "county": "Orange County"
        },
        "ids": "ID4"
    },
    {
        "title": "Biology Seminar",
        "texts": "Engage in thought-provoking discussions on the future of Biology research.",
        "metadatas": {
            "county": "LA County"
        },
        "ids": "ID5"
    },
    {
        "title": "Chemistry Symposium",
        "texts": "Experience the wonders of Chemistry through interactive exhibits and presentations.",
        "metadatas": {
            "county": "San Francisco County"
        },
        "ids": "ID6"
    },
    {
        "title": "Art Exhibition",
        "texts": "Immerse yourself in the beauty of Art through an array of stunning artworks.",
        "metadatas": {
            "county": "Orange County"
        },
        "ids": "ID7"
    },
    {
        "title": "History Symposium",
        "texts": "Delve into the past and uncover the hidden stories of History.",
        "metadatas": {
            "county": "LA County"
        },
        "ids": "ID8"
    },
    {
        "title": "Music Concert",
        "texts": "Enjoy a captivating performance by talented musicians celebrating Music.",
        "metadatas": {
            "county": "San Francisco County"
        },
        "ids": "ID9"
    },
    {
        "title": "Economics Forum",
        "texts": "Join us for insightful talks and debates on key issues in the field of Economics.",
        "metadatas": {
            "county": "Orange County"
        },
        "ids": "ID10"
    },
    {
        "title": "Physics Symposium",
        "texts": "Join us for an exciting discussion on the latest advancements in the field of Physics.",
        "metadatas": {
            "county": "LA County"
        },
        "ids": "ID11"
    },
    {
        "title": "Mathematics Conference",
        "texts": "Explore the fascinating world of Mathematics with leading experts in the field.",
        "metadatas": {
            "county": "San Francisco County"
        },
        "ids": "ID12"
    },
    {
        "title": "Literature Lecture",
        "texts": "Learn about the history and development of Literature from renowned scholars.",
        "metadatas": {
            "county": "Orange County"
        },
        "ids": "ID13"
    },
    {
        "title": "Computer Science Workshop",
        "texts": "Discover the intersection of technology and Computer Science in this hands-on workshop.",
        "metadatas": {
            "county": "LA County"
        },
        "ids": "ID14"
    },
    {
        "title": "Biology Seminar",
        "texts": "Engage in thought-provoking discussions on the future of Biology research.",
        "metadatas": {
            "county": "San Francisco County"
        },
        "ids": "ID15"
    },
    {
        "title": "Chemistry Symposium",
        "texts": "Experience the wonders of Chemistry through interactive exhibits and presentations.",
        "metadatas": {
            "county": "Orange County"
        },
        "ids": "ID16"
    },
    {
        "title": "Art Exhibition",
        "texts": "Immerse yourself in the beauty of Art through an array of stunning artworks.",
        "metadatas": {
            "county": "LA County"
        },
        "ids": "ID17"
    },
    {
        "title": "History Symposium",
        "texts": "Delve into the past and uncover the hidden stories of History.",
        "metadatas": {
            "county": "San Francisco County"
        },
        "ids": "ID18"
    },
    {
        "title": "Music Concert",
        "texts": "Enjoy a captivating performance by talented musicians celebrating Music.",
        "metadatas": {
            "county": "Orange County"
        },
        "ids": "ID19"
    },
    {
        "title": "Economics Forum",
        "texts": "Join us for insightful talks and debates on key issues in the field of Economics.",
        "metadatas": {
            "county": "LA County"
        },
        "ids": "ID20"
    },
    {
        "title": "Physics Symposium",
        "texts": "Join us for an exciting discussion on the latest advancements in the field of Physics.",
        "metadatas": {
            "county": "San Francisco County"
        },
        "ids": "ID21"
    },
    {
        "title": "Mathematics Conference",
        "texts": "Explore the fascinating world of Mathematics with leading experts in the field.",
        "metadatas": {
            "county": "Orange County"
        },
        "ids": "ID22"
    },
    {
        "title": "Literature Lecture",
        "texts": "Learn about the history and development of Literature from renowned scholars.",
        "metadatas": {
            "county": "LA County"
        },
        "ids": "ID23"
    },
    {
        "title": "Computer Science Workshop",
        "texts": "Discover the intersection of technology and Computer Science in this hands-on workshop.",
        "metadatas": {
            "county": "San Francisco County"
        },
        "ids": "ID24"
    },
    {
        "title": "Biology Seminar",
        "texts": "Engage in thought-provoking discussions on the future of Biology research.",
        "metadatas": {
            "county": "Orange County"
        },
        "ids": "ID25"
    }
]

if __name__ == '__main__':
    eb = EventEmbedder()
    vdb = VectorDB(local = True)

    # for event in events:
    #     print("Embedding")
    #     vdb.add(
    #         embeddings = eb.get_embeddings([event["texts"]]),
    #         documents = [event["title"]],
    #         metadatas = [event["metadatas"]],
    #         ids = [event["ids"]]
    #     )

    while True:
        request = input(">>>")
        result = vdb.query(query_embeddings = eb.get_embeddings([request])[0], n_results = 2)
        print(result)


