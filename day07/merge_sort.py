#1 - split the list
#2 recursively sort the split lists
#3 - merge sublists togethet
#4 - final merge, returning a sorted list

def merge_sort(l:[tuple])->[tuple]:
    #first define the base case
    if len(l)<=1:
        return l;
    
    #split the list
    mid = len(l)//2
    left_half = l[:mid]
    right_half = l[mid:]

    #recursively merge sort sublists, then merge together 
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left:[tuple],right:[tuple])-> [tuple]:
    #empty list to add sorted elements to
    merged = []
    #two pointers
    left_index=0
    right_index=0

    while left_index<len(left) and right_index<len(right):
        # if the leftmost element of the left sublist is smaller than the leftmost element of the right sublist, add it to the merged list first
        if left[left_index][0] <= right[right_index][0]:
            merged.append(left[left_index]);
            left_index += 1;
        else:
        #else add the leftmost element of the right sublist, so that the smallest value is added first
            merged.append(right[right_index]);
            right_index += 1;
    
    #when one of the sublists has been exausted, add the remaining (largest) element to the merged list
    merged += left[left_index:];
    merged += right[right_index:];
    
    #return the merged list
    return merged
