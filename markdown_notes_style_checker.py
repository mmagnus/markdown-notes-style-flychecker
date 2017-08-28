#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Notes?

# Inbox
^ dont check it

if # ends a header, then accept given header!
"""
from __future__ import print_function
import argparse
import os

from config import DONT_CHECK_NOTES, IGNORE_TAG


class Paragraph:
    def __init__(self, no, header):
        assert type(no) is int
        self.no = no
        self.header = header
        self.len = 0

    def __repr__(self):
        return (str(self.no) + ':' + self.header + '#' + str(self.len))


def get_parser():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file', help="Markdown file")
    parser.add_argument("-v", "--verbose",
                        action="store_true", help="be verbose")
    return parser


def check_md(fn, verbose=False):
    paragraphs = []
    lines = open(fn).read().split('\n')
    for no, l in enumerate(lines, 1):
        # print(l)
        if l.startswith('#'):
            header = l.replace('#', '').strip()
            if header in DONT_CHECK_NOTES:
                continue

            if header.endswith(IGNORE_TAG):
                continue

            if paragraphs:
                p = paragraphs.pop()
                if p.len < 5:
                    print(os.path.basename(fn) + ':' + str(p.no) +
                          ': error: Paragraph too short')

            paragraph = Paragraph(no, header)
            paragraphs.append(paragraph)

            # len
            words = l.replace('#', '').strip().split(' ')
            if verbose:
                print(words)
            if len(words) < 3:
                print(os.path.basename(fn) + ':' + str(no) +
                      ': info: Title with less than 3 words.')

        # - http://www.flycheck.org/en/latest/languages.html#flycheck-languages
        if l.startswith('- http'):
            print(os.path.basename(fn) + ':' + str(no) +
                  ': warning: A link without a description.')

        if l.startswith('![]('):
            if not lines[no]:
                print(os.path.basename(fn) + ':' + str(no) +
                      ': warning: An image without a caption.')

        try:
            paragraph.len += 1
        except UnboundLocalError:
            pass

    # print(paragraphs)


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    check_md(args.file)
