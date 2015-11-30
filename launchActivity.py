import commands
import sys
import re
import os

try:
    sys.path.append(os.path.join(os.environ['ANDROID_VIEW_CLIENT_HOME'], 'src'))
except:
    pass

from com.dtmilano.android.viewclient import ViewClient, TextView, EditText

import pkg_resources
from com.dtmilano.android.adb.adbclient import AdbClient
from PIL import Image

#Constants

#Login and password
LOGIN = 'test@vetondemand.com'
PASSWORD = "12345"

#Activities
TOUR_ACTIVITY_ID = 'com.lionhouse.vetondemand/.activities.TourActivity'
DASHBOARD_ACTIVITY_ID = 'com.lionhouse.vetondemand/.activities.DashboardActivity'

#TourActivity
TOUR_SIGN_UP_BTN_ID = 'com.lionhouse.vetondemand:id/tour_sign_up'

#SignUpActivity
LOG_IN_BTN_ID = 'com.lionhouse.vetondemand:id/log_in'
SIGN_UP_BTN_ID = 'com.lionhouse.vetondemand:id/tour_sign_up'
LOG_IN_WITH_EMAIL_BTN_ID = 'com.lionhouse.vetondemand:id/log_in_email'
EMAIL_TEXT_FIELD_ID = 'com.lionhouse.vetondemand:id/email'
PASSWORD_TEXT_FIELD_ID = 'com.lionhouse.vetondemand:id/password'
SUBMIT_BTN_ID = 'com.lionhouse.vetondemand:id/log_in'

#DashboardActivity
NEW_CONSULTATION_VIEW_ID = 'com.lionhouse.vetondemand:id/call_vet_now'
FIND_VET_ID = 'com.lionhouse.vetondemand:id/find_vet'
INVITE_VET_ID = 'com.lionhouse.vetondemand:id/invite_vet'
ENTER_CODE_ID = 'com.lionhouse.vetondemand:id/enter_code'
ADD_PET_ID = 'com.lionhouse.vetondemand:id/add_pet'

#AddPetFragment
ADD_PET_NAME_VIEW_ID = 'com.lionhouse.vetondemand:id/name'



#Header items
PROFILE_VIEW_ID = 'com.lionhouse.vetondemand:id/profile_name'

#Navigation Drawer Items
VETS = 'VETS'
PETS = 'PETS'
CONSULTS = 'CONSULTS'
SUBSCRIPTION = 'SUBSCRIPTION'
PROMOTION = 'PROMOTION'
PAYMENT = 'PAYMENT'
SUPPORT = 'SUPPORT'
ABOUT = 'ABOUT'

#VetsFragment
VETS_NAME_VIEW_ID = 'com.lionhouse.vetondemand:id/name'

#Tabs in ViewPager in VetsFragment
ABOUT_TAB_VIEW_ID = 'About'
DETAILS_TAB_VIEW_ID = 'Details'
HISTORY_TAB_VIEW_ID = 'History'

#PetsFragment
PETS_NAME_VIEW_ID = 'com.lionhouse.vetondemand:id/name'

#Tabs in ViewPager in PetsFragment
PROFILE_TAB_VIEW_ID = 'Profile'
PHOTOS_TAB_VIEW_ID = 'Photos'
HISTORY_TAB_VIEW_ID = 'History'

#ConsultsFragment
CONSULTS_VET_NAME_ID = 'com.lionhouse.vetondemand:id/vet_name'




# Function definition
def launchTourActivity():
    print "Opening TourActivity"
    device.startActivity(component='com.lionhouse.vetondemand/.activities.SplashActivity')
    return;

def launchActivity(activityId):
    print "launching " + activityId
    device.startActivity(component=activityId)
    return;

def clickViewById(viewId):
    button = vc.findViewByIdOrRaise(viewId)
    button.touch()
    return;

def clickViewByName(viewName):
    view = vc.findViewWithText(viewName);
    view.touch()
    return;

def typeText(viewId,text):
    textFiled = vc.findViewByIdOrRaise(viewId)
    textFiled.touch()
    textFiled.type(text)
    return;

def makeDump():
    print "Making dump..."
    vc.dump()
    vc.traverse(transform=ViewClient.TRAVERSE_CIT)
    return;

def wait():
    vc.sleep(3)
    return;

def waitForScreen():
    vc.sleep(2)
    return;

def makeScreen(name):
    print "Making screenshot..."
    device.takeSnapshot().save('/Users/Mikhail/screens/' + name +'.png')
    waitForScreen()
    return;

def makeSwipeForNavigationDrawer():
    print "Swiping..."
    AdbClient(serialno='.*').drag((5, 150), (550, 150), 100)
    vc.sleep(4)
    makeDump()
    return;

def makeSwipeDown():
    print "Swiping down..."
    AdbClient(serialno='.*').drag((550, 450), (550, 150), 100)
    vc.sleep(4)
    makeDump()
    return;

def makeScreenForProfile():
    clickViewById(PROFILE_VIEW_ID)
    vc.sleep(1)
    makeDump()
    makeScreen("ProfilePage")
    return;

def makeScreensForAddPet():
    clickViewById(ADD_PET_ID)
    vc.sleep(1)
    makeDump()
    makeScreen("AddPetSelect")
    vc.sleep(1)

    #Select type of pet (e.g. canine)
    clickViewById(ADD_PET_NAME_VIEW_ID)
    vc.sleep(1)
    makeDump()
    makeScreen("AddPetFragment")
    return;

def makeScreenForEnterACode():
    clickViewById(ENTER_CODE_ID)
    vc.sleep(1)
    makeScreen("EnterACodeFragment")
    vc.sleep(2)
    return;

def makeScreenForFindYourVet():
    clickViewById(FIND_VET_ID)
    vc.sleep(1)
    makeScreen("FindVetFragment")
    vc.sleep(2)
    return;

def makeScreenForInviteYourVet():
    clickViewById(INVITE_VET_ID)
    vc.sleep(1)
    makeScreen("InviteVetDialog")
    vc.sleep(2)
    return;

def makeScreenForNewConsultation():
    clickViewById(NEW_CONSULTATION_VIEW_ID)
    vc.sleep(1)
    makeScreen("NewConsultationFragment")
    vc.sleep(2)
    return;

def makeScreensForVets():
    clickViewByName(VETS)
    wait()
    makeDump()
    makeScreen("VetsFragment")


    clickViewById(VETS_NAME_VIEW_ID)
    wait()
    makeDump()

    clickViewByName(ABOUT_TAB_VIEW_ID)
    makeScreen("AboutViewPager")


    clickViewByName(DETAILS_TAB_VIEW_ID)
    makeScreen("DetailsViewPager")


    clickViewByName(HISTORY_TAB_VIEW_ID)
    makeScreen("HistoryViewPager")

    return;

def makeScreensForPets():
    # Launch PetsFragment
    clickViewByName(PETS)
    wait()
    makeDump()
    makeScreen("PetsFragment")

    # Open first pet
    clickViewById(PETS_NAME_VIEW_ID)
    wait()
    makeDump()

    # Select pet profile
    clickViewByName(PROFILE_TAB_VIEW_ID)
    makeScreen('PetsProfile')

    # Select pet photos
    clickViewByName(PHOTOS_TAB_VIEW_ID)
    makeScreen('PetsPhotos')

    # Select pet history
    clickViewByName(HISTORY_TAB_VIEW_ID)
    makeScreen('PetHistory')
    return;

def makeScreenForConsults():
    # Launch Consults fragment
    clickViewByName(CONSULTS)
    wait()
    makeDump()
    makeScreen('Consults')

    # Select first item from list
    clickViewById(CONSULTS_VET_NAME_ID)
    wait()
    makeScreen('ConsultsDetails')
    return;

def makeScreenForSubscription():
    # Launch Subscription fragment
    clickViewByName(SUBSCRIPTION)
    wait()
    makeDump()
    makeScreen('SubscriptionFragment')
    return;

def makeScreenForPromotion():
    # Launch Promotion fragment
    clickViewByName(PROMOTION)
    wait()
    makeDump()
    makeScreen('PromotionFragment')
    return;

def makeScreenForPayment():
    # Launch Payment fragment
    clickViewByName(PAYMENT)
    wait()
    makeDump()
    makeScreen('PaymentFragment')
    return;

def makeScreenForSupport():
    print "Making screenshots for Support fragment"
    # Launch Support fragment
    clickViewByName(SUPPORT)
    wait()
    makeDump()
    makeScreen('SupportFragment')
    returnToHome()
    return;

def makeScreenForAbout():
    print "Making screenshots for About fragment"
    # Launch About fragment
    clickViewByName(ABOUT)
    wait()
    makeDump()
    makeScreen('AboutFragment')
    returnToHome()
    return;

def returnToHome():
    print "Going home"
    launchActivity(DASHBOARD_ACTIVITY_ID)
    vc.sleep(2)
    makeSwipeForNavigationDrawer()
    return;


# starting script
print "start"

# connection to the current device, and return a MonkeyDevice object
device, serialno = ViewClient.connectToDeviceOrExit(verbose=True)
vc = ViewClient(device=device, serialno=serialno)

# apk_path = device.shell('pm path com.lionhouse.vetondemand')
# if apk_path.startswith('package:'):
#     print "myapp already installed."
# else:
#     print "myapp not installed, installing APKs..."
#     device.installPackage('base.apk')

print "launching myapp..."
case = "TourActivity"
launchTourActivity()
vc.sleep(10)
makeScreen(case)


# print "go to Sign Up"
# clickViewById(SIGN_UP_BTN_ID)
# vc.sleep(3)
# makeDump()
# makeScreen("SignUpActivity")
#
#
# print "go to LogIn"
# makeDump()
# clickViewById(LOG_IN_BTN_ID)
# vc.sleep(3)
# makeScreen("LoginDialog")
#
#
# print "go to LogIn with email"
# makeDump()
# clickViewById(LOG_IN_WITH_EMAIL_BTN_ID)
#
#
# print "start to put data"
# makeDump()
# typeText(EMAIL_TEXT_FIELD_ID,LOGIN)
# typeText(PASSWORD_TEXT_FIELD_ID,PASSWORD)
#
# clickViewById(SUBMIT_BTN_ID)
# vc.sleep(5)
#
# print "explore home activity"
# makeDump()
# makeScreen("DashboardActivity")

# #Swipe
# makeSwipeForNavigationDrawer()
# makeDump()


#region Vets

#makeScreensForVets()

#Return to Home Activity

#launchActivity(DASHBOARD_ACTIVITY_ID)
#makeSwipeForNavigationDrawer()

# region Pets
#makeScreensForPets()

# region Consults
#makeScreenForConsults()

# # region Subscription
# makeScreenForSubscription()
# returnToHome()
# vc.sleep(2)
#
# # region Promotion
# makeScreenForPromotion()
# returnToHome()
# vc.sleep(2)
#
# # region Payment
# makeScreenForPayment()
# returnToHome()
# vc.sleep(2)
#
# # region Support
# makeScreenForSupport()
# vc.sleep(2)
#
# makeSwipeDown()
#
# makeScreenForAbout()
# returnToHome()
# vc.sleep(2)
#
# makeScreenForProfile()
# vc.sleep(2)
# launchActivity(DASHBOARD_ACTIVITY_ID)
# vc.sleep(4)

# makeScreensForAddPet()
# launchActivity(DASHBOARD_ACTIVITY_ID)
# vc.sleep(4)
# makeDump()
#
# makeScreenForEnterACode()
# launchActivity(DASHBOARD_ACTIVITY_ID)
# vc.sleep(2)
# makeDump()
#
# makeScreenForFindYourVet()
# launchActivity(DASHBOARD_ACTIVITY_ID)
# vc.sleep(2)
# makeDump()
#
# makeScreenForInviteYourVet()
# launchActivity(DASHBOARD_ACTIVITY_ID)
# vc.sleep(2)
# makeDump()
#
# makeScreenForNewConsultation()
# launchActivity(DASHBOARD_ACTIVITY_ID)






# TODO write handle error when screen too small and the programm didn't find the items on the menu
# TODO add support of more than 2 devices

print "end of script"