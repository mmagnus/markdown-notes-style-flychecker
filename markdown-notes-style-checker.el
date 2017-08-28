;;; markdown-notes-style-checker --- On the fly (markdown) notes style checking in Python (standalone) and for GNU Emacs http://www.flycheck.org
;;; Commentary:
;;;  read more at https://github.com/mmagnus/markdown-notes-style-flychecker
;;; Code:
(require 'flycheck)

(flycheck-define-checker markdown-notes-style-checker
  "A Markdown notes style checker using the markdown_notes_style_checker.py script in Python.

See URL `https://github.com/mmagnus/markdown-notes-style-flychecker'."
  :command ("markdown_notes_style_checker.py" source-inplace)
  :error-patterns
  (
   (info line-start (file-name) ":" line ": info:" (message) line-end)
   (warning line-start (file-name) ":" line ": warning:" (message) line-end)
   (error line-start (file-name) ":" line ": error:" (message) line-end)
   )
  :modes markdown-mode)

(add-to-list 'flycheck-checkers 'markdown-notes-style-checker)
(provide 'markdown-notes-style-checker)

;;; markdown-notes-style-checker.el ends here
