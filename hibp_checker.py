import os
import sys
import pypwned
import json
import time


try:
    import pypwned
except ImportError as e:
    os.system("pip3 install pypwned")

your_hibp_key = open("api.txt").read().strip()
pwny = pypwned.pwned(your_hibp_key)


def write_file(filename, line):
    f = open(filename, "a+")
    f.write(line.strip() + "\n")
    f.close()


def check_email(email):
    a = pwny.getAllBreachesForAccount(email=email)
    tmpstr = ""

    try:
        for b in a:
            bn = b['Name']
            tmpstr = tmpstr + bn + ","

        tmpstr = tmpstr[0:len(tmpstr) - 1]

        new_line = email + ",\"" + tmpstr + "\""
        write_file("output.txt", new_line)
        print(new_line)

    except Exception as ex:
        write_file("output.txt", email + ",ERROR")
        print("%s, ERROR" % (email))

    time.sleep(1.5)


def check_from_start():
    try:
        for l in [x.strip() for x in open(sys.argv[1]).readlines() if x.strip() != ""]:
            check_email(l)

        if os.path.exists("continue.txt"):
            os.unlink("continue.txt")

    except KeyboardInterrupt:
        print("Stopped")

        f = open("continue.txt", "w+")
        f.write(l.strip() + "\n")
        f.close


if os.path.exists("continue.txt"):
    answer = input("Do you want to continue from previous session? Enter yes or no: ") 
    if answer == "yes": 
        # Continue from ...
        continue_from = open("continue.txt").read().strip()

        c = [x.strip() for x in open(sys.argv[1]).readlines() if x.strip() != ""]
        index_continue = c.index(continue_from)
        new_list = c[index_continue+1:len(c)]

        try:
            for l in new_list:
                check_email(l)

            if os.path.exists("continue.txt"):
                os.unlink("continue.txt")

        except KeyboardInterrupt:
            print("Stopped")

            f = open("continue.txt", "w+")
            f.write(l.strip() + "\n")
            f.close        


    elif answer == "no": 
        # Check all
        if os.path.exists("output.txt"):
            os.unlink("output.txt")

        check_from_start()

    else: 
        print("Please enter yes or no.") 

else:
    check_from_start()




