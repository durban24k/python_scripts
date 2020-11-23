import speedtest
from hurry.filesize import size

st = speedtest.Speedtest()

while(True):
    option = int(input(''' What speed do you want to test : 
    1) Download Speed
    2) Upload Speed
    Your Choice : '''))

    if(option == 1):
        print("Connecting...")
        print("Download speed is : ", size(st.download()))
        break
    elif(option == 2):
        print("Connecting...")
        print("Upload speed is : ", size(st.upload()))
        break
    else:
        print("Please choose an option !!")
        continue
    