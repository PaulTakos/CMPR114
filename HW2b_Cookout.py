guests = int(input('Enter the number of guests: '))
hotdogs_per = int(input('Enter the number of hotdogs each guest eats: '))

# calculates how many bags of hotdogs needed
hotdogs_total = guests * hotdogs_per
if hotdogs_total % 10 == 0:
    hotdogs_bags = int(hotdogs_total / 10)
    hotdogs_remain = 0
else:
    hotdogs_bags = int(hotdogs_total / 10) + 1
    hotdogs_remain = 10 - (hotdogs_total % 10)

# calculates how many bags of hotdog buns needed
if hotdogs_total % 8 == 0:
    buns_bags = int(hotdogs_total / 8)
    buns_remain = 0
else:
    buns_bags = int(hotdogs_total / 8) + 1
    buns_remain = 8 - (hotdogs_total % 8)

print('You need', hotdogs_bags, 'bags of hotdogs and', buns_bags, 'bags of buns.')
print('You have', hotdogs_remain, 'remaining hotdogs and', buns_remain, 'remaining buns.')