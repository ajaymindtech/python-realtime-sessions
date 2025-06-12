# Subject class definition
class Subject:
    # Initialize Subject with empty observers list
    def __init__(self):
        self._observers = [] # List to store observer objects

    # Method to add new observer to list
    def attach(self, observer):
        self._observers.append(observer) # Add observer to list

    # Method to notify all observers
    def notify(self):
        # Loop through each observer
        for observer in self._observers:
            observer.update() # Call update method on observer

# Base Observer class with empty update method
class Observer:
    def update(self):
        pass # Empty implementation to be overridden

# EmailObserver inherits from Observer
class EmailObserver(Observer):
    # Override update method
    def update(self):
        print("Sending email notification") # Print notification message

# Create Subject instance
subject = Subject()

# Create EmailObserver instance
observer = EmailObserver()

# Attach observer to subject
subject.attach(observer)

# Notify observers (triggers email notification)
subject.notify() # Output: Sending email notification
