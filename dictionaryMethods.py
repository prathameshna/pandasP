
# UPDATE keyword for change value in existing dictionary
ep = {101:343, 102:234, 103:342, 104:345, 105:421}
ep2 = { 106:353, 107:473}
ep.update(ep2)
print(ep)

# CLEAR keyword removes all the items fom the list.
emp = {101:343, 102:234, 103:342, 104:345, 105:421}
emp.clear()