from django import template
from urllib.parse import urlparse, parse_qs

register = template.Library()

@register.filter
def youtube_embed_url(url):

    parsed_url = urlparse(url)
    if 'youtu.be' in parsed_url.netloc:
        video_id = parsed_url.path.lstrip('/')
    elif 'youtube.com' in parsed_url.netloc:
        query_params = parse_qs(parsed_url.query)
        video_id = query_params.get('v', [None])[0]
    else:
        return ''
    if video_id:
        return f'https://www.youtube.com/embed/{video_id}'
    else:
        return ''
