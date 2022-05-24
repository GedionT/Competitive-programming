
def fuel_cost(n, v):

    # greedy approach to find the minimum fuel cost
    # n is the distance to the destination
    # v is the fuel capacity of the car

    # 4 2 returns 4
    # 7 6 returns 6

    city_cost = [x for x in range(1, n+1)]

    # if the fuel capacity is greater than the distance, return the distance
    if v >= n-1:
        return v

    # if the fuel capacity is less than the distance, return the fuel capacity
    else:
        cost = 0
        for i in range(len(city_cost)-1):
            if city_cost[i] <= v:
                cost += v
            else:
                if city_cost[-1] - city_cost[i] <= v:
                    cost += city_cost[-1] - city_cost[i]
                else:
                    cost += city_cost[i]
        return cost-(v*n)+1


n, v = map(int, input().split())
print(fuel_cost(n, v))
