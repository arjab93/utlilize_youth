from flask import Flask,render_template,request,redirect
app=Flask(__name__)

#posts=['nirjal','bikram','jell']


import pyttsx3
import wikipedia
import threading

s=pyttsx3.init()

global guides
guides=[]

global users
users=[]

global places
places=[]

global msgpool
msgpool=[]

#name,district,latitude,longitude,rate_history
class guide:
    def __init__(self,name,address,age,email,passkey,position,skill,desp_ur,liscence_no,contact,sex,lang,busy,rating):
        self.name=name
        self.address=address
        self.email=email
        self.passkey=passkey
        self.position=position
        self.skill=skill
        self.age=age
        self.desp_ur=desp_ur
        self.liscence=liscence_no
        self.contact=contact
        self.sex=sex
        self.lang=lang
        self.busy=busy
        self.rating=rating
        guide.Add(self.name,self.address,self.email,self.position,self.skill,self.passkey,self.age,self.desp_ur,self.liscence,self.contact,self.sex,self.lang,self.busy,self.rating)

    def Add(name,address,email,position,skill,passkey,age,desp_ur,liscence,contact,sex,lang,busy,rating):
        if (len(name)!=0 and len(address)!=0 and int(age)>17 and len(liscence)>8 and len(position)!=0 and len(contact)!=0):
            print('true')
            guides.append([name,address,email,position,skill,age,desp_ur,liscence,contact,sex,lang,busy,rating])
            return ("A with "+str(name)+" was added")

class user:
    def __init__(self,name,address,age,email,passkey,desp_ur,contact,sex,lang):
        self.name=name
        self.address=address
        self.email=email
        self.passkey=passkey
        self.age=age
        self.desp_ur=desp_ur
        self.contact=contact
        self.sex=sex
        self.lang=lang
        user.Add(self.name,self.address,self.email,self.passkey,self.age,self.desp_ur,self.contact,self.sex,self.lang)

    def Add(name,address,email,passkey,age,desp_ur,contact,sex,lang):
        if (len(name)!=0 and len(address)!=0 and int(age)>17 and len(contact)!=0):
            #formally adding to the list
            users.append([name,address,email,passkey,age,desp_ur,contact,sex,lang])
            print ("A block was added with \n")
            #print (users[(len(users)-1)]) 
        else:
            raise Exception


class place:
    def __init__(self,name,district,latitude,longitude,rate,tag,username):
        self.name=name
        self.district=district
        self.longitude=longitude
        self.latitude=latitude
        self.history=rate
        self.rate=round(sum(rate)/len(rate),2)
        self.tag=tag
        self.username=username
        place.Add(self.name,self.district,self.longitude,self.longitude,self.history,self.rate,self.tag,self.username)

    def isValid(username):
        for user in users:
            
            if user[0]==username:
                return True
        
        return False

    def Add(name,district,latitude,longitude,history,rate,tag,username):
        if (latitude!=0 and longitude!=0 and name!="0" and place.isValid(username)):
            places.append([name,district,latitude,longitude,history,rate,tag,username])
            return True
        else:
            raise Exception

    def getwikipediainfo(query):
        sum1=wikipedia.summary(query,sentences=1)
        sum2=wikipedia.summary(query)
        #tospeak is sum1,to print is sum 2
        query=wikipedia.page(query).title
        return([sum1,sum2,query])
    
    def getdistance(platlong,ulatlong):
        ux=float(ulatlong[0])
        uy=float(ulatlong[1])
        px=float(platlong[0])
        py=float(plytlong[1])
        distance=((ux-px)^2+(uy-py)^2)^(1/2)
        return distance

def speak(x):
    print(x)
    s.say(x)
    s.runAndWait()

#place.getwikipediainfo("Lumbini")



#name,address,age,email,passkey,desp_ur,liscence_no,contact,sex,lang,busy
user("Harry","London","19","harrydon@gmail.com","harrylovespreeti","i am harry from wonderland","harry's contact","m",["japanese","bhutanese","english"])

user("Nirjal","London","19","nirjal@gmail.com","nirjalrocks","i am harry from wonderland","harry's contact","m",["japanese","bhutanese","english"])

user("Carry","Houston","29","carrym@gmail.com","helloworld","i am a good boy","carry's contact","m",["french","english"])

user("Lauren","Kameski","19","lauren1@gmail.com","mercyplease","kindful to all","lauren's contact","f",["korean","chinese","english"])

user("Samira","Kaski","34","samirpok@gmail.com","samirkills","i love everyone","samira's contact","f",["japanese","chinese","nepalese"])



#self,name,address,age,email,passkey,position,skill,desp_ur,liscence_no,contact,sex,lang,busy,rating)

guide("Pratap","patan",19,"pratappokheral@gmail.com",'pratap_rocks','driver','10 +2','pratap is a lonely boy','890890890890','9841123456','m',['hindi','bhojpuri','french'],False,'4')
guide("Hiptap","pokhara",19,"hittappokheral@gmail.com",'hittaprocks','retired officer','masters','mero desh mero nepal','123123123123','9841823456','m',['hindi','english','french'],False,'4.3')
guide("hittap","pokhara",19,"hittappaudel@gmail.com",'hittaprockz','coffee maker','masters','mero desh mero country','123123123123','9848823456','m',['hindi','jeum','french'],False,'4.3')

#self,name,district,latitude,longitude,rate,tag
place("Butwal","Rupandehi",27.6866, 83.4323,[3,4,3,2,1],['park','lumbini'],"Nirjal")
place("Nagarkot","Kathamndu",27.7174, 85.5046,[3,4,5,1],['cycling','photography','adventure','sight seeing'],"Nirjal")
place("Lumbini","Rupandehi",27.6792, 83.5070,[5,4,5,4,5,5],['cycling','photography','buddhism','sight seeing'],"Nirjal")
place("Boudhanath","Kathmandu",27.7214, 85.3620,[5,4,2,1],['religious','spirituality','photography'],"Nirjal")
links=['butwal','nagarkot','lumbini','boudhanath']


'''


  def getwikipediainfo(query):
        sum1=wikipedia.summary(query,sentences=1)
        sum2=wikipedia.summary(query)
        #tospeak is sum1,to print is sum 2
        query=wikipedia.page(query).title
        return([sum1,sum2,query])
    

'''

#displayplace('Barhabise')

@app.route('/signup_guide/', methods=['post', 'get'])
def signup_guide():
    message = 'GUIDES MUST PROVIDE VALID INFORMATION'
    if request.method == 'POST':
        name = request.form.get('username')
        address = request.form.get('address')
        age = request.form.get('age')  
        email = request.form.get('email_address')
        passkey=request.form.get('passkey')  
        desp_ur=request.form.get('desp_ur')
        skill=request.form.get('skill')
        position=request.form.get('position')
        licence_no=request.form.get('licence_no')
        contact=request.form.get('contact')
        sex=request.form.get('sex')
        lang=request.form.get('lang')
        lang=str(lang).split(",")
        print(name,address,email,position,skill,passkey,age,desp_ur,licence_no,contact,sex,lang,False,2.5)
            
        try:
            guide.Add(name,address,email,position,skill,passkey,age,desp_ur,licence_no,contact,sex,lang,False,2.5)
        
        except:
            print("\n \n ")
            print("ERROr OCCURED")
            message=message+"ERRROR IN THE ENTERED DATA"  


    return render_template('guide_signup.html', message=message)


#add(name,district,latitude,longitude,history,rate,tag)
@app.route("/addplace/",methods=['post','get'])
def addplace():
    message="Enter a place"
    if request.method == 'POST':
        name = request.form.get('username')
        district = request.form.get('address')
        latitude =request.form.get('latitude') 
        longitude = request.form.get('longitude')
        username=request.form.get('userkoname')
        rates=[0,0,0,0]  
        rate=round(sum(rates)/len(rates),2)
        tags=request.form.get('tags')
        tags=tags.split(',')
        print((name,district,latitude,longitude,rate,tags,username))
        
        try:
            print((name,district,latitude,longitude,rates,rate,tags,username))
            place.Add(name,district,latitude,longitude,rates,rate,tags,username)            
        
        except Exception as e :
            print (e)
            print("\n")
            print("ERROr OCCURED")
            message=message+"ERRROR IN THE ENTERED DATA"  
    
    return render_template('enterplace.html', message=message)


@app.route('/signup_user/', methods=['post', 'get'])
def signup_user():
    message = 'USERS MUST PROVIDE VALID INFORMATION'
    if request.method == 'POST':
        name = request.form.get('username')
        address = request.form.get('address')
        age = request.form.get('age')  
        email = request.form.get('email_address')
        passkey=request.form.get('passkey')  
        desp_ur=request.form.get('desp_ur')
        contact=request.form.get('contact')
        sex=request.form.get('sex')
        lang=request.form.get('lang')
        lang=str(lang).split(",")
        try:
            print((name,address,email,passkey,age,desp_ur,contact,sex,lang))
            user.Add(name,address,email,passkey,age,desp_ur,contact,sex,lang)
            
            
        except:
            print("ERROr OCCURED")
            message=message+"ERRROR IN THE ENTERED DATA"  
    return render_template('user_signup.html', message=message)


@app.route("/butwal")
def butwal():
    wiki=place.getwikipediainfo("butwal")
    x=wiki[0]
    sum_2_print=wiki[1]
    body=sum_2_print
    head=wiki[2]
    threading.Thread(name="get",target=speak,args=(x,)).start()
    return render_template("desp.html",body=body,head=head)


@app.route("/nagarkot")
def nagarkot():
    wiki=place.getwikipediainfo("nagarkot")
    x=wiki[0]
    sum_2_print=wiki[1]
    body=sum_2_print
    head=wiki[2]
    threading.Thread(name="get",target=speak,args=(x,)).start()
    return render_template("desp.html",body=body,head=head)

global useris
useris=[]



#guide("Pratap","patan",19,"pratappokheral@gmail.com",'pratap_rocks','driver','10 +2','pratap is a lonely boy','890890890890','9841123456','m',['hindi','bhojpuri','french'],False,'4')


@app.route('/msgpool',methods=['post','get'])
def pool():
    i=0
    if request.method == 'POST':
        if (request.form.get('Yes') == 'Yes'):
            msgpool.remove(msgpool[i])

    
    for place in msgpool:
        i=i+1
        return render_template("msgpool.html",place=place)   



for place in places:
    if (place[5]==0):
        msgpool.append([place])


# if request.form.get('Encrypt') == 'Encrypt':

@app.route("/lumbini")
def lumbini():
    wiki=place.getwikipediainfo("lumbini")
    x=wiki[1]
    head=wiki[2]
    sum_2_print=wiki[0]
    threading.Thread(name="get",target=speak,args=(x,)).start()
    body=sum_2_print
    return render_template("desp.html",body=body,head=head) 


@app.route("/boudhanath")
def boudhanath():
    wiki=place.getwikipediainfo("boudhanath")
    x=wiki[1]
    sum_2_print=wiki[0]
    body=sum_2_print
    head=wiki[2]
    threading.Thread(name="get",target=speak,args=(x,)).start()
    return render_template("desp.html",body=body,head=head)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def abt():
    return render_template('home.html')

if __name__=="__main__":
    app.run(debug=True)