import numpy as np
from scipy import stats

def get_data():
    given_array = np.array([[1, 1, 3, 3, 4, 4], [4, 5, 7, 7, 8, 9]])

    return given_array

def select_subarray(given_array, mode, indices):
    if mode == 'all':
        return given_array
    
    elif mode == 'rows':
        return (given_array[indices, :])
    
    elif mode == 'columns':
        return (given_array[:, indices])
    
def compute_statistics(given_array, axis = None):
    calc_mean = np.mean(given_array, axis = axis)
    calc_median = np.median(given_array, axis = axis)
    calc_mode  = stats.mode(given_array, axis = axis)

    return calc_mean, calc_median, calc_mode

def show_results(stats):
    calc_mean, calc_median, calc_mode = stats

    print(f'The mean of given data = \n {calc_mean}')
    print(f'The median of given data =\n {calc_median}')
    print(f'The mode of given data = \n {calc_mode.mode}')
    print(f'The occurences of mode = \n {calc_mode.count}')

def main():
    given_array = get_data()
    
   
    print("\n=== All Data Statistics ===")
    full_stats = compute_statistics(given_array)
    show_results(full_stats)
    
    
    print("\n=== All rows Statistics ===")
    row_stats = compute_statistics(given_array, axis = 1)
    show_results(row_stats)

    
    print("\n=== All columns Statistics ===")
    column_stats = compute_statistics(given_array, axis = 0)
    show_results(column_stats)

    
    print("\n=== Specific rows Statistics ===")
    rows_selected = select_subarray(given_array, mode = 'rows', indices = [0])
    specific_row_stats = compute_statistics(rows_selected, axis = 1)
    show_results(specific_row_stats)

    
    print("\n=== Specific column Statistics ===")
    columns_selected = select_subarray(given_array, mode = 'columns', indices = [0, 2])
    specific_column_stats = compute_statistics(columns_selected, axis = 0)
    show_results(specific_column_stats)
    

if __name__ == '__main__':
    main()




# row_mean   = np.mean(array,axis = 1  ) # Average of  all rows(.i.e. axis = 1) #Average of all cols(.i.e. axis = 0)
# col_median = np.median(array, axis = 0)
# row_median = np.median(array, axis = 1 )
# row_mode   = scipy.stats.mode(array, axis = 1 ) # mode of all rows
# col_mode   = scipy.stats.mode(array, axis = 0 ) # mode of all cols
# print(f'Mean = ', row_mean)
# print(f'Median = ', col_median)
# print(f'Median = ', row_median)
# print(type(row_median[0]))

# print(f'col mode  = ', col_mode.mode)
# print(f'col Mode Count = ', col_mode.count)

# print(f'row mode  = ', row_mode.mode)
# print(f' row Mode Count = ', row_mode.count)

