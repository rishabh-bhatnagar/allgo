from django.shortcuts import render
import pandas as pd
# Create your views here.
from django.http import HttpResponse
df = pd.read_csv('students.csv')
cols = list(df.columns)

def index(request):
	return render(request, "index.html")


def add_new(request):
	if request.method == "POST":
		df = pd.read_csv('students.csv')
		sid = request.POST.get('sid')
		sname = request.POST.get('sname')
		gender = request.POST.get('gender')
		dob = request.POST.get('dob')
		city = request.POST.get('city')
		state = request.POST.get('state')
		
		merit = request.POST.get('qual')
		stream = request.POST.get('stream')
        
		df.loc[str(len(df))] = [sid, sname, gender, dob, city, state,  merit, stream]
		df.to_csv('students.csv', index = False)
		
		check = 'Data has been saved'
		return render(request, "add_new.html", {'check': check})
	return render(request, "add_new.html")


def search(request):
	if request.method == 'POST':
		df = pd.read_csv('students.csv')
		sid = request.POST.get('sid')
		print("-----------------WORKING----------------")
		

		try :
			ans = df.loc[(df.StudentID == int(sid))].values.tolist()[0]
		
			mylist = zip(cols, ans)
			context = {
	            'mylist': mylist,
	        }

			return render(request, 'search_student.html', context)
		except IndexError:

			return  HttpResponse('<h1><center>DATA NOT FOUND</center></h1>')
	return render(request, "search_student.html")

def display(request):
	df = pd.read_csv('students.csv')
	text = ''
	for i in range(len(df)):
		text += str(i)
		
	return render(request, "display.html", {'df': df.to_html(), 'length': text})
	
	
