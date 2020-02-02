from tkinter import *


global guides
guides=[]

global users
users=[]

global places
places=[]

#name,district,latitude,longitude,rate_history
places=[["Kathmandu","Kathmandu",[27.7172, 85.3240],[3,4,3,4,3,4,3,4]],
    ["Pokhara Valley","Pokahara",[28.2096, 83.9856],[2,4,5,4,4,5]],
    ["Bhaktapur","Bhaktapur",[27.6710, 85.4298],[4,3,2,1]],
    ["Pashupatinath","Kathmandu",[27.7105, 85.3487],[5,1,4,3]],
    ["Boudhanath","Kathmandu",[27.7214, 85.3620],[5,4,2,1]],
    ["Nagarkot","Kathamndu",[27.7174, 85.5046],[3,4,5,1]],
    ["Lumbini","Rupandehi",[27.6792, 83.5070],[5,4,5,4,5,5]]
    [""]]

class guide:
    def __init__(self,name,address,age,email,passkey,position,skill,desp_ur,liscence_no,contact,sex,lang,busy,rating):
        self.name=name
        self.address=address
        self.email=email
        self.position=position
        self.skill=skill
        self.age=age
        self.desp_ur=desp_ur
        self.liscence_no=liscense_no
        self.contact=contact
        self.sex=sex
        self.lang=lang
        self.busy=busy
        self.rating=rating
        Add(self.name,self.address,self.email,self.position,self.skill,self.age,self.deep_ur,self.liscence,self.contact,self.sex,self.lang,self.busy,rating)        

    def Add(name,address,email,position,skill,desp_ur,liscence_no,contact,sex,lang,busy):
        if (len(name)!=0 and len(address)!=0 and age>17 and len(liscence_no)==12 and len(position)!=0 and len(contact)!=0 and rating<=5):
            #formally adding to the list
            guides.append([name,address,email,passkey,position,skill,desp_ur,liscence_no,contact,sex,lang,busy,rating])
            return ("A with "+str(name)+" was added")

class user:
    def __init__(self,name,address,age,email,passkey,position,skill,desp_ur,liscence_no,contact,sex,lang,busy):
        self.name=name
        self.address=address
        self.email=email
        self.passkey=passkey
        self.position=position
        self.skill=skill
        self.age=age
        self.desp_ur=desp_ur
        self.contact=contact
        self.sex=sex
        self.lang=lang
        self.busy=busy
        Add(self.name,self.address,self.email,self.passkey,self.position,self.skill,self.age,self.deep_ur,self.liscence,self.contact,self.sex,self.lang,self.busy)



class place:
    def __init__(self,name,district,latitude,longitude,rate):
        self.name=name
        self.district=disctrict
        self.longitude=longitude
        self.latitude=latitude
        self.history=rate
        self.rate=sum(rate)/len(rate)

    def getdistance(platlong,ulatlong)
