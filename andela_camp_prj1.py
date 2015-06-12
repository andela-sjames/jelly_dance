
def n_sur_bestscore(total):
    whole_number = total / 3# divide by 3 because total is a summation of 3 digits
    if total % 3 > 0:
        return whole_number + 1
    #adding one because numbers in triplet score differ by 1
    return whole_number# return whole number for uniform triplet score





def sur_bestscore(total):
    b = total / 3
    # divide by 3 because total is a summation of 3 digits
    if total % 3 == 2:
        return b+2
    # for 3x +2 0r 3x-2
    if total % 3 == 1:
        return b+1
    # for 3x+ 3 or x+ 1
    if total % 3 == 0 and total > 0:
        return b+1
    #for remainder == 0
    return b
    





def find_best_Andel_above_p(s, p, ti):
    c = 0
    for t in ti:
        notSurScore = n_sur_bestscore(t)
        surScore = sur_bestscore(t)
        if s > 0 and surScore > notSurScore and surScore >= p and notSurScore == p:
                c+=1
                s-=1
        else:
            if notSurScore>=p:
                c+=1
    return c



with open(".input","r") as inputfile:
    with open ("output.txt","w") as outputfile:

        for case in range(int(inputfile.readline())):
            final = [int(x) for x in inputfile.readline().split()]
            outputfile.write("Case #%d:%d " % (case+1, find_best_Andel_above_p(final[1], final[2], final[3:])))

