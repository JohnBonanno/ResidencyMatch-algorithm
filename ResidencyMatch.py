'''
ResidencyMatch.py

This algorithm operates by reading an input file of the form

[residents | hospitals] preference 1, preference 2, preference 3, preference 4, ...

Any whitespace occurring in the input files is stripped off.

Usage:

    python ResidencyMatch.py [residents preference file] [hospitals preference file]

[Abdullah A, John B]

'''

import sys
import csv

class ResidencyMatch:

    # behaves like a constructor
    def __init__(self):
        '''
        Think of
        
            unmatchedHospitals
            residentsMappings
            hospitalsMappings
            matches
            
        as being instance data for your class.
        
        Whenever you want to refer to instance data, you must
        prepend it with 'self.<instance data>'
        '''
        
        # list of unmatched hospitals
        self.unmatchedHospitals = [ ]

        # list of unmatched residents
        self.unmatchedResidents = [ ]
        
        # dictionaries representing preferences mappings
        
        self.residentsMappings = { }
        self.hospitalsMappings = { }
        
        # dictionary of matches where mapping is resident:hospital
        self.matches = { }
        
        # read in the preference files
        
        '''
        This constructs a dictionary mapping a resident to a list of hospitals in order of preference
        '''
        
        prefsReader = csv.reader(open (sys.argv[1],'r'), delimiter = ',')
        for row in prefsReader:
            resident = row[0].strip()

             # all hospitals are initially unmatched
            self.unmatchedResidents.append(resident)

            # maps a resident to a list of preferences
            self.residentsMappings[resident] = [x.strip() for x in row[1:]]
            
            # initially have each resident as unmatched
            self.matches[resident] = None
        
        '''
        This constructs a dictionary mapping a hospital to a list of residents in order of preference
        '''
        
        prefsReader = csv.reader(open (sys.argv[2],'r'), delimiter = ',')
        for row in prefsReader:
            
            hospital = row[0].strip()
            
            # all hospitals are initially unmatched
            self.unmatchedHospitals.append(hospital)
            
            # maps a resident to a list of preferences
            self.hospitalsMappings[hospital] = [x.strip() for x in row[1:]] 
    
            
    def reportMatches(self):


        print("\n" + str(self.matches))

            
    def runMatch(self):
                     
        '''
        It is suggested you use the debugger or similar output statements
        to determine what the contents of the data structures are
        '''  
        
        # create dict to store hospital matches
        hospitalMatches = {}

        for i in self.unmatchedHospitals:
            hospitalMatches[i] = ""

        # this becomes False when all residents are matched
        unmatched = True

        # stores the resident's index
        idx = 0

        resident = ''

        # loop over unmatched residents
        while (unmatched):

            # End loop when all residents got matched
            if (None not in self.matches.values()):
                unmatched = False
                break

            # get the resident name with the given index
            resident = self.unmatchedResidents[idx] 

            # pop the hospital from the resident's list 
            hospital = self.residentsMappings[resident].pop(0)
            
            # if the hospital in the resident's list is unmatched, match them and increment index
            if hospitalMatches[hospital] == '':
                    self.matches[resident] = hospital 
                    hospitalMatches[hospital] = resident
                    idx = idx + 1 
                
            else:
                # get the resident that is currently matched with the hospital
                matchedResident = hospitalMatches[hospital] 
                
                # check if the current resident is higher in priority than the matched resident
                if (self.hospitalsMappings[hospital].index(resident) < self.hospitalsMappings[hospital].index(matchedResident)):

                    # unmatch the matched resident
                    self.matches[matchedResident] = None

                    # update index to return to the unmatched resident
                    idx = self.unmatchedResidents.index(matchedResident)

                    # match hospital and current resident
                    self.matches[resident] = hospital
                    hospitalMatches[hospital] = resident
                        


if __name__ == "__main__":
   
    # some error checking
    if len(sys.argv) != 3:
        print('ERROR: Usage\n python ResidencyMatch.py [residents preferences] [hospitals preferences]')
        quit()

    # create an instance of ResidencyMatch 
    match = ResidencyMatch()

    # now call the runMatch() function
    match.runMatch()
    
    # report the matches
    match.reportMatches()
