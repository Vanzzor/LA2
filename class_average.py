"""
input : the test scores
inititate a itrator or accumlator and set it to 0 
loop through the list
add all the test scores
increment the counter by 1
once the loop ends, there are no more scores to add
divide the acccumlator(sum)/ by counter 

display output to the end user
output: print the average of the class scores 

"""

"""
scores 
iterator, accumlator=0
loop through scores
    accumlator = accumlator + scores
    iterator = iterator + 1
average= accumlator / total scores
print average

"""


def calculate_average(scores):
    # input
    iterator = 0
    accumulator = 0
    student_count = len(scores)
    # print("length is: ", len(scores))

    while iterator < len(scores):
        #print("within while loop iterator: ", iterator)
        # print(f"item at index {iterator} is ", scores[iterator])
        accumulator = accumulator + scores[iterator]
        iterator = iterator+1
    # print("sum is: ", accumulator)
    average = accumulator/student_count
    return average


output = calculate_average(
    [100, 80, 90, 70, 50, 95, 60, 90, 50])

print("The average of total scores in the class is: ", output)
