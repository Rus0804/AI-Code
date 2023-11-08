# SNU_CHENNAI.

# L=[]
# n=int(input("Enter number of substrings: "))
# for i in range(n):
#     substring=input("Prompt",i,":")
#     L.append(substring)

l=['CHEN','U_CH','SNU_','ENNA','NAI.','abcd']

def check(s, l, i, c):
    if l[i] in s and l[i] != l[-1]:
        return check(s, l, i + 1, c)
    else:
        if s[-2:] == l[i][:-2]:
            s += l[i][-2:]
        elif l[i][-2:] == s[:2]:
            s = l[i] + s[2:]
        elif s == '':
            s = l[i]

        if i == len(l) - 1:
            l2=[s]
            t = True
            if c!=len(l):
                for j in l:
                    if j not in s:
                        t = False
            else:
                for j in l:
                    if j not in s:
                        l2.append(j)
                return [s]+check('',l2[1:],0,0)
            if t:
                return l2
            else:
                c+=1
                return check(s, l, 0, c)
        else:
            return check(s, l, i + 1, c)

RESULT = check('', l, 0, 0)
for i in RESULT:
    print("Seed",RESULT.index(i)+1,":",i)
