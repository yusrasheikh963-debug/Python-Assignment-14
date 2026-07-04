import numpy as np

marks = np.random.randint(30, 101, (10, 5))   #Generate marks for 10 students and 5 subjects

print("Student Marks (10 students * 5 subjects):")
print(marks)

total_marks = marks.sum(axis=1)     #Calculate total marks for each student
print("\nTotal Marks of Each Student:")
print(total_marks)

average_marks = marks.mean(axis=1)   #Calculate average marks for each student
print("\nAverage Marks of Each Student:")
print(np.round(average_marks, 2))

top_student = np.argmax(total_marks)    #Find student with highest and lowest total marks
low_student = np.argmin(total_marks)

print("\nTop Scoring Student Index:", top_student)
print("Lowest Scoring Student Index:", low_student)

class_mean = marks.mean()   #Overall class statistics
class_std = marks.std()

print("\nClass Mean:", round(class_mean, 2))
print("Class Standard Deviation:", round(class_std, 2))

reshaped = marks.reshape(10, 5)  #Reshape array 
print("\nReshaped Array (10*5):")
print(reshaped)

top3_indices = np.argsort(total_marks)[-3:]   # last 3 highest totals

print("\nTop 3 Students' Marks:")
print(marks[top3_indices])