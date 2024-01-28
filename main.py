def calc_ways(n:int, m:int):
    total_ways = 0
    ways_miss_cerm = 0
    miss_str = '1'*m
    for i in range(2**n):
        curr_prob = bin(i)[2:].zfill(n)
        if not miss_str in curr_prob:
            total_ways += 1
            if curr_prob[-1] == '1':
                ways_miss_cerm += 1
    return total_ways, ways_miss_cerm

if __name__ == '__main__':
    n, m = 10, 4
    x, y = calc_ways(n, m)
    print(f'{y}/{x}')