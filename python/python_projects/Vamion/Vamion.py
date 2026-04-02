# my own programming language
import sys



variables = {}
def raw_eval(expr):
     tokens = expr.replace("+"," + ").replace("-"," - ").replace("*"," * ").replace("/"," / ")
     total = int(tokens[0])
     i = 1
     while i < len(tokens):
          op = tokens[i]
          num = int(tokens[i+1])
          if op == "+": total += num
          elif op == "-": total -= num
          elif op == "*": total *= num
          elif op == "/": total /= num
          i += 2
     if total.is_integer():
          return int(total)
     return total



lines = None
if len(sys.argv) > 1:
     with open(sys.argv[1], "r") as file:
          lines = file.readlines()
    

    
    
    
print(">| Vamion shell version 1.0 release" \
     "\n>| type 'help' for commands or 'doc' for documents or 'exit' to terminate")
i = 0
while True:
     if lines is not None and i < len(lines):
          user = lines[i].strip()
          i += 1
          print(">|\t" + user)
     else:
          user = input(">|\t")
        
          
     
        
     # making the 'print' script
        

     if user == "help":
          print("Hello welcome to Vamion's programming language!" \
          "\ncheck out our document at {link} to know more about it." \
          "\nthank you for using Vamion...")
     if user == "doc":
          print("Document link: {link}")
     if user == "exit":
          break
        
     if user == "output":
          print("ERROR: unfinished value, did you mean 'output(string/int)'? ")
          break
        


        # variables
     if user.startswith("var "):
          if "=" not in user:
               print("Syntax ERROR: missing '='")
               break
             
          parts = user[len("var "):].split("=", 1)
          name = parts[0].strip()
          value = parts[1].strip()
          if user.startswith('"') and user.endswith('"'):
               value = value[1:-1]
          variables[name] = value.strip('"')
             
             
             
        # strips for strings
        
          
     

        # output() statment
     if user.startswith("output(") and user.endswith(")"):
             
          inside = user[len("output("):-1].strip()

          if inside in variables:
               print(variables[inside])
             
          if inside.isdigit():
               print(int(inside))
             

          if inside.startswith('"') and inside.endswith('"'):
               print(inside[1:-1])
     
     # comments

     if user.startswith("#"): #ignored
          pass 

