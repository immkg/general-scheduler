from PSRB import *

for date in StaticVariables.tdata:
    absent_teacher_list = StaticVariables.tdata[date]
    
    s = {}
    d = {}
    
    for x in StaticVariables.sdata:
        s[x] = StaticVariables.sdata[x]
    
    for x in StaticVariables.duration:
        d[x] = StaticVariables.duration[x]
    
    a = PSRB(date, absent_teacher_list, s, d)
    ttable = a.create_graph()
    print date
    if type(ttable) != type('str'):
        print tabulate(ttable, headers=["X"]+range(StaticVariables.p_max), tablefmt='fancy_grid').encode('utf-8')
    else:
        print ttable