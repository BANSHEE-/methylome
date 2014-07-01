import os
import glob

## list of directories

data_dir = "/home/blanche/Desktop/wilke/DNA_Methylation/JHU_USC__HumanMethylation27/Level_3"

working_dir ="/home/blanche/Desktop/wilke/DNA_Methylation/JHU_USC__HumanMethylation27"

## functions

def determine_file_type( file ):

  type = 0

  return type

def discretize_A( file, newlines ):
  
  print "Function A not yet written."

  return
  
def discretize_B( file, newlines ):

  print "Function B not yet written."

  return


###################
## Main function ##
###################

newlines =[]

# 1. access all files in a directory with os
files =[]
os.chdir( data_dir )
for file in glob.glob( "*.txt" ):
  filename = os.path.join( data_dir, file )
  files.append( filename )
os.chdir( working_dir )
  
print files


# 2. iterate through the level 3 directory
for file in files:
  # 3. open data file
  data_fh = open(file, "r")
  # determine if the file is type A or type B
  type = determine_file_type( file )    
  # run the code to discretize beta values, according to type
  if type == "A":
    # do A function
    discretize_A( file, newlines )
  elif type == "B":
    discretize_B( file, newlines )
  else:
    print "ERROR! invalid file type"


  print type



'''
      # 4. seperate and strip
      for line in data:
        line = line.strip( '\r\n' )
        
      # 5. determine if a or b version
      
      # 6. discretize beta function called determined by version
        #.7 construct new line with discretized beta
        # 8. append discretized line to list
         
      # 9. close data file
      # 10. open out put file in "w" mode
      # 11. add list of discretized lines to output file
      # 12. close output file (wiil i just conitnuosuly open and close this out put file the whole time?
'''    
      


      
   



    


