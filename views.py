from django.shortcuts import render, redirect
import random
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
	return render(request, "encyclopedia/title.html", {
			"title": util.get_entry(title)
		})

def search(request):
	title= request.GET.get("q")
	entry= util.get_entry(title)
	if entry is None:
		entry="Error, nothing was found."
	return render(request, "encyclopedia/search.html", {
		"entry":entry, "title":title.capitalize()
		})

def newpage(request):
	if request.method=="POST":
		title= request.GET.get("newtitle")
		content= request.GET.get("content")
		entry= util.save_entry(title, content)
		if entry.is_valid():
			entry = entry.cleaned_data["entries"]
			entries.append(entry)
		return render(request, "encyclopedia/index.html", {
			"entries":util.list_entry()
			})
	else:
		return render(request, "encyclopedia/newpage.html")

def randompage(request):
	entries = util.list_entries()
	entry = random.choice(entries)
	return render(request, "encyclopedia/randompage.html",{
		"entry": entry
		})