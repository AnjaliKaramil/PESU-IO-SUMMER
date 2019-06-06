# -*- coding: utf-8 -*-
''' 1. Write a Python program which accepts a sequence of comma-separated
numbers from the user and generate a list and a tuple with those numbers. '''
def main():
    list1 = (input("Enter a sequence of comma-separated numbers: ")).split(",")
    #tup1 = tuple(list1);
    for i in range(len(list1)):
        list1[i]= int(list1[i]);
    tup1 = tuple(list1);
    print("LIST = ", list1)
    print("TUPLE = ", tup1)

#main function
main()
