from  django.http import HttpResponse
from  django.shortcuts import render
def home(request):
    return render(request,'home.html')

def count(request):
    r=request.GET['文本']
    dict={}
    for i in r:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    k=sorted(dict.items(),key=lambda x:x[1],reverse=True)
    return render(request,'count.html',{'text':r,'key_dict':k})