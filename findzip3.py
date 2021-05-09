adress=input("市町村名を入力してください：")

fp=open("KEN_ALL.CSV","r",encoding="shift_jis")

for line in fp:
    line=line.replace(' ','')
    line=line.replace('"','')
    cells=line.split(",")
    zipno=cells[2]
    ken=cells[6]
    shi=cells[7]
    cho=cells[8]
    title=ken+shi+cho
    if title.find(adress)>=0:
        print(zipno+":"+title)

fp.close()
