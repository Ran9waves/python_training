#you will need to first download beautifulsoup4 and requests lib
import requests #allows us to download html
from bs4 import BeautifulSoup #uses html and grab different data
import pprint #prints things in a cleaner way
#items marked with "2" gives us an idea about how to get elements of 2 pages. We would also need to modify the upcoming functions and variables to achieve it

res = requests.get('https://news.ycombinator.com/news') #kind of like a browser without a GUI
#res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser') #converts our string into html
#soup2 = BeautifulSoup(res2.text, 'html.parser')
#print(soup.find_all('div')) #finds all divs in soup
#print(soup.find_all('a')) #finds all the links in soup. using only "find" will get only the first object with that attributes
#print(soup.find_all(id= 'score_1234567')) #finds the votes on hackernews (the example we used for this exercise)
#print(soup.select('.score')) #allows to select specific items with the css selector
#print(soup.select('#score_123456')) #allows us to select a specific id
links = soup.select('.titleline')
subtext = soup.select('.subtext')
#links2 = soup2.select('.titleline')
#subtext2 = soup2.select('.subtext')

#mega_links = links + links2
#mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True) #we need to use lambda to indicate sorted which is the dictionary key that we want it to sort by

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links): #for each of the links will grab the index
        title = links[idx].getText() #will turn the index into text
        href = links[idx].get('href', None) #will grab the attribute as it is
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', '')) 
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points}) #will add titles and the links into a list
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))




