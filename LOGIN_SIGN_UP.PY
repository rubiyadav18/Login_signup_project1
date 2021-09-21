import json

name=input("Please Enter Your Name\n--")
print("Hello",name)

user=input("Enter what you want :)\n1.signup\n2.login\n--")
if user=="1" or user=="signup":
    userName=input("Enter your userName:)\n--")
    password1=input("Enter password\n")
    password2=input("Enter the confirm password\n--")
    dob=input("enter your date of birth\n--")
    Gender=input("enter male or female\n--")
    Hobby=input("enter your hobby\n--")



    dic={"userName":userName,"password1":password1,"Profile":{"DOB":dob,"gender":Gender,"hobby":Hobby}}


    if len(password1)>=8 and "@" in password1 or "#" in password1:

            if password1==password2:
                # user existing checking here...
                with open('userDetails.json','r') as f:
                    userData=json.load(f)
                    for i in userData['allUserDetails']:

                        if i['userName']==userName and i['password']==password1:

                            print("User already Exist :)")
                            break
                    else:
                # -----SignUp Section----
                        with open('userDetails.json') as json_file: 

                            data = json.load(json_file) 

                            temp = data["allUserDetails"] 

                            temp.append(dic)

                        
                        with open("userDetails.json","w") as data1:
                            
                            json.dump(data, data1,indent=4)

                        print("congurlation",userName,"you account succesfully created....")
            # <------->
            else:
                print("your password not same please enter same password--")
    else:
        print("in your password no special character at least put 1 special character ")


else:
    if user=="2" or user=="login": 


        # ----Login Section---
        print('Hey:',name, 'Welcome To Login Page :)')

        userName=input("enter the userName:) ")

        loginPassword=input('enter the password:)')
     
        with open('userDetails.json','r') as f:

            userData=json.load(f)

            for i in userData['allUserDetails']:

                if i['userName']==userName and i['password']==loginPassword:

                    print("Login Successfully :)")

                    break
                    
            else:
                print("\n\n\tpassword/userName is wrong")
                
    else:
        print('Please Enter The C0rrect Input')
        
