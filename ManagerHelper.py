# This is the document of the Manager Helper String for the Mobile Application
###### By: Arav Raghunathan
manager_helper = """
ScreenManager:
    LoginScreen:
    CreateLoginScreen:
    HomeScreen:
    TaskListScreen:
    AccountScreen:
    IntroVisionScreen:
    IntroVisionScreenOne:
    IntroVisionScreenTwo:
    IntroVisionScreenThree:
    PreviousScoresScreen:
    DreamWaveScreen:
    DreamWaveScreenTwo:
    AboutScreen:
    OwnerScreen:
    AravScreen:
    AyanScreen:
    ShashankScreen:
        
<LoginScreen>:
    name: "login"
    MDLabel:
        id: label2
        text: "Login"
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        anchor: "center"
        text_color: "CF3131"
        halign: "center"
        font_style: "Headline"
        role: "small"
    MDTextField:
        id: user
        mode: "outlined"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint: None, None
        size: "160dp", "30dp"
        MDTextFieldHelperText:
            id: label4
            text: "Username"
            text_color_normal: "FF7C6E"
            mode: "on_focus"
        MDTextFieldMaxLengthText:
            max_text_length: 10
    MDTextField:
        id: passw
        mode: "outlined"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        size_hint: None, None
        size: "160dp", "30dp"
        password: True
        MDTextFieldHelperText:
            id: label4
            text: "Password"
            text_color_normal: "FF7C6E"
            mode: "on_focus"
        MDTextFieldMaxLengthText:
            id: max
            max_text_length: 10
            
    MDButton:
        id: button
        style: "filled"
        pos_hint: {"center_x": 0.5, "center_y": 0.25}
        on_press: 
            root.manager.transition.direction = "left" 
            if app.log_in(): root.manager.current = "home" 
            if app.log_in(): app.return_login_info() 
            if app.log_in(): app.return_user() 
        MDButtonText:
            text: "Log In"
            theme_text_color: "Custom"
            text_color: "CF3131"
            font_style: "Title"
            role: "medium"
    MDButton:
        id: button2
        style: "filled"
        pos_hint: {"center_x": 0.5, "center_y": 0.10}
        size_hint: None, None
        size: "50dp", "50dp"
        on_press: 
            root.manager.current = "create"
            root.manager.transition.direction = "left"
        MDButtonText:
            text: "Sign Up"
            theme_text_color: "Custom"
            text_color: "CF3131"
            font_style: "Title"
            role: "medium"
    MDButton:
        id: button7
        style: "filled"
        pos_hint: {"center_x": 0.85, "center_y": 0.4}
        size_hint: None, None
        size: "50dp", "50dp"
        on_press: app.show_pass('login')
        MDButtonIcon:
            icon: "eye-circle"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
    MDSmartTile:
        pos_hint: {"center_x": 0.5, "center_y": 0.9}
        size_hint: None, None
        size: "275dp", "75dp"
        overlap: False
        MDSmartTileImage:
            source: "MindGuard.jpg"
            radius: [dp(24), dp(24), dp(24), dp(24)]
    MDSmartTile:
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        size_hint: None, None
        size: "167dp", "50dp"
        overlap: False
        MDSmartTileImage:
            source: "Welcome.jpg"
            radius: [dp(24), dp(24), dp(24), dp(24)]
            
<CreateLoginScreen>
    name: "create"
    MDLabel:
        id: label5
        text: "Sign Up"
        pos_hint: {"center_x": 0.5, "center_y": 0.9}
        theme_text_color: "Custom"
        halign: "center"
        text_color: "FF7C6E"
        font_style: "Headline"
        role: "medium"
    MDLabel:
        id: label6
        text: "Please Enter Your Credentials Below!"
        pos_hint: {"center_x": 0.5, "center_y": 0.85}
        theme_text_color: "Custom"
        text_color: "CF3131"
        font_style: "Title"
        halign: "center"
        role: "medium"
    MDTextField:
        id: user_cred
        mode: "filled"
        pos_hint: {"center_x": 0.75, "center_y": 0.7}
        size_hint: None, None
        size: "120dp", "15dp"
        MDTextFieldHelperText:
            id: label4
            text: "Username"
            text_color_normal: "FF7C6E"
            mode: "persistent"
        MDTextFieldMaxLengthText:
            max_text_length: 10
    MDTextField:
        id: passw_cred
        mode: "filled"
        pos_hint: {"center_x": 0.75, "center_y": 0.5}
        size_hint: None, None
        size: "120dp", "15dp"
        password: True
        MDTextFieldHelperText:
            id: label4
            text: "Password"
            text_color_normal: "FF7C6E"
            mode: "persistent"
        MDTextFieldMaxLengthText:
            id: max2
            max_text_length: 10
    MDTextField:
        id: first_cred
        mode: "filled"
        pos_hint: {"center_x": 0.25, "center_y": 0.7}
        size_hint: None, None
        size: "120dp", "15dp"
        MDTextFieldHelperText:
            id: label4
            text: "First Name"
            text_color_normal: "FF7C6E"
            mode: "persistent"
    MDTextField:
        id: last_cred
        mode: "filled"
        pos_hint: {"center_x": 0.25, "center_y": 0.5}
        size_hint: None, None
        size: "120dp", "15dp"
        MDTextFieldHelperText:
            id: label4
            text: "Last Name"
            text_color_normal: "FF7C6E"
            mode: "persistent"
    MDTextField:
        id: age_cred
        mode: "filled"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        size_hint: None, None
        size: "120dp", "15dp"
        MDTextFieldHelperText:
            id: label4
            text: "Birthday (MM/DD/YYYY)"
            text_color_normal: "FF7C6E"
            mode: "persistent"
    MDButton:
        id: button3
        style: "elevated"
        pos_hint: {"center_x": 0.5, "center_y": 0.15}
        on_press: 
            app.create_login(self)
        MDButtonText:
            text: "Sign Up"
            theme_text_color: "Custom"
            text_color: "CF3131"
            font_style: "Title"
            role: "medium"
    MDButton:
        id: button4
        style: "elevated"
        pos_hint: {"center_x": 0.10, "center_y": 0.10}
        on_press: 
            root.manager.current = "login"
            root.manager.transition.direction = "right"
        size_hint: None, None
        size: "50dp", "50dp"
        MDButtonIcon:
            icon: "arrow-left-bold-box"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: "center"
    
        
        
<HomeScreen>
    name: "home"
    theme_screen_color: "Custom"
    screen_color: (1, 1, 1)
    MDCard:
        style: "elevated"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint: None, None
        size: "240dp", "100dp"
        theme_bg_color: "Custom"
        md_bg_color: (0, 0, 0)
        theme_shadow_color: "Custom"
        shadow_color: "FF7C6E"
        theme_shadow_offset: "Custom"
        shadow_offset: (1, -1)
        on_release: nav_drawer.set_state("toggle")
        MDRelativeLayout:
            MDLabel:
                text: "Welcome!"
                pos_hint: {"center_x": 0.85, "center_y": 0.5}
                theme_text_color: "Custom"
                text_color: "FF7C6E"
                font_style: "Title"
                role: "medium"
    MDNavigationDrawer:
        id: nav_drawer
        MDNavigationDrawerMenu:
            MDNavigationDrawerLabel:
                text: "Menu"
                theme_text_color: "Custom"
                text_color: "FF7C6E"
                font_style: "Title"
                role: "medium"
                valign: "center"
            MDNavigationDrawerDivider:
                    
            MDNavigationDrawerItem:
                style: "filled"
                size_hint: None, None
                size: "290dp", "50dp"
                on_release: 
                    root.manager.current = "task_l"
                    nav_drawer.set_state("close")
                MDNavigationDrawerItemLeadingIcon:
                    icon: "list-box"
                    theme_icon_color: "Custom"
                    icon_color: "FF7C6E"
                    valign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.575}
                MDNavigationDrawerItemText:
                    text: "Task List"
                    theme_text_color: "Custom"
                    pos_hint: {"center_x": 0.13, "center_y": 0.45}
                    text_color: "FF7C6E"
                    halign: "center"
                    font_style: "Title"
                    role: "medium"
            MDNavigationDrawerItem:
                style: "filled"
                size_hint: None, None
                size: "290dp", "50dp"
                on_release: 
                    nav_drawer.set_state("close")
                    root.manager.current = "intro_v"
                    root.manager.transition.direction = "left"
                    app.clear_screen()
                MDNavigationDrawerItemLeadingIcon:
                    icon: "account-heart"
                    theme_icon_color: "Custom"
                    icon_color: "FF7C6E"
                    valign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.575}
                MDNavigationDrawerItemText:
                    text: "IntroVision"
                    theme_text_color: "Custom"
                    pos_hint: {"center_x": 0.16, "center_y": 0.45}
                    text_color: "FF7C6E"
                    halign: "center"
                    font_style: "Title"
                    role: "medium"
            MDNavigationDrawerItem:
                style: "filled"
                size_hint: None, None
                size: "290dp", "50dp"
                on_release: 
                    nav_drawer.set_state("close")
                    root.manager.transition.direction = "left"
                    root.manager.current = "dream_w"
                MDNavigationDrawerItemLeadingIcon:
                    icon: "meditation"
                    theme_icon_color: "Custom"
                    icon_color: "FF7C6E"
                    valign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.575}
                MDNavigationDrawerItemText:
                    text: "DreamWave"
                    theme_text_color: "Custom"
                    pos_hint: {"center_x": 0.175, "center_y": 0.45}
                    text_color: "FF7C6E"
                    halign: "center"
                    font_style: "Title"
                    role: "medium"
            MDNavigationDrawerItem:
                style: "filled"
                size_hint: None, None
                size: "290dp", "50dp"
                on_release: 
                    nav_drawer.set_state("close")
                    root.manager.current = "about"
                    root.manager.transition.direction = "left"
                MDNavigationDrawerItemLeadingIcon:
                    icon: "information"
                    theme_icon_color: "Custom"
                    icon_color: "FF7C6E"
                    valign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.575}
                MDNavigationDrawerItemText:
                    text: "About Us"
                    theme_text_color: "Custom"
                    pos_hint: {"center_x": 0.13, "center_y": 0.45}
                    text_color: "FF7C6E"
                    halign: "center"
                    font_style: "Title"
                    role: "medium"
            
    MDTopAppBar:
        type: "small"
        theme_bg_color: "Custom"
        md_bg_color: "FF7C6E"
        MDTopAppBarLeadingButtonContainer:
            MDActionTopAppBarButton:
                icon: "menu"
                theme_icon_color: "Custom"
                icon_color: "4C0000"
                on_release: nav_drawer.set_state("toggle")
        MDTopAppBarTitle:
            text: "MindGuard"
            valign: "center"
            theme_text_color: "Custom"
            text_color: "4C0000"
        MDTopAppBarTrailingButtonContainer:
            MDActionTopAppBarButton:
                icon: "account"
                on_press: 
                    root.manager.current = "main"
                    root.manager.transition.direction = "left"
                    app.return_name()
                theme_icon_color: "Custom"
                icon_color: "4C0000"

                
    
<AccountScreen>
    name: "main"
    MDTopAppBar:
        type: "small"
        theme_bg_color: "Custom"
        md_bg_color: "FF7C6E"
        MDTopAppBarTitle:
            text: "Account Info"
            valign: "center"
            theme_text_color: "Custom"
            text_color: "4C0000"
        MDTopAppBarTrailingButtonContainer:
            MDActionTopAppBarButton:
                icon: "arrow-left-bold-box"
                on_release: 
                    root.manager.current = "home"
                    root.manager.transition.direction = "right"
                theme_icon_color: "Custom"
                icon_color: "4C0000"
    MDLabel:
        id: label10
        text: "Account Info"
        pos_hint: {"center_x": 0.5, "center_y": 0.9}
        halign: "center"
        theme_text_color: "Custom"
        text_color: "CF3131"
        font_style: "Headline"
        role: "medium"
    MDLabel:
        id: label8
        text: "Name: "
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        theme_text_color: "Custom"
        text_color: "FF7C6E"
        font_style: "Title"
        role: "large"
    MDLabel:
        id: label9
        text: "Username: "
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        theme_text_color: "Custom"
        text_color: "FF7C6E"
        font_style: "Title"
        role: "large"
    MDButton:
        id: button26
        style: "elevated"
        pos_hint: {"center_x": 0.5, "center_y": 0.25}
        size_hint: None, None
        size: "75dp", "40dp"
        halign: "center"
        on_press: 
            app.remove_account()
            root.manager.current = "login"
            root.manager.transition.direction = "right"
        MDButtonText:
            text: "Remove Account"
            theme_text_color: "Custom"
            text_color: "FF7C6E"
            font_style: "Title"
            role: "medium"
    MDButton:
        id: button26
        style: "elevated"
        pos_hint: {"center_x": 0.5, "center_y": 0.15}
        size_hint: None, None
        size: "75dp", "40dp"
        halign: "center"
        on_press: 
            app.update_account()
            root.manager.current = "login"
            root.manager.transition.direction = "right"
        MDButtonText:
            text: "Update Account"
            theme_text_color: "Custom"
            text_color: "FF7C6E"
            font_style: "Title"
            role: "medium"
    
<TaskListScreen>
    name: "task_l"
    MDSmartTile:
        pos_hint: {"center_x": 0.5, "center_y": 0.9}
        size_hint: None, None
        size: "236dp", "75dp"
        overlap: False
        MDSmartTileImage:
            source: "Task_list.jpg"
            radius: [dp(24), dp(24), dp(24), dp(24)]
    MDLabel:
        id: label11
        text: "Enter a Task with a Priority Level Between 1 and 100!"
        pos_hint: {"center_x": 0.5, "center_y": 0.775}
        halign: "center"
        theme_text_color: "Custom"
        text_color: "FF7C6E"
        font_style: "Title"
        role: "medium"
    MDButton:
        id: button10
        style: "elevated"
        pos_hint: {"center_x": 0.5, "center_y": 0.25}
        size_hint: None, None
        size: "50dp", "50dp"
        on_press: app.task_dialog()
        MDButtonIcon:
            icon: "plus-box"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            halign: "center"
    
    MDButton:
        id: button11
        style: "elevated"
        pos_hint: {"center_x": 0.5, "center_y": 0.15}
        size_hint: None, None
        size: "75dp", "40dp"
        halign: "center"
        on_press: app.restore_dialog()
        MDButtonText:
            text: "Restore"
            theme_text_color: "Custom"
            text_color: "FF7C6E"
            font_style: "Title"
            role: "medium"
    MDButton:
        id: button12
        style: "elevated"
        pos_hint: {"center_x": 0.2, "center_y": 0.15}
        halign: "center"
        size_hint: None, None
        size: "75dp", "40dp"
        on_press: app.clear_dialog()
        MDButtonText:
            text: "Clear"
            theme_text_color: "Custom"
            text_color: "FF7C6E"
            font_style: "Title"
            role: "medium"
    
    MDButton:
        id: button13
        style: "elevated"
        pos_hint: {"center_x": 0.825, "center_y": 0.15}
        halign: "center"
        size_hint: None, None
        size: "75dp", "40dp"
        on_release: app.reorder_dialog()
        MDButtonText:
            text: "Reorder"
            theme_text_color: "Custom"
            text_color: "FF7C6E"
            font_style: "Title"
            role: "medium"
    MDExpansionPanel:
        id: panel
        pos_hint: {"center_x": 0.5, "center_y":0.425}
        size_hint: None, None
        halign: "center"
        size: "280dp", "50dp"
        theme_bg_color: "Custom"
        md_bg_color: "FF7C6E"
        MDExpansionPanelHeader:
            MDListItem:
                ripple_effect: False
                halign: "center"
                MDListItemHeadlineText:
                    text: "Task List"
                MDRelativeLayout:
                    MDButton:
                        style: "filled"
                        on_press: app.tap_chevron(panel, "task_l")
                        pos_hint: {"center_x": 0.9, "center_y": 0.5}
                        MDButtonIcon:
                            id: icon1
                            icon: "chevron-down"
                            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDExpansionPanelContent:
            id: panel_cont
            orientation: "vertical"
    MDNavigationDrawer:
        id: nav_drawer
        MDNavigationDrawerMenu:
            MDNavigationDrawerLabel:
                text: "Menu"
                theme_text_color: "Custom"
                text_color: "FF7C6E"
                font_style: "Title"
                role: "medium"
                valign: "center"
            MDNavigationDrawerDivider:
            
            MDNavigationDrawerItem:
                style: "filled"
                size_hint: None, None
                size: "290dp", "50dp"
                on_release: 
                    root.manager.current = "home"
                    nav_drawer.set_state("close")
                    root.manager.transition.direction = "left"
                MDNavigationDrawerItemLeadingIcon:
                    icon: "home-modern"
                    theme_icon_color: "Custom"
                    icon_color: "FF7C6E"
                    valign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.575}
                MDNavigationDrawerItemText:
                    text: "Home"
                    theme_text_color: "Custom"
                    pos_hint: {"center_x": 0.075, "center_y": 0.45}
                    text_color: "FF7C6E"
                    halign: "center"
                    font_style: "Title"
                    role: "medium"
            MDNavigationDrawerItem:
                style: "filled"
                size_hint: None, None
                size: "290dp", "50dp"
                on_release: 
                    nav_drawer.set_state("close")
                    root.manager.current = "intro_v"
                    root.manager.transition.direction = "left"
                    app.clear_screen()
                MDNavigationDrawerItemLeadingIcon:
                    icon: "account-heart"
                    theme_icon_color: "Custom"
                    icon_color: "FF7C6E"
                    valign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.575}
                MDNavigationDrawerItemText:
                    text: "IntroVision"
                    theme_text_color: "Custom"
                    pos_hint: {"center_x": 0.16, "center_y": 0.45}
                    text_color: "FF7C6E"
                    halign: "center"
                    font_style: "Title"
                    role: "medium"
            MDNavigationDrawerItem:
                style: "filled"
                size_hint: None, None
                size: "290dp", "50dp"
                on_release: 
                    nav_drawer.set_state("close")
                    root.manager.transition.direction = "left"
                    root.manager.current = "dream_w"
                MDNavigationDrawerItemLeadingIcon:
                    icon: "meditation"
                    theme_icon_color: "Custom"
                    icon_color: "FF7C6E"
                    valign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.575}
                MDNavigationDrawerItemText:
                    text: "DreamWave"
                    theme_text_color: "Custom"
                    pos_hint: {"center_x": 0.175, "center_y": 0.45}
                    text_color: "FF7C6E"
                    halign: "center"
                    font_style: "Title"
                    role: "medium"
            MDNavigationDrawerItem:
                style: "filled"
                size_hint: None, None
                size: "290dp", "50dp"
                on_release: 
                    nav_drawer.set_state("close")
                    root.manager.current = "about"
                    root.manager.transition.direction = "left"
                MDNavigationDrawerItemLeadingIcon:
                    icon: "information"
                    theme_icon_color: "Custom"
                    icon_color: "FF7C6E"
                    valign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.575}
                MDNavigationDrawerItemText:
                    text: "About Us"
                    theme_text_color: "Custom"
                    pos_hint: {"center_x": 0.13, "center_y": 0.45}
                    text_color: "FF7C6E"
                    halign: "center"
                    font_style: "Title"
                    role: "medium"
            
    MDTopAppBar:
        type: "small"
        theme_bg_color: "Custom"
        md_bg_color: "FF7C6E"
        MDTopAppBarLeadingButtonContainer:
            MDActionTopAppBarButton:
                icon: "menu"
                theme_icon_color: "Custom"
                icon_color: "4C0000"
                on_press: nav_drawer.set_state("toggle")
        MDTopAppBarTitle:
            text: "Task List"
            valign: "center"
            theme_text_color: "Custom"
            text_color: "4C0000"       

<IntroVisionScreen>
    name: "intro_v"
    MDSmartTile:
        pos_hint: {"center_x": 0.5, "center_y": 0.85}
        size_hint: None, None
        size: "236dp", "75dp"
        overlap: False
        MDSmartTileImage:
            source: "IntroVision.jpg"
            radius: [dp(24), dp(24), dp(24), dp(24)]
    MDLabel:
        text: "Please Click the Start Button to Begin Your Quiz!"
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        anchor: "center"
        text_color: "FF7C6E"
        halign: "center"
        font_style: "Body"
        role: "medium"
    MDLabel:
        id: label18
        text: ""
        theme_text_color: "Custom"
        text_color: "FF7C6E"
        font_style: "Title"
        role: "large"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        halign: "center"
    MDLabel:
        id: label19
        text: ""
        theme_text_color: "Custom"
        text_color: "FF7C6E"
        font_style: "Title"
        role: "large"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        halign: "center"
        font_style: "Body"
        role: "medium"
    MDButton:
        id: button14
        style: "elevated"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        halign: "center"
        size_hint: None, None
        size: "75dp", "40dp"
        on_release: root.manager.current = "intro_v1"
        MDButtonText:
            text: "Start"
            theme_text_color: "Custom"
            text_color: "FF7C6E"
            font_style: "Title"
            role: "medium"
    MDButton:
        id: button20
        style: "elevated"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        halign: "center"
        size_hint: None, None
        size: "75dp", "40dp"
        on_release: 
            root.manager.current = "prev"
            app.previous_scores()
        MDButtonText:
            text: "See Previous Scores"
            theme_text_color: "Custom"
            text_color: "FF7C6E"
            font_style: "Title"
            role: "medium"
    MDNavigationDrawer:
        id: nav_drawer
        MDNavigationDrawerMenu:
            MDNavigationDrawerLabel:
                text: "Menu"
                theme_text_color: "Custom"
                text_color: "FF7C6E"
                font_style: "Title"
                role: "medium"
                valign: "center"
            MDNavigationDrawerDivider:
            
            MDNavigationDrawerItem:
                style: "filled"
                size_hint: None, None
                size: "300dp", "50dp"
                on_release: 
                    root.manager.current = "home"
                    nav_drawer.set_state("close")
                    root.manager.transition.direction = "left"
                MDNavigationDrawerItemLeadingIcon:
                    icon: "home-modern"
                    theme_icon_color: "Custom"
                    icon_color: "FF7C6E"
                    valign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.575}
                MDNavigationDrawerItemText:
                    text: "Home"
                    theme_text_color: "Custom"
                    pos_hint: {"center_x": 0.075, "center_y": 0.45}
                    text_color: "FF7C6E"
                    halign: "center"
                    font_style: "Title"
                    role: "medium"
            MDNavigationDrawerItem:
                style: "filled"
                size_hint: None, None
                size: "290dp", "50dp"
                on_release: 
                    root.manager.current = "task_l"
                    nav_drawer.set_state("close")
                    root.manager.transition.direction = "left"
                MDNavigationDrawerItemLeadingIcon:
                    icon: "list-box"
                    theme_icon_color: "Custom"
                    icon_color: "FF7C6E"
                    valign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.575}
                MDNavigationDrawerItemText:
                    text: "Task List"
                    theme_text_color: "Custom"
                    pos_hint: {"center_x": 0.13, "center_y": 0.45}
                    text_color: "FF7C6E"
                    halign: "center"
                    font_style: "Title"
                    role: "medium"
            MDNavigationDrawerItem:
                style: "filled"
                size_hint: None, None
                size: "290dp", "50dp"
                on_release: 
                    nav_drawer.set_state("close")
                    root.manager.transition.direction = "left"
                    root.manager.current = "dream_w"
                    
                MDNavigationDrawerItemLeadingIcon:
                    icon: "meditation"
                    theme_icon_color: "Custom"
                    icon_color: "FF7C6E"
                    valign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.575}
                MDNavigationDrawerItemText:
                    text: "DreamWave"
                    theme_text_color: "Custom"
                    pos_hint: {"center_x": 0.175, "center_y": 0.45}
                    text_color: "FF7C6E"
                    halign: "center"
                    font_style: "Title"
                    role: "medium"
            MDNavigationDrawerItem:
                style: "filled"
                size_hint: None, None
                size: "290dp", "50dp"
                on_release: 
                    nav_drawer.set_state("close")
                    root.manager.current = "about"
                    root.manager.transition.direction = "left"
                MDNavigationDrawerItemLeadingIcon:
                    icon: "information"
                    theme_icon_color: "Custom"
                    icon_color: "FF7C6E"
                    valign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.575}
                MDNavigationDrawerItemText:
                    text: "About Us"
                    theme_text_color: "Custom"
                    pos_hint: {"center_x": 0.13, "center_y": 0.45}
                    text_color: "FF7C6E"
                    halign: "center"
                    font_style: "Title"
                    role: "medium"
           
    MDTopAppBar:
        type: "small"
        theme_bg_color: "Custom"
        md_bg_color: "FF7C6E"
        MDTopAppBarLeadingButtonContainer:
            MDActionTopAppBarButton:
                icon: "menu"
                theme_icon_color: "Custom"
                icon_color: "4C0000"
                on_press: nav_drawer.set_state("toggle")
        MDTopAppBarTitle:
            text: "IntroVision"
            valign: "center"
            theme_text_color: "Custom"
            text_color: "4C0000"       
            

<IntroVisionScreenOne>
    name: "intro_v1"
    MDTextField:
        id: q1
        mode: "outlined"
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        size_hint: None, None
        size: "160dp", "30dp"
        MDTextFieldMaxLengthText:
            id: max
            max_text_length: 2
    MDTextField:
        id: q2
        mode: "outlined"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint: None, None
        size: "160dp", "30dp"
        MDTextFieldMaxLengthText:
            max_text_length: 2
    MDTextField:
        id: q3
        mode: "outlined"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        size_hint: None, None
        size: "160dp", "30dp"
        MDTextFieldMaxLengthText:
            max_text_length: 2
    MDLabel:
        id: title1
        text: "How many days, on average, during the 7-day week do you feel sad or depressed?"
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.9}
        anchor: "center"
        text_color: "FF7C6E"
        halign: "center"
        padding: "8dp"
        font_style: "Body"
        role: "medium"
    MDLabel:
        id: title2
        text: "On a scale of 0-10, how do you feel about your job or school?"
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        anchor: "center"
        text_color: "FF7C6E"
        halign: "center"
        padding: "8dp"
        font_style: "Body"
        role: "medium"
    MDLabel:
        id: title3
        text: "On a scale of 0-10, how much do you enjoy your hobbies?"
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        anchor: "center"
        text_color: "FF7C6E"
        halign: "center"
        padding: "8dp"
        font_style: "Body"
        role: "medium"   
    MDButton:
        id: button16
        style: "elevated"
        pos_hint: {"center_x": 0.85, "center_y": 0.2}
        halign: "center"
        size_hint: None, None
        size: "75dp", "40dp"
        on_release: 
            app.intro_vision_one()
            root.manager.current = "intro_v2"
        MDButtonIcon:
            icon: "arrow-right-bold-box"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
    MDButton:
        id: button19
        style: "elevated"
        pos_hint: {"center_x": 0.15, "center_y": 0.2}
        halign: "center"
        size_hint: None, None
        size: "75dp", "40dp"
        on_release: 
            app.exit_dialog()
            root.manager.current = "intro_v"
            root.manager.transition.direction = "right"
        MDButtonIcon:
            icon: "arrow-left-bold-box"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
    MDTopAppBar:
        type: "small"
        theme_bg_color: "Custom"
        md_bg_color: "FF7C6E"
        MDTopAppBarTitle:
            text: "IntroVision"
            valign: "center"
            theme_text_color: "Custom"
            text_color: "4C0000"  
            
<IntroVisionScreenTwo>
    name: "intro_v2"
    MDTextField:
        id: q1
        mode: "outlined"
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        size_hint: None, None
        size: "160dp", "30dp"
        MDTextFieldMaxLengthText:
            id: max
            max_text_length: 2
    MDTextField:
        id: q2
        mode: "outlined"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint: None, None
        size: "160dp", "30dp"
        MDTextFieldMaxLengthText:
            max_text_length: 2
    MDTextField:
        id: q3
        mode: "outlined"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        size_hint: None, None
        size: "160dp", "30dp"
        MDTextFieldMaxLengthText:
            max_text_length: 2
    MDLabel:
        id: title1
        text: "How many days, on average, during the 7-day week do you remotely think about harming yourself?"
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.9}
        anchor: "center"
        text_color: "FF7C6E"
        halign: "center"
        padding: "8dp"
        font_style: "Body"
        role: "medium"
    MDLabel:
        id: title2
        text: "On a scale of 0-10, how would you rate your confidence in yourself?"
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        anchor: "center"
        text_color: "FF7C6E"
        halign: "center"
        padding: "8dp"
        font_style: "Body"
        role: "medium"
    MDLabel:
        id: title3
        text: "On average, how many activities do you do during the day help you relax?"
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        anchor: "center"
        text_color: "FF7C6E"
        halign: "center"
        padding: "8dp"
        font_style: "Body"
        role: "medium"
    MDButton:
        id: button17
        style: "elevated"
        pos_hint: {"center_x": 0.85, "center_y": 0.2}
        halign: "center"
        size_hint: None, None
        size: "75dp", "40dp"
        on_release: 
            root.manager.current = "intro_v3"
            app.intro_vision_one()
        MDButtonIcon:
            icon: "arrow-right-bold-box"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
    MDNavigationDrawer:
        id: nav_drawer
        MDNavigationDrawerMenu:
            MDNavigationDrawerLabel:
                text: "Menu"
                theme_text_color: "Custom"
                text_color: "FF7C6E"
                font_style: "Title"
                role: "medium"
                valign: "center"
            MDNavigationDrawerDivider:
            
            MDNavigationDrawerItem:
                style: "filled"
                size_hint: None, None
                size: "300dp", "50dp"
                on_release: 
                    root.manager.current = "home"
                    nav_drawer.set_state("close")
                    root.manager.transition.direction = "left"
                MDNavigationDrawerItemLeadingIcon:
                    icon: "home-modern"
                    theme_icon_color: "Custom"
                    icon_color: "FF7C6E"
                    valign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.575}
                MDNavigationDrawerItemText:
                    text: "Home"
                    theme_text_color: "Custom"
                    pos_hint: {"center_x": 0.075, "center_y": 0.45}
                    text_color: "FF7C6E"
                    halign: "center"
                    font_style: "Title"
                    role: "medium"
            MDNavigationDrawerItem:
                style: "filled"
                size_hint: None, None
                size: "290dp", "50dp"
                on_release: 
                    root.manager.current = "task_l"
                    nav_drawer.set_state("close")
                    root.manager.transition.direction = "left"
                MDNavigationDrawerItemLeadingIcon:
                    icon: "list-box"
                    theme_icon_color: "Custom"
                    icon_color: "FF7C6E"
                    valign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.575}
                MDNavigationDrawerItemText:
                    text: "Task List"
                    theme_text_color: "Custom"
                    pos_hint: {"center_x": 0.13, "center_y": 0.45}
                    text_color: "FF7C6E"
                    halign: "center"
                    font_style: "Title"
                    role: "medium"
    MDTopAppBar:
        type: "small"
        theme_bg_color: "Custom"
        md_bg_color: "FF7C6E"
        MDTopAppBarTitle:
            text: "IntroVision"
            valign: "center"
            theme_text_color: "Custom"
            text_color: "4C0000"
            
<IntroVisionScreenThree>
    name: "intro_v3"
    MDTextField:
        id: q1
        mode: "outlined"
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        size_hint: None, None
        size: "160dp", "30dp"
        MDTextFieldMaxLengthText:
            id: max
            max_text_length: 2
    MDTextField:
        id: q2
        mode: "outlined"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint: None, None
        size: "160dp", "30dp"
        MDTextFieldMaxLengthText:
            max_text_length: 2
    MDTextField:
        id: q3
        mode: "outlined"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        size_hint: None, None
        size: "160dp", "30dp"
        MDTextFieldMaxLengthText:
            max_text_length: 2
    MDLabel:
        id: title1
        text:"How many days, on average, during the 7-day week do you smoke or drink alcohol?"
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.9}
        anchor: "center"
        text_color: "FF7C6E"
        halign: "center"
        padding: "8dp"
        font_style: "Body"
        role: "medium"
    MDLabel:
        id: title2
        text: "On a scale of 0-10, how much do you value your skills, aptitudes, or abilities (in general)?"
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        anchor: "center"
        text_color: "FF7C6E"
        halign: "center"
        padding: "8dp"
        font_style: "Body"
        role: "medium"
    MDLabel:
        id: title3
        text: "On a scale of 0-10, how much respect do you believe your family and friends have for you?"
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        anchor: "center"
        text_color: "FF7C6E"
        halign: "center"
        padding: "8dp"
        font_style: "Body"
        role: "medium"
    MDButton:
        id: button18
        style: "elevated"
        pos_hint: {"center_x": 0.85, "center_y": 0.2}
        halign: "center"
        size_hint: None, None
        size: "75dp", "40dp"
        on_release: 
            root.manager.current = "intro_v"
            app.append_dialog()
            root.manager.transition.direction = "left"
        MDButtonIcon:
            icon: "arrow-right-bold-box"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
    
    MDTopAppBar:
        type: "small"
        theme_bg_color: "Custom"
        md_bg_color: "FF7C6E"
        MDTopAppBarTitle:
            text: "IntroVision"
            valign: "center"
            theme_text_color: "Custom"
            text_color: "4C0000"
            
<AboutScreen>
    name: "about"
    MDTopAppBar:
        type: "small"
        theme_bg_color: "Custom"
        md_bg_color: "FF7C6E"
        MDTopAppBarTitle:
            text: "About Us"
            valign: "center"
            theme_text_color: "Custom"
            text_color: "4C0000"
        MDTopAppBarTrailingButtonContainer:
            MDActionTopAppBarButton:
                icon: "arrow-left-bold-box"
                on_release: 
                    root.manager.current = "home"
                    root.manager.transition.direction = "right"
                theme_icon_color: "Custom"
                icon_color: "4C0000" 
    MDLabel:
        text: "About Us!"
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.9}
        anchor: "center"
        text_color: "FF7C6E"
        halign: "center"
        font_style: "Headline"
        role: "medium"
    MDLabel:
        text: "MindGuard is an app created by three students from Lambert High School in Suwanee, GA who want to make an impact in the realm of mental health. Our mission is to promote characteristics like organization, relaxation , and concentration that can help people manage and improve their mental health. Please click the button below to learn more about our team!"
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        anchor: "center"
        text_color: "FF7C6E"
        halign: "center"
        font_style: "Body"
        role: "medium"
        padding: "8dp"
    MDButton:
        id: button15
        style: "elevated"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        halign: "center"
        size_hint: None, None
        size: "75dp", "40dp"
        on_release: 
            root.manager.current = "owner"
            root.manager.transition.direction = "left"
        
        MDButtonText:
            text: "Meet the Owners!"
            theme_text_color: "Custom"
            text_color: "FF7C6E"
            font_style: "Title"
            role: "medium"
                
<OwnerScreen>
    name: "owner"
    MDSmartTile:
        pos_hint: {"center_x": 0.5, "center_y": 0.875}
        size_hint: None, None
        size: "125dp", "125dp"
        overlap: False
        on_press:
            root.manager.current = "arav"
            root.manager.transition.direction = "left"
        
        MDSmartTileImage:
            source: "Arav_Picture.jpg"
            radius: [dp(24), dp(24), dp(24), dp(24)]
            
    MDLabel:
        text: "Arav Raghunathan"
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.725}
        anchor: "center"
        text_color: "FF7C6E"
        halign: "center"
        font_style: "Title"
        role: "small"        

                
    MDSmartTile:
        pos_hint: {"center_x": 0.5, "center_y": (0.575)}
        size_hint: None, None
        size: "125dp", "125dp"
        overlap: False
        on_press:
            root.manager.current = "ayan"
            root.manager.transition.direction = "left"
        
        MDSmartTileImage:
            source: "Ayan Rag Photo.jpg"
            radius: [dp(24), dp(24), dp(24), dp(24)]
            
    MDLabel:
        text: "Ayan Raghunathan"
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.425}
        anchor: "center"
        text_color: "FF7C6E"
        halign: "center"
        font_style: "Title"
        role: "small"           
        
    MDSmartTile:
        pos_hint: {"center_x": 0.5, "center_y": 0.275}
        size_hint: None, None
        size: "125dp", "125dp"
        overlap: False
        on_press:
            root.manager.current = "shashank"
            root.manager.transition.direction = "left"
        
        MDSmartTileImage:
            source: "Shashank R Photo.jpg"
            radius: [dp(24), dp(24), dp(24), dp(24)]
            
    MDLabel:
        text: "Shashank Ramireddy"
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.125}
        anchor: "center"
        text_color: "FF7C6E"
        halign: "center"
        font_style: "Title"
        role: "small"        
        
    MDTopAppBar:
        type: "small"
        theme_bg_color: "Custom"
        md_bg_color: "FF7C6E"
        MDTopAppBarTitle:
            text: "About Us"
            valign: "center"
            theme_text_color: "Custom"
            text_color: "4C0000"
        MDTopAppBarTrailingButtonContainer:
            MDActionTopAppBarButton:
                icon: "arrow-left-bold-box"
                on_release: 
                    root.manager.current = "about"
                    root.manager.transition.direction = "right"
                theme_icon_color: "Custom"
                icon_color: "4C0000"     

<PreviousScoresScreen>
    name: "prev"  
    MDLabel:
        text: "Previous Scores"
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.9}
        anchor: "center"
        text_color: "FF7C6E"
        halign: "center"
        font_style: "Headline"
        role: "medium"  
    MDLabel:
        id: label21
        text: ""
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        anchor: "center"
        text_color: "CF3131"
        halign: "center"
        font_style: "Title"
        role: "small"    
    MDTopAppBar:
        type: "small"
        theme_bg_color: "Custom"
        md_bg_color: "FF7C6E"
        MDTopAppBarTitle:
            text: "Previous Scores"
            valign: "center"
            theme_text_color: "Custom"
            text_color: "4C0000"
        MDTopAppBarTrailingButtonContainer:
            MDActionTopAppBarButton:
                icon: "arrow-left-bold-box"
                on_release: 
                    root.manager.current = "intro_v"
                    root.manager.transition.direction = "right"
                    app.clear_screen()
                theme_icon_color: "Custom"
                icon_color: "4C0000"       
    
<DreamWaveScreen>
    name: "dream_w"
    MDSmartTile:
        pos_hint: {"center_x": 0.5, "center_y": 0.9}
        size_hint: None, None
        size: "285dp", "75dp"
        overlap: False
        MDSmartTileImage:
            source: "DreamWave.jpg"
            radius: [dp(24), dp(24), dp(24), dp(24)]
    MDLabel:
        text: "Please Answer Click the Buttons Above to Record Sleep and Wake-Up Times!"
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        anchor: "center"
        text_color: "FF7C6E"
        halign: "center"
        font_style: "Title"
        role: "medium"
    MDButton:
        id: button23
        style: "filled"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint: None, None
        size: "50dp", "50dp"
        on_press: app.record_time()
        MDButtonText:
            text: "Record Wake Time?"
            theme_text_color: "Custom"
            text_color: "CF3131"
            font_style: "Title"
            role: "medium"
    MDButton:
        id: button24
        style: "filled"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        size_hint: None, None
        size: "50dp", "50dp"
        on_press: app.record_time(pm = True)
        MDButtonText:
            text: "Record Sleep Time?"
            theme_text_color: "Custom"
            text_color: "CF3131"
            font_style: "Title"
            role: "medium"
            
    MDButton:
        style: "elevated"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        size_hint: None, None
        size: "40dp", "40dp"
        on_press:
            root.manager.transition.direction = "left"
            if app.print_sleep_log(self) and app.sleep_difference(self): root.manager.current = "dream_w2"
            
        MDButtonText:
            text: "See Records"
            theme_text_color: "Custom"
            text_color: "CF3131"
            font_style: "Title"
            role: "medium"
    MDNavigationDrawer:
        id: nav_drawer
        MDNavigationDrawerMenu:
            MDNavigationDrawerLabel:
                text: "Menu"
                theme_text_color: "Custom"
                text_color: "FF7C6E"
                font_style: "Title"
                role: "medium"
                valign: "center"
            MDNavigationDrawerDivider:
            
            MDNavigationDrawerItem:
                style: "filled"
                size_hint: None, None
                size: "300dp", "50dp"
                on_release: 
                    root.manager.current = "home"
                    nav_drawer.set_state("close")
                    root.manager.transition.direction = "left"
                MDNavigationDrawerItemLeadingIcon:
                    icon: "home-modern"
                    theme_icon_color: "Custom"
                    icon_color: "FF7C6E"
                    valign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.575}
                MDNavigationDrawerItemText:
                    text: "Home"
                    theme_text_color: "Custom"
                    pos_hint: {"center_x": 0.075, "center_y": 0.45}
                    text_color: "FF7C6E"
                    halign: "center"
                    font_style: "Title"
                    role: "medium"
            MDNavigationDrawerItem:
                style: "filled"
                size_hint: None, None
                size: "290dp", "50dp"
                on_release: 
                    root.manager.current = "task_l"
                    nav_drawer.set_state("close")
                    root.manager.transition.direction = "left"
                MDNavigationDrawerItemLeadingIcon:
                    icon: "list-box"
                    theme_icon_color: "Custom"
                    icon_color: "FF7C6E"
                    valign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.575}
                MDNavigationDrawerItemText:
                    text: "Task List"
                    theme_text_color: "Custom"
                    pos_hint: {"center_x": 0.13, "center_y": 0.45}
                    text_color: "FF7C6E"
                    halign: "center"
                    font_style: "Title"
                    role: "medium"
            MDNavigationDrawerItem:
                style: "filled"
                size_hint: None, None
                size: "290dp", "50dp"
                on_release: 
                    nav_drawer.set_state("close")
                    root.manager.current = "intro_v"
                    root.manager.transition.direction = "left"
                    app.clear_screen()
                MDNavigationDrawerItemLeadingIcon:
                    icon: "account-heart"
                    theme_icon_color: "Custom"
                    icon_color: "FF7C6E"
                    valign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.575}
                MDNavigationDrawerItemText:
                    text: "IntroVision"
                    theme_text_color: "Custom"
                    pos_hint: {"center_x": 0.16, "center_y": 0.45}
                    text_color: "FF7C6E"
                    halign: "center"
                    font_style: "Title"
                    role: "medium"
            MDNavigationDrawerItem:
                style: "filled"
                size_hint: None, None
                size: "290dp", "50dp"
                on_release: 
                    nav_drawer.set_state("close")
                    root.manager.current = "about"
                    root.manager.transition.direction = "left"
                MDNavigationDrawerItemLeadingIcon:
                    icon: "information"
                    theme_icon_color: "Custom"
                    icon_color: "FF7C6E"
                    valign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.575}
                MDNavigationDrawerItemText:
                    text: "About Us"
                    theme_text_color: "Custom"
                    pos_hint: {"center_x": 0.13, "center_y": 0.45}
                    text_color: "FF7C6E"
                    halign: "center"
                    font_style: "Title"
                    role: "medium"
    MDTopAppBar:
        type: "small"
        theme_bg_color: "Custom"
        md_bg_color: "FF7C6E"
        MDTopAppBarLeadingButtonContainer:
            MDActionTopAppBarButton:
                icon: "menu"
                theme_icon_color: "Custom"
                icon_color: "4C0000"
                on_press: nav_drawer.set_state("toggle")
        MDTopAppBarTitle:
            text: "DreamWave"
            text: "DreamWave"
            valign: "center"
            theme_text_color: "Custom"
            text_color: "4C0000"    

<AravScreen>
    name:"arav"
    MDSmartTile:
        pos_hint: {"center_x": 0.5, "center_y": 0.85}
        size_hint: None, None
        size: "236dp", "75dp"
        overlap: False
        MDSmartTileImage:
            source: "Arav_R.jpg"
            radius: [dp(24), dp(24), dp(24), dp(24)]
    MDLabel:
        id: label21
        text: "Hello, everyone! I am Arav Raghunathan, the Chief Technical Officer of MindGuard. I manage, develop, and communicate our novel technological and scientific ideas, which currently include our mobile application. From a young age, I have always been interested in biology. I am truly honored to present our idea and ecstatic about where this road takes us!"
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        anchor: "center"
        text_color: "CF3131"
        halign: "center"
        font_style: "Title"
        role: "small"    
    MDTopAppBar:
        type: "small"
        theme_bg_color: "Custom"
        md_bg_color: "FF7C6E"
        MDTopAppBarTitle:
            text: "Arav Raghunathan"
            valign: "center"
            theme_text_color: "Custom"
            text_color: "4C0000"
        MDTopAppBarTrailingButtonContainer:
            MDActionTopAppBarButton:
                icon: "arrow-left-bold-box"
                on_release: 
                    root.manager.current = "owner"
                    root.manager.transition.direction = "right"
                theme_icon_color: "Custom"
                icon_color: "4C0000"

<AyanScreen>
    name: "ayan"
    MDSmartTile:
        pos_hint: {"center_x": 0.5, "center_y": 0.85}
        size_hint: None, None
        size: "236dp", "75dp"
        overlap: False
        MDSmartTileImage:
            source: "Ayan_R.jpg"
            radius: [dp(24), dp(24), dp(24), dp(24)]
    MDLabel:
        id: label21
        text: "Hello, everyone! I am Ayan Raghunathan, the Chief Financial Officer of MindGuard. I manage the financial side of the business. I am thrilled at the prospect of turning my interest in these things into something that has a real world tangible benefit. I am excited for the future of this business and the impact we can make on the world."
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        anchor: "center"
        text_color: "CF3131"
        halign: "center"
        font_style: "Title"
        role: "small"    
    MDTopAppBar:
        type: "small"
        theme_bg_color: "Custom"
        md_bg_color: "FF7C6E"
        MDTopAppBarTitle:
            text: "Ayan Raghunathan"
            valign: "center"
            theme_text_color: "Custom"
            text_color: "4C0000"
        MDTopAppBarTrailingButtonContainer:
            MDActionTopAppBarButton:
                icon: "arrow-left-bold-box"
                on_release: 
                    root.manager.current = "owner"
                    root.manager.transition.direction = "right"
                theme_icon_color: "Custom"
                icon_color: "4C0000"
    
<ShashankScreen>
    name: "shashank"
    MDSmartTile:
        pos_hint: {"center_x": 0.5, "center_y": 0.85}
        size_hint: None, None
        size: "315dp", "75dp"
        overlap: False
        MDSmartTileImage:
            source: "Shashank_R.jpg"
            radius: [dp(24), dp(24), dp(24), dp(24)]
    MDLabel:
        id: label21
        text: "Hello! My name is Shashank Ramireddy and I am the Chief Executive Officer of MindGuard.  I manage the operational aspects of our business and ensure our company is headed towards success. I am excited about the prospect of our busines and the monumental impact we can have on society."
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        anchor: "center"
        text_color: "CF3131"
        halign: "center"
        font_style: "Title"
        role: "small"    
    MDTopAppBar:
        type: "small"
        theme_bg_color: "Custom"
        md_bg_color: "FF7C6E"
        MDTopAppBarTitle:
            text: "Shashank Ramireddy"
            valign: "center"
            theme_text_color: "Custom"
            text_color: "4C0000"
        MDTopAppBarTrailingButtonContainer:
            MDActionTopAppBarButton:
                icon: "arrow-left-bold-box"
                on_release: 
                    root.manager.current = "owner"
                    root.manager.transition.direction = "right"
                theme_icon_color: "Custom"
                icon_color: "4C0000"

<DreamWaveScreenTwo>
    name: "dream_w2"
    MDSmartTile:
        pos_hint: {"center_x": 0.5, "center_y": 0.9}
        size_hint: None, None
        size: "285dp", "75dp"
        overlap: False
        MDSmartTileImage:
            source: "Analytics.jpg"
            radius: [dp(24), dp(24), dp(24), dp(24)]
    MDLabel:
        id: label23
        text: ""
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        anchor: "center"
        text_color: "CF3131"
        halign: "center"
        font_style: "Title"
        role: "small"
    MDLabel:
        id: label24
        text: ""
        theme_text_color: "Custom"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        anchor: "center"
        text_color: "FF7C6E"
        halign: "center"
        font_style: "Title"
        role: "medium"
    MDButton:
        id: button12
        style: "elevated"
        pos_hint: {"center_x": 0.5, "center_y": 0.15}
        halign: "center"
        size_hint: None, None
        size: "75dp", "40dp"
        on_press: app.clear_all()
        MDButtonText:
            text: "Clear All"
            theme_text_color: "Custom"
            text_color: "FF7C6E"
            font_style: "Title"
            role: "medium"
    MDTopAppBar:
        type: "small"
        theme_bg_color: "Custom"
        md_bg_color: "FF7C6E"
        MDTopAppBarTitle:
            text: "Sleep Log"
            valign: "center"
            theme_text_color: "Custom"
            text_color: "4C0000"
        MDTopAppBarTrailingButtonContainer:
            MDActionTopAppBarButton:
                icon: "arrow-left-bold-box"
                on_release: 
                    root.manager.current = "dream_w"
                    root.manager.transition.direction = "right"
                theme_icon_color: "Custom"
                icon_color: "4C0000"

"""