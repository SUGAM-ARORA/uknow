number_of_elements = input("Enter the number of elements: ")
elements = eval(input("Enter the list(eg: 1,2,3): "))

maxi = -1
for ele in elements:
    if (ele > maxi):
        maxi = ele

print("The maximum element is: ", maxi)