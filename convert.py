#!/usr/bin/env python3
"""
Convert md.md and rst.rst into useful output and comparisons.
"""

import pprint
import re
import textwrap

import markdown2

def parse_md(lines):
    buffer = []

    def flush_buffer():
        buffered = "".join(buffer).strip()
        if buffered:
            yield ("text", buffered)

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
            yield from flush_buffer()
            hashes, text = header_match.groups()
            yield (f"h{len(hashes)}", text)
            buffer = []
        else:
            buffer.append(line)
    yield from flush_buffer()


def parse_rst(lines):
    buffer = []

    def flush_buffer():
        buffered = "".join(buffer).strip()
        if buffered:
            yield ("text", buffered)

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
                yield from flush_buffer()
            yield (f"h{level}", prev_line.rstrip())
            buffer = []
            prev_line = None
        else:
            if prev_line:
                buffer.append(prev_line)
            prev_line = line

    if prev_line:
        buffer.append(prev_line)
    yield from flush_buffer()

SHEET_HEAD = """\
#################################
RSt cheat sheet for Markdown fans
#################################

"""

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

"""

ROW_CODE_INDENT = 10


def combine(mdlines, rstlines):
    mddata = parse_md(mdlines)
    rstdata = parse_rst(rstlines)

    yield SHEET_HEAD
    h3 = None
    for (mtype, mtext), (rtype, rtext) in zip(mddata, rstdata):
        # print(repr([mtype, mtext, rtype, rtext]))
        if mtype != rtype:
            raise Exception(f"Token mismatch: {mtype} vs {rtype}")
        if rtype == "h1":
            continue
        if rtype == "h2":
            if mtext != rtext:
                raise Exception(f"Mismatched headers: {mtext!r} vs {rtext!r}")
            yield mtext
            yield "*" * len(mtext)
            yield TABLE_HEAD
        elif rtype == "h3":
            if mtext != rtext:
                raise Exception(f"Mismatched headers: {mtext!r} vs {rtext!r}")
            assert h3 is None
            h3 = rtext
        else:
            assert rtype == "text", f"Expected text, got {rtype}"
            assert h3 is not None
            code_indent = " " * ROW_CODE_INDENT
            yield ROW_FORMAT.format(
                h3=h3,
                md=textwrap.indent(mtext, prefix=code_indent),
                rst=textwrap.indent(rtext, prefix=code_indent),
                )
            h3 = None
            
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

def make_md(md_filename, html_filename):
    print(f"Converting markdown: {md_filename} -> {html_filename}")
    with open(md_filename) as mdfile:
        with open(html_filename, "w") as htmlfile:
            htmlfile.write(markdown2.markdown(mdfile.read()))

def rst_to_html(rst):
    from docutils import core
    from docutils.writers.html4css1 import Writer,HTMLTranslator

    html_fragment_writer = Writer()
    html_fragment_writer.translator_class = HTMLTranslator

    return core.publish_string(rst, writer = html_fragment_writer)

def make_rst(rst_filename, html_filename):
    print(f"Converting ReST: {rst_filename} -> {html_filename}")
    with open(rst_filename) as rstfile:
        with open(html_filename, "wb") as htmlfile:
            htmlfile.write(rst_to_html(rstfile.read()))

if __name__ == "__main__":
    make_md(MD_SOURCE, "md.html")
    make_rst(RST_SOURCE, "rst.html")
    make_comparison(MD_SOURCE, RST_SOURCE, "mdrst.rst")
    make_rst("mdrst.rst", "mdrst.html")
