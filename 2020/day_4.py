f = list(open("day_4_input.txt", "r")) + ["\n"]
for i in range(len(f)):
	f[i] = f[i].replace("\n", " ")

def separate_documents():
	documents = []
	doc = ""
	for i in range(len(f)):
		if f[i] == " ":
			for field in doc:
				field = field.split(" ")
			doc = doc.split(" ")
			dic = {}
			for i in range(len(doc)):
				field = doc[i]
				field = field.split(":")
				if len(field)==2:
					dic[field[0]] = field[1] 
			documents.append(dic)
			doc = ""
		else:
			doc += f[i]
	return documents

def check_document(document):

	if "byr" not in document:
		return False
	else:
		if int(document["byr"]) < 1920 or int(document["byr"]) > 2002:
			return False

	if "iyr" not in document:
		return False
	else:
		if int(document["iyr"]) < 2010 or int(document["iyr"]) > 2020:
			return False

	if "eyr" not in document:
		return False
	else:
		if int(document["eyr"]) < 2020 or int(document["eyr"]) > 2030:
			return False


	if "hgt" not in document:
		return False
	else:
		if document["hgt"][:-2] == '': return False
		height = int(document["hgt"][:-2])
		if document["hgt"][-2:] == "cm":
			if height < 150 or height > 193:
				return False
		else:
			if height < 59 or height > 76:
				return False

	if "hcl" not in document:
		return False
	else:
		if document["hcl"][0] != "#":
			return False
		elif len(document["hcl"]) != 7: 
			return False
		else:
			for letter in document["hcl"][1:]:
				if letter.isalnum() == False:
					return False

	if "ecl" not in document:
		return False
	else:
		if document["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
			return False

	if "pid" not in document:
		return False
	else:
		if len(document["pid"]) != 9 or document["pid"].isnumeric() == False:
			return False

	return True



def solution_1():
	valid = 0
	documents = separate_documents()
	for doc in documents:
		print(doc)
		if len(doc) >= 7:
			if len(doc) == 8:
				print("valid")
				valid +=1
			elif "cid" not in doc:
				print("valid")
				valid += 1

	return valid

def solution_2():
	valid = 0
	documents = separate_documents()
	for doc in documents:
		if check_document(doc):
			valid += 1

	return valid


s1 = solution_1()
print("Solution for part 1: ", s1)

s2 = solution_2()
print("Solution for part 2: ", s2)