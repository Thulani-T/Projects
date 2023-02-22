
data = '0010101011111111'
print('Input bit:'+data)
lst = []
binLst = []
count = 0
 
for letter in data:
    lst.append(letter)
    
#check region 1
for x in range(1, 16, 2):
    if lst[x]=='1':
        count = count+1

bin1 = count%2
binLst.append(bin1)

#check region 2
count=0
if lst[2]=='1':
    count = count+1
    
if lst[3]=='1':
    count = count+1
    
if lst[6]=='1':
    count = count+1
    
if lst[7]=='1':
    count = count+1
    
if lst[10]=='1':
    count = count+1
    
if lst[11]=='1':
    count = count+1
    
if lst[14]=='1':
    count = count+1
    
if lst[15]=='1':
    count = count+1

bin2 = count%2
binLst.append(bin2)

#check region 3
count = 0
for x in range(4, 8):
    if lst[x]=='1':
        count = count+1
for x in range(12, 16):
    if lst[x]=='1':
        count = count+1

bin3 = count%2
binLst.append(bin3)

#check region 4
count=0
for x in range(8, 16):
    if lst[x]=='1':
        count = count+1
bin4 = count%2
binLst.append(bin4)

# Converting integer list to string list
s = [str(i) for i in binLst]
     
# Join list items using join()
res = int("".join(s))

decimalNumber = (binLst[0]*pow(2,0))+(binLst[1]*pow(2,1))+(binLst[2]*pow(2,2))+(binLst[3]*pow(2,3))

# declaring an empty list
fixedData = []
fixedBit = ''

# creating a clone using a loop
for i in data:
    fixedData.append(i)
    
if decimalNumber!=0:
    if fixedData[decimalNumber]=='0':
        fixedData[decimalNumber]='1'
         
    elif fixedData[decimalNumber]=='1':
        fixedData[decimalNumber]='0'
        
print('Fixed bit:')
if decimalNumber==0:
    for i in fixedData:
        fixedBit = fixedBit+i
    print(fixedBit)
    print('There are no corrupted bits.')
else:
    for i in fixedData:
        fixedBit = fixedBit+i
    print(fixedBit)
    print("The corrupted bit is in: "+str(decimalNumber))

