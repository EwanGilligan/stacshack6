import markovify
from pylatex import Document, Section, Subsection, Subsubsection, Command, NoEscape
from pylatex.base_classes.containers import ContainerCommand, Environment
from pylatex.package import Package
import random


def create_adventure(filename: str, title_model: markovify.Text, chapter_model: markovify.Text,
                     heading_model: markovify.Text, spoken_model: markovify.Text, paragraph_model: markovify.Text):
    doc = Document()
    doc.documentclass = Command('documentclass', options="letterpaper,twocolumn,openany,nodeprecatedcode", arguments=["dndbook"])
    doc.preamble.append(Command('title', title_model.make_sentence()))
    doc.append(NoEscape(r'\maketitle'))
    doc.append(NoEscape(r'\tableofcontents'))
    for _ in range(random.randint(5, 12)):
        with doc.create(chapter(chapter_model.make_sentence())):
            for _ in range(random.randint(5, 15)):
                heading = heading_model.make_sentence()
                while heading is None:
                    heading = heading_model.make_sentence()
                with doc.create(Section(heading)):
                    with doc.create(DndReadAloud()):
                        doc.append(spoken_model.make_sentence())
                    for _ in range(3, 9):
                        doc.append(paragraph_model.make_sentence())
    doc.generate_tex(filename)
    #doc.generate_pdf(filename)


class chapter(ContainerCommand):
    pass


class DndReadAloud(Environment):
    _latex_name = "DndReadAloud"
    _escape = False
