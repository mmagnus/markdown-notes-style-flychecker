#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Notes?

# Inbox
^ dont check it

if '@ok' in header, then accept given header!
"""

from __future__ import print_function
import os
import sys

DONT_CHECK_NOTES = ["Inbox"]


class Paragraph:
    def __init__(self, no, header):
        assert type(no) is int
        self.no = no
        self.header = header
        self.len = 0

    def __repr__(self):
        return (str(self.no) + ':' + self.header + '#' + str(self.len))


def check_md(fn, verbose=False):
    paragraphs = []
    lines = open(fn).read().split('\n')
    for no, l in enumerate(lines, 1):
        # print(l)
        if l.startswith('#'):
            header = l.replace('#', '').strip()
            if header in DONT_CHECK_NOTES:
                continue

            if '@ok' in header:
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
    check_md(sys.argv[1])
