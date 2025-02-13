marks = []
def stud_get():
    print("Enter the number no students in class")
    N = int(input())
    global marks
    for i in range(N):
        print("Enter the marks and write -1 for absent students")
        M = int(input())
        marks.append(M)
    print(marks)

def avg_marks():
    sum = 0
    cnt = 0
    for i in range(len(marks)):
        if marks[i] is not -1:
            sum = sum + marks[i]
            cnt += 1
    print("Total marks is " , sum)
    print("Avg in float " , sum/cnt)
    print("Avg in integer " , sum//cnt)


def high_low():
    temp = marks[0]
    for i in range(len(marks)):
        if temp < marks[i]:
            temp = marks[i]
    print("Highest marks = " , temp)
    temp = marks[0]
    for i in range(len(marks)):
        if marks[i] is not -1:
            if temp > marks[i]:
                temp = marks[i]
        print("Lowest marks = " , temp)


def count_abs():
    cnt = 0;
    for i in range(len(marks)):
        if marks[i] is -1:
            cnt += 1
    print("No of absent students" , cnt)


def high_freq():
    freq=[]
    for i in range(len(marks)):
        if marks[i] is not -1:
            freq.append(marks.count(marks[i]))
    print(freq)
    k=max(freq)
    print("Highest frequency = ",k)
    print("Highes marks = ",marks[k])


                
if __name__ == '__main__':
    print("********Take Input*********")
    stud_get()
    while(True):
        print("1. The average score of class")
        print("2. Highest score and lowest score of class")
        print("3. Count of students who were absent for the test")
        print("4. Display marks with highest frequency")
        print("Enter choice")
        choice=int(input())
        if (choice == 1):
            avg_marks()
        if (choice == 2):
            high_low()
        if (choice == 3):
            count_abs()
        if (choice == 4):
            high_freq()
        if (choice == 5):
            exit()     




                    


