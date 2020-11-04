
cd = int(input("CD: ")) * 3
sd = int(input("SD: ")) * 3
da = int(input("DA: ")) * 3
vc = int(input("VC: ")) * 3
pe = int(input("STQA: ")) * 3
oe = int(input("RES: ")) * 3
# cdl = int(input("CD lab:")) * 2
# casel = int(input("Case tools lab: ")) * 2
# cdal = int(input("Cloud lab: ")) * 2
# mini = int(input("Mini project: ")) * 2
# nptel = int(input("Nptel: ")) * 1
cdl = 10 * 2
casel = 10 * 2
cdal = 10 * 2
mini = 10 * 2
nptel = 10 * 1

_6 = (cd + sd + da + vc + pe + oe + cdl + casel +  cdal + mini + nptel) / 27
print("Congrtulations, SGPA", _6)
_1 = float(input("1st sem: "))
_2 = float(input("2nd sem: "))
_3 = float(input("3rd sem: "))
_4 = float(input("4th sem: "))
_5 = float(input("5th sem: "))


print("CGPA: ", (_1 + _2 + _3 + _4 + _5 + _6) / 6)
