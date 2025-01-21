#CITS1401 - Project_2 - by Adharsh Sundaram Soudakar(23796349).
#-------------------------------------------------------------begin---------------------------------------------------------------#
#-------------------------------------------------------------#
#Function that the testing software will call.
def main(csvfile):
    try:
        raw_countries_list = []                                             #list that will hold the i/p data without newline characters and commas.                                                                                         
        countries_data = open(csvfile,'r')                                  #variable that opens and holds all the raw data from the i/p file.                                              
        #Getting the file data into a list.
        for line in countries_data:     
            line_without_newline_char = line.strip()                              
            words_separated_by_comma = line_without_newline_char.split(",")      
            raw_countries_list.append(words_separated_by_comma)
        countries_data.close()
        countries_list = []                                                 #list that will hold the i/p data in the desired form.
        #Calling function "required_format" to tranform the data to the required format.
        required_format(countries_list,raw_countries_list)
        #Calling function "solution" to get the desired O/P.
        res1,res2 = solution(countries_list)
        return res1,res2
    #Check for no such file error or any errors thrown by the called function.
    except Exception as e:
        print("An error has occurred:",e)
        return {},{} 
#-------------------------------------------------------------#
#Function that will convert the raw i/p into a format that's required to process the data.
#This function also removes erroneous data. 
def required_format(countries_list,raw_countries_list):
    try:
        duplicates_index_list = []                                           #list that will hold the indices of the elements that are being used to check for duplicates.     
        for i in range(1,len(raw_countries_list)):
            flag = 0                                                         #flag variable.
            flag1 = 0                                                        #flag variable1.
            flag2 = 0                                                        #flag variable2.
            temp = {}                                                        #temporary dictionary that will contain headers as keys and data from row 1 as values.
            for k in range(len(raw_countries_list[0])):
                temp[raw_countries_list[0][k].lower()] = raw_countries_list[i][k]
            #Checking if the population/net change/land area fields only contain numeric values.
            for i in (temp['population'] + temp['net change'] + temp['land area']):
                if i.isdigit():
                    continue
                elif i == '-':
                    continue
                else:
                    flag += 1
            if flag > 0: continue                  
            #Checking for null/empty fields and, zero or negative value for population and land area and, excluding them.
            if temp['country'] == '' or temp['regions'] == '' or temp['net change'] == '' or temp['population'] == '' or temp['land area'] == '' or temp['population'] <= '0' or temp['land area'] <= '0':
                continue
            #Checking if the country/regions fields only contain non-numeric values.
            for i in (temp['country'] + temp['regions']):
                if i.isdigit():
                    flag1 += 1
            if flag1 > 0: continue
            for j in countries_list:
                #Checking for duplicate countries in the same region.
                if temp['country'] == j['country']:
                    flag2 = 1
                    index = countries_list.index(j)                          #variable that will hold the index of the element that is being used to check for duplicates.
                    #Adding the index of the element that is being used to check for duplicates.
                    if index not in duplicates_index_list:
                        duplicates_index_list.append(index)
            if flag2 == 1: continue      
            countries_list.append(temp)
            place_holder = len(countries_list)                               #variable that will hold the length of countries_list's length.
            #Removing the elements that are used to check for duplicates only if the end of a region has been reached.
            if (place_holder > 1 and place_holder <= len(countries_list) and countries_list[place_holder-1]['regions'] != countries_list[place_holder-2]['regions']):
                for k in duplicates_index_list:
                    countries_list.pop(k)
                duplicates_index_list = []
        return None
    except Exception as e:
        print("An error has occured:",e)
        return str(e)
# ------------------------------------------------------------#   
#Function to find the two required solutions.
def solution(c_list):
    total_regional_pop = 0                            #variable that holds the total regional population.
    countries_density_list = []                       #list that will hold the population density of each country in the region.
    dict1 = {}                                        #dictionary that will hold the final solution for question 1. 
    dict2 = {}                                        #dictionary that will hold the final solution for question 2.
    list1_temp = []                                   #temporary list that will hold the standard error and cosine similarity of a region.         
    dict2_temp = {}                                   #temporary dictionary that will hold the country data in a particular format of each region. 
    population = []                                   #list that will hold the population of each country in a region.          
    land_area = []                                    #list that will hold the land area of each country in a region.
    i = 0                                             #iterable variable for while loop.
    place_holder = 0                                  #variable that will hold the index of the first country of a region.
    
    while i in range(len(c_list)):         
        
        if (i == len(c_list)-1) or (c_list[i]['regions'] != c_list[i-1]['regions'] and c_list[i]['regions'] != c_list[i+1]['regions'] and i-1>0) or (c_list[i]['regions']!=c_list[i+1]['regions'] and c_list[i]['regions'] == c_list[i-1]['regions']):
            #If only one country exists for that region.
            #Or if the final row/country for that region has been reached.
            #Or if the final row/country of the i/p data has been reached.
            each_country_pop=general(c_list,i,population,land_area,countries_density_list)
            total_regional_pop += each_country_pop
            per_pop = percent_pop(population,total_regional_pop)
            for k in range(len(population)):  
                if place_holder == len(c_list): break        
                dict2_temp[c_list[place_holder]['country'].lower()] = [int(c_list[place_holder]['population']),int(c_list[place_holder]['net change']),per_pop[k],countries_density_list[k]]
                place_holder = place_holder+1
            dict2_temp = sort_rank(dict2_temp)
            cos_sim = cosine_sim(population,land_area)
            stand_err = stand_error(population,total_regional_pop)
            list1_temp.append(stand_err)
            list1_temp.append(cos_sim)
            dict1[c_list[i]['regions'].lower()] = list1_temp
            dict2[c_list[i]['regions'].lower()] = dict2_temp
            place_holder = i+1
            total_regional_pop,list1_temp,dict2_temp,countries_density_list,population,land_area = 0,[],{},[],[],[]
            #Come out of the loop / stop when the end of the data has been reached.
            if i == len(c_list)-1 : break
            i += 1

        #If the current country / row and the next country / row belong to the same region and include them.
        #Or if the current country / row is the first country of the new region and include it.
        elif (c_list[i]['regions'] == c_list[i+1]['regions']) or (c_list[i]['regions'] != c_list[i-1]['regions'] and c_list[i]['regions'] == c_list[i+1]['regions']):
            each_country_pop=general(c_list,i,population,land_area,countries_density_list)
            total_regional_pop += each_country_pop
            i += 1
            
    return dict1,dict2 
#-------------------------------------------------------------#
#Function that fetches the required fields from the whole data. 
def general(c_list,i,population,land_area,countries_density_list):
    population_of_each_country = int(c_list[i]['population'])
    density_of_a_country = round(int(c_list[i]['population']) / int(c_list[i]['land area']),4)
    population.append(int(c_list[i]['population']))
    land_area.append(int(c_list[i]['land area']))
    countries_density_list.append(density_of_a_country)
    return population_of_each_country
#-------------------------------------------------------------#
#Function that finds the percentage of population of each country in the region. 
def percent_pop(pop,total_regional_pop):
    per_pop=[]
    for k in range(len(pop)):
        percent=round((pop[k]*100)/total_regional_pop,4)
        per_pop.append(percent)      
    return per_pop        
#-------------------------------------------------------------#
#Function that sorts the solution 2 in the required format.
def sort_rank(dict):
    sorted_countries_list = sorted(dict.keys(),key = lambda x:(-dict[x][0],-dict[x][3],x))
    rank = 1
    for i in sorted_countries_list:
        dict[i].append(rank)
        rank += 1
    return dict
#-------------------------------------------------------------#
#Function that finds the cosine similarity between population and land area in each region.
def cosine_sim(pop,land):
    product_sum=0
    pop_sum=0
    land_sum=0
    for i in range(len(pop)):
        product_sum += (pop[i]*land[i])
        pop_sum += (pop[i]**2) 
        land_sum += (land[i]**2)
    #Check for any errors that could occur when calculating cosine similarity
    try:
        similarity = round(product_sum/((pop_sum**0.5)*(land_sum**0.5)),4)
    except ZeroDivisionError:
        return 0
    return similarity
#-------------------------------------------------------------#
#Function that finds the standard error of population in each region.
def stand_error(pop,total_regional_pop):
    num_of_countries = len(pop)
    mean_pop = total_regional_pop/num_of_countries
    numerator = 0
    for i in range(len(pop)):
        numerator += ((pop[i]-mean_pop)**2)
    #Check for  division by zero error.
    try:
        standard_deviation = (numerator/(num_of_countries-1))**0.5
    except ZeroDivisionError:
        return 0
    standard_error = round(standard_deviation / (num_of_countries**0.5),4)    
    return standard_error 
#--------------------------------------------------------------end----------------------------------------------------------------#
