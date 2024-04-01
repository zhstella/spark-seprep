def avg_calculator():
    '''calculates the average of any set of numbers given'''
    numbers_tuple = input("Want to find the average of your numbers?\nEnter the numbers you want to find the average of here, separating each with a comma: ")
    list_num = [int(num_str.strip()) for num_str in numbers_tuple.split(',')]
    sum = 0
    for n in list_num:
        sum += n
    avg = sum/len(list_num)
    return avg

if __name__ == '__main__':

    print(avg_calculator())