#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Take an input and output the number of consecutive numbers  
in a row, or what you would say if you were to read it out loud 

ex input: 111222289 
"three ones three fours one eight one nine" 
outputs: 31421819
"""

def Print_Outloud(digit_list, counter_list):
    if len(digit_list) != len(counter_list):
        raise Exception("wrong logic for counting, fix bug")
    else:
        for i in range(len(digit_list)):
            print(f"{counter_list[i]}{digit_list[i]}", end='')

def ReadOutloud(numbers):

    num_str = list(str(numbers));
    counter_list = [];
    digit_list = [];
    counter = 1;
    i = 1;
    while i < len(num_str) :
        
        if i == len(num_str) - 1:
            if num_str[i] == num_str[i-1]:
                counter +=1;
                digit_list.append(num_str[i-1]);
                counter_list.append(counter);
            else:
                counter_list.append(counter);
                digit_list.append(num_str[i-1])
                counter_list.append(str(1));
                digit_list.append(num_str[i])
                
                
        else:
            if num_str[i] == num_str[i-1]:
                counter +=1;
            
            else:
                digit_list.append(num_str[i-1])
                counter_list.append(counter);
                counter = 1;
        i+=1;

    Print_Outloud(digit_list,counter_list);




numbers = 111222289;

ReadOutloud(numbers);

