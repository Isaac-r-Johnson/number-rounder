import json


def round_num(num, dp):
    try:
        def clts(li):
            string = ''
            return string.join(li)
        num = str(num)
        w, d = num.split(".")
        d = list(str(d))
        if int(d[dp]) >= 5:
            ntm = int(d[dp-1])
            d[dp-1] = ntm + 1
            d[dp-1] = str(d[dp-1])
            d[dp] = "/"
        elif int(d[dp]) < 5:
            d[dp] = "/"
        d = clts(d)
        d, _d = d.split("/")
        rn = str(w) + "." + str(d)
        return float(rn)
    except:
        return num


def jprint(obj):
    string = json.dumps(obj, sort_keys=True, indent=4)
    print(string)