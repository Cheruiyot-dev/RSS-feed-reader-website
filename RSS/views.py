from django.shortcuts import render
import feedparser

def short_description(description, length):
    short_desc = description[:length] + '...'
    return [short_desc[i:i + length] for i in range(0, len(short_desc), length)]

def index(request):
    if request.method == 'POST':
        url = request.POST.get('url')

        d = feedparser.parse(url)
    
        entries = []
        for item in d['entries']:
# .get() method checks whether the title key exists in the item before it is accessed.
#  If it doesn't exist,a default value is set, which is returned.This  allows you to specify a default value
#  that will be returned if the key you're looking for doesn't exist.

            title = item.get('title', 'No title available')
            description = item.get('description', 'No description available')
            short_desc = short_description(description, 80)
            link = item.get('link', 'No link available')
            entries.append({
                'title': title,
                'description': short_desc,
                'link': link
            })
        
        context = {
            'entries':entries,
            'feed_title': d.get('feed', {}).get('title', 'No feed title available') 
        
        }
        return render(request, 'RSS/index.html', context)
    return render(request, 'RSS/index.html')

