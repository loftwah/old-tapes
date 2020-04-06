from old_tapes.client import initialize_client
from old_tapes.posts import pretty_print_posts

fb_client = initialize_client()
posts, next_page = fb_client.get_user_posts()

while next_page is not None:
    pretty_print_posts(posts)
    posts, next_page = fb_client.get(next_page)
