

# VARIABLES
_DISTRIBUTION = { 'INTEREST': 44.80, 'LEARNING_STYLE' : 20.3, 'ACAD_ACHIEVMENTS': 34.90 }

# CATEGORIES
_VARIABLES = {

    "INTEREST" : {
        "REALISTIC" : { "GAS": 100, "STEM": 93, "HUMSS": 45,  "ABM": 23 },
        "INVESTIGATE" : { "STEM": 93, "ABM": 90, "HUMSS": 43, "GAS": 11 },
        "ARTISTIC" : { "HUMSS": 82, "GAS": 38, "STEM": 27, "ABM": 13 },
        "SOCIAL" : {  "HUMSS": 103, "GAS": 94, "STEM": 34,  "ABM": 16 },
        "ENTERPRISING" : { "ABM": 120, "GAS": 36, "HUMSS": 30, "STEM": 27 },
        "CONVENTIONAL" : { "ABM": 113, "STEM": 102, "GAS": 96,  "HUMSS": 80 }
    },

    "LEARNING_STYLE" : {
        "LINGUISTIC" : { "HUMSS": 111, "ABM": 94, "GAS": 44, "STEM": 6 },
        "LOGICAL" :  { "STEM": 98, "ABM": 90,  "HUMSS": 24,  "GAS": 23 },
        "SPATIAL" :  { "ABM": 62, "STEM": 37, "HUMSS": 29, "GAS":  19 },
        "BODILY" : { "HUMSS": 54, "GAS": 26, "STEM": 13, "ABM": 1 },
        "MUSICAL" : { "GAS": 53, "HUMSS": 35, "STEM": 32, "ABM": 21 },
        "INTERPERSONAL" : { "ABM": 110, "HUMSS": 64,"GAS": 31, "STEM": 30 },
        "INTRAPERSONAL" : { "STEM": 94, "GAS": 84, "HUMSS": 34, "ABM": 18 },
        "NATURALIST" : { "GAS": 92,"HUMSS": 49, "ABM": 34, "STEM": 27 }
    },


    "ACAD_ACHIEVMENTS" : {
        "MATH" :  { "STEM": 103, "ABM": 89, "GAS": 53, "HUMSS": 32},
        "ENGLISH" : { "HUMSS": 93, "ABM": 82, "GAS": 36, "STEM": 29},
        "SCIENCE" : { "STEM": 88, "GAS": 61, "HUMSS": 58, "ABM": 46},
        "SOCIAL_SCIENCE"  : { "HUMSS":111, "ABM": 87, "GAS": 32, "STEM": 25 }
    }
   
}

# TOTAL RESPONDENTS
_TOTAL_RESPONDENTS = 500


#  https://www.statisticshowto.com/weighting-factor/
def WeightFactorAlgorithm(data): 
    print(data)
    res = { "HUMSS": 0, "GAS": 0, "STEM": 0, "ABM": 0 }
    data_counter = 0
    for variable_id, variable_value in _VARIABLES.items():
        categories = variable_value
        for category_Id, category_value in categories.items():
            strands = category_value
            for strand_Id, strand_value in strands.items():
                score = data[data_counter]
                if(score > 0):
                    if(variable_id != "ACAD_ACHIEVMENTS"):
                        res[strand_Id] += ((strand_value / _TOTAL_RESPONDENTS) * 100) * score
                    else:
                        grade = strand_value
                        res[strand_Id] +=  grade
              
            data_counter += 1   

        
        
        for temp_counter_id, temp_counter_value in res.items():
            res[temp_counter_id] += res[temp_counter_id] * (_DISTRIBUTION[variable_id] / 100)
      
        

    
    
    tentativeStrand = ["", float("-inf")]
    for res_id, res_value in res.items():
        if(tentativeStrand[1] < res_value):
            tentativeStrand[1] = res_value
            tentativeStrand[0] = res_id
    
   
    return tentativeStrand[0]


# connect this function 
#def getRecommendedTrack(data):
#    weightFactor = WeightFactorAlgorithm(data)
#    randomForest = predict_probabilities([data])[0][0]
#    if(weightFactor != randomForest):
#        return weightFactor
#    return randomForest




    # data = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 90, 90, 90] 
    # data = [3, 2, 3, 1, 4, 4, 4, 5, 5, 5, 6, 3, 5, 6, 86, 81, 84, 87] 
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 90, 90, 90]
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 90, 90, 90]
    # data = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 90, 90, 90] 
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0]    
    # data = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 90, 90, 90] 
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0]  
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0]  
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0]
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0]  
    # data = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]  
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] 
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    # data = [3, 0, 3, 0, 0, 0, 3, 3, 0, 3, 0, 0, 3, 0, 90, 90, 90, 90]
    # data = [0, 0, 4, 4, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 90, 90, 90, 90]
    # data = [0, 0, 0, 0, 4, 4, 0, 0, 4, 0, 0, 0, 4, 0, 90, 90, 90, 90]




    








