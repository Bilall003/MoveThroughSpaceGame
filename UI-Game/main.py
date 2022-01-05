from os import name
import sys
from PyQt5 import QtCore
from PySide2 import *
from PySide2 import QtWidgets
from PySide2 import QtGui
from ui_about_form import *
from ui_game_ui_file import *
from ui_map_form import *
from ui_username_form import *

formNumber = 1

class MainWindow (QMainWindow):

    
    def __init__(self):
        #User Data
        self.name_of_user = ""
        self.east = ""
        self.west = ""
        self.north = ""
        self.south = ""
        self.current_location = "Home"
        self.energy = 30
        self.money = 30

        #Loading login window
        QMainWindow.__init__(self)
        self.ui = Ui_login()
        self.ui.setupUi(self)

        #Loading dashboard window
        self.dashboard_win =  QtWidgets.QMainWindow()
        self.dashboard_ui = Ui_GameWindow()
        self.dashboard_ui.setupUi(self.dashboard_win)
        self.dashboard_ui.currentLocation_lbl.setText("Current Location: "+self.current_location)

        #Loading About window
        self.about_win =  QtWidgets.QMainWindow()
        self.aboutui = Ui_About_window()
        self.aboutui.setupUi(self.about_win)

        #Loading map window
        self.map_win =  QtWidgets.QMainWindow()
        self.map_ui = Ui_map_window()
        self.map_ui.setupUi(self.map_win)

        #---------------------------Goto buttons events--------------------------------------
        #Submit button click event
        self.ui.submit_btn.clicked.connect(lambda: self.goto_dashboard())

        #About Button click event
        self.dashboard_ui.about_btn.clicked.connect(lambda: self.goto_about())

        #Map button click event
        self.dashboard_ui.map_btn.clicked.connect(lambda: self.goto_map())
        #-------------------------------------------------------------------------------------

        self.dashboard_ui.action_btn.clicked.connect(lambda:self.actionfunction())


        #-----------------------------Back Button clicked------------------------------------
        self.aboutui.back_btn.clicked.connect(lambda: self.comeback(self.about_win))
        self.map_ui.back_btn.clicked.connect(lambda: self.comeback(self.map_win))
        #------------------------------------------------------------------------------------


        #-------------------------------Go Button Clicked------------------------------------
        self.dashboard_ui.go_btn.clicked.connect(lambda: self.updateLocation())

        self.show()

    #-----------------------------Go to different forms---------------------------------------

    #Take user to the main screen after name validation
    def goto_dashboard(self):

        #Validating if user entered an acceptable name or not
        self.name_of_user = self.ui.name_txt.text()
        
        
        if self.name_of_user != "":
            #Go to next form if name of user is valid
            self.dashboard_ui.player_name_lbl.setText("Player Name: "+self.name_of_user)
            self.hide()
            self.dashboard_win.show()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Enter a valid name to continue")
            msg.setWindowIcon(QtGui.QIcon(":/icons/icons/frown.svg"))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
    
    #Go to about form when about button is clicked
    def goto_about(self):
        self.dashboard_win.hide()
        self.about_win.show()

    #Go to map form when map button is clicked
    def goto_map(self):
        self.dashboard_win.hide()
        self.map_win.show()

    #Come back to dashboard when back button is clicked
    def comeback(self, form):
        form.hide()
        self.dashboard_win.show()
    
    #------------------------------------------------------------------------------------------

    #---------------------------------Update Location------------------------------------------
    def updateLocation(self):
        ans = self.dashboard_ui.action_txt.text()
        north_value = self.dashboard_ui.north_lbl.text()
        south_value = self.dashboard_ui.south_lbl.text()
        east_value = self.dashboard_ui.east_lbl.text()
        west_value = self.dashboard_ui.west_lbl.text()

        #Value formatting
        ans = ans.lower()
        north_value = north_value[10:]
        south_value = south_value[10:]
        east_value = east_value[9:]
        west_value = west_value[9:]
        east_value = east_value.lower()
        south_value = south_value.lower()
        west_value = west_value.lower()
        north_value = north_value.lower()

        #Answer validating
        if ans == "north":
            if north_value == "nothing":
                self.null_location()
            else:
                self.set_new_location(ans)

        elif ans == "south":
            if south_value == "nothing":
                self.null_location()
            else:
                self.set_new_location(ans)
        
        elif ans == "east":
            if east_value == "nothing":
                self.null_location()
            else:
                self.set_new_location(ans)
        
        elif ans == "west":
            if west_value == "nothing":
                self.null_location()
            else:
                self.set_new_location(ans)
        
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Enter a valid action")
            msg.setWindowIcon(QtGui.QIcon(":/icons/icons/frown.svg"))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
    
    def null_location(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setIcon(QMessageBox.Critical)
        msg.setText("There is nothing in the direction you entered, try again")
        msg.setWindowIcon(QtGui.QIcon(":/icons/icons/frown.svg"))
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    
    #--------------------------Updating contents of main form----------------------------------
    
    def set_new_location(self, direction):
        self.current_location = self.current_location.lower()


        #Condition if home is current location
        if self.current_location == "home" and direction == "west":
            self.current_location = "Yard"
            self.update_wids("Yard","Home","University","Market","Sidewalk")



        #Conditions if Yard is current location
        elif self.current_location == "yard" and direction == "east":
            self.current_location = "Home"
            self.update_wids("Home","Nothing","Yard","Nothing","Nothing")

        elif self.current_location == "yard" and direction == "west":
            self.current_location = "University"
            self.update_wids("University","Yard","Nothing","Nothing","Nothing")

        elif self.current_location == "yard" and direction == "north":
            self.current_location = "Sidewalk"
            self.update_wids("Sidewalk","Nothing","Work Office","Yard","Mall (Ground Floor)")

        elif self.current_location == "yard" and direction == "south":
            self.current_location = "Market"
            self.update_wids("Market","Nothing","Nothing","Nothing","Yard")



        #Conditions if Market is current location
        elif self.current_location == "market" and direction == "north":
            self.current_location = "Yard"
            self.update_wids("Yard","Home","University","Market","Sidewalk")




        #Conditions if University is current location
        elif self.current_location == "university" and direction == "east":
            self.current_location = "Yard"
            self.update_wids("Yard","Home","University","Market","Sidewalk")



        #Conditions if Sidewalk is current location
        elif self.current_location == "sidewalk" and direction == "north":
            self.current_location = "Mall (Ground Floor)"
            self.update_wids("Mall (Ground Floor)","Pizzeria","Brasserie","Sidewalk","Mall (First floor)")

        elif self.current_location == "sidewalk" and direction == "south":
            self.current_location = "Yard"
            self.update_wids("Yard","Home","University","Market","Sidewalk")

        elif self.current_location == "sidewalk" and direction == "west":
            self.current_location = "Work Office"
            self.update_wids("Work Office","Sidewalk","Nothing","Nothing","Nothing")



        #Conditions if Mall (Ground Floor) is current location
        elif self.current_location == "mall (ground floor)" and direction == "north":
            self.current_location = "Mall (First Floor)"
            self.update_wids("Mall (First Floor)","Cloth and Shoes shop","Pharmacy","Mall (Ground Floor)","Nothing")

        elif self.current_location == "mall (ground floor)" and direction == "south":
            self.current_location = "SideWalk"
            self.update_wids("SideWalk","Nothing","Work Office","Yard","Mall (Ground Floor)")

        elif self.current_location == "mall (ground floor)" and direction == "west":
            self.current_location = "Brasserie"
            self.update_wids("Brasserie","Mall (Ground Floor)","Nothing","Nothing","Nothing")

        elif self.current_location == "mall (ground floor)" and direction == "east":
            self.current_location = "Pizzeria"
            self.update_wids("Pizzeria","Nothing","Mall (Ground Floor)","Nothing","Nothing")

        
        #Conditions if Pizzeria is current location
        elif self.current_location == "pizzeria" and direction == "west":
            self.current_location = "Mall (Ground Floor)"
            self.update_wids("Mall (Ground Floor)","Pizzeria","Brasserie","Sidewalk","Mall (First floor)")



        #Conditions if Brasserie is current location
        elif self.current_location == "brasserie" and direction == "east":
            self.current_location = "Mall (Ground Floor)"
            self.update_wids("Mall (Ground Floor)","Pizzeria","Brasserie","Sidewalk","Mall (First floor)")



        #Condition if Mall (First floor) is current location
        elif self.current_location == "mall (first floor)" and direction == "east":
            self.current_location = "Cloth and Shoes shop"
            self.update_wids("Cloth and Shoes shop","Nothing","Mall (First floor)","Nothing","Nothing")

        elif self.current_location == "mall (first floor)" and direction == "west":
            self.current_location = "Pharmacy"
            self.update_wids("Pharmacy","Mall (First Floor)","Nothing","Nothing","Nothing")

        elif self.current_location == "mall (first floor)" and direction == "south":
            self.current_location = "Mall (Ground Floor)"
            self.update_wids("Mall (Ground Floor)","Pizzeria","Brasserie","Sidewalk","Mall (First floor)")

        
        #Conditions if Pizzeria is current location
        elif self.current_location == "cloth and shoes shop" and direction == "west":
            self.current_location = "Mall (First Floor)"
            self.update_wids("Mall (First Floor)","Cloth and Shoes shop","Pharmacy","Mall (Ground Floor)","Nothing")



        #Conditions if Brasserie is current location
        elif self.current_location == "pharmacy" and direction == "east":
            self.current_location = "Mall (First Floor)"
            self.update_wids("Mall (First Floor)","Cloth and Shoes shop","Pharmacy","Mall (Ground Floor)","Nothing")

    def update_wids(self,location_name, east, west, south, north):
        self.dashboard_ui.currentLocation_lbl.setText("Current Location: "+location_name)
        self.dashboard_ui.east_lbl.setText("On East: "+east)
        self.dashboard_ui.west_lbl.setText("On West: "+west)
        self.dashboard_ui.north_lbl.setText("On North: "+north)
        self.dashboard_ui.south_lbl.setText("On South: "+south)
    
    #-------------------------------------------------------------------------------------------------

    def actionfunction(self):
        loc = self.current_location.lower()

        if loc == "home":
            self.home_buttons()
        elif loc == "yard":
            self.yard_buttons()
        elif loc == "university":
            self.university_buttons()
        elif loc == "work place":
            self.work()
        elif loc == "mall (ground floor)" or loc == "mall (first floor)" or loc == "pharmacy" or loc == "cloth and shoes shop" or loc == "brasserie" or loc == "pizzeria":
            self.mall_buttons() 

    #-----------------------------Action Buttons-------------------------------------------------
    def home_buttons(self):
        answer = self.show_msg("Do you want to rest?")
        self.energy += 10
        self.check_results()

        energy_v = str(self.energy)
        energy_v ="Energy: "+energy_v
        

        if answer:
            self.dashboard_ui.energy_lbl.setText(energy_v)

    def yard_buttons(self):
        answer = self.show_msg("Do you want to take a walk?")
        self.energy -=5
        self.check_results()

        energy_v = str(self.energy)
        energy_v ="Energy: "+energy_v

        if answer:
            self.dashboard_ui.energy_lbl.setText(energy_v)

    def university_buttons(self):
        answer = self.show_msg("Do you want to study?")
        self.energy -=5
        self.money -=10
        self.check_results()

        energy_v = str(self.energy)
        energy_v ="Energy: "+energy_v

        money_v = str(self.money)
        money_v = "Money: "+money_v

        if answer:
            self.dashboard_ui.energy_lbl.setText(energy_v)
            self.dashboard_ui.money_lbl.setText(money_v)

    def work(self):
        answer = self.show_msg("Do you want to Work?")
        self.energy -=20
        self.money +=10
        self.check_results()

        energy_v = str(self.energy)
        energy_v ="Energy: "+energy_v

        money_v = str(self.money)
        money_v = "Money: "+money_v

        if answer:
            self.dashboard_ui.energy_lbl.setText(energy_v)
            self.dashboard_ui.money_lbl.setText(money_v)

    def mall_buttons(self):
        answer = self.show_msg("Do you want to do shopping?")
        self.energy -=20
        self.money -=50
        self.check_results()

        energy_v = str(self.energy)
        energy_v ="Energy: "+energy_v

        money_v = str(self.money)
        money_v = "Money: "+money_v

        if answer:
            self.dashboard_ui.energy_lbl.setText(energy_v)
            self.dashboard_ui.money_lbl.setText(money_v)

    def check_results(self):
        if self.energy <=0 or self.money<=0:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("You lost because the resourses are low")
            msg.setWindowIcon(QtGui.QIcon(":/icons/icons/frown.svg"))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.close()
            sys.exit()
        elif self.energy >=300:
            msg = QMessageBox()
            msg.setWindowTitle("Congratulations")
            msg.setIcon(QMessageBox.warning)
            msg.setText("You have won the game")
            msg.setWindowIcon(QtGui.QIcon(":/icons/icons/frown.svg"))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.close()
            sys.exit()


    def show_msg(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Question")
        
        msg.setText(message)
        msg.setWindowIcon(QtGui.QIcon(":/icons/icons/triangle.svg"))
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        answer = msg.buttonClicked.connect(self.check_ans)
        msg.exec_()
        return answer

    def check_ans(self, i):
        i = str(i)
        i = i.lower()

        if i == "yes":
            return True
        else:
            return False

    


if __name__ == "__main__":
    app=QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())