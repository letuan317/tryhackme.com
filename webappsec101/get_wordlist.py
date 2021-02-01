fr = open('/usr/share/seclists/Usernames/Names/names.txt','r')
fw = open('new_wordlist.txt','w')
for line in fr:
	if(len(line) == 6):
		print(line)
		fw.write(line)

fr.close()
fw.close()