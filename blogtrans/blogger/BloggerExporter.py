import codecs

try:
    from xml.etree.ElementTree import * # for Python 2.5 users
except:
    from elementtree.ElementTree import *

from datetime import datetime
from blogtrans.data import *

def blogger_label(str) :
    result = u""
    for c in str:
        if not c in ['!', '&', '<', '>', '@'] :
            result += c
    return result

def write_comment(feed, c, aid, cid) :
    centry = SubElement(feed, "entry")
    SubElement(centry, "id").text = "tag:blogger.com,1999:blog-1.post-" + str(cid+10000)
    time_str = c.date.strftime("%Y-%m-%dT%H:%M:%S.000+08:00")
    SubElement(centry, "published").text = time_str
    SubElement(centry, "updated").text = time_str

    category = SubElement(centry, "category")
    category.attrib["scheme"]="http://schemas.google.com/g/2005#kind"
    category.attrib["term"]="http://schemas.google.com/blogger/2008/kind#comment"

    title = SubElement(centry, "title")
    title.attrib["type"]="text"
    title.text = "Title"

    content = SubElement(centry, "content")
    content.attrib["type"] = "html"
    content.text = c.body

    link = SubElement(centry, "link")
    link.attrib["rel"]="alternate"
    link.attrib["type"]="text/html"
    link.attrib["href"]="http://gfsgdfg.blogspot.com/2008/09/article2.html?showComment=" + str(cid) + "#c2499467377739779311"
    link.attrib["title"]=""

    link = SubElement(centry, "link")
    link.attrib["rel"]="self"
    link.attrib["type"]="application/atom+xml"
    link.attrib["href"]="http://www.blogger.com/feeds/1/comments/default/" + str(cid)

    if c.prev_comment != "" :
        link = SubElement(centry, "link")
        link.attrib["rel"]="related"
        link.attrib["type"]="application/atom+xml"
        link.attrib["href"]="http://www.blogger.com/feeds/1/comments/default/" + str(c.prev_comment)

    author = SubElement(centry, "author")
    if c.author != "" :
        SubElement(author, "name").text = c.author
    else :
        SubElement(author, "name").text = "Anonymous"

    if c.url != "" :
        SubElement(author, "uri").text = c.url

    SubElement(author, "email").text = "noreply@blogger.com"

    thr = SubElement(centry, "thr:in-reply-to")
    thr.attrib["href"]="http://www.blogger.com/feeds/1/posts/default/" + str(aid)
    thr.attrib["source"]="http://www.blogger.com/feeds/1/posts/default/" + str(aid)
    thr.attrib["ref"]="tag:blogger.com,1999:blog-1.post-" + str(aid)
    thr.attrib["type"] = "text/html"

    if c.reply != "" :
        comment = Comment()
        comment.date = c.rdate
        comment.body = c.reply
        comment.author = c.host
        comment.prev_comment = cid
        write_comment(feed, comment, aid, cid+1)

def make_comment_task(feed, c, aid) :
    return lambda cid : write_comment(feed, c, aid, cid)

class BloggerExporter :
    def __init__(self, filename, blogdata) :
        self.filename = filename
        self.blogdata = blogdata

    def Export(self) :
        comment_tasks = []

        feed = Element("feed")
        feed.attrib["xmlns"]="http://www.w3.org/2005/Atom"
        feed.attrib["xmlns:openSearch"]="http://a9.com/-/spec/opensearchrss/1.0/"
        feed.attrib["xmlns:thr"]="http://purl.org/syndication/thread/1.0"

        SubElement(feed, "id").text = "tag:blogger.com,1999:blog-1.archive"
        SubElement(feed, "updated").text = "2008-09-10T10:44:09.799-07:00"
        SubElement(feed, "title").text = "test123456"

        link = SubElement(feed, "link")
        link.attrib["rel"]="http://schemas.google.com/g/2005#feed"
        link.attrib["type"]="application/atom+xml"
        link.attrib["href"]="http://www.blogger.com/feeds/1/archive"

        link = SubElement(feed, "link")
        link.attrib["rel"]="alternate"
        link.attrib["type"]="text/html"
        link.attrib["href"]="http://test123456.blogspot.com"

        link = SubElement(feed, "link")
        link.attrib["rel"]="self"
        link.attrib["type"]="application/atom+xml"
        link.attrib["href"]="http://www.blogger.com/feeds/1/archive"

        author = SubElement(feed, "author")
        SubElement(author, "name").text = "test123456"
        SubElement(author, "uri").text = "http://www.blogger.com/profile/1"
        SubElement(author, "email").text = "noreply@blogger.com"

        generator = SubElement(feed, "generator")
        generator.attrib["version"] = "7.00"
        generator.attrib["uri"]="http://www.blogger.com"
        generator.text = "Blogger"

        for i, a in enumerate(self.blogdata.articles) :
            aid = i + 1

            entry = SubElement(feed, "entry")
            SubElement(entry, "id").text = "tag:blogger.com,1999:blog-1.post-" + str(aid)
            time_str = a.date.strftime("%Y-%m-%dT%H:%M:%S.000+08:00")
            SubElement(entry, "published").text = time_str
            SubElement(entry, "updated").text = time_str

            category = SubElement(entry, "category")
            category.attrib["scheme"]="http://schemas.google.com/g/2005#kind"
            category.attrib["term"]="http://schemas.google.com/blogger/2008/kind#post"

            for i, v in enumerate(a.category):
                if v=="":
                    continue
                category = SubElement(entry, "category")
                category.attrib["scheme"]="http://www.blogger.com/atom/ns#"
                category.attrib["term"]= blogger_label(v)

            title = SubElement(entry, "title")
            title.attrib["type"]="text"
            title.text = a.title

            content = SubElement(entry, "content")
            content.attrib["type"] = "html"

            content.text = a.body + a.extended_body

            link = SubElement(entry, "link")
            link.attrib["rel"]="alternate"
            link.attrib["type"]="text/html"
            link.attrib["href"]="http://tesafsdfa.blogspot.com/2008/09/test1.html"
            link.attrib["title"]="test1"

            link = SubElement(entry, "link")
            link.attrib["rel"]="self"
            link.attrib["type"]="application/atom+xml"
            link.attrib["href"]="http://www.blogger.com/feeds/1/posts/default/" + str(aid)

            author = SubElement(entry, "author")
            SubElement(author, "name").text = "test123456"
            SubElement(author, "uri").text = "http://www.blogger.com/profile/1"
            SubElement(author, "email").text = "noreply@blogger.com"
            for c in a.comments :
                task = make_comment_task(feed, c, aid)
                comment_tasks.append(task)

        #   0 1 2 3 4 5  ...
        #        +          
        #   1 2 3 4 5 6  ...
        #        =
        #   1 3 5 7 9 11 ...
        # reason for use 1 3 5 7 9 .... is left one for reply
        accumulation = 1
        for i, task in enumerate(comment_tasks):
            cid = i + accumulation
            task(cid)
            accumulation += 1

        ElementTree(feed).write(self.filename, "utf-8")
