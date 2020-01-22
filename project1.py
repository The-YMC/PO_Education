#!/usr/bin/env python
# coding: utf-8

# #  파이썬 프로그래밍 프로젝트

#     2020년 1월 20일(월)     이름: (    양 명 철     )    이메일: (   jk00085@naver.com      )

# In[1]:


# 학생들 성적 보여주기
def show(line_list):
    line_list = sorted(line_list, key=lambda line_list: line_list[4], reverse = True) # 정렬
    print("Stuent\t\tName\t\tMidterm\tFinal\tAverage\tGrade") # 출력
    print("-"*60)
    
    for i in range(len(line_list)):
        print("%s\t%s\t%s\t%s\t%.1f\t%s" %tuple(line_list[i]))
       


# In[2]:


# 학생 ID로 검색
def search(line_list):
    flag = len(line_list)
    ID = input("Student ID: ") # 학생 ID입력 받기
    for i in range(len(line_list)):
        if ID in line_list[i][0]:
            print("%s\t%s\t%s\t%s\t%.1f\t%s" %tuple(line_list[i]))
            flag -= 1
            break
    if flag == len(line_list): # 검색 결과가 없다면
        print("NO SUCH PERSON.")


# In[3]:


# 점수 수정
def changescore(line_list):
    flag = len(line_list)
    ID = input("Student ID: ") # 학생 ID입력 받기
    for i in range(len(line_list)):
        if ID in line_list[i][0]:
            se = input("Mid/Final? ").lower() # Mid/Final 대소문자를 소문자로 바꾼다.
            if se == 'mid': # mid인경우
                mscore = int(input("input new score: "))
                if mscore > 100 or mscore < 0:
                    print("wrong")
                    flag -=2
                    break
                else:
                    print("Stuent\t\tName\t\tMidterm\tFinal\tAverage\tGrade")
                    print("%s\t%s\t%s\t%s\t%.1f\t%s" %tuple(line_list[i]))
                    print("-"*60)
                    
                    line_list[i][2] = mscore
                    flag -=1
                    break


            elif se == 'final': # final인경우
                fscore = int(input("input new score: "))
                if fscore > 100 or fscore < 0:
                    print("wrong")
                    flag -=2
                    break
                else:
                    print("Stuent\t\tName\t\tMidterm\tFinal\tAverage\tGrade")
                    print("%s\t%s\t%s\t%s\t%.1f\t%s" %tuple(line_list[i]))
                    print("-"*60)
                    
                    line_list[i][3] = fscore
                    flag -=1
                    break
                
            else:
                print("wrong ")
                flag -=2
                break
    # 점수 수정 이후
    if flag == len(line_list) -1:
        avg = (int(line_list[i][2]) + int(line_list[i][3]))/2
        line_list[i][4]= avg
        if avg >= 90:
            line_list[i][5]="A"
        elif avg >= 80:
            line_list[i][5]="B"
        elif avg >= 70:
            line_list[i][5]="C"
        elif avg >= 60:
            line_list[i][5]="D"
        else :
            line_list[i][5]="F"
        print("Score changed.")
        print("%s\t%s\t%s\t%s\t%.1f\t%s" %tuple(line_list[i][:]))
    
    # 검색 결과가 없다면
    if flag == len(line_list):
        print("NO SUCH PERSON.")
        


# In[4]:


# 학생 추가
def add(line_list):
    ID = input("Student ID: ")
    for i in range(len(line_list)):
        if ID in line_list[i][0]: # 이미 학번이 존재하는 경우
            print("ALREADY EXISTS.")
            break
        else :
            newName = input("Name: ").lower()  # Name을 대소문자를 소문자로 바꾼다.
            newMScore = input("Midterm Score: ")
            newFScore = input("Final Score: ")
            avg = (int(newMScore) + int(newFScore)) /2

            if avg >= 90:
                 line_list.append([ID, newName, newMScore, newFScore, avg,"A"])
            elif avg >= 80:
                line_list.append([ID, newName, newMScore, newFScore, avg,"B"])
            elif avg >= 70:
                line_list.append([ID, newName, newMScore, newFScore, avg,"C"])
            elif avg >= 60:
                line_list.append([ID, newName, newMScore, newFScore, avg,"D"])
            else :
                line_list.append([ID, newName, newMScore, newFScore, avg,"F"])        

            print("Student added.")
            break


# In[5]:


# 학점 검색
def searchgrade(line_list):
#     grad = input("Grade to search: ").lower()  # 학점 등급을 대소문자를 소문자로 바꾼다.
    grad = input("Grade to search: ").upper()  # 학점 등급을 대소문자를 대문자로 바꾼다.

    found = len(line_list)
    for i in range(len(line_list)):
        if grad == 'A' or grad == 'B' or grad == 'C' or grad == 'D' or grad == 'F':
            if grad in line_list[i][5]:
                print("%s\t%s\t%s\t%s\t%.1f\t%s" %tuple(line_list[i]))
                found = found- 1
        else:
            found = -1
            print("wrong") # 학점 등급이 존재하지 않는 경우
            break
    if found == len(line_list):
        print("No RESULT")


# In[6]:


# 삭제
def remove(line_list):
    if line_list == []:
        print("List is empty") # 리스트가 비어 있는 경우
    else:
        ID = input("Student ID: ")
        flag = len(line_list)
        if line_list == []:
            print("List is empty") # 리스트가 비어 있는 경우
        for i in range(len(line_list)):
            if ID in line_list[i][0]:
                del line_list[i] # 해당 학생 삭제
                print("Student removed.")
                flag -=2
                break
        if flag == len(line_list):
            print("NO SUCH PERSON.")


# In[7]:


# 저장 함수
def quit(line_list):
    # 파일 쓰기
    line_list = sorted(line_list, key=lambda line_list: line_list[4], reverse = True) # 총점 기준으로 정렬
    newFilename = input("File name:")
    f = open( newFilename, "w")
        
    for i in range(len(line_list)):
        f.write("%s\t%s\t%s\t%s\n" %tuple(line_list[i][0:4]))
    f.close()


# In[8]:


import sys 

def main():
    address = 'student.txt'

    for v in sys.argv[1:]:
        address = v

    # 파일 읽기
    score = open( address, "r")
    data = score.read().split("\n")


    line_list = []
    for line in data[:-1]: # 제일 마지막은 "\n"이므로
        line_list.append(line.split("\t"))
    #print(line_list)
    
    # 학점 등급 계산
    for i in range(0, len(line_list)):
        avg = (int(line_list[i][2]) + int(line_list[i][3]))/2
        line_list[i].append(avg)
        if avg >= 90:
             line_list[i].append("A")
        elif avg >= 80:
            line_list[i].append("B")
        elif avg >= 70:
            line_list[i].append("C")
        elif avg >= 60:
            line_list[i].append("D")
        else :
            line_list[i].append("F")

    # 출력
    show(line_list)
    
    # 명령어 입력 받기 (무한 루프)
    while True:
        dir = input("Please give me direction: # ").lower() # 명령을 대소문자를 소문자로 바꾼다.
        if dir == "show":
            show(line_list)
        elif dir == 'search':
            search(line_list)
        elif dir == 'changescore':
            changescore(line_list)
        elif dir == 'add':
            add(line_list)
        elif dir == 'searchgrade':
            searchgrade(line_list)
        elif dir == 'remove':
            remove(line_list)
        elif dir == 'quit':
            save = input("Save data?[yes/no] ")
            if save == 'yes':
                quit(line_list) #파일 저장
                print("File Saved")
                break
            else: # 저장 없이 종료
                print("Not saved")
                break

    score.close()
    
        
if __name__=='__main__': # 파일 제일 아래에 작성
    main()


# In[ ]:




