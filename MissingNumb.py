# Popular interview question e.g. amazon, adobe, microsoft, linkedin
# Finding missing number in an array means finding according to range of values inside
# Given an array containing array of numbs from 0 to n with missing numb, find it
# Need to iterate over input array and store numbers not found in another

def missingnumb(n):
    numbers = set(n)
    #length = len(n) not needed?
    missing = []
    for i in range(1, n[-1]): # or whatever starting number is
        if i not in numbers:
            missing.append(i)
    return missing

nlist = [1,2,3,4,5,6,7,8,9,10,12,13,14, 16, 19, 21]
print(missingnumb(nlist))


