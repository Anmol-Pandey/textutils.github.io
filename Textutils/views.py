

# Views.py
# I have created this file - Anmol
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")





def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')



def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
        
    elif fullcaps == "on":
        analyzed=""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and char !="\r" :
                analyzed = analyzed+char
        params = {'purpose':  'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    elif extraspaceremover == "on":
        analyzed=""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char


        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)


    elif charcount == "on":
        analyzed = ""
        for char in djtext:
            analyzed = str(len(djtext))
        params = {'purpose': 'Charactors in your given text', 'analyzed_text': "Number of charactors in ypur given text::"+analyzed}
        

    if removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and charcount!="on":
        return render(request, 'Error.html')

    return render(request, 'analyze.html', params)