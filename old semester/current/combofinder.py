import itertools


inlist = ['g', 'b']
slots = 4

in1 = ['g', 'g', 'g', 'g']
in2 = ['b', 'b', 'b', 'b']



out = list(itertools.combinations_with_replacement(inlist, slots))
print(out)
for i in out:
    out2 = list(itertools.permutations(i))
    for i in out2:
        print(i)