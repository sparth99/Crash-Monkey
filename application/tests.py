import logging

logging.basicConfig(filename='app.log',
                    filemode='w', 
                    format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s'
                    )
                    
def open_file(name):
    try:
        f = open(name,'r')
    except Exception as e:
        logging.error("Exception occured", exc_info=True)
    finally:
        f.close()

def write_file(name,num=400000):
    try:
        f = open(name,'a+')
        for i in range(0,num):
            f.write("SPAM\n")
    except Exception as e:
        logging.error("Exception occured", exc_info=True)
    finally:
        f.close()

write_file("spam.txt")







