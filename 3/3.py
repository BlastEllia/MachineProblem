infile = open("tweetlebeetle.txt")
concordance = {}
linecount = 0
for aline in infile:
    linecount = linecount + 1
    wordlist = aline.split()
    for aword in wordlist:
        if aword in concordance:
            if linecount not in concordance[aword]:
                concordance[aword].append(linecount)
        else:
            concordance[aword] = [linecount]
            
for aword in concordance:
	print(aword, "appears on line(s)", end="")
	for linenum in concordance[aword]:
		print(" ",linenum,"\n", end="")
