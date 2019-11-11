def binary_area_search(target_list, target_item):
    low = 0
    high = len(target_list) - 1
    while low <= high:
        mid = (low + high) //2
        guess = target_list[mid]
        if guess > target_item:
            if mid == 0:
                return 0
            if target_item > target_list[mid-1]:
                return target_list[mid] 
            high = mid -1
        else:
            if mid == len(target_list) - 1:
                return None
            if target_list[mid+1] > target_item:
                return target_list[mid+1] 
            low = mid + 1
    return None

print(binary_area_search([1,3,5,7,9],10))