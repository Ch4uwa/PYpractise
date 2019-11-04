# 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

with open('p022_names.txt') as f:
    fl = f.readlines()
    n = fl[0].split(",")
    n = sorted(n)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_value = {}

for i in range(len(alphabet)):
    letter_value[alphabet[i]] = i+1

name_score = 0

for i in range(len(n)):
    tmp_score = 0
    for j in range(1, len(n[i])-1):
        tmp_score += letter_value[n[i][j]]
    name_score += tmp_score*(i+1)

print('Total score of all names in list: ', name_score)
