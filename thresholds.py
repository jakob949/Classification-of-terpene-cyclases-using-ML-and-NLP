#!/usr/bin/env python3
import json

def thresholds(file_path, class_of_interest, Json):
    # Initialize variables
    type_class = set()  # Stores unique class types
    type_class_dict_wrongly_pred = {}  # Stores predictions that were incorrect
    type_class_dict_correctly_pred = {}  # Stores predictions that were correct
    threshold_type_class = []  # Stores the threshold scores for each class type
    threshold_type_class_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            split = line.split('\t')

            # Get the relevant information from the line
            class_type = split[2]
            correct_class = split[3][6:]
            predicted_class = split[4][6:]
            pos = split[1][3:]
            score = split[-1][7:-1]
            e_val = split[-2][7:]

            # Check if the current line corresponds to the class of interest
            if class_type == class_of_interest:
                if correct_class == predicted_class:
                    type_class.add(correct_class)

                    # Add the prediction to the dictionary of correct predictions
                    if predicted_class in type_class_dict_correctly_pred:
                        type_class_dict_correctly_pred[predicted_class].append([pos, score, e_val, predicted_class, correct_class])
                    else:
                        type_class_dict_correctly_pred[predicted_class] = [[pos, score, e_val, predicted_class, correct_class]]
                # If the prediction was incorrect
                elif correct_class != predicted_class:
                    type_class.add(correct_class)
                    if predicted_class in type_class_dict_wrongly_pred:
                        type_class_dict_wrongly_pred[predicted_class].append([pos, score, e_val, predicted_class, correct_class])
                    else:
                        type_class_dict_wrongly_pred[predicted_class] = [[pos, score, e_val, predicted_class, correct_class]]

                    
    # Calculate the threshold scores for each class type. 

    for item in type_class:
        correcrly_pred = []
        wrongly_pred = []
        # In the cases. Where a class has both correct and wrongly predicted instances
        # And in the cases where there are only correct predictions
        if item in type_class_dict_correctly_pred:
            for item1 in type_class_dict_correctly_pred[item]:
                correcrly_pred.append(item1[1])
                

        if item in type_class_dict_wrongly_pred:
            for item2 in type_class_dict_wrongly_pred[item]:
                wrongly_pred.append(item2[1])
                
        # In the cases where class is never predicted
        if item not in type_class_dict_correctly_pred:
            threshold_type_class.append((item, 10000))
            threshold_type_class_dict[item] = 10000
        if len(wrongly_pred) != 0:
            highest_negative_score = max(wrongly_pred)
        else:
            highest_negative_score = 0

        correcrly_pred.sort()

        for pred_score in correcrly_pred:
            if float(pred_score) > float(highest_negative_score):
                temp_threshold = pred_score
                threshold_type_class.append((item, temp_threshold))
                threshold_type_class_dict[item] = temp_threshold
                break
    
    # saves output as Json format. Or returns a list with the same values.
    if Json:
        with open(f'thresholds_{class_of_interest}.json', 'w') as f:
            json.dump(threshold_type_class_dict, f)
        return None
    else:
        return threshold_type_class


thresholds('log_13022023_VAL_small_homo.txt', 'small', True)

