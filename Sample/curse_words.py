from urllib.request import urlopen

html = urlopen("http://www.wdylike.appspot.com/?q=")
print(html)
def read_file():
   contents = open(r"C:\Users\HP\Desktop\karma\cursewords\movie_quotes.txt")
   quotes = contents.read()
   print(quotes)
   check_for_badwords("quotes")

def check_for_badwords():
    urlopen("http://www.wdylike.appspot.com/?q="+ word_to_check)
    output = connection.read()
    print(output)

read_file()


