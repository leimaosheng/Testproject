#!-coding:utf-8-
#!auuthor lms
import os

unconfirmed_users=['alice','brain','candace']
confirmed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print("Verifying user:"+current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

responses={}
polling_active=True

while polling_active:
    name=input("\nWhat is your name? :")
    response=input("which is mountain would you like to climb someday?")
    responses[name]=response
    repeat=input("Would you like to let anthor person respond(yes/no)")
    if repeat == "no":
        polling_active=False

print("=====poll Reslts====")
for name,response in responses.items():
    print(name+" would you like climb "+response+".")

def my_print(var):
    print(var)