
from datetime import datetime
class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name=name
        self.salutation=salutation
        self.age=age
        self.rating=rating
        self.chat=[]
        self.is_status=True


class chat_message:
    def __init__(self,text,send_by_me):
        self.text=text
        self.time=datetime.now()
        self.send_by_me=send_by_me


spy=Spy("Swayam","Mr.","23","4.0")
