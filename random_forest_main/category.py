# VARIABLES
_DISTRIBUTION = { 'INTEREST': 44.80, 'LEARNING_STYLE' : 20.3, 'ACAD_ACHIEVMENTS': 34.90 }

_VARIABLES = {

    "INTEREST" : {
        "REALISTIC" : { "STEM": 4, "GAS": 3, "HUMSS": 2,  "ABM": 1 },
        "INVESTIGATE" : { "STEM": 4, "ABM": 3, "HUMSS": 2, "GAS": 1 },
        "ARTISTIC" : { "HUMSS": 4, "GAS": 3, "STEM": 2, "ABM": 1 },
        "SOCIAL" : {  "HUMSS": 4, "GAS": 3, "STEM": 2,  "ABM": 1 },
        "ENTERPRISING" : { "ABM": 4, "GAS": 3, "HUMSS": 2, "STEM": 1 },
        "CONVENTIONAL" : { "ABM": 4, "STEM": 3, "GAS": 2,  "HUMSS": 1 }
    },

    "LEARNING_STYLE" : {
        "LINGUISTIC" : { "HUMSS": 4, "ABM": 3, "GAS": 2, "STEM": 1 },
        "LOGICAL" :  { "STEM": 4, "ABM": 3,  "HUMSS": 2,  "GAS": 1 },
        "SPATIAL" :  { "ABM": 4, "STEM": 3, "HUMSS": 2, "GAS":  1 },
        "BODILY" : { "HUMSS": 4, "GAS": 3, "STEM": 2, "ABM": 1 },
        "MUSICAL" : { "GAS": 4, "HUMSS": 3, "STEM": 2, "ABM": 1 },
        "INTERPERSONAL" : { "ABM": 4, "HUMSS": 3,"GAS": 2, "STEM": 1 },
        "INTRAPERSONAL" : { "STEM": 4, "GAS": 3, "HUMSS": 2, "ABM": 1 },
        "NATURALIST" : { "GAS": 4,"HUMSS": 3, "ABM": 2, "STEM": 1 }
    },


    "ACAD_ACHIEVMENTS" : {
        "MATH" :  { "STEM": 4, "ABM": 3, "GAS": 2, "HUMSS": 1},
        "ENGLISH" : { "HUMSS": 4, "ABM": 3, "STEM": 2, "GAS": 1},
        "SCIENCE" : { "STEM": 4, "GAS": 3,  "HUMSS": 2, "ABM": 1},
        "SOCIAL_SCIENCE"  : { "HUMSS": 4, "ABM": 3, "GAS": 2, "STEM": 1 }
    }
   
}

def checkDataDependability(data_x):

    isOnlyGrade = 0
    isAllSimilar = 1

    for i in range(14):
        isOnlyGrade += data_x[i]
    
    if(isOnlyGrade != 0):
        return None

    for current_idx in range(14, len(data_x) - 1):
        if(data_x[current_idx] == data_x[current_idx + 1]):
            isAllSimilar += 1
           
    if(isAllSimilar == 1):
        return None

    if isAllSimilar == 4: 
        return 'GAS'
    
    return None

   

#  https://www.statisticshowto.com/weighting-factor/
def WeightFactorAlgorithm(data): 
   
    res = { "HUMSS": 0, "GAS": 0, "STEM": 0, "ABM": 0 }

    spRes = checkDataDependability(data)
    if(spRes != None):
        return spRes
    else:
        
        data_counter = 0
        for variable_id, variable_value in _VARIABLES.items():
                        

            categories = variable_value
            
            temp_counter = { "HUMSS": 0, "GAS": 0, "STEM": 0, "ABM": 0 }

            for category_idx, category_value in categories.items():
                strands = category_value
                for strand_name, strand_value in strands.items():
                    test_score = data[data_counter]
                    if(test_score > 0):
                        if(variable_id != "ACAD_ACHIEVMENTS"):
                            temp_counter[strand_name] += (strand_value * test_score)
                        else:
                            temp_counter[strand_name] += ((strand_value / 10) * test_score)
                data_counter += 1   
            
    
            
            for temp_counter_id, temp_counter_value in temp_counter.items():
               
                res[temp_counter_id] += temp_counter[temp_counter_id] * (_DISTRIBUTION[variable_id] / 100)
        
            
    tentativeStrand = ["", float("-inf")]
    for res_id, res_value in res.items():
        if(tentativeStrand[1] < res_value):
            tentativeStrand[1] = res_value
            tentativeStrand[0] = res_id
    
   
    print("final Result: ", res)
    return tentativeStrand[0]



  


    # data = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 90, 90, 90]   # OUTPUT STEM ✔️
    # data = [3, 2, 3, 1, 4, 4, 4, 5, 5, 5, 6, 3, 5, 6, 86, 81, 84, 87]   # OUTPUT HUMSS ✔️ 
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 90, 90, 90]  # OUTPUT STEM ✔️ 
    # data = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 90, 90, 90]   # OUTPUT STEM ✔️ 
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0]     # OUTPUT HUMSS ✔️ 

   
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0]      # OUTPUT STEM ✔️ 
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0]      # OUTPUT STEM ✔️
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 75, 75, 100, 75]   # OUTPUT STEM ✔️
    # data = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]        # OUTPUT STEM ✔️
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]        # OUTPUT STEM ✔️   
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 75, 75, 75, 75]    # OUTPUT STEM ✔️
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 75, 100, 75, 100]  # OUTPUT STEM ✔️


    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]        # OUTPUT STEM ✔️
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]        # OUTUPUT GAS ✔️ 
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]        # OUTPUT ABM ✔️
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]        # OUTPUTSTEM ✔️
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]        # OUTPUT HUMSS ✔️
    # data = [3, 0, 3, 0, 0, 0, 3, 3, 0, 3, 0, 0, 3, 0, 90, 90, 90, 90]    # OUTPUT HUMSS ✔️
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 75, 100,75, 75]    # OUTPUT HUMSS ✔️
    # data = [0, 0, 0, 0, 4, 4, 0, 0, 4, 0, 0, 0, 4, 0, 90, 90, 90, 90]    # OUTPUT ABM  ✔️ 
    # data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 75, 100,75, 75]    # OUTPUT HUMS ✔️
    # data = [0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 90, 90, 90]    # OUTPUT STEM ✔️




    








