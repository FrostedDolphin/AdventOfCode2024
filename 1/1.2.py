#adventofcode01 


# step 1 - put numbers into two lists
# store data in a file called data.txt
file = "data.txt"

l1 = []
l2 = []

with open(file) as f:
    for number in f:
        n1,n2 = map(int, number.strip().split("   "))
        l1.append(n1)
        l2.append(n2)

#print(l1)
#print(l2)


# step 2 - sort the lists from least to greatest 

l1.sort()
l2.sort()

# step 3 - iterate throught l1 and search in l2 for the value and print how many times it exists
# then use that number in a formala to get a similarity score 
# simscore = item in l1 * number of times it appears in l2 

l3 = []
for item in l1: 
    count = l2.count(item)
    simscore = item * count
    l3.append(simscore)

# step 4 - add all the simscores together and print the result

print(sum(l3))
