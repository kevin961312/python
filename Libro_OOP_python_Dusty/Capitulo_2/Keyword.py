# include keyword library in this program 
import keyword 
# Function to check whether the given  
# string is a keyword or not  
def isKeyword(word) : 
  
    # kwlist attribute of keyword 
    # library return list of keywords 
    # present in current version of 
    # python language. 
    keyword_list = keyword.kwlist 
  
    # check word in present in 
    # keyword_list or not. 
    if word in keyword_list : 
        return "Yes"
    else : 
        return "No"
  

# Driver Code 
if __name__ == "__main__" : 
  
    print(isKeyword("formatter")) 
    print(isKeyword("for")) 