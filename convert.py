#!/usr/bin/env python3
"""
Convert md.md and rst.rst into useful output and comparisons.
"""

import re
import textwrap

import docutils.core
import markdown2
from docutils.writers.html4css1 import Writer, HTMLTranslator


class Buffer:
    def __init__(self):
        self.buffer = []

    def append(self, text):
        self.buffer.append(text)

    def clear(self):
        self.buffer = []

    def flush(self):
        buffered = "".join(self.buffer).strip()
        if buffered:
            yield "text", buffered
        self.clear()


def parse_md(lines):
    buffer = Buffer()
    parsing_headers = True

    for line in lines:
        if "parse-headers-off" in line:
            parsing_headers = False
            continue
        elif "parse-headers-on" in line:
            parsing_headers = True
            continue

        is_header = False
        if parsing_headers:
            header_match = re.search(r"^(#+) (.+)$", line)
            if header_match:
                is_header = True
        if is_header:
            yield from buffer.flush()
            hashes, text = header_match.groups()
            yield f"h{len(hashes)}", text
        elif "<!-- note:" in line:
            note = line.strip().strip("-!><").partition(":")[-1].strip()
            yield "note", note
        else:
            buffer.append(line)
    yield from buffer.flush()


def parse_rst(lines):
    buffer = Buffer()

    prev_line = None
    rules = {}
    parsing_headers = True
    for line in lines:
        if "parse-headers-off" in line:
            parsing_headers = False
            continue
        elif "parse-headers-on" in line:
            parsing_headers = True
            continue

        is_header = False
        if parsing_headers:
            header_match = re.search(r"^([^\w\d])\1\1+$", line)
            if header_match and prev_line:
                is_header = True
        if is_header:
            char = header_match.group(1)
            if char not in rules:
                rules[char] = len(rules) + 1
            level = rules[char]
            if level != 1:
                yield from buffer.flush()
            buffer.clear()
            yield (f"h{level}", prev_line.rstrip())
            prev_line = None
        elif ".. note: " in line:
            yield ("note", line.partition(':')[-1].strip())
        else:
            if prev_line:
                buffer.append(prev_line)
            prev_line = line

    if prev_line:
        buffer.append(prev_line)
    yield from buffer.flush()


TABLE_HEAD = """\

.. list-table::
   :widths: 15 30 30 15
   :header-rows: 1

   * - What
     - Markdown
     - reStructuredText
     - Notes

"""

ROW_FORMAT = """\
   * - {h3}
     - ::

{md}

     - ::

{rst}

     -

{notes}
"""

ROW_INDENT = 10


def row_indented(text):
    return textwrap.indent(text, prefix=" " * ROW_INDENT)


def sections(parsed_data):
    """Convert a stream of parsed tokens into sections with text and notes.

    Yields a stream of:
        ('h-level', 'header text', 'text', 'notes')

    """
    header = None
    text = []
    notes = []
    for ttype, ttext in parsed_data:
        if ttype.startswith('h'):
            if header:
                yield *header, "\n".join(text), "\n".join(notes)
            text = []
            notes = []
            header = (ttype, ttext)
        elif ttype == "text":
            text.append(ttext)
        elif ttype == "note":
            notes.append(ttext)
        else:
            raise Exception(f"Don't know ttype {ttype!r}")
    yield *header, "\n".join(text), "\n".join(notes)


SCARE_COMMENT = """
.. Don't edit this file directly.  It's created from four parts:
..      sheet_head.rst is the first content
..      md.md is a Markdown file parsed for content to go in the table.
..      rst.rst is an RST file parsed for content to go in the table.
..      sheet_foot.rst is the final content
..
.. See the README.rst for instructions.

"""


def combine(mdlines, rstlines):
    """Combine md lines and rst lines into a comparison sheet.

    Yields text chunks.

    """
    msections = sections(parse_md(mdlines))
    rsections = sections(parse_rst(rstlines))

    yield SCARE_COMMENT
    with open("sheet_head.rst") as fhead:
        yield fhead.read()

    for (mh, mhtext, mtext, mnotes), (rh, rhtext, rtext, rnotes) in zip(msections, rsections):
        # print(repr([mtype, mtext, rtype, rtext]))
        if mh != rh:
            raise Exception(f"Header mismatch: {mh} vs {rh}: {mhtext!r} vs {rhtext!r}")
        if rh == "h1":
            # H1 is for the document titles, which differ.
            continue
        if mhtext != rhtext:
            raise Exception(f"Mismatched headers: {mhtext!r} vs {rhtext!r}")
        if rh == "h2":
            yield mhtext
            yield "*" * len(mhtext)
            yield TABLE_HEAD
        elif rh == "h3":
            notes = (mnotes + "\n" + rnotes).strip()
            yield ROW_FORMAT.format(
                h3=rhtext,
                md=row_indented(mtext),
                rst=row_indented(rtext),
                notes=row_indented(notes),
            )
        else:
            raise Exception(f"Surprising header: {rh!r}: {rhtext!r}")

    with open("sheet_foot.rst") as fhead:
        yield fhead.read()


MD_SOURCE = "md.md"
RST_SOURCE = "rst.rst"


def make_comparison(md_filename, rst_filename, output_filename):
    print(f"Making comparison: {md_filename} + {rst_filename} -> {output_filename}")
    with open(output_filename, "w") as out:
        with open(md_filename) as mdlines:
            with open(rst_filename) as rstlines:
                for text in combine(mdlines, rstlines):
                    out.write(text)
                    out.write("\n")


def md_to_html(md_text):
    """Convert Markdown, using GitHub-like options."""
    # I copied this monstrosity from: https://github.com/trentm/python-markdown2/wiki/link-patterns#converting-links-into-links-automatically
    link_patterns = [
        (re.compile(
            r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)'
            r'[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)'), r'\1'),
    ]
    html_text = markdown2.markdown(
        md_text,
        extras=['fenced-code-blocks', 'link-patterns', 'footnotes'],
        link_patterns=link_patterns,
    )
    return html_text


def make_md(md_filename, html_filename):
    print(f"Converting markdown: {md_filename} -> {html_filename}")
    with open(md_filename) as mdfile:
        with open(html_filename, "w") as htmlfile:
            htmlfile.write(md_to_html(mdfile.read()))


def rst_to_html(rst):
    html_fragment_writer = Writer()
    html_fragment_writer.translator_class = HTMLTranslator
    return docutils.core.publish_string(rst, writer=html_fragment_writer)


def make_rst(rst_filename, html_filename):
    print(f"Converting ReST: {rst_filename} -> {html_filename}")
    with open(rst_filename) as rstfile:
        with open(html_filename, "wb") as htmlfile:
            htmlfile.write(rst_to_html(rstfile.read()))


def main():
    make_md(MD_SOURCE, "md.html")
    make_rst(RST_SOURCE, "rst.html")
    make_comparison(MD_SOURCE, RST_SOURCE, "mdrst.rst")
    make_rst("mdrst.rst", "mdrst.html")


if __name__ == "__main__":
    main()
