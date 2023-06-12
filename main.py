# file_to_dir_p4.py
import glob

def getarr():
    res=[]
    with open('./SearchTtarget.txt') as f:
        lines = f.read()
        for l in lines.split("\n"):
            #print(l)
            if l != '':
                res.append(l)
    #print(res)
    return res

def main():
    arr=getarr()
    #print(arr)

    j={}

    files = glob.glob("./files/*")
    for file in files:
        print(file)
        f = open(file, 'r')
        s = f.read()
        #print(s)
        for k in arr:
            print(k,s.count(k))
            if not(k in j):
                j[k]=0
            j[k]+=s.count(k)

        f.close()

    #print (j)
    print("--------")
    print("TOTAL")
    for key in j:
        print(key,":",j[key]) # titleのみ参照

if __name__ == '__main__':
    main()
