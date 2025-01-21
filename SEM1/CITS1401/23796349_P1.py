
#Python Project1.
#By Adharsh Sundaram Soudakar(23796349).

#Legend:
#c_list[i][0] is each "country's name" column.
#c_list[i][1] is each "country's population" column.
#c_list[i][3] is each "country's net change in population" column.
#c_list[i][4] is each "country's land area" column.
#c_list[i][5] is each "country's region that it belongs to" column.

#-----------------------------------------------------------------------#

#Main function that will be called by the testing software.
def main(csvfile,region):

    countries_list=[]                       #initialize list that holds the data from the input file in a way to work on it.
    countries_data = open(csvfile,'r')      #initialize a variable that opens and holds all the raw data from the input file.

    #Logic to  read the input file and store the values in a list.
    for line in countries_data:     
        line_without_newline_char = line[:-1]                               #initialize a variable that holds each line without the newline character.
        words_separated_by_comma = line_without_newline_char.split(",")     #initialize a variable that holds each word in that line split by a comma. 
        countries_list.append(words_separated_by_comma) 
    countries_data.close()
      

    #Solution1: List that contains the names of the countries with highest and lowest population with a positive net change  in the given region.
    list_max_country_and_min_country = max_min(countries_list,region)

    #Solution2: List that contains the mean/average and the standard deviation of the population in the given region.
    mean_reg_land,mean_reg_pop,countries_density_list,num_countries_in_region = avg(countries_list,region)
    numerator_sum_for_sd_x,numerator_for_corr,denominator_sum_for_corr_x,denominator_sum_for_corr_y = sd_crr(countries_list,region,mean_reg_pop,mean_reg_land) 
    if (num_countries_in_region == 0):
        std_dev_for_region = 0
    else:
        std_dev_for_region = round((numerator_sum_for_sd_x / (num_countries_in_region - 1)) ** 0.5,4)
    list_avg_pop_and_std_dev_for_region = [round(mean_reg_pop,4),std_dev_for_region]

    #Solution3: List that is sorted in the descending order of the country's population density containing each country's name and corresponding population density in the given region as list elements. 
    def sort_based_on_density(density):
        return density[1]     
    countries_density_list.sort(key=sort_based_on_density,reverse=True) 

    #Solution4: Variable that holds the correlation coefficient of the given region.
    if (denominator_sum_for_corr_x == 0 or denominator_sum_for_corr_y == 0):
        correlation_co_eff = 0
    else: 
        correlation_co_eff = round(numerator_for_corr / ((denominator_sum_for_corr_x * denominator_sum_for_corr_y) ** 0.5),4)

    return list_max_country_and_min_country,list_avg_pop_and_std_dev_for_region,countries_density_list,correlation_co_eff
    

#-----------------------------------------------------------------------#

def max_min(c_list,region):

    max_pop = 0                             #initialize a variable for maximum population. 
    max_country = ""                        #initialize a variable for country name with maximum population.
    min_pop = 999999999999                  #initialize a variable for minimum population (a very high value in the range of billion is chosen as no country's population till date has grown to 999,999,999,999).
    min_country = ""                        #initialize a variable for country name with minimum population. 
        
    #Logic to find the name of the countries with maximum and minimum population in a give region with a positive net change in population.
    for i in range(len((c_list))):    
        if(c_list[i][5] == region and int(c_list[i][3]) > 0):
            if(int(c_list[i][1]) > max_pop):
                max_pop = int(c_list[i][1])
                max_country = c_list[i][0]
            elif(int(c_list[i][1]) < min_pop):
                min_pop = int(c_list[i][1])
                min_country = c_list[i][0]
    list_max_country_and_min_country=[max_country,min_country]        
    return list_max_country_and_min_country            
            
#------------------------------------------------------------------------#

def avg(c_list,region):
    total_regional_pop = 0                  #initialize a variable for total population of the region.
    num_countries_in_region = 0             #initialize a variable for the total number of countries in the region.
    total_land_area_in_region = 0           #initialize a vairiable for the total land area of the region.
    density_of_a_country = 0.0              #initialize a variable for the density of a country.
    temp_list = []                          #initialize a temporary list that holds the country's name and its density in that region as elements.
    countries_density_list = []             #initialize a list that will hold each country's name and its population density as a single element in the form of a list. 
    
    #Logic To find the required variables to calculate the average/mean of the population and land area of all the countries in the given region. Also to find the density of population of each country in the given region.
    for i in range(len((c_list))): 
        if(c_list[i][5] == region):
            total_regional_pop += int(c_list[i][1])
            total_land_area_in_region += int(c_list[i][4])
            num_countries_in_region += 1
            density_of_a_country = round(float(c_list[i][1]) / float(c_list[i][4]),4)
            temp_list.append(c_list[i][0])
            temp_list.append(density_of_a_country)
            countries_density_list.append(temp_list)
            temp_list = []
    mean_reg_land = total_land_area_in_region / num_countries_in_region     #initialize a variable to calculate the mean/average of the land area of all countries in the given region.  
    mean_reg_pop = total_regional_pop / num_countries_in_region             #initialize a variable to calculate the mean/average of the population of all countries in the given region. 
    return mean_reg_land,mean_reg_pop,countries_density_list,num_countries_in_region
         

#-------------------------------------------------------------------------#

def sd_crr(c_list,region,mean_reg_pop,mean_reg_land):
    numerator_sum_for_sd_x = 0.0             #initialize a variable for the numerator sum (x-xi)**2 in the std. deviation formula.
    sum_for_corr_x = 0.0                     #initialize a variable for the numerator sum (x-xi) in the correlation coefficient formula.
    sum_for_corr_y = 0.0                     #initialize a variable for the numeartor sum (y-yi) in the correlation coefficient formula.
    numerator_for_corr = 0.0                 #initialize a variable for the numerator sum (x-xi)(y-yi) in the correlation coefficient formula.
    denominator_sum_for_corr_y = 0.0         #initialize a variable for the denominator sum (y-yi)**2 in the correlation coefficient formula.
    denominator_sum_for_corr_x = 0.0         #initialize a variable for the denominator sum (x-xi)**2 in the correlation coefficient formula.

    #logic to find the required variables to calculate the population's standard deviation and correlation coefficient of the given region.
    for i in range(len((c_list))):
        if(c_list[i][5] == region):
            numerator_sum_for_sd_x += (float(c_list[i][1]) - mean_reg_pop)**2
            sum_for_corr_x = float(c_list[i][1]) - mean_reg_pop
            sum_for_corr_y = float(c_list[i][4]) - mean_reg_land
            numerator_for_corr += (sum_for_corr_x * sum_for_corr_y)
            denominator_sum_for_corr_y += (float(c_list[i][4]) - mean_reg_land)**2
    denominator_sum_for_corr_x = numerator_sum_for_sd_x
    return numerator_sum_for_sd_x,numerator_for_corr,denominator_sum_for_corr_x,denominator_sum_for_corr_y

#--------------------------------------------------------------------------#    