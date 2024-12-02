#adventofcode01.1

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

#  step 3 - return the absolute value of the difference between the two lists
 
l3 = []

for a,b in zip(l1,l2):
    l3.append(abs(a-b))


# step 4 - add the differences together

print(sum(l3))
