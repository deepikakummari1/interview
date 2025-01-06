set={8,9,2,5,1,7}
set1={3,9,1,11,2,6}

print(set.union(set1))
matched=set.intersection(set1)
unmatched=set-set1
unmatched1=set1-set

print(matched)
print(unmatched)
print(unmatched1)