import bisect
N = int(input())
Ln = list(map(int,input().split(' ')))

def binary_area_search(target_list: list, target_item: int) -> int:
    '''
    @params
    target_list: [1,3,5](ACC)
    target_item: 2

    @return
    return index
    '''
    low = 0
    high = len(target_list) - 1
    while low <= high:
        mid = (low + high) //2
        guess = target_list[mid]
        if guess > target_item:
            if mid == 0:
                return 0
            if target_item > target_list[mid-1]:
                return mid 
            high = mid -1
        else:
            if mid == len(target_list) - 1:
                return None
            if target_list[mid+1] > target_item:
                return mid + 1 
            low = mid + 1
    return None

def main():
    '''
    N^2*logN
    '''
    Ln.sort()
    count = 0
    for a in range(N):
        a_l = Ln[N-a-1]
        for b in range(a+1, N):
            b_idx = N-b-1
            b_l = Ln[b_idx]
            c_threshold = a_l - b_l
            #c_list = Ln[0:N-b-1]
            c_idx = bisect.bisect_right(Ln,c_threshold)
            #c_idx = binary_area_search(c_list,c_threshold)
            if c_idx >= b_idx:
                continue
            count += b_idx - c_idx
    print(count)

def main2():
    '''
    N^2
    '''
    Ln.sort(reverse=True)
    count = 0
    for a in range(N):
        a_l = Ln[a]
        current_min = N-1
        b = a +1
        while b <= current_min:
            c_idx = current_min
            bc = Ln[b] + Ln[c_idx]
            if a_l < bc:
                count += (current_min - b)
                b += 1
                continue
            current_min -= 1
    print(count)

def main3():
    '''
    N^2*logN
    '''
    Ln.sort()
    count = 0
    for a in range(N):
        a_l = Ln[N-a-1]
        for b in range(a+1, N):
            b_idx = N-b-1
            b_l = Ln[b_idx]
            c_threshold = a_l - b_l
            #c_list = Ln[0:b_idx+1]
            c_idx = bisect.bisect_right(Ln,c_threshold)
            #c_idx = binary_area_search(c_list,c_threshold)
            if c_idx >= b_idx:
                continue
            count += b_idx - c_idx
    print(count)

main3()