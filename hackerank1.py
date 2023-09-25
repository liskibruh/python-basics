def compareTriplets(a, b):
    # Write your code here
    alice_pts=0
    bob_pts= 0
    a = list(a)
    b = list(b)
    
    for each_elem_a, each_elem_b in zip(a,b):
        if each_elem_a>each_elem_b:
            alice_pts+=1
        elif each_elem_a<each_elem_b:
            bob_pts+=1
        elif each_elem_b==each_elem_a:
            pass
        
    return alice_pts,bob_pts


result = compareTriplets([5,6,3],[5,2,6])
print(result)