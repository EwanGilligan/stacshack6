import markovify


def generate_from_small_corpus(filename: str):
    with open(filename) as f:
        text = f.read()

    text_model = markovify.NewlineText(text, state_size=1)
    return text_model


def generate_title():
    return generate_from_small_corpus("../data/titles.txt")


def generate_chapter_title():
    return generate_from_small_corpus("../data/chapterTitles.txt")

def generate_heading():
    return generate_from_small_corpus("../data/headingsFull.txt")


def generate_large_model(filename: str, output_model: str):
    with open(filename) as f:
        text_model = markovify.Text(f, retain_original=False)
    if output_model is not None:
        model_json = text_model.to_json()
        with open(output_model, "w") as output:
            output.write(model_json)
    return text_model


generate_large_model("../data/paragraphsFull.txt", "../models/paragraph_model.json")
