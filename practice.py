
def hello():
    print("greetings user!")


def pack(user1, user2, user3):
    return [user1, user2, user3]

def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

hello()
print(pack("user1","user2","user3"))
lunch_items = ['chips', 'turkey', 'cheesesticks']
eat_lunch(lunch_items)