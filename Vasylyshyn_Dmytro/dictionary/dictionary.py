Days = { 1:'Mon', 2:'Tue', 3:'Wed',
         4:'Thu', 5:'Fri', 6:'Sat', 7:'Sun' }


day = int(input("Enter day: "))

try:
    print('day = ', Days[day])
except KeyError:
    print('2. Using try-except statement: Error.')

Days[1]="monday"
print(Days)
Days.pop(1)
print(Days)
