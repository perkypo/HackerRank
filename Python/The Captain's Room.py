# Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms. 
# One fine day, a finite number of tourists come to stay at the hotel.
# The tourists consist of:
#   A Captain.
#   An unknown group of families consisting of K members per group where K ≠ 1.
# 
# The Captain was given a separate room, and the rest were given one room per group.
# Mr. Anant has an unordered list of randomly arranged room entries. The list consists of 
# the room numbers for all of the tourists. The room numbers will appear K times per group 
# except for the Captain's room.
# 
# Mr. Anant needs you to help him find the Captain's room number. 
# The total number of tourists or the total number of groups of families is not known to you.
# You only know the value of K and the room number list.

K = int(input())
room_numbers = list(map(int, input().split()))
for i in set(room_numbers):
    if(room_numbers.count(i) != K ):
        print(i)

# OR

K = int(input())
room_numbers = list(map(int, input().split()))
unique_set = set() #unique number set
repetitive_set = set() #repititive number set
for i in room_numbers:
    if(i in unique_set):
        repetitive_set.add(i)
    else:
        unique_set.add(i)

captain_room=list(unique_set.difference(repetitive_set))
print(captain_room[0])