#calculate avg temperature 
#DS - arrays/lists

numDays = int(input("Enter number of days"))
total = 0
tmp = []

for i in range(numDays):
    nxtDay = int(input(f"Enter Day {i}'s High temp:"))
    tmp.append(nxtDay)
    total += tmp[i]

avgtmp = round(total/numDays,2)
print("Average Temerature is: " + str(avgtmp))


count = 0
for i in tmp:
    if i > avgtmp:
        count += 1

print("Number of Days with above Average Temp: " +str(count))