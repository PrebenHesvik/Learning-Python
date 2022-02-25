from urllib.parse import urlparse


# Get domain name (example.com)
def get_domain_name(url):
    try:
        # get entire network location
        results = get_sub_domain_name(url).split('.')
        # return last two strings (like vg.no)
        return results[-2] + '.' + results[-1]
    except:
        return ''


# Get sub-domain name
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
