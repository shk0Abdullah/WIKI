from django.shortcuts import render
from markdown2 import Markdown
from . import util
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def checker(request, title):
    markdowner = Markdown()
    md = util.get_entry(title)
    return md

def convertHTML(request, md, title):
    if md is None:
        return render(request, "encyclopedia/error.html", {
            'error': "File Not Found!"
        })
    else:
        markdowner = Markdown()
        html = markdowner.convert(md)
        return render(request, "encyclopedia/ame.html", {
            'html_content': html,
            'title': title.upper(),
        })
def retrieve(request,title):
    m_d = util.get_entry(title)
    return convertHTML(request,m_d,title)


def search(request):
    if request.method == 'POST':
        user_search = request.POST.get('q', '')

        # Check for an exact match
        html = checker(request, user_search)

        if html:
            # Return the exact match HTML
            return convertHTML(request, html, user_search)
        else:
            # No exact match; check for partial matches
            entries = util.list_entries()
            li = []
            for entry in entries:
                if user_search.lower() in entry.lower():
                    md = checker(request, entry)
                    li.append(entry)
            return render(request,'encyclopedia/search_results.html',{
                         'query':li,

                    })
            
            # If no matches found, render the error page
            return render(request, "encyclopedia/error.html", {
                'error': f"No results found for '{user_search}'"
            })
def create(request):
    if request.method == "GET":
        return render(request,"encyclopedia/create.html")
    else:
        title = request.POST['title']
        text = request.POST['text']
        title_Collision = util.get_entry(title)
        if title_Collision:
            return render(request,"encyclopedia/error.html",{
                "error":"Title Already Exists!"
            })
        else:
            util.save_entry(title,text)
            content = convertHTML(request,text,title)
            return render(request,"encyclopedia/ame.html",{
                'title':title,
                'html_content':content,
            })
def changes(request):
    if request.method == "POST":
        title = request.POST.get('entry_title')
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html",{
            'entrytitle': title,
            'entry_content': content
        })

def save(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('text')
        util.save_entry(title,content)
        return convertHTML(request,content,title)
def rand(request):
        mylist = util.list_entries()
        while '' in mylist:
            mylist.remove('')
        title = random.choice(mylist)
        mark = util.get_entry(title)
        return convertHTML(request, mark, title)

