from django.shortcuts import render
import feedparser



def index(request):
    # if request.method == 'POST':
    #     url = request.POST.get('url')

    
    # url = input('enter url link:')
    url = 'https://www.standardmedia.co.ke/rss/headlines.php'

# print(url)

    d = feedparser.parse(url)
    title = d['feed']['title']

    entries = []

    # try:
    #     print(title)

    # except:
    #     print('There is no source title')


    for item in d['entries']:
        title = item['title']
        description = item['description']
        link = item['link']

        entries.append({
            'title': title,
            'description': description,
            'link': link
        })
        
    context = {
        'entries':entries,
        'feed_title': d['feed']['title']
        
    }
    return render(request, 'RSS/index.html', context)