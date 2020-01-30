import pandas as pd


street_suffixes = ['PATH','BRIDGE','BAY','TECH','ALLEY','CENTER','PIERS','RDG','RIVER','HL','COVE','ROW','PIER','TNPK','FAIR','ISLAND','MALL','AVE','THRU','HILL','RIDGE','PKW','COURSE','PARKLANE','THRUWAY','WAY','HEIGHTS','SLIP','EXPY','ST','PLAZA','PKWY','GREEN','CAMP','TURNPIKE','BL','OVAL','LOOP','BLVD','DR','CIRCLE','WALK','HIGHWAY','CONCOURSE', 'SQUARE','CRESCENT', 'AVENUE', 'ROAD', 'STREET', 'BOULEVARD', 'PLACE', 'DRIVE', 'LANE', 'PARKWAY', 'PARK','EXPRESSWAY', 'TERRACE', 'RD', 'COURT']

exceptions = ["B'WAY",'PCT','FDR','PPW','GCP','GREENWAY','CPW','KINGSBRIDGE','ESPLANADE','GRANDCONCOURSE','BQE','KINGSHIGWY','BOWERY','BROADWAY']



def get_street_address(series, separate=True):
    '''
    Description:
                Parses a pandas series with rows of addresses for the street address. For example, if one row of the series is
                "431 85th St. Brooklyn, NY 11209" this function will parse it and return only "431 85th St." If the address is 
                unusual in that it does not have a street number, it is stored in another series if the separate option is set
                to True
                
    Parameters:
                series - (pandas.Series) series of addresses to be parsed.
                separate - (bool) True returns two series, one with unusual addresses (no street numbers), and one with street 
                           numbers. If set to False, one series is returned with all parsed, regardless of street number.
                
    Returns:    A list of just the street addresses
    '''
    
    # Break up the addresses on the comma and take the first part. Store each bit in a list
    street_addresses = [x[0].split(' ') for x in series.str.split(',')]
    
    regular_street_addresses = []
    unusual_addresses = []
    for add in street_addresses:
        counted = False
        index = 0
        for i in add:
            index += 1
            if (((i in street_suffixes) or (i in exceptions)) and (index > 2)):
                regular_street_addresses.append(add[:index])
                counted = True
                break

            elif i == 'BROADWAY':
                regular_street_addresses.append(add[:index])
                counted = True

            elif (i == 'AVENUE') and (len(add[index]) == 1):
                regular_street_addresses.append(add[:index+1])
                counted = True





        if counted == False:
            unusual_addresses.append(add)

    st_add = []
    for x in regular_street_addresses:
        try:
            if len(x[0].split('-')) == 2:
                x[0] =  ''.join(x[0].split('-'))
        except:
            print('Error with split on hyphen')

        try:
            convert = int(x[1])
            st_no = [i for i in str(x[1])]

            if x[1] == '1':
                x[1] = x[1] + 'ST'

            elif x[1] == '2':
                x[1] = x[1] + 'ND'

            elif x[1] == '3':
                x[1] = x[1] + 'RD'

            elif (st_no[-1] == '1') and (st_no[-2] != '1'):
                x[1] = x[1] + 'ST'

            elif (st_no[-1] =='2') and (st_no[-2] != '1'):
                x[1] = x[1] + 'ND'

            elif (st_no[-1] == '3') and (st_no[-2] != '1'):
                x[1] = x[1] + 'RD'

            else:
                x[1] = x[1] + 'TH'

        except:
            pass


        try:
            convert = int(x[2])
            st_no = [i for i in str(x[2])]

            if x[2] == '1':
                x[2] = x[2] + 'ST'

            elif x[2] == '2':
                x[2] = x[2] + 'ND'

            elif x[2] == '3':
                x[2] = x[2] + 'RD'

            elif (st_no[-1] == '1') and (st_no[-2] != '1'):
                x[2] = x[2] + 'ST'

            elif st_no[-1] =='2' and (st_no[-2] != '1'):
                x[2] = x[2] + 'ND'

            elif st_no[-1] == '3' and (st_no[-2] != '1'):
                x[2] = x[2] + 'RD'

            else:
                x[2] = x[2] +'TH'

        except:
            pass

        try:
            if type(int(x[0])) == type(1):
                st_add.append(' '.join(x))

        except:
            pass


    if separate == True:
        return st_add
    

    
    
    
    
    
    
    weird_add = []

    for add in unusual_addresses:
        counted = False
        index = 0
        for i in add:
            index += 1
            if (((i in street_suffixes) or (i in exceptions))):
                weird_add.append(add[:index])
                counted = True
                break

            elif i == 'BROADWAY':
                weird_add.append(add[:index])
                counted = True

            elif (i == 'AVENUE') and (len(add[index]) == 1):
                weird_add.append(add[:index+1])
                counted = True

    unus_add = []
    for x in weird_add:
        try:
            if len(x[0].split('-')) == 2:
                x[0] =  ''.join(x[0].split('-'))
        except:
            print('Error with split on hyphen')

        try:
            convert = int(x[0])
            st_no = [i for i in str(x[0])]

            if x[0] == '1':
                x[0] = x[0] + 'ST'

            elif x[0] == '2':
                x[0] = x[0] + 'ND'

            elif x[0] == '3':
                x[0] = x[0] + 'RD'

            elif (st_no[-1] == '1') and (st_no[-2] != '1'):
                x[0] = x[0] + 'ST'

            elif (st_no[-1] =='2') and (st_no[-2] != '1'):
                x[0] = x[0] + 'ND'

            elif (st_no[-1] == '3') and (st_no[-2] != '1'):
                x[0] = x[0] + 'RD'

            else:
                x[0] = x[0] + 'TH'

        except:
            pass


        try:
            convert = int(x[1])
            st_no = [i for i in str(x[1])]

            if x[1] == '1':
                x[1] = x[1] + 'ST'

            elif x[1] == '2':
                x[1] = x[1] + 'ND'

            elif x[1] == '3':
                x[1] = x[1] + 'RD'

            elif (st_no[-1] == '1') and (st_no[-2] != '1'):
                x[1] = x[1] + 'ST'

            elif st_no[-1] =='2' and (st_no[-2] != '1'):
                x[1] = x[1] + 'ND'

            elif st_no[-1] == '3' and (st_no[-2] != '1'):
                x[1] = x[1] + 'RD'

            else:
                x[1] = x[1] +'TH'

        except:
            pass


        unus_add.append(' '.join(x)) 
        
    return st_add + unus_add




def get_state(series):
    
