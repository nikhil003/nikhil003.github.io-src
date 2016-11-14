import sys
from datetime import datetime
import os

def Template(title=None, year=None, month=None, day = None,
        category=None, slug=None, nbname=None):
    out = ""
    out += "Title: " + title + ' \n'
    out += "Date: "+str(year)+"-"+str(month)+"-"+str(day)+"\n"
    out += "Tags: \n"
    out += "Category: " + category + "\n"
    out += "Slug: " + slug + '\n'
    out += "Summary: \n"
    out += "Author: " + "Nikhil Garg \n"
    out += "{% notebook "+nbname+".ipynb %}"
    return out

def make_nb_entry(title, category):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    nbname = title.lower().strip().replace(' ', '_')
    if os.name == 'nt':
        f_create = "content\\{}.md".format(slug)
    else:
        f_create = "content/{}_{:0>2}_{:0>2}_{}.md".format(
            today.year, today.month, today.day, slug)
    print(f_create)
    t = Template(title=title, year=today.year, month=today.month,
                                day=today.day, category=category,
                                slug=slug, nbname=nbname)
    if os.path.isfile(f_create):
        print("File with same name exists")
    else:
        if os.name == 'nt':
            if os.path.isfile(os.path.join(f_create.split(os.sep)[:-1][0], 'notebooks', nbname + '.ipynb')):
                with open(f_create, 'w') as w:
                    w.write(t)
                print("File created -> " + f_create)
            else:
                print("No notebook with same exist in notebook directory")
        else:
            if os.path.isfile('/'.join(f_create.split(os.sep)[:-1], 'notebooks', nbname + '.ipynb')):
                with open(f_create, 'w') as w:
                    w.write(t)
                print("File created -> " + f_create)
            else:
                print("No notebook with same exist in notebook directory")
    

if __name__ == '__main__':

    if len(sys.argv) > 1:
        make_nb_entry(sys.argv[1], sys.argv[2])
    else:
        print "No title given"