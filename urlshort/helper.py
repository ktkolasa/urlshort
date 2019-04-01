import base64
import hashlib
import re
from .models import FullURL


def shorten_url(full_url):
    for i in range(100):
        full_url= full_url.encode('utf-8')
        short_url = base64.b64encode(hashlib.sha1(full_url).digest())
        short_url = short_url.decode(encoding='utf-8')
        alnum_hash = re.sub(r'[^a-zA-Z0-9]', "", short_url)[:8]
        q = FullURL.objects.filter(short_url=alnum_hash).exists()
        if not q:
            return alnum_hash
        full_url = full_url.decode('utf-8')+str(i)
    return -1

def check_for_protocol(full_url):
    if (full_url[:4]=='http'):
        return full_url
    else:
        return ('http://' + full_url) 