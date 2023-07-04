#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui



#Create instance of main social network object
ai_social_network = SocialNetwork()
list_of_people_here = ai_social_network.list_of_people
list_of_names_here = ai_social_network.list_of_names
list_of_ages_here = ai_social_network.list_of_ages

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()

        elif choice == "2":
            name1 = input("Account Name: ")
            index_of_name1 = list_of_names_here.index(name1)
            me = list_of_people_here[index_of_name1]
            #Handle inner menu here
            while True:
                inner_menu_choice = social_network_ui.manageAccountMenu()
                if inner_menu_choice == "6":
                    break
                else:
                    if inner_menu_choice == "1":
                        sub_choice = social_network_ui.editMyDetails()
                        if sub_choice == "1":
                            name = input("New Name: ")
                            print("Saved!")
                            list_of_names_here[index_of_name1] = name
                        if sub_choice == "2":
                            age = input("Your Age: ")
                            print("Saved!")
                            list_of_ages_here[index_of_name1] = age
                        if sub_choice == "3":
                            blocked_friend = input("Friend Name You Want to Block: ")
                            me.block_friend(blocked_friend)
                    if inner_menu_choice == "2":
                        new_friend = str(input("Friend name: "))
                        if new_friend in list_of_names_here:
                            me.add_friend(new_friend)
                            print("Friend added!")
                            index_of_friend1 = list_of_names_here.index(new_friend)
                            friendlist_of_friend = list_of_people_here[index_of_friend1].friendlist
                            friendlist_of_friend.append(name1)
                        else:
                            print("Friend not Found...")
                    if inner_menu_choice == "3":
                        print("Friend List: ")
                        print(me.friendlist)
                    if inner_menu_choice == "4":
                        friend_name = input("Send message to who?: ")
                        if friend_name in me.friendlist:
                            message = input("Send message to " + friend_name + ": ")
                            me.send_message(friend_name, message, ai_social_network, name1)
                        # friend_name_message = input("Send message to who?: ")
                        # if friend_name_message in me.friendlist:
                        #    message1 = input("Send message to " + friend_name_message + ": ")
                        #    index_of_name2 = list_of_names_here.index(friend_name_message)
                        #    inbox_of_friend = list_of_people_here[index_of_name2].inbox
                        #    inbox_of_friend.append("from " + name1 + ": " + message1)
                        else:
                            print("this person is not your friend")
                            print("\ncannot send message!")
                    if inner_menu_choice == "5":
                        print(me.inbox)
                
        elif choice == "3":
            print("Thank you for visiting. Goodbye!")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
