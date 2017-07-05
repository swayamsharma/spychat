from detail import spy,Spy,chat_message
from  steganography.steganography import Steganography
print 'hello'
#print command tells python whatever comes after it on screen.it can be written with single('') or double quotes(" ")
print "let\'s begin"
user=raw_input("continue as swayam or not(Y/N)")
if user.upper()=="Y":
    print "your details"
    spy.age=int(spy.age)
    spy.rating=float(spy.rating)
    #here i use space specifier in this %s act as string and %f act as float
    print "your name is %s. %s. Your age is %d.Your rating is %.2f.You are online"%(spy.salutation,spy.name,spy.age,spy.rating)
else:

    spy.name =raw_input("welcome to spychat,your name is :")
    # here i use string concatination by "+" symbol and " " is used for space purpose between two strings
    question = "Do you want to continue as " + " " + spy.name + " (Y/N)? "
    existing = raw_input(question)
# the len specifier defines the length of the string
    if len(spy.name)> 0:
        print " welcome " + spy.name
        #spy salutation is used for compairing purpose like gender(male or female)
        spy.salutation=raw_input("what we call you (mr or ms)")
        spy.name=spy.salutation + "" +spy.name
        spy.age = 0
        spy.rating = 0.0
        spy_is_online = False
#here i convert string into integer like spy.age = int(spy.age) and string also convert into float like spy.rating = float(spy.rating)
        spy.age = raw_input("What is your age?")
        print type(spy.age)
        spy.age=int(spy.age)
        if spy.age > 15 and spy.age < 70:
             # if condition is used for compairing purpose.if its condition satifies otherwise it print the object that we want to print by using else condition in end

            print ""
            show_menu = True
            spy.rating = raw_input("What is your spy rating?")
            spy.rating = float(spy.rating)
            if spy.rating > 4.5:
                print 'exellent rating'
            elif spy.rating > 3.5 and spy.rating <= 4.5:
                print 'good rating.'
            elif spy.rating >= 2.5 and spy.rating <= 3.5:
                print 'normal rating'
            else:
                print "you have low rating. we are always here to help you"
        ## elif condition is used for continuing if condition
            print " welcome user "+ spy.name + " age " + str(spy.age) + " your rating of " + str(spy.rating)
        else:
             print " invalid age "

spy_is_online=int(raw_input(" 1 for online" " 2 for offline"))
if (spy_is_online==1):
    print "user is online"
else:

    print "bye"
    exit()
# exit() condition is used for ending the upper condition and starting new condition

old_status=None
status=[]
#def stand for default by this condition we can be applicable to compare other condition with our condition like new_status ==1:print "hii"else: default old_status == None
def select_status(old_status):

    if old_status==None:
        print " No status "
    else:
        print " your current status is %s"%(old_status)
    choose=raw_input(" what you  want to do \n1.Add new status \n2.choose old status ")
    choose = int(choose)
    if choose ==1:
        new_status =raw_input("enter your status")
        if len(new_status)>0:
            print " status successfully updated"
            status.append(new_status)
            return new_status
        else:
            print "invalid status"
            #append condition is used for holding any condition we want

    elif choose ==2:
        position=1
        for x in status:
            print "%d.%s"%(position,x)
            position=position+1
        entry=int(raw_input("choose any one"))
        if entry <= len(status):
            new_status=status[entry-1]
            return new_status
    else:
        print "invalid entry"

friends=[]
def add_friend():
    new_friend=Spy("","",0,0.0)
    new_friend.name=raw_input("enter friend\'s name.")
    new_friend.salutation=raw_input("should i call u mr or ms")
    new_friend.age=int(raw_input("enter age"))

    new_friend.rating=float(raw_input("enter rating"))

    if len(new_friend.name)>0 and new_friend.age>15 and new_friend.age<70 and new_friend.rating>=spy.rating:
        friends.append(new_friend)
        print "friend successfully added"
    else:
        print "insufficient details"


def select_friends():
    position=1
    for friend in friends:
        print "%d.%s having age %d and rating %.2f is online"%(position,friend.name,friend.age,friend.rating)

        position=position+1
    select=int(raw_input("select your friend"))
    if select<=len(friends):
        return select-1
    else:
        print "wrong input"

def send_message():
    sender=select_friends()
    image=raw_input("enter image name:")
    output=raw_input("enter output path:")
    text=raw_input("enter your message:")

    Steganography.encode(image,output,text)
    print "your message ready."
    new_chat=chat_message(text,True)
    friends[sender].chat.append(new_chat)
    print "chat is stored"
    #steganography is used for creating a virtual environment such as time and image

def read_message():
    recieve=select_friends()
    rec=raw_input("enter image name:")
    hidden_msg=Steganography.decode(rec)

    print "message successfully recieved"
    send_by_me=False
    new=chat_message(hidden_msg,send_by_me)
    friends[recieve].chat.append(new)

def read_chat():
    read=select_friends()

    for chats in friends[read].chat:
        if chats.send_by_me:
            print '[%s] %s: %s' % (chats.time.strftime("%d %B %Y"), 'You said:', chats.text)

        else:
            print '[%s] %s said: %s' % (chats.time.strftime("%d %B %Y"), friends[read].name, chats.text)
            #here i use Strf which can used for time format
            # here i can create a menu bar


choice=1
while choice !=6:

    print " choose any one"
    print " 1.Add status \n2.Add friends \n3. send a message \n4. recieve a message\n 5.chat history \n6.exit "
    choice = raw_input(" select option ")
    choice=int(choice)

    if choice == 1:
        old_status=select_status(old_status)

    elif choice==2:
        add_friend()

    elif choice==3:
        send_message()

    elif choice==4:
        read_message()

    elif choice==5:
        read_chat()

    elif choice==6:
        exit()

    else:
        print "wrong input"

