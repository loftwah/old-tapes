from datetime import datetime

from termcolor import colored

def get_date(created_time: str) -> datetime:
    return datetime.strptime(created_time, "%Y-%m-%dT%H:%M:%S+%f")

format_date = lambda date: colored(datetime.strftime(date, "%d/%m/%y %H:%M"), 'magenta')


def pretty_print_posts(posts):
    for post in posts:
        link = post.get("link")
        if link is None:
            continue
        if "facebook.com" in link:
            continue
        created = get_date(post.get("created_time"))
        name = post.get("name", "")

        print(f"{format_date(created)} {colored(name, 'green', attrs=['blink'])}")
        print(f"\t\t {colored(link, 'blue', on_color='on_cyan')}")