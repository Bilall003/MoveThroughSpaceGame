from os import name
import sys
from PyQt5 import QtCore
from PySide2 import *
from PySide2 import QtWidgets
from PySide2 import QtGui
from ui_dash_board_final import *
from ui_info_form import *
from ui_about_form import *
import MongoDB_module as db
import threading as th
from ui_summary_form import *
from ui_signup_form import *
import re

current_form_number = 106
form_counter = 0


class MainWindow (QMainWindow):

    
    def __init__(self):

        #Loading main window
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()
        self.regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        #Loading guide window
        self.info_win = QtWidgets.QMainWindow()
        self.info_ui = Ui_infowindow()
        self.info_ui.setupUi(self.info_win)


        #Loading about window
        self.about_win = QtWidgets.QMainWindow()
        self.about_ui = Ui_aboutwindow()
        self.about_ui.setupUi(self.about_win)

        #Loading summary window
        self.summary_win = QtWidgets.QMainWindow()
        self.summary_ui = Ui_summary_window()
        self.summary_ui.setupUi(self.summary_win)
        self.summary_win.showMaximized()

        #Loading signup window
        self.signup_win = QtWidgets.QMainWindow()
        self.signup_ui = Ui_signup_form()
        self.signup_ui.setupUi(self.signup_win)



        #Removing frame of all windows
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.info_win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.about_win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.summary_win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.signup_win.setWindowFlags(QtCore.Qt.FramelessWindowHint)


        #------------------------Close & Minimize button events--------------------------
        #Main Form
        self.ui.minimize_btn.clicked.connect(lambda:self.showMinimized())
        self.ui.close_win_btn.clicked.connect(lambda:self.close())

        #Close and minimize buttons actions for info form
        self.info_ui.min_btn.clicked.connect(lambda:self.info_win.showMinimized())
        self.info_ui.close_btn.clicked.connect(lambda:self.comeback(self.info_win))

        #Close and minimize buttons actions for about form
        self.about_ui.minim_btn.clicked.connect(lambda:self.info_win.showMinimized())
        self.about_ui.closewin_btn.clicked.connect(lambda:self.comeback(self.about_win))

        #Close and minimize buttons actions for summary form
        self.summary_ui.minimm_btn.clicked.connect(lambda:self.summary_win.showMinimized())
        self.summary_ui.close_button.clicked.connect(lambda:self.comeback(self.summary_win))

        #SignUp
        self.signup_ui.minimize_btn.clicked.connect(lambda:self.signup_win.showMinimized())
        self.signup_ui.close_win_btn.clicked.connect(lambda:self.comeback(self.signup_win))

        #Setting submit and clear buttons
        self.signup_ui.clear_btn.clicked.connect(lambda: self.clearstuff())
        self.signup_ui.submit_btn.clicked.connect(lambda: self.submitdata())

        #---------------------------------------------------------------------------------


        #Calling info form
        self.ui.guide_btn.clicked.connect(lambda:self.goto_info())


        #Calling about form
        self.ui.about_btn.clicked.connect(lambda:self.goto_about())


        #Calling summary form
        self.ui.summary_btn.clicked.connect(lambda:self.goto_summary())


        #Calling signup form
        self.ui.signup_btn.clicked.connect(lambda:self.goto_signup())

        #------------------------Room number button actions------------------------------
        self.ui.room109_btn.clicked.connect(lambda:self.change_room_number(109))
        self.ui.room106_btn.clicked.connect(lambda:self.change_room_number(106))
        self.ui.room111_btn.clicked.connect(lambda:self.change_room_number(111))
        #---------------------------------------------------------------------------------

        
        #------------------------Setting table dimensions---------------------------------
        self.ui.tableWidget.horizontalHeader().setMinimumSectionSize(500)
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setRowCount(5)
        self.ui.tableWidget.horizontalHeader().hide()
        self.ui.tableWidget.verticalHeader().hide()
        #---------------------------------------------------------------------------------


        self.show()
        self.update_nizaam()


    #--------------------Update the current number of room form is in----------------------
    def change_room_number(self,num):
        global current_form_number

        current_form_number = num
        self.update_nizaam()
    #--------------------------------------------------------------------------------------
    


    #--------Updates the form and runs a thread in parallel for constant updation----------
    def update_nizaam(self):

        global form_counter

        t =th.Timer(5.0,self.update_nizaam) 
        t.daemon = True
        t.start()
        
        #-------------------------Update dashboard-----------------------------------------

        if form_counter == 0:
            names = 2
            rollno = 3
            index = 0
            names_of_students = []
            rollno_of_students = []

            #Thread initializing
        
            print("Updating page.....")
            global current_form_number
            number = str(current_form_number)
            self.ui.current_room_lbl.setText("Room# "+number)
            number = "room"+number

            #Taking data from database
            room_capacity, num_of_ppl, teacher_in_class, subject = db.take_room_data(number)
            names_of_students, rollno_of_students = db.take_students_info(number)

            #Updating form according to data
            numb = int(num_of_ppl)

            room_capacity = str(room_capacity)
            num_of_ppl = str(num_of_ppl)


            self.ui.no_of_total_capacity_lbl.setText(room_capacity)
            self.ui.no_of_present_student_lbl.setText(num_of_ppl)
            self.ui.name_of_teacher_in_class_lbl.setText(teacher_in_class)
            self.ui.name_of_subject_lbl.setText(subject)

            
            if numb!=0:
                numb+=1
                self.ui.tableWidget.setRowCount(numb)
                self.ui.tableWidget.setColumnCount(2)
                self.ui.tableWidget.setItem(0,0,QTableWidgetItem("Name of Students"))
                self.ui.tableWidget.setItem(0,1,QTableWidgetItem("Reg# of Students"))

                for n in names_of_students:
                    self.ui.tableWidget.setItem(0,names,QTableWidgetItem(n))
                    self.ui.tableWidget.setItem(0,rollno,QTableWidgetItem(rollno_of_students[index]))
                    index+=1
                    names+=2
                    rollno+=2
            else:
                self.ui.tableWidget.setRowCount(1)
                self.ui.tableWidget.setColumnCount(1)
                self.ui.tableWidget.setItem(0,0,QTableWidgetItem("No student found in the room"))

        #------------------------------------------------------------------------------------------
        
        elif form_counter == 1:

            print("Updating summary page.....")
            #Taking data from database
            room_capacity106, num_of_ppl106, teacher_in_class106, subject106 = db.take_room_data("room106")
            room_capacity109, num_of_ppl109, teacher_in_class109, subject109 = db.take_room_data("room109")
            room_capacity111, num_of_ppl111, teacher_in_class111, subject111 = db.take_room_data("room111")


            #Type casting
            room_capacity106 = str(room_capacity106)
            num_of_ppl106 = str(num_of_ppl106)

            room_capacity109 = str(room_capacity109)
            num_of_ppl109 = str(num_of_ppl109)

            room_capacity111 = str(room_capacity111)
            num_of_ppl111 = str(num_of_ppl111)


            #Update for room 106
            self.summary_ui.no_of_total_capacity_lbl109_2.setText(room_capacity106)
            self.summary_ui.no_of_present_student_lbl106.setText(num_of_ppl106)
            self.summary_ui.name_of_teacher_in_class_lbl106.setText(teacher_in_class106)
            self.summary_ui.name_of_subject_lbl106.setText(subject106)

            #Update for room 109
            self.summary_ui.no_of_total_capacity_lbl109.setText(room_capacity109)
            self.summary_ui.no_of_present_student_lbl109.setText(num_of_ppl109)
            self.summary_ui.name_of_teacher_in_class_lbl109.setText(teacher_in_class109)
            self.summary_ui.name_of_subject_lbl109.setText(subject109)

            #Update for room 111
            self.summary_ui.no_of_total_capacity_lbl111.setText(room_capacity111)
            self.summary_ui.no_of_present_student_lbl111.setText(num_of_ppl111)
            self.summary_ui.name_of_teacher_in_class_lbl111.setText(teacher_in_class111)
            self.summary_ui.name_of_subject_lbl111.setText(subject111)
        
        else:
            print("On standby mode currently.....")
    #----------------------------------------------------------------------------------------------
    

    
    #-----------------------------Going to info window---------------------------------------------
    def goto_info(self):
        self.hide()
        self.info_win.show()
    #----------------------------------------------------------------------------------------------
    
    
    #-----------------------------Going to about window--------------------------------------------
    def goto_about(self):
        self.hide()
        self.about_win.show()
    #----------------------------------------------------------------------------------------------

    #-----------------------------Going to about window--------------------------------------------
    def goto_summary(self):
        self.hide()
        global form_counter
        form_counter = 1
        self.summary_win.show()
    #----------------------------------------------------------------------------------------------
    
    #-----------------------------Going to about window--------------------------------------------
    def goto_signup(self):
        self.hide()
        global form_counter
        form_counter = 2
        self.signup_win.show()
    #----------------------------------------------------------------------------------------------

    #-----------------------------Come back to main window-----------------------------------------
    def comeback(self, current_form):
        current_form.close()
        global form_counter
        form_counter = 0
        self.show()
    #----------------------------------------------------------------------------------------------


    #----------------------------Clear textboxes from signup form----------------------------------
    def clearstuff(self):
        self.signup_ui.fname_txt.clear()
        self.signup_ui.lname_txt.clear()
        self.signup_ui.email_txt.clear()
        self.signup_ui.username_txt.clear()
        self.signup_ui.password_txt.clear()
        self.signup_ui.subjectcode_txt.clear()
        self.signup_ui.varification_txt.clear()
        self.signup_ui.fname_txt.setFocus()
    #----------------------------------------------------------------------------------------------

    #-------------------------------Data add and check---------------------------------------------
    def submitdata(self):

        #Check if all text boxes are filled
        if self.empty_check():
            self.messagebox_creator("Enter all fields to continue")
            self.signup_ui.fname_txt.setFocus()
            return


        #Get varification code from database
        v_code = self.signup_ui.varification_txt.text()
        checker = db.varify_signup(v_code)


        #See if varification code matches
        if checker == "NULL":
            self.messagebox_creator("Invalid varification code")
            self.signup_ui.varification_txt.setFocus()
            return

        #User confirmation
        answer_box = QMessageBox()
        answer_box.setWindowTitle("Confirmation")
        answer_box.setIcon(QMessageBox.Question)
        answer_box.setText(f"Sign up as {checker} faculty?")
        answer_box.setWindowIcon(QtGui.QIcon("C:/fyp/UI-invigilator/icons/question.ico"))
        answer_box.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        answer = answer_box.buttonClicked.connect(self.check_confirmation)
        answer_box.exec_()


        #Data storing
        if answer:
            name_v = f"{self.signup_ui.fname_txt.text()} {self.signup_ui.lname_txt.text()}"
            email_v = self.signup_ui.email_txt.text()
            subject_code_v = self.signup_ui.subjectcode_txt.text()
            username_v = self.signup_ui.username_txt.text()
            password_v = self.signup_ui.password_txt.text()
            gender_v = self.signup_ui.gender_txt.currentText()
            
            if not (re.fullmatch(self.regex, email_v)):
                self.messagebox_creator("invalid email address!")
                self.signup_ui.email_txt.setFocus()
                return
            
            if db.username_duplecate(username_v):
                self.messagebox_creator("Username already exists!")
                self.signup_ui.username_txt.setFocus()
                return


            db.add_faculty(name_v,email_v,checker,subject_code_v,username_v,password_v,gender_v)
            msg = QMessageBox()
            msg.setWindowTitle("Result")
            msg.setIcon(QMessageBox.Information)
            msg.setText("Profile created successfully")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setWindowIcon(QtGui.QIcon("C:/fyp/UI-invigilator/icons/done.ico"))
            msg.exec_()
            self.clearstuff()
            self.signup_ui.fname_txt.setFocus()

    #User confirmation
    def check_confirmation(self, val):
        x = val.text()
        if x == "Yes":
            return(True)
        elif x=="No":
            return(False)

    #If a textbox is left unfilled
    def empty_check(self):
        fname = self.signup_ui.fname_txt.text()
        lname = self.signup_ui.lname_txt.text()
        email_v = self.signup_ui.email_txt.text()
        subject_code_v = self.signup_ui.subjectcode_txt.text()
        username_v = self.signup_ui.username_txt.text()
        password_v = self.signup_ui.password_txt.text()
        gender_v = self.signup_ui.gender_txt.currentText()

        if fname == "" or lname == "" or email_v == "" or subject_code_v == "" or username_v == "" or password_v == "" or gender_v == "":
            return True
        else:
            return False
    

    #Create an error messagebox
    def messagebox_creator(self, body):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setIcon(QMessageBox.Critical)
        msg.setText(body)
        msg.setWindowIcon(QtGui.QIcon("C:/fyp/UI-invigilator/icons/error.ico"))
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    #----------------------------------------------------------------------------------------------



if __name__ == "__main__":
    app=QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())