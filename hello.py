import random


eligible_signs = "abcdefghijklmnopqrstuvwxyz1234567890!§$%&()"
eligible_signs_list = list(eligible_signs)
random.shuffle(eligible_signs_list)
eligible_signs = "".join(eligible_signs_list)
eligible_signs = eligible_signs[0:15]
print(eligible_signs)







