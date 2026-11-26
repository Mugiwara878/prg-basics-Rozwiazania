from stadium_c import C

stadium = C({"A":120, "D":150, "G":90, "K":110})
stadium.m1("G", 130)
print(stadium.m2("GD"))    # 280
print(stadium.m2("KEJ"))   # 110
