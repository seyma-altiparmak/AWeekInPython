#PRINT#
#FOR : FILE --- PRINT FUNCTION
import sys 

#Print-Functions:
a = 2001
b = 1968

# print("")

#sep = "only string"
print(a,b,sep="-")
#OUTPUT:
    # 2001-1968 

#end
print(a,b,end="-")
#OUTPUT:
    # 2001 1968-

#file
print(a,b,file=sys.stdout)

#flush = TRUE & FALSE
print(a,b,flush="flush")

# print('') 
print('Python is a "special" language.')

# print(""" """)
print(""" 

░░▒░░█░
░░▒░█
░░░█
░░█░░░░███████
░██░░░██▓▓███▓██▒
██░░░█▓▓▓▓▓▓▓█▓████
██░░██▓▓▓(◐)▓█▓█▓█
███▓▓▓█▓▓▓▓▓█▓█▓▓▓▓█
▀██▓▓█░██▓▓▓▓██▓▓▓▓▓█
░▀██▀░░█▓▓▓▓▓▓▓▓▓▓▓▓▓█
░░░░▒░░░█▓▓▓▓▓█▓▓▓▓▓▓█
░░░░▒░░░█▓▓▓▓█▓█▓▓▓▓▓█
░▒░░▒░░░█▓▓▓█▓▓▓█▓▓▓▓█
░▒░░▒░░░█▓▓▓█░░░█▓▓▓█
░▒░░▒░░██▓██░░░██▓▓██
████████████████████████

""")