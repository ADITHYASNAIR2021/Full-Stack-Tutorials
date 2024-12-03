from django import template
from urllib.parse import urlparse, parse_qs

register = template.Library()

@register.filter
def youtube_embed_url(url):
    if not url:
        return ''

    parsed_url = urlparse(url)

    if parsed_url.netloc in ['youtu.be', 'www.youtu.be']:
        video_id = parsed_url.path.lstrip('/')
    
    elif 'youtube.com' in parsed_url.netloc:
        if parsed_url.path == '/watch':
            query_params = parse_qs(parsed_url.query)
            video_id = query_params.get('v', [None])[0]
        elif parsed_url.path.startswith('/embed/'):
            video_id = parsed_url.path.split('/embed/')[1].split('/')[0]
        else:
            video_id = None
    else:
        video_id = None

    if video_id and len(video_id) == 11:
        return f'https://www.youtube.com/embed/{video_id}'
    else:
        return ''
