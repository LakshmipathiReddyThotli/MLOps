from OOPs_Demo import chatbook

obj = chatbook()


# getter and setter methods
print(obj.get_private())
obj.set_private("Lakhsmipathi")
print(obj.get_private())

# Demonstration of static methods 
user1 = chatbook()
print(user1.id)

chatbook.set_id(10)
user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)