# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 17:37:32 2020

@author: Utente
"""
import pandas as pd
import random
pos = input ('Insert the name of the "autosampler positions file" with "tab" as space inbetween positions (.txt): ')
position = pos+'.txt'
# importing txt file with the available autosample positions as df
df = pd.read_csv(position, sep = '\t')
#trasforming df in list
position = []
for word in df:
    position.append(word)
#INFORMATION REGARDING THE ADDITION OF WASHES TO THE SEQUENCE
#Asking if python has to add washes in the sequence beside randomizing the order of injection
wash = input ('Do you want to add washes to your seuence (y/n)? ')
# While loop to check that the data inserted are correct if not re-insert data
if wash.lower().startswith('y'):
    procede = 'n'
    while procede.lower() != 'y':
        if procede == 'yes':
            break
        else:
            wash_position = input ('What is the position of the wash in the autosampler?: ')
# Asks how many time in a row a washe has to be repeted
            num_wash = input ('How many repetion of wash do you want?: (insert an integer) ')
# Check that an integer is insert, if not reask the question
            while num_wash.isdigit() == False:
                num_wash = input ('How many repetion of wash do you want?: (insert an integer) ')
# Asks how many sample in row you want to send before sending the set of washes
            bracketing = input ('After how many samples you want a (set of) wash?: ')
 # check that an integer is insert, if not reask the question
            while bracketing.isdigit() == False:
                bracketing = input ('How many repetion of wash do you want?: (insert an integer) ')
            print ('\nDATA INSERTED:\nAdd Wash to the sequence: "YES"','\nWash position:', wash_position, '\nNumber of washes in row =', num_wash,'\nNumber of samples in a row =',bracketing)
            procede = input('Check if the data inserted are correct (y/n): ')
else:
    print ('\nDATA INSERTED:\nAdd Wash to the sequence: "NO"')

#wash_adder is the function that will modify the random lists of injection created and add the washes where it has been defined from the user
# wash_position = position autosampler of wash vial (value tu insert in the list)
# num_wash = repetition of wash each time
# bracketing = n° samples inbetween a set of wash
#always add a wash at the beginning
def wash_adder(pos):
    new_sequence = []
# add the first wash
    new_sequence.append(wash_position)
# split the sequence at the bracketing number and reconsitute in the final list adding the wash_num defined based on a while loop
    while pos:
        for coordinate in pos[0:int(bracketing)]:
            new_sequence.append(coordinate)
            pos.remove(coordinate)
        for num in range(int(num_wash)):
            new_sequence.append(wash_position)
#trasforming the sequence in dataframe
    seq = pd.DataFrame(new_sequence, columns = [0])
#print out the dataframe as CSV
    name = input("Insert a name to save the sequence: ")
    name_csv = name+'.csv'
    seq.to_csv(name_csv, index = False, header= False)
    return print('A csv file called:',name,' has been created with the randomized sequence.')

#The code randomizes the sequence. If washes need to be added, it runs wash_adder, if not it prints out the file.
if wash.lower().startswith('y'):
    list_sequence = []
#In a while loop, choose randomply a position and add it to the sequence list.
    while position:
        word = random.choice(position)
        list_sequence.append(word)
#Remove the position choosen from the list in order to continue with the random position identification.
        position.remove(word)
    wash_adder(list_sequence)
else:
    sequence = []
#In a while loop, choose randomply a position and add it to the sequence list.
    while position:
        word = random.choice(position)
        sequence.append(word)
#Remove the position choosen from the list in order to continue with the random position identification.
        position.remove(word)
    seq = pd.DataFrame(sequence, columns = [0])
#print out the dataframe as CSV
    name = input("Insert a name to save the sequence: ")
    name_csv = name+'.csv'
    seq.to_csv(name_csv, index = False, header= False)
    print('A csv file called:',name,' has been created with the randomized sequence.')

## FINE - /EG