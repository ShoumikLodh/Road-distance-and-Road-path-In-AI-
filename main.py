import nltk
#nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from pyswip import Prolog
import pandas as pd
import io
from pyswip import Functor, Variable, Query, call
import re
swipl = Prolog()


def format_text(text):
    text = text.lower()
   
    text = re.sub(r"([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", " ", text)
    
    text = re.sub(r'\s+', ' ', text)
    
    text=word_tokenize(text)
    return text


# print(df)

f = open("temp.pl", 'w')
f.truncate(0)

print('----------------------------------------------------------------------------------------------')
print('Electives Advisory System')
print('----------------------------------------------------------------------------------------------')
print('-----------By Shoumik Lodh - Roll no 2020407')
#take year input
x=input('What year are you currently studying in ? (1st , 2nd, 3rd, 4th or MTECH ?)\n')
x=format_text(x)

# print(x)
for g in x:
    if g == '1' or g =='first' or g =='1st':
        #f.write(f'year({x}).\n')
        f.write('year(1).\n')
        print('You cannot take any electives just yet')
        quit()
         
    elif g == '2' or g =='second' or g=='2nd':
        f.write('year(2).\n')
        break
    elif g== '3'or g =='third' or g=='3rd':
        f.write('year(3).\n')
        break
    elif g =='4' or g =='fourth' or g=='4th':
        f.write('year(4).\n')
        break
    elif g== 'mtech':
        f.write('year(5).\n')
        break
   


i=input("Please enter your interest :- math , sde , ai_ml , data_science , bio , cyber_sec , elec , ui_ux , eco , hum , psy , \n")
interest=format_text(i)
#print(interest)
for z in interest:
    if z == 'maths' or z =='mathematics' or z =='math':
        f.write(f'interest({"math"}).\n')
        break
    elif z == 'software' or z =='sde' :
        f.write(f'interest({"sde"}).\n')
        break
    elif z =='ai' or z =='ml' or z =='artificial' or z =='machine':
        f.write(f'interest({"ai_ml"}).\n')
        break
    elif z == 'data' or z =='science' :
        f.write(f'interest({"data_science"}).\n')
        break
    elif z == 'bio' or z =='biology':
        f.write(f'interest({"bio"}).\n')
        break
    elif z == 'cyber' or z =='security':
        f.write(f'interest({"cyber_sec"}).\n')
        break
    elif z == 'elec' or z =='electrical' or z =='electronics':
        f.write(f'interest({"elec"}).\n')
        break
    elif z == 'ui' or z =='ux' or z =='design' or z =='interface' or z =='designing':
        f.write(f'interest({"ui_ux"}).\n')
        break
    elif z == 'eco' or z =='economics' or z =='ecology':
        f.write(f'interest({"eco"}).\n')
        break
    elif z == 'hum' or z =='humanity' or z =='humanities':
        f.write(f'interest({"hum"}).\n')
        break
    elif z == 'psy' or z =='psychology' or z =='psycho' :
        f.write(f'interest({"psy"}).\n')
        break




l =input('what is your plan? Aiming for campus placements or Higher Studies?\n')
plans=format_text(l)
for p in plans :
    if p =='campus' or p =='placed' or p =='placement' or p=='placements' or p=='job' or p=='jobs':
        f.write('plans(1).\n')
        break

    elif p=='higher' or p=='studies' or p=='study' or p=='masters':
        f.write('plans(2).\n')
        break



i=input("If you have done a project enter topic :- math , sde , ai_ml , data_science , bio , cyber_sec , elec , ui_ux , eco , hum , psy \n or enter no \n")
proj=format_text(i)
#print(proj)
for z in proj:
    if z=='no' or z=='not' or z=='nope':
        f.write("extra(n).\n")
        break
    if z == 'maths' or z =='mathematics' or z =='math':
        f.write(f'projects({"math"}).\n')
        f.write("extra(y).\n")
        break
    elif z == 'software' or z =='sde' :
        f.write(f'projects({"sde"}).\n')
        f.write("extra(y).\n")
        break
    elif z =='ai' or z =='ml' or z =='artificial' or z =='machine':
        f.write(f'projects({"ai_ml"}).\n')
        f.write("extra(y).\n")
        break
    elif z == 'data' or z =='science' :
        f.write(f'projects({"data_science"}).\n')
        f.write("extra(y).\n")
        break
    elif z == 'bio' or z =='biology':
        f.write(f'projects({"bio"}).\n')
        f.write("extra(y).\n")
        break
    elif z == 'cyber' or z =='security':
        f.write(f'projects({"cyber_sec"}).\n')
        f.write("extra(y).\n")
        break
    elif z == 'elec' or z =='electrical' or z =='electronics':
        f.write(f'projects({"elec"}).\n')
        f.write("extra(y).\n")
        break
    elif z == 'ui' or z =='ux' or z =='design' or z =='interface' or z =='designing' or z=='user':
        f.write(f'projects({"ui_ux"}).\n')
        f.write("extra(y).\n")
        break
    elif z == 'eco' or z =='economics' or z =='ecology':
        f.write(f'projects({"eco"}).\n')
        f.write("extra(y).\n")
        break
    elif z == 'hum' or z =='humanity' or z =='humanities':
        f.write(f'projects({"hum"}).\n')
        f.write("extra(y).\n")
        break
    elif z == 'psy' or z =='psychology' or z =='psycho' :
        f.write(f'projects({"psy"}).\n')
        f.write("extra(y).\n")
        break

i=input("Is your CGPA above 8 or less than 8 \n")
gpa=format_text(i)
#print(gpa)
for g in gpa:
    if g=='less' or g=='lesser' or g=='lower' or g=='low' or g=='below' or g=='under':
        f.write("gpa(2).")
    elif g=='more' or g=='greater' or g=='above' or g=='bigger' or g=='higher':
        f.write("gpa(1).")
     


f.close()





