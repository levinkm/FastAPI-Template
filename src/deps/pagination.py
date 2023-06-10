from fastapi import Request


def get_pagination(request:Request,skip: int = 0, limit: int = 10, total_items: int =10):
    """
    Generates the pagination links for the response header.
    """
    server_url = str(request.url)
    print(str(server_url))
    base_url = f"{server_url}/?limit={limit}"
    links = {}
    if skip > 0:
        prev_skip = max(0, skip - limit)
        prev_link ={'prev': f'{base_url}&skip={prev_skip}'}
        links.update(prev_link)
    if skip + limit < total_items:
        next_skip = skip + limit
        next_link = {"next": f'{base_url}&skip={next_skip}'}
        links.update(next_link)

    context = {
        "links":  links,
        "limit" : limit,
        "skip": skip,
        "url": server_url,

    }

    return context
