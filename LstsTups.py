#Q1-> input movie names and print them in a list
movies=[]
movies.append(input("Enter fave movie: "))
movies.append(input("Enter fave movie: "))
movies.append(input("Enter fave movie: "))

print(movies)

#Q2-> check if a list is a palindrime list
nums=[2,1,2]
nums2= nums.copy()
nums.reverse()
if(nums == nums2):
    print("List is palindrome")
else:
    print("List is not palindrome")