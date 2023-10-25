import random;
def xor(a, b):

	result = []
	for i in range(1, len(b)):
		if a[i] == b[i]:
			result.append('0')
		else:
			result.append('1')

	return ''.join(result)


def crcdiv(dividend, divisor):

	pick = len(divisor)
	tmp = dividend[0: pick]
	while pick < len(dividend):
		if tmp[0] == '1':
			tmp = xor(divisor, tmp) + dividend[pick]
		else: 
			tmp = xor('0'*pick, tmp) + dividend[pick]

		pick += 1

	if tmp[0] == '1':
		tmp = xor(divisor, tmp)
	else:
		tmp = xor('0'*pick, tmp)

	checkword = tmp
	return checkword

def bin_to_dec(bin_no):
	res = 0
	j =0
	for i in range (len(bin_no)-1,0,-1):
		res += int(bin_no[i])* (2**j)
		j+=1
	res += int(bin_no[0])*(2**j)
	return res

def encodeData(data, key):

	l_key = len(key)

	appended_data = data + '0'*(l_key-1)
	print("Dividend: ", appended_data)

	remainder = crcdiv(appended_data, key)

	codeword = data + remainder

	print("\n************AFTER CRC*************\n")
	
	
	final_rem = crcdiv(codeword, key)
	print("final_rem: ", final_rem)

	print("\nRemainder : ", remainder)
	print("Encoded Data (Data + Remainder) : ",codeword)

	if (final_rem != "000"):
		print("Syndrome is  not 0, CRC Fail, ERROR DETECTED")
		print(data)
		original_data = bin_to_dec(data)
		print(original_data)
		print("Decoded data: ", chr(original_data) )
	else:
		print("Syndrome is 0, CRC Passed, NO ERROR DETECTED")
		
		error = input("\nDo you want to induce an error (y/n): ")
		
		if error =='y':
			random_position = random.randint(0, len(data)-1)
			l_data = list(data)
			
			if (l_data[random_position]== '1'):
				l_data[random_position] = '0'
			else:
				l_data[random_position] = '1'

			
			# New data after inducing

			new_data = ""
			for i in range( len(l_data)):
				new_data += l_data[i]

			codeword1 = new_data + remainder 
			print(" \n  After inducing error: \n ")

			# dec_data = bin_to_dec(new_data)
		
			# print("\nDecoded data: ", chr(dec_data))
			encodeData(codeword1, key)

			# convert new_data (binary string) to decimal ascii and then perform chr

		else:
			print("Without inducing error: ",codeword)
			original_data = bin_to_dec(data)
			print("Original data: ", chr(original_data) )
			


    

print("\n-----------------------------CRC DETECTION--------------------------\n")
string1 = input("\nEnter data (string): ")
ascii_1 = 0

ascii_list =[]

bin_list =  []

for i in string1:
	ascii_1 += ord(i)

for j in string1:
	ascii_list.append(ord(j))	

print("\n")
for i in string1:
	print (i, " ->\t", ord(i), " ->\t", bin(ord(i))[2:] )

print("Ascii sum: ", ascii_1)

for i in ascii_list:
	bin_list.append(bin(i)[2:])

data = bin(ascii_1)[2:]
print("Binary form of ", ascii_1, "is: ", data)

# print("Generator: ", data)


key = input("\nEnter generator: ")


for i in range(len(bin_list)):
	print("----------------------------------------------------------------------")

	print("\nFor letter", string1[i], ": ")
	encodeData(bin_list[i], key)



print("--------------------------------------------------------------------------")


