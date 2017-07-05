from detail import spy,Spy,chat_message
from steganography.steganography import Steganography
print 'Hello'
#print command tells python whatever comes after it on screen.it can be written with single('') or double quotes(" ")
print "Let\'s Begin"
user=raw_input("Continue As swayam or Not(Y/N)")
if user.upper()=="Y":
    print "Your Details"
    spy.age=int(spy.age)
    spy.rating=float(spy.rating)
    #here i use space specifier in this %s act as string and %f act as float
    print "your name is %s. %s. your age is %d.your rating is %.2f.you are online"%(spy.salutation,spy.name,spy.age,spy.rating)
else:

    spy.name =raw_input("Welcome to SpyChat,Your Name is.")
    # here i use string concatination by "+" symbol and " " is used for space purpose between two strings
    question = "Do You Want To Continue As " + " " + spy.name + " (Y/N)? "
    existing = raw_input(question)
# the len specifier defines the length of the string
    if len(spy.name)> 0:
        print " Welcome " + spy.name
        #spy salutation is used for compairing purpose like gender(male or female)
        spy.salutation = raw_input("What We Call You ? Mr or Ms")
        spy.name = spy.salutation + "" +spy.name
        spy.age = 0
        spy.rating = 0.0
        spy_is_online = False
#here i convert string into integer like spy.age = int(spy.age) and string also convert into float like spy.rating = float(spy.rating)
        spy.age = raw_input("What is your Age?")
        print type(spy.age)
        spy.age=int(spy.age)
        if spy.age > 15 and spy.age < 70:
             # if condition is used for compairing purpose.if its condition satifies otherwise it print the object that we want to print by using else condition in end

            print ""
            show_menu = True
            spy.rating = raw_input("What is your Spy Rating?")
            spy.rating = float(spy.rating)
            if spy.rating > 4.5:
                print 'Exellent Rating.'
            elif spy.rating > 3.5 and spy.rating <= 4.5:
                print 'Good Rating.'
            elif spy.rating >= 2.5 and spy.rating <= 3.5:
                print 'Normal Rating.'
            else:
                print "You have Low Rating. We are always here to help you."
        # elif condition is used for continuing if condition
            print " Welcome User " + spy.name + " Age " + str(spy.age) + " Your Rating of " + str(spy.rating)
        else:
            print " Invalid Age. "

spy_is_online=int(raw_input(" 1 for Online " " 2 for Offline"))
if (spy_is_online==1):
    print "User is Online."
else:

    print "Bye."
    exit()
# exit() condition is used for ending the upper condition and starting new condition

old_status = None
status = []
def select_status(old_status):

#def stand for default by this condition we can be applicable to compare other condition with our condition like new_status ==1:print "hii"else: default old_status == None

    if old_status == None :
        print " No Status. "
    else:
        print " Your Current Status is %s"%(old_status)
    choose = raw_input(" What You  Want to do  \n1.Add new status \n2.Choose old status ")
    choose = int(choose)
    if choose == 1:
        new_status = raw_input("Enter Your Status:-")
        if len(new_status) > 0:
            print " Status Successfully Updated."
            status.append(new_status)
            return new_status
        else:
            print "Invalid Status."
            #append condition is used for holding any condition we want

    elif choose == 2:
        position = 1
        for x in status:
            print "%d.%s"%(position,x)
            position = position+1
        entry = int(raw_input("Choose Any One."))
        if entry <= len(status):
            new_status=status[entry-1]
            return new_status
    else:
        print "Invalid Entry."

friends=[]
def add_friend():
    new_friend = Spy("","",0,0.0)
    new_friend.name = raw_input("Enter Friend\'s Name:-")
    new_friend.salutation = raw_input("Should I Call You (Mr or Ms)")
    new_friend.age = int(raw_input("Enter Age."))

    new_friend.rating = float(raw_input("Enter Rating."))

    if len(new_friend.name) > 0 and new_friend.age > 15 and new_friend.age < 70 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print "Friend Successfully Added."
    else:
        print "InSufficient Details."


def select_friends():
    position = 1
    for friend in friends:
        print "%d.%s having Age %d and Rating %.2f is Online"%(position,friend.name,friend.age,friend.rating)

        position = position+1
    select = int(raw_input("Select Your Friend."))
    if select <= len(friends):
        return select-1
    else:
        print "Wrong Input."

def send_message():
    sender = select_friends()
    image = raw_input("Enter Image Name:-")
    output = raw_input("Enter Output Path:-")
    text = raw_input("Enter Your Message:-")

    Steganography.encode(image,output,text)
    print "Your Message is Ready to Send."
    new_chat = chat_message(text,True)
    friends[sender].chat.append(new_chat)
    print "Chat Is Stored."
    #steganography is used for creating a virtual environment such as time and image

def read_message():
    recieve = select_friends()
    rec = raw_input("Enter Image Name:-")
    hidden_msg = Steganography.decode(rec)

    print " Message Recieved Successfully "
    send_by_me = False
    new = chat_message(hidden_msg,send_by_me)
    friends[recieve].chat.append(new)

def read_chat():
    read = select_friends()

    for chats in friends[read].chat:
        if chats.send_by_me:
            print '[%s] %s: %s' % (chats.time.strftime("%d %B %Y"), 'You said:', chats.text)

        else:
            print '[%s] %s said: %s' % (chats.time.strftime("%d %B %Y"), friends[read].name, chats.text)
            #here i use Strf which can used for time format
            # here i can create a menu bar


choice = 1
while choice != 6:

    print " choose any one"
    print " 1.Add Status \n2.Add Friends \n3. Send a Message \n4. Recieve a Message\n 5.Chat History \n6.Exit "
    choice = raw_input(" Select Option. ")
    choice = int(choice)

    if choice == 1:
        old_status=select_status(old_status)

    elif choice == 2:
        add_friend()

    elif choice == 3:
        send_message()

    elif choice == 4:
        read_message()

    elif choice == 5:
        read_chat()

    elif choice == 6:
        exit()

    else:
        print "Wrong Input."

