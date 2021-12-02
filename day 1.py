file = open(__file__[:-2]+"txt", "r")
input = file.readlines()

print(sum(1 for i in range(len(input)-1) if int(input[i]) < int(input[i+1])))

print(sum(1 for i in range(len(input)-3) if int(input[i])+int(input[i+1])+int(input[i+2]) < int(input[i+1])+int(input[i+2])+int(input[i+3])))