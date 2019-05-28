from django.shortcuts import render

# Create your views here.
from searching import main

def index(request):
    return  render(request,'index.html')

def result(request):
    if request.method == 'POST':
        query = request.POST['input_text']
        result,resultatas,all_tokens,tokens_doc, query, queries,weight, proximity_index = main.main(query)
        content = {'result':result, 'query': query, 'resultatas' : resultatas, 'all_tokens': all_tokens, 'tokens_doc':tokens_doc, 'query': query, 'queries':queries, 'weight':weight, 'proximity_index':proximity_index}

    return render(request,'result.html',content)
