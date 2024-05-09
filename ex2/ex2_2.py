# open the file and read the data
f = open("id.txt", "r")
data = f.readlines()
# delete the '\n' in the end of each line
data = [i.strip() for i in data]
# delete the last data idk why it's there
data.pop()
sum = 0
for i in data:
    sum += int(i)
    
# close the file
f.close()

# open the file, create it if it doesn't exist
f = open("result.txt", "w")
f.write(str(sum))

# close the file
f.close