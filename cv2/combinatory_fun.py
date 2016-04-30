#!/usr/bin/env python

def permutation(l):

    if len(l) == 1:
        return [l]
    else:
        perm_list = []
        for e in l:
            tmp_l = list(l)
            tmp_l.remove(e)
            for perm in permutation(tmp_l):
                perm.insert(0, e)
                perm_list.append(perm)
    return perm_list


def combination(l, k, repetition = False):

    if k == 1:
        return [[i] for i in l]
    else:
        ret_list = []
        for i, e in enumerate(l[:]):
            if not repetition:
                i = 0
                l.remove(e)
            for comb in combination(l[i:], k-1, repetition=repetition):
                comb.insert(0, e)
                ret_list.append(sorted(comb))
        return sorted(ret_list)


def variation(l, k, repetition = False):

    if k == 1:
        return [[i] for i in l]
    else:
        perm_list = []
        for e in l:
            tmp_l = list(l)
            if not repetition:
                tmp_l.remove(e)
            for var in variation(tmp_l, k-1, repetition=repetition):
                var.insert(0, e)
                perm_list.append(var)
    return sorted(perm_list)


def printer(l):

    for pom in l:
        print "    " + "".join(pom)
    print

if __name__ == "__main__":
    
    p = permutation([1,2,3])
    print('Permutacie z [1,2,3] (' + str(len(p)) + ' total): ', p)

    c1 = combination([1,2,3], 2, False)
    print("Dvojice z [1,2,3] (combinacie bez opakovania, " + \
            str(len(c1)) + " total):", c1)
    c2 = combination([1,2,3], 2, True)
    print("Dvojice z [1,2,3] (combinacie s opakovanim, " + \
            str(len(c2)) + " total):", c2)

    v1 = variation([1,2,3], 2, False)
    print("Dvojice z [1,2,3] (variacie bez opakovania, " + \
            str(len(v1)) + " total):", v1)
    v2 = variation([1,2,3], 2, True)
    print("Dvojice z [1,2,3] (variacie s opakovanim, " + \
            str(len(v2)) + " total):", v2)
