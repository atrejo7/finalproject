'''
Created on Mar 10, 2018

@author: ITAUser
'''
def tax (filing_status,income):
    if filing_status == 'single':
      
        if (income >= 0) and (income <=9275):
            tax = (0.1*income)
        elif (income > 9275) and (income <= 37650):
            tax=(.1*9275+ 0.15*(income-9275))
        elif (income > 37650) and (income<=91150):
            tax=(.1*9275+0.15*(37650-9275)+.25*(income-37650))
        elif (income > 91150) and (income <= 190150):
            tax=(.1*9275+0.15*(37650-9275)+.25*(91150-37650)+ .28*(income-91151))
        elif (income > 190150) and (income<=190150):
            tax=(.1*9275+0.15*(37650-9275)+.25*(91150-37650)+ .28*(190150-91151)+.33*(income-190151)) 
        elif (income > 413351) and (income<=415050):
            tax=(.1*9275+0.15*(37650-9275)+.25*(91150-37650)+ .28*(190150-91151)+.33*(413350-190151)+.35*(income-413351))
        elif (income > 415051):
            tax=(.1*9275+0.15*(37650-9275)+.25*(91150-37650)+ .28*(190150-91151)+.33*(413350-190151)+.35*(415050-413351)+.396*(income-415051))
            
    elif filing_status == 'married filing jointly':
        if (income >= 0) and (income <=18550):
            tax = (0.1*income)
        elif (income > 18551) and (income <= 75300):
            tax=(.1*18550+ 0.15*(income-18550))
        elif (income > 75301) and (income<=151900):
            tax=(.1*18550+ 0.15*(75300-18550)+.25*(income-75301))
        elif (income > 151901) and (income <= 231450):
            tax=(.1*18550+ 0.15*(75300-18550)+.25*(151900-75301)+.28*(income-151901))
        elif (income > 231451) and (income<=413350):
            tax=(.1*18550+ 0.15*(75300-18550)+.25*(151900-75301)+.28*(231450-151901)+.33(income-231451)) 
        elif (income > 413351) and (income<=466950):
            tax=(.1*9275+0.15*(37650-9275)+.25*(91150-37650)+ .28*(190150-91151)+.33*(413350-190151)+.35*(income-466951))
        elif (income > 466951):
            tax=(.1*9275+0.15*(37650-9275)+.25*(91150-37650)+ .28*(190150-91151)+.33*(413350-190151)+.35*(415050-466951)+.396*(income-466951))
            
    elif filing_status == 'married filing separately':
        if (income >= 0) and (income <=9275):
            tax = (0.1*income)
        elif (income > 9275) and (income <= 37650):
            tax=(.1*9275+ 0.15*(income-9275))
        elif (income > 37650) and (income<=75950):
            tax=(.1*9275+0.15*(37650-9275)+.25*(income-37650))
        elif (income > 75950) and (income <= 115725):
            tax=(.1*9275+0.15*(37650-9275)+.25*(75950-37650)+ .28*(income-75951))
        elif (income > 115725) and (income<=206675):
            tax=(.1*9275+0.15*(37650-9275)+.25*(75950-37650)+ .28*(115725-74951)+.33*(income-115726)) 
        elif (income > 206675) and (income<=233475):
            tax=(.1*9275+0.15*(37650-9275)+.25*(75950-37650)+ .28*(115725-74951)+.33*(206675-115726)+ .35(income-206675))
        elif (income > 233476):
            tax=(.1*9275+0.15*(37650-9275)+.25*(75950-37650)+ .28*(115725-74951)+.33*(206675-115726)+ .35(233475-206675)+.396(income-233476))
        
    elif filing_status == 'Head of household':
        if (income >= 0) and (income <=13250):
            tax = (0.1*income)
        elif (income > 13251) and (income <= 50400):
            tax=(.1*13250+ 0.15*(income-13251))
        elif (income > 50400) and (income<=130150):
            tax=(.1*13250+0.15*(50400-13251)+.25*(income-50400))
        elif (income > 130151) and (income <= 210800):
            tax=(.1*13250+0.15*(50400-13251)+.25*(130150-50401)+ .28*(income-130151))
        elif (income > 210801) and (income<=413350):
            tax=(.1*13250+0.15*(50400-13251)+.25*(130150-50401)+ .28*(210800-130151)+.33*(income-210801)) 
        elif (income > 413350) and (income<=441000):
            tax=(.1*13250+0.15*(50400-13251)+.25*(130150-50401)+ .28*(210800-130515)+.33*(413350-210801)+ .35(income-413351))
        elif (income > 441001):
            tax=(.1*13250+0.15*(50400-13251)+.25*(130150-50401)+ .28*(210800-130515)+.33*(413350-210801)+ .35(441000-413351)+.396(income-441001))
    return tax

    
def is_valid(filing_status,income):
    if filing_status == 'single' or 'married filing jointly' or 'married filing separately' or 'Head of household':
        if (income >=0):
            return True
        return False
    return False
def main():
    user_input = input ("Filing status:")
    user_input2 = (int)(input ("User income:"))
    if is_valid(user_input,user_input2):
        print(tax(user_input,user_input2))

main()
    
    