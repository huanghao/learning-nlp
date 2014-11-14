"""
Make testing data for ex1.

Dump nltk.book.text? and sent? into a file named book.py, in
which those varialbes are list type rather than nltk.text.Text.
"""
import re
import nltk.book as book

buf = []
for name in dir(book):
    if not re.match(r'(text|sent)\d', name):
        continue

    text = getattr(book, name)
    string = str([i.encode('utf8') for i in list(text)])
    statement = '%s = %s' % (name, string)
    buf.append(statement)

with open('book.py', 'w') as file:
    file.write('\n'.join(buf))
