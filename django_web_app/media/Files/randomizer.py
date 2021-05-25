# Created by Yesh Jadav #

#A randomizer for secret santa

from random import choice
from time import sleep


giver_list = ["Shishir","Janhavi","Maheshwari","Amog","Parnika","Chandrika","Mourya","Nikhil","Manvith","Ritvik","Nishank","Susan","Yashwanth","Harsha","Khushi","Vishnu Priya","Parthiv","Nityanth","Aniket","Avinash","Kundana","Alekhya","Pushpa Hasini","Meghana","Charan","Karthika","Kaushal","Rishika","Akanksh Shalem","Neeharika","Dhruti","Vidya","Pragnya Jabili","Shanti","Deepak","Sahith","Dushyant","Havish","Abhignya","Eekshitha","Kowshik","Akhil","Mijith","Siddhi","Harini","Srikar","Dhanush","Harshini","Tejasri","Likitha","Srija"]
receiver_list = ["Shishir","Janhavi","Maheshwari","Amog","Parnika","Chandrika","Mourya","Nikhil","Manvith","Ritvik","Nishank","Susan","Yashwanth","Harsha","Khushi","Vishnu Priya","Parthiv","Nityanth","Aniket","Avinash","Kundana","Alekhya","Pushpa Hasini","Meghana","Charan","Karthika","Kaushal","Rishika","Akanksh Shalem","Neeharika","Dhruti","Vidya","Pragnya Jabili","Shanti","Deepak","Sahith","Dushyant","Havish","Abhignya","Eekshitha","Kowshik","Akhil","Mijith","Siddhi","Harini","Srikar","Dhanush","Harshini","Tejasri","Likitha","Srija"]

dictionary = {}

print("Loading, please wait...")
sleep(5)
print("Starting to randomize...")
sleep(5)
print("Randomizing complete. Getting names now...")
sleep(2)

def randomizer():
    
    for giver in giver_list:

        def chooser():
            global receiver
            receiver = choice(receiver_list)
            if giver == receiver:
                chooser()
            else:
                pass

        chooser()
        receiver_list.remove(receiver)

        dictionary[giver] = receiver

randomizer()

print("Giver  :  Receiver")
for i in dictionary:
    print("{}  :  {}".format(i,dictionary[i]))
    sleep(0.1)