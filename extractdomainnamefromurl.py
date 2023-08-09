import re

def domain_name(url: str) -> str:

    if type(url) != str:
        return False
    
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')

print(domain_name("www.google.de"))