import pandas as pd

class Address:
    
    
    street_suffixes =['PATH','BRIDGE','BAY','TECH','ALLEY','CENTER','PIERS','RDG','RIVER','HL','COVE','ROW','PIER','TNPK','FAIR','ISLAND','MALL','AVE','THRU','HILL','RIDGE','PKW','COURSE','PARKLANE','THRUWAY','WAY','HEIGHTS','SLIP','EXPY','ST','PLAZA','PKWY','GREEN','CAMP','TURNPIKE','BL','OVAL','LOOP','BLVD','DR','CIRCLE','WALK','HIGHWAY','CONCOURSE', 'SQUARE','CRESCENT', 'AVENUE', 'ROAD', 'STREET', 'BOULEVARD', 'PLACE', 'DRIVE', 'LANE', 'PARKWAY', 'PARK','EXPRESSWAY', 'TERRACE', 'RD', 'COURT']
    
    
    exceptions = ["B'WAY",'PCT','FDR','PPW','GCP','GREENWAY','CPW','KINGSBRIDGE','ESPLANADE','GRANDCONCOURSE','BQE','KINGSHIGWY','BOWERY','BROADWAY']
    
    
    def __init__(self, full_address):
        self.full_address = full_address
        self.suffixes = street_suffixes
        self.exceptions = exceptions
        
    def append_exception(self, exception):
        '''
        Description: Appends an exception to exceptions list; which is a list of streets that do not have a typical suffix for a 
                     street. Typical suffixes are things like 'Avenue', 'Street', 'Road', see street_suffixes list. Typical 
                     streets that do not have these suffixes are streets like Broadway and Bowery. See street_suffixes list.
                     
        Parameters: 
                    exception - (str) The exception street name to be appended
                    
        Returns:
                    None
                    
        '''
        
        self.exceptions.append(exception)
        
        
        