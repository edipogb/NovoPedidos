from django.shortcuts import render
from django.http import HttpResponse
import gspread

gc = gspread.service_account(filename='service_account.json')
sh = gc.open_by_key('1KWwSQgz9cQV3Pcjboq97sKak_L2AWbuC0YiaLuyfLcI')


# Create your views here.
def home(request):
    worksheet = sh.worksheet("DADOS")
    data={}
    data['values']=worksheet.get_all_records()
    return render(request, 'index.html')
    #return HttpResponse(worksheet.acell('B5').value)
