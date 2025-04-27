from database import get_name
import platform  


name = get_name()

def is_windows():
    if 'Windows' in str(platform.uname()):
        return True 
    else:
        return False

is_windows()


    
    
'''if True:
        return True
    else:
        return False'''