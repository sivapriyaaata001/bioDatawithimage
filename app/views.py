from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def bioData(request):
    return HttpResponse('''<h1>I am sivapriya</h1>
                          <i>I am from Andhrapradesh</i>
                          <div><img align="center" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrhbE_z4qEXDE_AVInfdBA8_xHOWNFb3Q3ew&s" alt="">
                          <img height=200px width=200px src="https://cdn.pixabay.com/photo/2023/07/24/07/24/flower-wallpaper-8146421_960_720.png"></div>
                          <div><b>I have done my post graduation</b></div>''')