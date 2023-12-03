# wrrite a programm to find a person is eligiable to vate or not.if person is not eleigiable thow tto year are left to be eligilable
# age=int(input("Enter your age: "))
# if age<18:
#     print("You have to wait for",18-age,"to age to vote")
# else:
#     print("You are able to vote")


#write a progamm to enter a cher if the enter cher is in lowwer case then convert it into upper case and if the enter char is in upper case than convert it into lower case

char=str(input("Enter the char: "))
if char>="A" and char<="Z":
    ch=char.lower()
    print("the char is in lower case:",ch)
else:
    ch=char.upper()
    print("the char is in upper case:",ch)