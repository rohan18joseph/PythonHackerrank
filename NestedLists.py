if __name__ == '__main__':
    list_students=[]
    scoreset=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        scoreset.append(score)
        list_students.append([name,score])
    scoreset.sort()
    scores=list(set(scoreset))   
    scores.remove(min(scores))
    list_students.sort()
    for i in range(len(list_students)):
        if list_students[i][1]==min(scores):
            print(list_students[i][0])
