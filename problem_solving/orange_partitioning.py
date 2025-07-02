def orange_partitioning():
    n = int(input(f"Enter the number of oranges plucked :"))
    oranges_diameter = list(map(int,input("Enter the size of oranges in diameters:").split()))
    k = 0
    for i in range(1, n-1):
        if oranges_diameter[i] <= oranges_diameter[n-1]:
            oranges_diameter[i],oranges_diameter[k] = oranges_diameter[k], oranges_diameter[i]
            k += 1

    oranges_diameter[k], oranges_diameter[n-1] = oranges_diameter[n-1], oranges_diameter[k]

    print(f"The oranges to be sold : {oranges_diameter}")

orange_partitioning()