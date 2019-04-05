try:
    with open("test.txt",'r') as r:
        s=s
        pass
except FileNotFoundError:
    print("no such file exist my lord")
except Exception:
    print("no clues")
    
    try:
        with open("tewst.txt",'r') as r:
            print(r.read())
    
        
  
except FileNotFoundError as f:
    print(f)
except Exception as e:
    print(e)
else:
    print("executing else")  #else block will run when there is no error in the try block  
finally:
    print("exection of finall block being done")  #this bock exectes no matter if there is an error or not




try:
    f = open('curruptfile.txt')
    # if f.name == 'currupt_file.txt':
    #     raise Exception
except IOError as e:
    print('First!')
except Exception as e:
    print('Second')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

print('End of program')
