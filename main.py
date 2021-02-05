

def simple_slug_generator(str):
    """Title ==> slug"""
    slug = str.lower()
    dict_symbol = ('@', '#', '(', ')', '%', '№', ',', '.', ':', ';', '"', "'")
    for symbol in dict_symbol:
        slug = slug.replace(symbol, '')
    slug = slug.replace('--', '-')
    slug = slug.strip()
    slug = slug.replace(' ', '-')
    return slug
