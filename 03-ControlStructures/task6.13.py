facebook = True
twitter = False
instagram = True
good_influ = 0

if facebook == True:
    good_influ += 1
if twitter == True:
    good_influ += 1
if instagram == True:
    good_influ += 1

if good_influ >= 2:
    print("You are a good influencer!")
else:
    print("Ugh..")
