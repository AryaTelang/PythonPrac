try:
    n=int(input("Enter num"))
    res=5/n
except:
    print("Divided by 0")
else:
    print(res)
finally:# print error or not
    print("Code executed")

k=int(input("Enter age of child"))
if(k>12):
    raise Exception("Too old for registration") # choose ur exception
    pass
else:
    print("Accepted")


try:
    imp="import "+ input("Enter module to import")
    exec(imp)# import error

    x=int(input("Enter number to divide"))# 0 error
    res=10/x
    
    lis=[1,4,2,2,1,3,6,3]
    print(lis)
    i=int(input("Enter index"))
    print(lis[i])# Index error/ Keyboard error  Ctrl+c

    dick={"Arya": 10,"Pratham":11,"Kanye": 9}
    print(dick)
    xy=input("Enter key")
    print(dick[xy])

except NameError:
    print("Name Error")
except ValueError:
    print("Invalid literal.")
except ImportError:
    print("Module not found.")
except ZeroDivisionError:
    print("Division by zero.")
except SyntaxError:
    print("Comma missing.")
except RuntimeError:
    print("May be meaningless.")
except KeyboardInterrupt:
    print()
    print("Program was interrupted.")
except KeyError:
    print("The requested key wasn't found.")
except:
    print("Something wrong in input.")
else:
    print("No exceptions.")
finally:
    print("Finally call is executed.")


class BaseError(Exception):# inherit from exception class
    pass

class HighValueError(BaseError):
    pass

class LowValueError(BaseError):
    pass


value = 29


while(1):
    try:
        n = int(input("Enter a number: "))
        if n > value:
            raise HighValueError
        elif n < value:
            raise LowValueError
    except LowValueError:
        print("Very low value, give i/p again.")
        print()
    except HighValueError:
        print("Very high value, give i/p again.")
        print()
    else:   
        print("Nice! Correct answer!")
        break
