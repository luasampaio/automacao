#Lembrar Tomar Agua

import time 
from plyer import notification 

if __name__ == "__main__" : 
    while  True : 
        notification.notify( 
            title= "Beba água" , 
            message= "Continue bebendo água !!!" , app_icon = 
            " " , 
            limite = 12
        )
        time.sleep( 1800 )
