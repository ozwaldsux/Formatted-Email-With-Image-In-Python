# Formatted-Email-With-Image-In-Python

This Python script allows formatted emails to be sent from a parsed mailing list and also allows user to add images. More personalized than bcc and a free option over paid alternatives that offer the same service.


## Getting Started


First thing you'll need is a .csv file with your mailing list. If you've stored these in an Excel spreadsheet, fear not as you can simply export it to .csv directly. Your .csv file needs to formatted as follows:
```
name,email,present
Bob,youremail@gmail.com,yes

```
The rows will correspond to parts of the script which we will discuss later. The 'present' row will act as an indicator for the object creator script to indicate that there is a name in the field to be formatted. I've found this particualrly useful when dealing with large mailing lists as often times you may have a person's email but not their first name. By including this feature we can skip over the emails which have no name and only format the ones that do without having to remove these fields. 
Now you need to save the .csv mailing list. As an example, lets call it 'example_list.csv'.


Once you have your .csv file ready, open the CSV_parse_object_create.py and insert the your mailing list into the csv reader as follows:
```
with open("example_list.csv") as csv_file:
```
Now you can run the script and it will output an object like this for each name and its corresponding email:

```
obj.add_user('Bob', email='youremail@gmail.com')
```
You should copy these and save them for later. 

## Deployment


In order for Python to able to access your gmail account, you need to enable less secure apps. This is obviously risky so I recommend only switching this on for the short ammount of time you need it and ONLY on a private, secure network or better yet with an email you've specifically created in order to use this script which has no sensitive or private information. You can access the less secure apps control panel from the link below:

https://myaccount.google.com/lesssecureapps

If you're still following, congrats! you're almost there. Now you need to open the 'Formatted_Email_Name_With_Image.py'. Here you need to insert your email and password as follows:

```
username = "youremail@gmail.com"
password = "Password"
from_email = "youremail@gmail.com"
```
and here:

``
the_msg["From"] = str('Bob <youremail@gmail.com>')
``

Next part is optional. If you want to embed an image in your email, simply copy and paste the path to the image file in the following line:
``
fp = open('Path/to/your/photo.png', 'rb')
``

If you don't need this feature simply comment out the following lines by using cmd+/ if you're on mac or alt+3 on windows:
``
                    fp = open('Path/to/your/photo.png', 'rb')
                    msgImage = MIMEImage(fp.read())
                    fp.close()
                    msgImage.add_header('Content-ID', '<image1>')
                    the_msg.attach(msgImage)
``

Finally you need to copy the output that you set aside from the CSV_parse_object_create.py file and paste it below the following line:
``
obj = MessageUser()
#Paste the obj.add_user() here
``
Now just run the script and watch you're mail fly out!

Disclaimer: gmail may stop the script from running depending on how many emails you send out as there is a limit per day. I've seen a few different metrics as to how many can be sent per minute but it's pretty unclear. However you can always start again from where the script was stopped by looking in your sent mail to see the last mail sent and run it again. If you're including images, bear in mind that gmail bandwidth limit is 300mb. The intent of this script is not to spam people so please use it responsibly.

## Authors
Ozwaldsux 

## Contributers
Big thanks to python Codex for his tutorials and Coding is for girls for hers.
