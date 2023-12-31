from plyer import notification
import time
import tkinter
import threading
import yaml
import os
import random
import ctypes



class PyAdware:

    def __init__(self):
               
        # Get the directory containing the script
        script_directory = os.path.dirname(os.path.abspath(__file__))
        
        with open(f'{script_directory}\\config.yaml', 'r') as config_file:
            self.config = yaml.safe_load(config_file)
        
        #print(self.config['ad_texts'])
        #self.run_ads()
        self.show_message_box()
        
        

    def run_ads(self):

        num_of_ads = len(self.config['ad_texts'])
        counter = 1
        
        while True:

            
            rand_pos = random.randint(0,num_of_ads-1)
            # Set notification title and message
            title = 'Important'
            message = f"This is the {counter}. notification message.\n{self.config['ad_texts'][rand_pos]}"

            # Configure notification
            notification_settings = {
                'title': title,
                'message': message,
                'timeout': 2,  # Notification will disappear after xy seconds
            }

            # Display notification
            notification.notify(**notification_settings)

  
            

            # Keep the script running for a while (to see the notification)
            time.sleep(6)
            counter += 1
        
    # Function to display a message box
    def show_message_box(self):
        

        
        num_of_ads = len(self.config['ad_texts'])
        counter = 1
        
        while True:

            rand_pos = random.randint(0,num_of_ads-1)
            # Set notification title and message
            title = 'Important'
            message = f"This is the {counter}. notification message.\n{self.config['ad_texts'][rand_pos]}"

            ctypes.windll.user32.MessageBoxW(0, message, title, 1)
  
            

            # Keep the script running for a while (to see the notification)
            time.sleep(6)
            counter += 1
    


# Example usage
if __name__ == "__main__":

    # Create an instance of the class
    pyadware = PyAdware()












