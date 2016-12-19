# -*- coding: utf-8 -*-
from docx import Document

def parseMesh(filename):
    document = Document(filename)
    count = 0

    for item in document.paragraphs:
        content = item.text.strip()
        count += 1

    print(count)

if __name__ == '__main__':
    parseMesh('Mesh-医学主题词表.docx')