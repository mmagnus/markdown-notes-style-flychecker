# markdown-notes-style-flychecker (notes-debugger)

(super proof of concept)

On the fly (markdown) notes style checking in Python (standalone) and for GNU Emacs http://www.flycheck.org

A Lisp script to interpret an output of a Python script `markdown_notes_style_checker.py`:

```shell
/markdown_notes_style_checker.py ../notes/rna-dca.md
rna-dca.md:1: info: Title with less than 3 words.
rna-dca.md:5: warning: A link without a description.
rna-dca.md:33: warning: A link without a description.
rna-dca.md:73: info: Title with less than 3 words.
rna-dca.md:95: info: Title with less than 3 words.
rna-dca.md:95: error: Paragraph too short
rna-dca.md:108: info: Title with less than 3 words.
rna-dca.md:108: error: Paragraph too short
rna-dca.md:145: info: Title with less than 3 words.
rna-dca.md:176: warning: An image without a caption.
rna-dca.md:178: warning: An image without a caption.
```
Define new rules in the Python script!
