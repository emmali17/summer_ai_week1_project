# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        self.list_of_names = []

        self.list_of_ages = []
        
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def create_account(self):
        name = input("Your Name: ")
        age = input("Your age: ")
        pers = Person(name, age)
        self.list_of_people.append(pers)
        self.list_of_names.append(name)
        print("Creating ...")
        print("\nAccount completed")
        #implement function that creates account here
    



class Person:

    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []
        self.inbox = []

    def add_friend(self, person_object):
        self.friendlist.append(person_object)
        return self.friendlist
        #implement adding friend. Hint add to self.friendlist
        
    def block_friend(self, person_object):
        self.friendlist.remove(person_object)
        return self.friendlist

    def send_message(self, friend_name, message, this_social_network, name1):
        index_of_name2 = this_social_network.list_of_names.index(friend_name)
        inbox_of_friend = this_social_network.list_of_people[index_of_name2].inbox
        inbox_of_friend.append("from " + name1 + ": " + message)
        #implement sending message to friend here
