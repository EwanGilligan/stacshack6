from document_generation import *
from generation import *


def create_document():
    title_model = generate_title()
    chapter_model = generate_chapter_title()
    heading_model = generate_heading()
    paragraph_model = generate_large_model("../data/paragraphsFull.txt", "../models/paragraph_model")
    spoken_model = generate_large_model("../data/spokenFullCleaned.txt", None)
    create_adventure("../documents/test", title_model, chapter_model, heading_model, spoken_model, paragraph_model)


if __name__ == "__main__":
    create_document()
