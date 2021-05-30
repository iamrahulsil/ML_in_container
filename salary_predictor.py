from joblib import load
from subprocess import getstatusoutput

model = load("salary.pk1")

rc, host = getstatusoutput("hostname")
print("\n\n\t Welcome to ML model inside a container with Hostname: ", host )
while True:
    yop = float( input ( "\n\n\t Please Enter the years of Experience: " ) )

    print("\n\t Your salary is : Rs. ", str(list(model.predict([[ yop ]])))[1:-1])

    choice = input( "\n\n\t Do you want to enter another value: Y or N:  ")
    if( choice == "N" ):
        print("\n\n\t Thank you for using the app !!\n\n " )
        exit()
    else:
        continue
