import re, operator, bs4 #beautiful soup web-scrapper
import tamil #open-tamil library
def print_tamil_words( tatext ):
     taletters = tamil.utf8.get_letters(tatext)
     # tamil words only
     frequency = {}
     for pos,word in enumerate(tamil.utf8.get_tamil_words(taletters)):
          print pos, word
          frequency[word] = 1 + frequency.get(word,0)
     # sort words by descending order of occurence
     for l in sorted(frequency.iteritems(),           key=operator.itemgetter(1)):
          print l[0],’:’,l[1]
def demo_tamil_text_filter( ):
     url2 = u”http://ta.wikipedia.org&#8221;
     tapage = bs4.BeautifulSoup(urlopen(url))
     tatext = tapage.body.text;
     print_tamil_words( tatext )
if __name__ == u”__main__”:
     demo_tamil_text_filter()
