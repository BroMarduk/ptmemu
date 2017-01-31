#!/usr/bin/python
##################################################################################
# IMPORTS
##################################################################################
# The "from tftmenu import *" and "from tfttemplates import *" items need to be
# present in all display applicaitons.
from tfttemplates import *
from tftmenu import *


##################################################################################
# DISPLAY_PI_TEMP CUSTOM HEADER FUNCTION
##################################################################################
def display_pi_temp(header=None):
    res = os.popen('vcgencmd measure_temp').readline()
    deg = u'\N{DEGREE SIGN}'
    if isinstance(header, Header):
        temp = res.replace("temp=", "").replace("'C\n", "")
        val = float(temp)
        if val < 0:
            header.text.fontColor = Color.Blue
        elif val < 80.0:  # Pi turns on processor throttling
            header.text.fontColor = Color.Green
        elif val < 85.0:  # Pi turns on processor and cpu throttling
            header.text.fontColor = Color.Yellow
        else:
            header.text.fontColor = Color.Red
    return res.replace("temp=", "Pi Temp: ").replace("'", deg).replace("\n", "")


##################################################################################
# DISPLAY INITIALIZATION
##################################################################################
# The proper Adafruit PiTFT type needs to be passed to the initialization method
# in order to correctly initialize the GPIOs for the button functionality and set
# the correct screen resolution.  The following displays are supported, which is
# all of the Adafruit PiTFT displays.  If using the 2.2 inch display without
# touch support (currently the only one), a mouse will need to be utilized for
# the menu to work correctly.
# DISP22NT   = AF_2315 = NONE22 = 1  # GPIOs 17,22,23,27,(18)
# DISP24R    = AF_2455 = RES24  = 2  # GPIOs 16,13,12,6,5,(18)
# DISP28R    = AF_1601 = RES28  = 3  # GPIOs 23,22,21/27,18,(None)
# DISP28C    = AF_1983 = CAP28  = 4  # GPIOs 23,22,21/27,17,(18)
# DISP28RP   = AF_2298 = RES28P = 5  # GPIOs 17,22,23,27,(18)
# DISP28CP   = AF_2423 = CAP28P = 6  # GPIOs 17,22,23,27,(18)
# DISP32RP   = AF_2626 = RES32P = 7  # GPIOs 22,23,17,27,(18)
# DISP35R    = AF_2097 = RES35  = 8  # GPIOs (18)
# DISP35RP   = AF_2441 = RES35P = 9  # GPIOs (18)
Displays.initialize(DISP28CP)


##################################################################################
# MENU TEMPLATES
##################################################################################
mainMenuButtons = get_buttons(ButtonTemplate.FullScreen3x4, border_color=Color.Blue, font_size=10,
                              names=["No Header",
                                     "Date ",
                                     "Time (12 Hour)",
                                     "Time (24 Hour)",
                                     "Date/Time (US)",
                                     "Date/Time (Intl)",
                                     "Custom Date 12",
                                     "Custom Date 24",
                                     "Host Name",
                                     "User Text ",
                                     "User Function",
                                     "Exit"],
                              actions=[Action(DisplayAction.Display, "menuNone"),
                                       Action(DisplayAction.Display, "menuDate"),
                                       Action(DisplayAction.Display, "menuTime12"),
                                       Action(DisplayAction.Display, "menuTime24"),
                                       Action(DisplayAction.Display, "menuDateTime12"),
                                       Action(DisplayAction.Display, "menuDateTime24"),
                                       Action(DisplayAction.Display, "menuDateCust1"),
                                       Action(DisplayAction.Display, "menuDateCust2"),
                                       Action(DisplayAction.Display, "menuHostName"),
                                       Action(DisplayAction.Display, "menuUserText"),
                                       Action(DisplayAction.Display, "menuUserFunc"),
                                       Action(DisplayAction.Exit)])
if mainMenuButtons is not None:
    mainMenu = Menu(timeout=90, buttons=mainMenuButtons, border_color=Color.Green)
    Displays.menus["Main"] = mainMenu
header_none = get_buttons(ButtonTemplate.Header2x3, border_color=Color.Orange)
if header_none is not None:
    header_none[len(header_none) - 1].text = "Back"
    header_none[len(header_none) - 1].action = Action(DisplayAction.Display, "Main")
    menu_header_none = Menu(timeout=90, buttons=header_none,
                            header=Header(type=HeadFootType.NoDisplay))
    Displays.menus["menuNone"] = menu_header_none
header_date = get_buttons(ButtonTemplate.Header2x3, border_color=Color.Yellow)
if header_date is not None:
    header_date[len(header_date) - 1].text = "Back"
    header_date[len(header_date) - 1].action = Action(DisplayAction.Display, "Main")
    menu_header_date = Menu(timeout=90, buttons=header_date,
                            header=Header(type=HeadFootType.Date))
    Displays.menus["menuDate"] = menu_header_date
header_time_12 = get_buttons(ButtonTemplate.Header2x3, border_color=Color.Red)
if header_time_12 is not None:
    header_time_12[len(header_time_12) - 1].text = "Back"
    header_time_12[len(header_time_12) - 1].action = Action(DisplayAction.Display, "Main")
    menu_header_time_12 = Menu(timeout=90, buttons=header_time_12,
                               header=Header(type=HeadFootType.Time12))
    Displays.menus["menuTime12"] = menu_header_time_12
header_time_24 = get_buttons(ButtonTemplate.Header2x3, border_color=Color.Red)
if header_time_24 is not None:
    header_time_24[len(header_time_24) - 1].text = "Back"
    header_time_24[len(header_time_24) - 1].action = Action(DisplayAction.Display, "Main")
    menu_header_time_24 = Menu(timeout=90, buttons=header_time_24,
                               header=Header(type=HeadFootType.Time24))
    Displays.menus["menuTime24"] = menu_header_time_24
header_date_time_12 = get_buttons(ButtonTemplate.Header2x3, border_color=Color.Green)
if header_date_time_12 is not None:
    header_date_time_12[len(header_date_time_12) - 1].text = "Back"
    header_date_time_12[len(header_date_time_12) - 1].action = Action(DisplayAction.Display, "Main")
    menu_header_date_time_12 = Menu(timeout=90, buttons=header_date_time_12,
                                    header=Header(type=HeadFootType.DateTime12))
    Displays.menus["menuDateTime12"] = menu_header_date_time_12
header_date_time_24 = get_buttons(ButtonTemplate.Header2x3, border_color=Color.Green)
if header_date_time_24 is not None:
    header_date_time_24[len(header_date_time_24) - 1].text = "Back"
    header_date_time_24[len(header_date_time_24) - 1].action = Action(DisplayAction.Display, "Main")
    menu_header_date_time_24 = Menu(timeout=90, buttons=header_date_time_24,
                                    header=Header(type=HeadFootType.DateTime24))
    Displays.menus["menuDateTime24"] = menu_header_date_time_24
header_date_cust_1 = get_buttons(ButtonTemplate.Header2x3, border_color=Color.Magenta)
if header_date_cust_1 is not None:
    header_date_cust_1[len(header_date_cust_1) - 1].text = "Back"
    header_date_cust_1[len(header_date_cust_1) - 1].action = Action(DisplayAction.Display, "Main")
    menu_header_date_cust_1 = Menu(timeout=90, buttons=header_date_cust_1,
                                   header=Header(type=HeadFootType.DateTimeCustom,
                                                 data="%-I:%M:%S %p",
                                                 refresh=DisplayHeaderRefresh.Second))
    Displays.menus["menuDateCust1"] = menu_header_date_cust_1
header_date_cust_2 = get_buttons(ButtonTemplate.Header2x3, border_color=Color.Magenta)
if header_date_cust_2 is not None:
    header_date_cust_2[len(header_date_cust_2) - 1].text = "Back"
    header_date_cust_2[len(header_date_cust_2) - 1].action = Action(DisplayAction.Display, "Main")
    menu_header_date_cust_2 = Menu(timeout=90, buttons=header_date_cust_2,
                                   header=Header(type=HeadFootType.DateTimeCustom, data="%H:%M:%S",
                                                 refresh=DisplayHeaderRefresh.Second))
    Displays.menus["menuDateCust2"] = menu_header_date_cust_2
header_host_name = get_buttons(ButtonTemplate.Header2x3, border_color=Color.Purple)
if header_host_name is not None:
    header_host_name[len(header_host_name) - 1].text = "Back"
    header_host_name[len(header_host_name) - 1].action = Action(DisplayAction.Display, "Main")
    menu_header_host_name = Menu(timeout=90, buttons=header_host_name,
                                 header=Header(type=HeadFootType.HostName))
    Displays.menus["menuHostName"] = menu_header_host_name
header_user_text = get_buttons(ButtonTemplate.Header2x3, border_color=Color.Cyan)
if header_user_text is not None:
    header_user_text[len(header_user_text) - 1].text = "Back"
    header_user_text[len(header_user_text) - 1].action = Action(DisplayAction.Display, "Main")
    menu_header_user_text = Menu(timeout=90, buttons=header_user_text,
                                 header=Header(type=HeadFootType.UserText,
                                               text=HeadFootLine(text="Custom User Text",
                                                                 font_size=32, font_color=Color.Cyan,
                                                                 font_h_align=TextHAlign.Left)))
    Displays.menus["menuUserText"] = menu_header_user_text
header_user_func = get_buttons(ButtonTemplate.Header2x3, border_color=Color.White)
if header_user_func is not None:
    header_user_func[len(header_user_func) - 1].text = "Back"
    header_user_func[len(header_user_func) - 1].action = Action(DisplayAction.Display, "Main")
    menu_header_user_func = Menu(timeout=90, buttons=header_user_func,
                                 header=Header(type=HeadFootType.UserFunction,
                                               data=display_pi_temp, refresh=DisplayHeaderRefresh.Minute))
    Displays.menus["menuUserFunc"] = menu_header_user_func
Displays.start(initial_menu=Displays.menus["Main"], backlight_method=BacklightMethod.Pwm)