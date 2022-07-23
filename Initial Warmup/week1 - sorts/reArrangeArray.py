
def rearrangeArray(numb) -> int:
    

    for i in range(1, len(numb) - 1):
        if numb[i] == (numb[i-1] + numb[i+1]) / 2:
            numb[i], numb[i-1] = numb[i-1], numb[i]
        elif numb[i] == (numb[i-1] + numb[i+1]) / 2:
            numb[i], numb[i+1] = numb[i+1], numb[i]
    return numb


if __name__ == "__main__":
    print(rearrangeArray([1,2,3,4,5,6,7,8]))