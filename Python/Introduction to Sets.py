# Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student 
# Mickey to compute the average of all the plants with distinct heights in her greenhouse. 
# The resulting float value should be rounded to 3 places after the decimal.

def average(array):
    height=set(array)
    return round(sum(height)/len(height),3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)