class solution:
    def remove_duplicates():
        nums = [1, 1, 2]
        unique_nums = []
        for num in nums:
            if num not in unique_nums:
                unique_nums.append(num)
        
        print(unique_nums)
    

    remove_duplicates()
