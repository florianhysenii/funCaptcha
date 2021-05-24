input_value = input("Please enter path: \n")
# file = open("C:\\Users\\flori\\OneDrive\\Desktop\\cvv.txt", "r")
# file = open("C:\\Users\\flori\\OneDrive\\Desktop\\cvv.txt", "r")
num_inter = 0
i = 0
index = 0
cvv = 0
for line in file:
    fields = line.split(":")
    card = fields[0]
    month = fields[1]
    year = fields[2]
    print(card + ':' + month + ':' + year)
    for index in range(999):
        index = index+1
        cvv = index
        print(card + ':' + month + ':' + year + ':')
        print(cvv)
file.close()