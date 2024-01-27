newf=""
with open('domains.txt','r') as f:
    for line in f:
        newf+= "||" + line.strip() + "\n"
    f.close()
with open('domains-done.txt','w') as f:
    f.write(newf)
    f.close()