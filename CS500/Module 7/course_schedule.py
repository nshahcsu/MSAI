dict_room_number = {
                    "CSC101":"3004",
                    "CSC102":"4501",
                    "CSC103":"6755",
                    "NET110":"1244",
                    "COM241":"1411"
                    }

dict_instructors = {
                    "CSC101":"Haynes",
                    "CSC102":"Alvarado",
                    "CSC103":"Rich",
                    "NET110":"Burke",
                    "COM241":"Lee"
                    }

dict_meeting = {
                "CSC101":"8:00 a.m.",
                "CSC102":"9:00 a.m.",
                "CSC103":"10:00 a.m.",
                "NET110":"11:00 a.m.",
                "COM241":"1:00 p.m."
                }
avail_courses = ''
MAX_FAIL_COUNT = 5
fail_count = 0
while (fail_count < MAX_FAIL_COUNT):
    try:
        course_cd = input('Please enter Course Code to view schedule.\n').upper()
        avail_courses = ''
        if course_cd in (dict_room_number and dict_instructors and dict_meeting):     
            print('     ___                            ___         __                         _    _      ')      
            print('    / __| ___  _  _  _ _  ___ ___  |_ _| _ _   / _| ___  _ _  _ __   __ _ | |_ (_) ___  _ _   ')
            print('   | (__ / _ \| || || \'_|(_-</ -_)  | | | \' \ |  _|/ _ \| \'_|| \'  \ / _\` ||  _|| |/ _ \| \' \ ')
            print('    \___|\___/ \_,_||_|  /__/\___| |___||_||_||_|  \___/|_|  |_|_|_|\__,_| \__||_|\___/|_||_| ')
            print('\n\nInformation for the class:',course_cd)
            print("Room:", dict_room_number[course_cd], "Instructor:",dict_instructors[course_cd], "Meeting at:", dict_meeting[course_cd])
            if input("\n\nDo you wish to check details for another course? Type 'Y' for yes or press any key to Quit.\n").upper() == 'Y':
                continue
            else:
                print("Enjoy your Learning journey!!\n")
                break
        else:
            fail_count += 1
            if ( fail_count == MAX_FAIL_COUNT):
                print('\nMax allowed count of error reached. Please try again later.\n')
                break
            else:
                print("Please Enter correct Course Info.\nCurrently, Schedule is available for these courses:")
                for key in (dict_room_number and dict_instructors and dict_meeting):
                    avail_courses += (key + ' ')
                print(avail_courses)
    except:
        fail_count += 1
        print("Error. Something went wrong. Please try again.")






