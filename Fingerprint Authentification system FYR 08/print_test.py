# This is the code for printing the database to a pdf file

# Code made on  14th Jan 2022
#version 1
import tempfile
import win32print
import locale
import ghostscript
import render_to_pdf

pdf = render_to_pdf('XXXXXXXXXXXXXXprintfile.db', context)
temp1 = tempfile.mktemp('.pdf')
f1 = open(temp1, 'ab')
f1.write(pdf)
f1.close()

args = [
        "-dPrinted", "-dBATCH", "-dNOSAFER", "-dNOPAUSE", "-dNOPROMPT"
        "-q",
        "-dNumCopies#1",
        "-sDEVICE#mswinpr2",
        f'-sOutputFile#"%printer%{win32print.GetDefaultPrinter()}"',
        f'"{temp1}"'
    ]

encoding = locale.getpreferredencoding()
args = [a.encode(encoding) for a in args]
ghostscript.Ghostscript(*args)