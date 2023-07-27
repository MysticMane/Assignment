import csv
def write_csv(info_list):
    with open('student.csv','a', newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name", "Age", "Contact_number", "E-mail_ID"])
        writer.writerow(info_list)

if __name__=="__main__":
    condition=True
    num=1
    while(condition):
        sf=input("Enter the info for student #{} in (Name Age Contact_number E-main ID) format\n".format(num))
        a=sf.split(' ')
        print("\nThe Entered info is \nName: {}\nAge: {}\nContact_number: {}\nE-mail_ID: {}"
              .format(a[0],a[1],a[2],a[3]))
        n=input("Is the Entered value correct?(y/n)")
        if n=="y":
            write_csv(a)
            p=input("\nPress yes(y)to continue adding student info or no(n) to stop: ")
            if (p=="yes" or p=="y"):
                condition=True
                num+=1
            elif (p=="no" or p=="n"):
                condition=False
        elif n=="n":
            print("\nRe enter the correct value")
