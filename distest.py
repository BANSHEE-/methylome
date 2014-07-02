import os
import glob

## list of directories#########
#still would like to set this up using os.abspath instead, talk to dakota/claus
data_dir = "/home/blanche/Desktop/wilke/DNA_Methylation/JHU_USC__HumanMethylation27/Level_3"

working_dir ="/home/blanche/Desktop/wilke/DNA_Methylation/JHU_USC__HumanMethylation27"

## functions

def determine_file_type( data_fh ):

  for line in data_fh:
    line = line.strip( '\r\n' )
    fields = line.split( '\t' )
    if fields[0] == "barcode":
      ver = "A" #why did dakota suggest *type* in this instance?
      return ver
    elif fields[0] == "Hybridization REF":
      ver = "B"
      return ver
    break 
    #break so that the loop will end after only one line iteration through the file
    
def discretize_A( data_fh, outlist ):
  
  print "Function A not yet written."

  return
  
def discretize_B( data_fh, outlist ):
  for line in data_fh:
  # strip the line of whitespace characters and separate by tabs is this redundant!!
    line = line.strip( '\r\n' )
    fields = line.split( '\t' )


    ref = fields[ 0 ]
  

    level = "NA"  
    beta = fields[ 1 ]
#continue goes to next iteration of the loop to skip the headers
    if beta[0:5] == "TCGA":
    #header differs in each file. index string to check for first 4 chr TCGA
      print "TCGA"
    if beta == "Beta_value":
      continue
#now we have gotten past ver b header
    if beta != "NA":
  
      beta = float(beta)
      
      if beta <= 0.2:
        level = 0
      elif beta >= 0.6:
        level = 2
      else:
        level = 1
  
  gene = fields[ 2 ]
  chrome = fields[ 3 ]
  gencoord = fields[ 4 ]

  # 6. write newline
  disline = "%s\t%s\t%s\t%s\t%s\n" % ( ref, level, gene, chrome, gencoord )
  #return of the function
  outlist.append(disline)
  

  
  
  
  
  


###################
## Main function ##
###################

outlist =[]

# 1. access all files in a directory with os
files =[]
os.chdir( data_dir )
for file in glob.glob( "*.txt" ):
  filename = os.path.join( data_dir, file )
  files.append( filename )
os.chdir( working_dir )
  



# 2. iterate through the level 3 directory
for file in files:
  # 3. open data file
  data_fh = open(file, "r")
  # determine if the file is type A or type B
  ver = determine_file_type( data_fh )    
  # run the code to discretize beta values, according to type
  if ver == "A":
    # do A function
    discretize_A( data_fh , outlist )
  elif ver == "B":
    discretize_B( data_fh , outlist )
  else:
    print "ERROR >___<"
  
print outlist #only getting last line of files ... hmmmm ...




'''

  print type



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
      


      
   



    


