import sys
from datetime import datetime

TEMPLATE = """
Title:{title}
Date: {year}-{month}-{day}
Tags:
Category:{category}
Slug: {slug}
Summary:
Author: Nikhil Garg

post goes here

"""


def make_entry(title, category):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    f_create = "content/{}_{:0>2}_{:0>2}_{}.md".format(
        today.year, today.month, today.day, slug)
    t = TEMPLATE.strip().format(title=title,
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                slug=slug,
                                category=category)
    with open(f_create, 'w') as w:
        w.write(t)
    print("File created -> " + f_create)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        make_entry(sys.argv[1], sys.argv[2])
    else:
        print "No title given"