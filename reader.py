# using pyttsx3 library for this project
import pyttsx3
import PyPDF4

book = open('python.pdf' , 'rb')
pdfReader = PyPDF4.PdfFileReader(book)
pages = pdfReader.numPages
print(pages  , 'pages')
speaker = pyttsx3.init()

# reading text page  by page
for num in range(11 , pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
print(speaker)
