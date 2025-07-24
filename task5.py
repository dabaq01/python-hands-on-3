"""
    You're cleaning up your phone's contact list and organizing your close friends from Jos.
    Your friends list is: friends = ["Aisha", "Daniel", "Esther", "John", "Mary", "Paul", "Ruth"]
    
    1. You made a new close friend "Kemi" and want to add her between "John" and "Mary".
    2. "Daniel" moved to Lagos and you don't talk anymore, so remove him from your close friends list.
    3. "Aisha" got married and now goes by "Aisha_M". Update her name in the list.
    4. You want to add your cousin "Zainab" at the end of the list.
    5. Create a new list with only the first 3 friends from your updated list and display it.
    6. Find out what position "Paul" is in your final friends list (remember: position counting starts from 1 for humans!).
    7. arrange your contacts in Descending Alphabetical Order using.
"""
#cleaning up your phone's contact list 
friends = ["Aisha", "Daniel", "Esther", "John", "Mary", "Paul", "Ruth"]
#add "Kemi" between "John" and "Mary"
friends.insert(4, "Kemi")
print (friends)
#remove "Daniel"
friends.remove(friends[1])
print (friends)
#Update "Aisha" to "Aisha_M"
friends[0] = ("Aisha_M")
print (friends)
#add "Zainab" at the end of the list
friends.append("Zainab")
print (friends)
#Create a new list with only the first 3 friends from your updated list and display it
newFriends = friends[0:3]
print (newFriends)
#what position is "Paul" in on your final friends list
paulPosition = friends.index("Paul")
print (f"Paul's position on the contacts list is number:", paulPosition)
#arrange your contacts in Descending Alphabetical Order
friends.sort(reverse=True)
print (f"the contacts list in descending order is:", friends)
