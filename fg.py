import os

#"date {month}{day}{hour}{minute}{year}"

cmd = "date  %s%s1223%s"

ech = "echo %c > a"
add = "git add a"
com = "git commit -m green"

for k in [14]:
    for j in range(1,5):
        for  i in range(1, 32):
            d = ""
            m = ""
            y = ""

            if i  <  10:
                d = "0"
            if j  <  10:
                m = "0"

            l = i

            d += str(i)
            m += str(j)
            y += str(k)



            print cmd %(m,d,y)
            os.system(cmd %(m, d, y))
            for z in range(1,4):
                os.system(ech % l)
                os.system(add)
                os.system(com)
