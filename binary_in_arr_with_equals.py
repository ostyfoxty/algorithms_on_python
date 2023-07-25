# объявление функции
def binary_search(num, lst):
    low = 0
    high = len(lst) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If num is greater, ignore left half
        if lst[mid] < num:
            low = mid + 1

        # If num is smaller, ignore right half
        elif lst[mid] > num:
            high = mid - 1

        # means num is present at mid
        else:
            n = lst.count(lst[mid])-1
            mid += 1
            if n+1 == mid:
                mid = 1
            if n > 0:
                return mid, mid+n
            else:
                return mid, mid

    # If we reach here, then the element was not present
    return 0


numbers = list(map(int, input().split()))
check = list(map(int, input().split()))

for i in range(len(check)):
    print(binary_search(check[i], numbers))
