import markovify


def generate_from_small_corpus(filename: str):
    with open(filename) as f:
        text = f.read()

    text_model = markovify.NewlineText(text, state_size=1)
    return text_model.make_sentence()


def generate_title():
    return generate_from_small_corpus("../data/titles.txt")

def generate_chapter_title():
    return generate_from_small_corpus("../data/chapterTitles.txt")

print(generate_title() + "\n")
print(generate_chapter_title() + "\n")
print(generate_chapter_title() + "\n")
print(generate_chapter_title() + "\n")
print(generate_chapter_title() + "\n")
print(generate_chapter_title() + "\n")

