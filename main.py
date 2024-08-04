# This is the document for the main code of Manager App
##### By: Arav Raghunathan

# Imports
import os

import kivy.core.window
from kivymd.app import MDApp
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen, Screen
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogButtonContainer, MDDialogSupportingText
from ManagerHelper import manager_helper
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon
from kivymd.uix.widget import Widget
from kivymd.uix.behaviors import RotateBehavior
from kivymd.uix.list import MDListItemTrailingIcon
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList, MDListItem, MDListItemHeadlineText, MDListItemSupportingText, MDListItemTrailingCheckbox, MDListItemLeadingIcon
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText, MDTextFieldHelperText, MDTextFieldTrailingIcon
from TaskManager import TaskManager
from kivymd.uix.widget import MDAdaptiveWidget
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.imagelist import MDSmartTile, MDSmartTileImage
from kivy.core.window import Window
import datetime


Window.size = (320, 600)


# SQL Database Setup
import sqlite3
new_connect = sqlite3.connect("database.db")
cursor = new_connect.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS login (first_name TEXT, last_name TEXT, username TEXT, password TEXT, age INTEGER, list_contents TEXT, intro_vision TEXT, intro_vision_date TEXT,  wake_times TEXT, sleep_times TEXT)")
new_connect.commit()
# More Inheritance
# Screen Manager Application
class LoginScreen(Screen):
    pass
class CreateLoginScreen(Screen):
    pass
class HomeScreen (Screen):
    pass
class AccountScreen (Screen):
    pass
class TaskListScreen (Screen):
    pass
class IntroVisionScreen (Screen):
    pass
class IntroVisionScreenOne (Screen):
    pass
class AboutScreen (Screen):
    pass
class OwnerScreen (Screen):
    pass
class IntroVisionScreenTwo (Screen):
    pass
class IntroVisionScreenThree (Screen):
    pass

class PreviousScoresScreen (Screen):
    pass

class DreamWaveScreen (Screen):
    pass

class AravScreen (Screen):
    pass

class AyanScreen(Screen):
    pass

class ShashankScreen (Screen):
    pass
class DreamWaveScreenTwo (Screen):
    pass

main = ScreenManager()
main.add_widget(LoginScreen(name="login"))
main.add_widget(CreateLoginScreen(name="create"))
main.add_widget(HomeScreen(name="home"))
main.add_widget(AccountScreen(name="main"))
main.add_widget(TaskListScreen(name="task_l"))
main.add_widget(IntroVisionScreen(name="intro_v"))
main.add_widget(IntroVisionScreenOne(name="intro_v1"))
main.add_widget(AboutScreen(name="about"))
main.add_widget(OwnerScreen(name="owner"))
main.add_widget(IntroVisionScreenTwo(name="intro_v2"))
main.add_widget(IntroVisionScreenThree(name="intro_v3"))
main.add_widget(PreviousScoresScreen(name="prev"))
main.add_widget(DreamWaveScreen(name="dream_w"))
main.add_widget(AravScreen(name="arav"))
main.add_widget(AyanScreen(name="ayan"))
main.add_widget(ShashankScreen(name="shashank"))
main.add_widget(DreamWaveScreenTwo(name="dream_w2"))

# Main App Class


class Manager (MDApp):
    def build (self):
        # 1. Initializing objects and variables used through the app
        self.task_m = TaskManager()
        self.task_list = []
        self.done_list = []
        self.task_name = ""
        self.priority = ""
        self.dates = []
        self.answers = []
        self.intro_vision_score = 0
        self.intro_vision_scores = []
        self.libraries = []
        self.time_differences = []
        self.WEIGHT_PER_QUESTION = 0.1
        self.current_date = datetime.datetime.now()
        self.ACTIVITIES = {}
        self.dialog = MDDialog(MDDialogHeadlineText(text="Invalid Login"), MDDialogSupportingText(
            text="Please Enter a Valid Login"),
                               MDDialogButtonContainer(Widget(),
                                                       MDButton(MDButtonIcon(icon="arrow-left-bold-box"),
                                                                on_release=self.close_dialog)))
        # 2. Setting the Theme and Color
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        self.main_screen = Builder.load_string(manager_helper)
        return self.main_screen


    # log_in: mimics a simple log_in with by referencing the SQL Page
    def log_in (self):
        try:
            user = self.main_screen.get_screen("login").ids.user.text
            password = self.main_screen.get_screen("login").ids.passw.text
            max_length = self.main_screen.get_screen("login").ids.max.max_text_length
            if (self.check_data(user, password) == False):
                self.main_screen.get_screen("login").ids.user.text = ""
                self.main_screen.get_screen("login").ids.passw.text = ""
                raise InvalidLoginError
            return (self.check_data(user, password)) and not(user == "" or password == "")
        except InvalidLoginError:
            self.dialog.children[0].children[1].children[2].children[0].text = "Invalid Login"
            self.dialog.children[0].children[1].children[1].children[
                0].text = "Please Enter A Valid Login"
            self.dialog.open()

    # calculate_age: calculates and records the age of the person
    def calculate_age(self):
        try:
            birthday = self.main_screen.get_screen("create").ids.age_cred.text
            self.main_screen.get_screen("create").ids.age_cred.text = ""
            date = []
            for i in range(0, 2):
                val = birthday[:birthday.index("/")]
                date.append(val)
                birthday = birthday[birthday.index("/") + 1:]
            date.append(birthday)
            birth_obj = datetime.datetime(int(date[2]), int(date[0]), int(date[1]))
            difference = self.current_date - birth_obj
            age = int(difference.total_seconds() / (60 * 60 * 24 * 365))
            return age
        except Exception as error:
            print(error)
            self.dialog.children[0].children[1].children[2].children.text = "Invalid Entry"
            self.dialog.children[0].children[1].children[1].children[0].text = "Please Enter a Correct Birthday (MM/DD/YYYY)"
            self.dialog.open()

    # check_data: checks to see if user and pass are in the database to verify login
    def check_data (self, user, passw):
        data = self.sql_to_array()
        for tuple in data:
            if user in tuple and passw in tuple:
                return True

        return False
    # sql_to_array: A function used to convert sql data into array
    def create_login(self, instance):
        try:
            first = self.main_screen.get_screen("create").ids.first_cred.text
            last = self.main_screen.get_screen("create").ids.last_cred.text
            new_user = self.main_screen.get_screen("create").ids.user_cred.text
            new_passw = self.main_screen.get_screen("create").ids.passw_cred.text
            age = self.calculate_age()
            self.main_screen.get_screen("create").ids.user_cred.text = ""
            self.main_screen.get_screen("create").ids.passw_cred.text = ""
            self.main_screen.get_screen("create").ids.first_cred.text = ""
            self.main_screen.get_screen("create").ids.last_cred.text = ""
            max_length = self.main_screen.get_screen("create").ids.max2.max_text_length
            if len(new_user) > max_length or len(new_passw) > max_length:
                raise MaxLengthError
            data = self.sql_to_array()
            if not (new_user == "" or new_passw == "" or first == "" or last == ""):
                if self.check_data(new_user, new_passw) == False:
                    cursor.execute("INSERT INTO login VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (first, last, new_user, new_passw, age, "", "", "", "", ""))
                    new_connect.commit()
                    self.new_dialog = MDDialog(MDDialogHeadlineText(text="Login Created"), MDDialogSupportingText(text="Please Click the 'Back' Button To Return to the Home Page"),
                                           MDDialogButtonContainer(Widget(), MDButton(MDButtonIcon(icon="arrow-left-bold-box"), on_release=self.close_dialog)))
                    self.new_dialog.open()


        except MaxLengthError:
            self.dialog.children[0].children[1].children[1].children[0].text = "Entries May Be Only Up to 10 characters"
            self.dialog.open()

    # show_pass: Used as a Toggle to Hide and Show the Password
    def show_pass (self, id):
        password = self.main_screen.get_screen(id).ids.passw.password
        if password == True:
            self.main_screen.get_screen(id).ids.passw.password = False
        else:
            self.main_screen.get_screen(id).ids.passw.password = True

    # sql_to_array: converts SQL Database Entry into Array
    def sql_to_array(self):
        cursor.execute("SELECT * FROM login")
        data = cursor.fetchall()
        return data

    # return_login_info: returns the all the data entries for the user that is logging in
    def return_login_info (self):
        try:
            if self.log_in():
                user = self.main_screen.get_screen("login").ids.user.text
                passw = self.main_screen.get_screen("login").ids.passw.text
                cursor.execute("SELECT * FROM login WHERE username = ? AND password = ?", (user, passw))
                data = cursor.fetchall()
                self.age = data[0][4]
                return data
                new_connect.commit()
        except:
            self.main_screen.get_screen("login").ids.user.text = ""
            self.main_screen.get_screen("login").ids.passw.text = ""
            self.dialog = MDDialog(MDDialogHeadlineText(text="Invalid Login"), MDDialogSupportingText(
                text="Please Try Again"),
                                   MDDialogButtonContainer(Widget(),
                                                           MDButton(MDButtonIcon(icon="arrow-left-bold-box"),
                                                                    on_release=self.close_dialog)))
            self.dialog.open()

    # return_name: Displays the Name of User on Account Info Page
    def return_name (self):
        try:
            self.main_screen.get_screen("main").ids.label8.text = "Name: {}".format(self.return_login_info()[0][0] + " " + self.return_login_info()[0][1])
        except:
            pass
    # return_name: Displays the Username of User on Account Info Page
    def return_user (self):
        try:
            self.main_screen.get_screen("main").ids.label9.text += (self.return_login_info()[0][2])
        except:
            pass

    # tap_chevron: Changes the Chevron Icon / Closes and Opens the Expansion Panel
    def tap_chevron (self, panel: MDExpansionPanel, screen: str):
        if panel.is_open:
            panel.close()
            self.main_screen.get_screen(screen).ids.icon1.icon = "chevron-down"
        else:
            panel.open()
            self.main_screen.get_screen(screen).ids.icon1.icon = "chevron-up"

    # task_dialog: Displays Dialog to Enter a New Task
    def task_dialog (self):
        self.dialog2 = MDDialog(MDRelativeLayout(MDDialogHeadlineText(text="Enter New Task", pos_hint={"center_x":0, "center_y":0.75}, font_style="Title", role="medium"), MDTextField( id="dialog", mode="outlined",
    pos_hint={"center_x": -0.35, "center_y": 0.35}, size_hint=(None, None), size=("72dp", "100dp"), halign="center"), MDTextField(MDTextFieldHelperText(text="Priority", mode="persistent"), id="dialog1", mode="outlined",
    pos_hint={"center_x": 0.35, "center_y": 0.35}, size_hint=(None, None), size=("72dp", "100dp"), halign="center"),
                                                       MDButton(MDButtonIcon(icon="arrow-left-bold-box"),
                                                                on_release=self.close_dialog2, pos_hint={"center_x": -0.75, "center_y": 0.75}, size_hint=(None, None), size=("30dp", "50dp")), MDButton(MDButtonIcon(icon="plus", pos_hint={"center_x": 0.5, "center_y":0.5}), pos_hint={"center_x": 0.75, "center_y": 0.75}, on_press=self.task_manager, size_hint=(None, None), size=("30dp", "50dp"))))
        self.dialog2.open()
    # task_manager: adds task_dialog entry into the TaskManager class instance "task_m"
    def task_manager (self, *args, change = False):
        try:
            self.priority = int(self.dialog2.children[0].children[2].text)
            if not (self.priority > 1 and self.priority < 100):
                raise RatingError
            self.task_name = self.dialog2.children[0].children[3].text
            if change:
                return self.task_name
            else:
                TaskManager.add(self.task_m, self.task_name, self.priority)
                self.update_list(self.task_name, self.priority, self.dialog2)
        except RatingError:
            self.dialog2.children[0].children[2].text = ""
            self.dialog2.children[0].children[3].text = ""
            self.dialog = MDDialog(MDDialogHeadlineText(text="Invalid Entry"), MDDialogSupportingText(
                text="Please Enter A Valid Priority Level"),
                                   MDDialogButtonContainer(Widget(),
                                                           MDButton(MDButtonIcon(icon="arrow-left-bold-box"),
                                                                    on_release=self.close_dialog)))
            self.dialog.children[0].children[1].children[2].children[0].text = "Invalid Entry"
            self.dialog.children[0].children[1].children[1].children[
                0].text = "Please Enter A Priority Level"
            self.dialog.open()
        except Exception as error:
            self.dialog2.children[0].children[2].text = ""
            self.dialog2.children[0].children[3].text = ""
            self.dialog.children[0].children[1].children[2].children[0].text = "Invalid Entry"
            self.dialog.children[0].children[1].children[1].children[
                0].text = "Please Enter A Valid Task and Priority Level"
            self.dialog.open()
            self.dialog.open()

    # update_list: Central Method that a new item to the list
    def update_list (self, task_name, priority, dialog : MDDialog, record = True):
        for i in range(0, len(self.task_m.task_list)):
            list_item = TaskManager.to_string(self.task_m, i)
            if not (list_item in self.done_list):
                new_list_item = MDListItem(MDListItemHeadlineText(id="text", text=list_item), MDListItemTrailingCheckbox(on_release=self.remove), ripple_effect=False, size_hint=(None, None),
                                        size=("280dp", "50dp"), halign="center")
                self.main_screen.get_screen("task_l").ids.panel_cont.add_widget(new_list_item)
                self.done_list.append(list_item)
                if record:
                    self.record_task(task_name, priority)
        dialog.dismiss()
        self.dialog = MDDialog(MDDialogHeadlineText(text="Task List Udpated"), MDDialogSupportingText(
            text="Please Click on the Expansion Panel to Verify Your Task Has Been Updated!"),
                               MDDialogButtonContainer(Widget(),
                                                       MDButton(MDButtonIcon(icon="arrow-left-bold-box"),
                                                                on_release=self.close_dialog)))
        self.dialog.open()

    # record_task: Records Task List Entry into the SQL Database
    def record_task (self, task_name, priority, clear = False):
        self.data = self.return_login_info()
        if clear:
            self.task_list = []
        self.task_list.append("{}({})".format(task_name, priority))
        self.task_l = ", ".join(self.task_list)
        cursor.execute("UPDATE login SET list_contents = ? WHERE username = ? AND password = ?", (self.task_l, self.data[0][2], self.data[0][3]))
        new_connect.commit()

    # restore: Displays the Dialog to Verify Database Restoration
    def restore_dialog (self):
        self.dialog = MDDialog(MDRelativeLayout(
            MDDialogHeadlineText(text="Restore Task List?", valign="center", pos_hint={"center_x": 0, "center_y": 0.75}, font_style="Title", role="medium"),
                                    MDButton(MDButtonIcon(icon="arrow-left-bold-box"),
                                             on_release=self.close_dialog,
                                             pos_hint={"center_x": -0.75, "center_y": 0.25}),
            MDButton(MDButtonIcon(icon="backup-restore", pos_hint={"center_x": 0.5, "center_y": 0.5}),
                     pos_hint={"center_x": 0.75, "center_y": 0.25}, on_press=self.save_data)))
        self.dialog.open()

    # save_data: Uses the Database to Restore Data
    def save_data (self, obj):
        try:
            self.dialog.dismiss()
            user = self.main_screen.get_screen("login").ids.user.text
            password = self.main_screen.get_screen("login").ids.passw.text
            cursor.execute("SELECT * FROM login WHERE username = ? AND password = ?", (user, password))
            data = cursor.fetchone()
            list_content = data[5]
            if "," in list_content:
                list_content = list_content.split(", ")
                for task in list_content:
                    task_name = task[:task.index("(")]
                    priority = int(task[task.index("(") + 1:task.index(")")])
                    TaskManager.add(self.task_m, task_name, priority)
                self.update_list(task_name, priority, self.dialog, record = False)
            else:
                task_name = list_content[:list_content.index("(")]
                priority = int(list_content[list_content.index("(") + 1:list_content.index(")")])
                TaskManager.add(self.task_m, task_name, priority)
                self.update_list(task_name, priority, self.dialog, record = False)
        except Exception as error:
            print(error)
            self.dialog = MDDialog(MDDialogHeadlineText(text="Error"), MDDialogSupportingText(
                text="There are no items to restore!"),
                                   MDDialogButtonContainer(Widget(),
                                                           MDButton(MDButtonIcon(icon="arrow-left-bold-box"),
                                                                    on_release=self.close_dialog)))
            self.dialog.open()


    # clear_dialog: Displays the Dialog to Verify Clearing Data
    def clear_dialog (self, *args):
        self.dialog2 = MDDialog(MDRelativeLayout(
            MDDialogHeadlineText(text="Clear Task List?", valign="center", pos_hint={"center_x": 0, "center_y": 0.75},
                                 font_style="Title", role="medium"),
                                    MDButton(MDButtonIcon(icon="arrow-left-bold-box"),
                                             on_release=self.close_dialog2,
                                             pos_hint={"center_x": 0.75, "center_y": 0.25}),
            MDButton(MDButtonIcon(icon="close-box", pos_hint={"center_x": 0.5, "center_y": 0.5}),
                     pos_hint={"center_x": -0.75, "center_y": 0.25}, on_press=self.clear_data)))
        self.dialog2.open()

    # clear_item: Uses the Database to Clear Data
    def clear_data (self, *args):
        self.dialog2.dismiss()
        user = self.main_screen.get_screen("login").ids.user.text
        password = self.main_screen.get_screen("login").ids.passw.text
        self.main_screen.get_screen("task_l").ids.panel_cont.clear_widgets()
        cursor.execute("UPDATE login SET list_contents = ? WHERE username = ? AND password = ?", ("", user, password))
        new_connect.commit()

    # remove: Uses the TaskManager Class to Remove List Widget On Checkbox Click
    def remove (self, obj):
        self.dialog.dismiss()
        for widget in self.main_screen.get_screen("task_l").ids.panel_cont.children:
            if widget.children[0].children[0].active:
                self.main_screen.get_screen("task_l").ids.panel_cont.remove_widget(widget)
                headline_obj = widget.children[1].children[0].children[0]
                task = headline_obj.text
                task_name = task[:task.index(",")]
                TaskManager.remove(self.task_m, task_name)
                self.manipulate_item_d()
        if len(self.main_screen.get_screen("task_l").ids.panel_cont.children) == 0:
            self.main_screen.get_screen("task_l").ids.panel.close()
    # manipulate_item_d: Changes Data in the Database
    def manipulate_item_d (self):
        user = self.main_screen.get_screen("login").ids.user.text
        password = self.main_screen.get_screen("login").ids.passw.text
        cursor.execute("UPDATE login SET list_contents = ? WHERE username = ? AND password = ?",
                       ("", user, password))
        for task in self.task_m.task_list:
            task_name = task[0]
            priority = task[1]
            self.record_task(task_name, priority, clear = True)
        new_connect.commit()

    # reorder_dialog: Displays the Dialog to Verify Reordering Data
    def reorder_dialog (self):
        self.dialog = MDDialog(MDRelativeLayout(
            MDDialogHeadlineText(text="Reorder Task List?", valign="center", pos_hint={"center_x": 0, "center_y": 0.75},
                                 font_style="Title", role="medium"),
            MDButton(MDButtonIcon(icon="arrow-left-bold-box"),
                     on_release=self.close_dialog,
                     pos_hint={"center_x": 0.75, "center_y": 0.25}),
            MDButton(MDButtonIcon(icon="reorder-horizontal", pos_hint={"center_x": 0.5, "center_y": 0.5}),
                     pos_hint={"center_x": -0.75, "center_y": 0.25}, on_press=self.manipulate_item)))
        self.dialog.open()

    # manipulate_item: Remove all Widgets and Displays Reordered or Changed Version of Widgets on Screen and Database
    def manipulate_item (self, *args, reorder = True):
        if reorder:
            TaskManager.reorder(self.task_m)
        self.main_screen.get_screen("task_l").ids.panel_cont.clear_widgets()
        self.done_list = []
        for item in self.task_m.task_list:
            task_name = item[0]
            priority = item[1]
            self.update_list(task_name, priority, self.dialog, record = False)
        if reorder:
            self.manipulate_item_d()

    # intro_vision_one: receives the responses for the three questions
    def intro_vision_one (self, *args):
        try:
            answer_one =  7 - int(self.main_screen.get_screen("intro_v1").ids.q1.text)
            answer_two = int(self.main_screen.get_screen("intro_v1").ids.q2.text)
            answer_three = int(self.main_screen.get_screen("intro_v1").ids.q3.text)
            if (answer_one > 7 and answer_one < 7) or (answer_two > 10 and answer_two < 0) or (answer_three > 10 and answer_three < 0):
                raise IntroVisionError
            self.intro_vision_score += (answer_one * self.WEIGHT_PER_QUESTION) + (answer_two * self.WEIGHT_PER_QUESTION) + (answer_three * self.WEIGHT_PER_QUESTION)
        except ValueError as error:
            self.dialog.children[0].children[1].children[2].children[0].text = "Error"
            self.dialog.children[0].children[1].children[1].children[0].text = "You must enter in numerical values for the questions asked!"
            self.dialog.open()
        except IntroVisionError:
            self.dialog.children[0].children[1].children[2].children[0].text = "Error"
            self.dialog.children[0].children[1].children[1].children[0].text = "Please Enter Valid Entries for the Questions Above!"
            self.dialog.open()

    # append_dialog: The IntroVision Score is appended to the main page
    def append_dialog (self, *args):
        self.data = self.return_login_info()
        self.date = datetime.date.today()
        self.list_contents = self.data[0][6]
        self.date_contents = self.data[0][7]
        activities = self.activities()
        score_results = "Your IntroVision Score: " + str(round(self.intro_vision_score, 1))
        self.main_screen.get_screen("intro_v").ids.label18.text = score_results
        self.main_screen.get_screen("intro_v").ids.label19.text = activities
        self.intro_vision_scores.append(str(round(self.intro_vision_score, 1)))
        self.intro_l = ", ".join(self.intro_vision_scores)
        self.dates.append(str(self.date))
        self.dates_s = ", ".join(self.dates)
        if self.list_contents == "":
            cursor.execute("UPDATE login SET intro_vision = ? WHERE username = ? AND password = ?",
                       (self.intro_l, self.data[0][2], self.data[0][3]))
        else:
            cursor.execute("UPDATE login SET intro_vision = ? WHERE username = ? AND password = ?",
                           (self.list_contents + ", " + self.intro_l, self.data[0][2], self.data[0][3]))
        if self.date_contents == "":
            cursor.execute("UPDATE login SET intro_vision_date = ? WHERE username = ? AND password = ?",
                       (self.dates_s, self.data[0][2], self.data[0][3]))
        else:
            cursor.execute("UPDATE login SET intro_vision_date = ? WHERE username = ? AND password = ?",
                       (self.date_contents + ", " + self.dates_s, self.data[0][2], self.data[0][3]))
        new_connect.commit()

    # exit_dialog: Ask User if He Wish to Exit the IntroVision Quiz
    def exit_dialog (self, *args):
        self.main_screen.get_screen("intro_v1").ids.q1.text = ""
        self.main_screen.get_screen("intro_v1").ids.q2.text = ""
        self.main_screen.get_screen("intro_v1").ids.q3.text = ""
        self.main_screen.get_screen("intro_v").ids.label18.text = "You Have Just Exited the Quiz!"

    # clear_screen: clears result text from the screen
    def clear_screen (self, *args):
        self.main_screen.get_screen("intro_v").ids.label18.text = ""
        self.main_screen.get_screen("intro_v").ids.label19.text = ""
        self.main_screen.get_screen("intro_v1").ids.q1.text = ""
        self.main_screen.get_screen("intro_v1").ids.q2.text = ""
        self.main_screen.get_screen("intro_v1").ids.q3.text = ""


    # previous_scores: return and the labels for all previous scores from the user
    def previous_scores (self, *args):
        data = self.return_login_info()
        intro_vision_scores = data[0][6]
        intro_vision_dates = data[0][7]
        scores = intro_vision_scores.split(", ")
        dates = intro_vision_dates.split(", ")
        final_label_string = ""
        for i in range(len(scores)):
            final_label_string += "IntroVision Score #{}:  {},  Date: {}".format((i + 1), scores[i], dates[i])
            final_label_string += "\n"
        self.main_screen.get_screen("prev").ids.label21.text = final_label_string
    # empty_times: returns if certain times are empty
    def empty_times (self, *args, pm = False):
        data = self.return_login_info()
        if pm:
            return data[0][9] == ""
        else:
            return data[0][8] == ""

    # record_wake_time: records the wake time when the button is pressed
    def record_time (self, *args, pm = False):
        keyword = ''
        if pm:
            keyword = "S"
        else:
            keyword = "W"
        user = self.main_screen.get_screen("login").ids.user.text
        password = self.main_screen.get_screen("login").ids.passw.text
        current_date = datetime.datetime.now()
        hour = current_date.strftime("%I")
        minute = current_date.strftime("%M")
        am_pm = current_date.strftime("%p")
        current_date_str  = ("{}:{} {} ({})").format(hour, minute, am_pm, keyword)
        contents = self.return_login_info()[0][8]
        if self.empty_times() and not pm:
            cursor.execute("UPDATE login SET wake_times = ? WHERE username = ? AND password = ?",
                           (current_date_str, user, password))
        elif pm == False:
            cursor.execute("UPDATE login SET wake_times = ? WHERE username = ? AND password = ?",
                           (contents + ", " + current_date_str, user, password))
        elif self.empty_times(pm = True) and pm == True:
            cursor.execute("UPDATE login SET sleep_times = ? WHERE username = ? AND password = ?",
                           (current_date_str, user, password))
        elif pm == True:
            cursor.execute("UPDATE login SET sleep_times = ? WHERE username = ? AND password = ?",
                           (contents + ", " + current_date_str, user, password))
        new_connect.commit()
        self.dialog.children[0].children[1].children[2].children[0].text = "New Time Has Been Updated"
        self.dialog.children[0].children[1].children[1].children[0].text = "Please Look at the Analytics to See the Data!"
        self.dialog.open()
    # sleep_list: returns sleep lists that are necessary
    def sleep_list (self, *args):
        data = self.return_login_info()
        wake_log = data[0][8]
        wake = wake_log.split(", ")
        sleep_log = data[0][9]
        sleep = sleep_log.split(", ")
        return (wake, sleep)

    def modify_times (self, *args):
        times = self.sleep_list()
        wake = times[0]
        sleep =times[1]
        new_wake = []
        new_sleep = []
        for time in wake:
            time = time[:time.index("(")]
            new_wake.append(time)
        for time in sleep:
            time = time[:time.index("(")]
            new_sleep.append(time)
        return (new_wake, new_sleep)
    def convert(self, arr, sleep=False):
        new_arr = []
        for i in range(len(arr)):
            hour_w = int(arr[i][:arr[i].index(":")])
            min_w = int(arr[i][arr[i].index(":") + 1:arr[i].index(" ")])
            if (hour_w == 12) and ("A" in arr[i].upper()):
                hour_w = 0
            if (sleep == True) and not ("A" in arr[i]) and not (hour_w == 12) :
                date_obj = datetime.datetime(2000, 1, 1, hour_w + 12, min_w)
            else:
                date_obj = datetime.datetime(2000, 1, 2, hour_w, min_w)
            new_arr.append(date_obj)
        return new_arr

    def sleep_difference(self, *args):
        wake = self.modify_times()[0]
        sleep = self.modify_times()[1]
        if not(len(wake) == len(sleep)) or wake == "" or sleep == "":
            raise DifferenceError
        differences = []
        wake_times = self.convert(wake)
        sleep_times = self.convert(sleep, sleep=True)
        for i in range(len(wake)):
            difference = str(wake_times[i] - sleep_times[i])
            hour = int(difference[:difference.index(":")])
            difference = difference[difference.index(":") + 1:]
            min = int(difference[:difference.index(":")])
            differences.append((hour, min))
        string = self.calculate_average(differences)
        self.main_screen.get_screen("dream_w2").ids.label24.text = string
        return True

    def calculate_average(self, differences: list):
        new_arr = []
        for tup in differences:
            total_time = (tup[0] * 60) + tup[1]
            new_arr.append(total_time)
        avg = (sum(new_arr) / len(new_arr)) / 60
        hours = int(avg)
        minutes = int((avg - hours) * 60)
        new_string = "Average: {} Hours, {} Minutes".format(str(hours), str(minutes))
        return new_string

    # print_sleep_log: prints sleep_log with your sleep and wake-up time arranged in days
    def print_sleep_log (self, *args):
        try:
            wake, sleep = self.sleep_list()
            final_label_string = ""
            for i in range(0, len(wake)):
                final_label_string += "Day #{}: Wake: {}".format((i + 1), wake[i][:wake[i].index("(") - 1])
            for i in range (0, len(sleep)):
                final_label_string += ", Sleep: {}\n".format(sleep[i][:sleep[i].index("(") - 1])
            self.main_screen.get_screen("dream_w2").ids.label23.text = final_label_string
            return True
        except:
            self.dialog.children[0].children[1].children[2].children.text = "Error"
            self.dialog.children[0].children[1].children[1].children[
                    0].text = "You have don't have enough wake-up times or sleep times"
            self.dialog.open()
            return False

    # activities: list the activities you need based on IntroVision Score:
    def activities (self, *args):
        activities = ""
        if self.intro_vision_score <= 1.35:
            activities = "Your Score is Really Low!\n Activities to Try: Physical Activity, Self-Care Schedule, Journaling, and Meditation"
        elif self.intro_vision_score <= 2.7:
            activities = "Your Score is Somewhat Low!\n You should continue doing newly-found activities that have helped you relax!"
        elif self.intro_vision_score <= 4.05:
            activities = "Your Score is Somewhat High!\n You are doing a fantastic job maintaining your mental health. Keep it Up!"
        elif self.intro_vision_score <= 5.4:
            activities = "Your Score is Really High!\n Your mental health is at peak level right now! Awesome!"
        return activities

    # clear_all: clear_all clears all of the entries for wake_times and sleep_times
    def clear_all (self, *args):
        self.main_screen.get_screen("dream_w2").ids.label23.text = ""
        self.main_screen.get_screen("dream_w2").ids.label24.text = ""
        user = self.main_screen.get_screen("login").ids.user.text
        password = self.main_screen.get_screen("login").ids.passw.text
        cursor.execute("UPDATE login SET wake_times = ? WHERE username = ? AND password = ?",
                       ("", user, password))
        cursor.execute("UPDATE login SET sleep_times = ? WHERE username = ? AND password = ?",
                       ("", user, password))
        new_connect.commit()


    def remove_account (self, *args):
        user = self.main_screen.get_screen("login").ids.user.text
        password = self.main_screen.get_screen("login").ids.passw.text
        cursor.execute("DELETE FROM login WHERE username = ? and password = ?", (user, password))
        self.main_screen.get_screen("login").ids.user.text = ""
        self.main_screen.get_screen("login").ids.passw.text = ""
        new_connect.commit()

    def update_account (self, *args):
        self.remove_account()
        self.main_screen.get_screen("create").ids.label5.text = "Update"

    # Close Dialog Methods
    def close_dialog (self, obj):
       try:
            self.new_dialog.dismiss()
       except:
            self.dialog.dismiss()

    def close_dialog2 (self, obj):
        try:
            self.dialog2.dismiss()
        except:
            self.dialog3.dismiss()


# Exceptions
class MaxLengthError (Exception):
    def __init__ (self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class InvalidLoginError (Exception):
    def __init__ (self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class EmptyDatabaseError (Exception):
    def __init__ (self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class RatingError (Exception):
    def __init__ (self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class IntroVisionError (Exception):
    def __init__ (self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class DifferenceError (Exception):
    def __init__ (self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

Manager().run()
