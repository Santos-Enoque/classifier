#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Santos Enoque
# DATE CREATED: 21st May 2020
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    # retrive a file name list from a fiven folder
    file_name_list = listdir(image_dir)
    file_name_list = [x for x in file_name_list if not x.startswith('.')]
    # create a pet label
    pet_labels = []
    #iterate through the file name list to create pet labels
    for file_name in file_name_list:
                    # put the file name in lower case and split by _
            word_list = file_name.lower().split("_")

            pet_name = ""
            #add only words to the pet name
            for word in word_list:
                if word.isalpha():
                    pet_name += word + " "
            # remove whitespaces        
            pet_name = pet_name.strip()
            # add pet_name tothe pets list
            pet_labels.append(pet_name)
            # clear pet_name varible
            pet_name = ""


        
    # crete a new dictionary
    result_dict = dict()   
    
    # add the file names to the keys and the pet_labels to the values
    for idx in range(0, len(file_name_list), 1):
        if file_name_list[idx] not in result_dict:
            result_dict[file_name_list[idx]] = [pet_labels[idx]]
        else:
             print("** Warning: Key=", file_name_list[idx], 
               "already exists in results_dic with value =", 
               result_dict[file_name_list[idx]])

    # return the final dictionary
    return result_dict
