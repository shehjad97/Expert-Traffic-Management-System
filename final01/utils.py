from plyer import notification  

def notify(number_plate):
    notification.notify(  
        title = "Detected Number Plate",  
        message = number_plate,  
        app_icon = None,  
        timeout = 10,  
        toast = False  
    )  