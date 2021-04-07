# LaTeX Escape

Started to write this package but then found:
The [LaTeX package](https://github.com/mbr/latex/) which already
included a similar maybe even better escape.

Simple script that escapes all LaTeX characters, i.e. from users
inputs, so that they will be displayed as the user intents them to be
displayed.

Best used together with a template system like [Jinja](https://jinja.palletsprojects.com/).

Usage is easy
```python
from latex_escape import do_latex_escape
do_latex_escape(r'This is a test \/ of some \ special %character%')
```

Will return:
> "This is a test \\textbackslash / of some \\textbackslash\\space special \\%character\\%"
