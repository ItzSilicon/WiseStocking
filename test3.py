from functions import getstockinfo
import json,glob,os


def update(code):
    try:
        D=getstockinfo(f"{code}.tw")
    except:
        return None
    S=json.dumps(D)
    with open(f"StockLibrary/{code}.json","w") as f:
        f.write(S)
        print(f"{code}.json Updated.")

def importinfo():
    N={}
    L=glob.glob(os.path.join("StockLibrary", "*"))
    for i in L:
        code=i[13:17]
        update(code)
        try:
            with open(i,'r',encoding='utf-8') as f:
                S=f.read()
                # print(S)
                C=json.loads(S)
                D=C["longName"]
                # print(type(D))
                N[i]=D
                G=json.dumps(N)
                with open("StockLibrary/Name.json","w") as k:
                    k.write(G)
        except KeyError:
            continue
        

importinfo()