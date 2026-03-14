import string
import secrets
from flask import Flask, send_file

app = Flask(__name__)

plain_text = 'Executing Code with Too Much Privilege Computers talk to other computers and are users in their own rights As users they must have privileges to access program and data on other computers  When systems are set up withexcessive privileges they can create security issues  Just like users systems and applications should only have theleast privilege they need to do the job  Developers may initially assign higherlevel privileges in the development of anapplication and then may forget to lower those privileges  If attackers can compromise a system with these highlevelprivileges they can use that access to take over other systems  One of the greatest concerns in this area occurs whenindividuals download and run code from public sources like Web sites  Because you did not develop the code or paya professional vendor for it you can not be certain that the code does not contain malicious components like back doorsor data exfiltration components Failure to Protect Stored Data Protecting stored data is a large enough issue to be the core subject of this entiretext  Programmers are responsible for integrating access controls into programs and keeping secret information outof them  Access controls the subject of later modules regulate who what when where and how users and systemsinteract with data  Failure to properly implement sufficiently strong access controls makes the data vulnerable  Overlystrict access controls hinder business users in the performance of their duties and as a result the controls may beadministratively removed or bypassed  The integration of secret informationsuch as the hard coding of passwordsencryption keys or other sensitive informationcan put that information at risk of disclosure The Sins of Mobile Code In this context mobile code is an application applet macro or script that may be imbedded in another application or document and thus downloaded and executed without the user even knowing andespecially without consenting  Office suite tools are notorious for using macros and third parties could insert malicious content into existing office documents shared by users'.upper()


secret_key = {}
decription_key = {}
cipher_text = ""
decryted_text = ""

alphabet = string.ascii_uppercase

for i in alphabet:
    ch = secrets.choice(alphabet)
    secret_key[i] = ch
    alphabet = alphabet.replace(ch,'')


for k,v in secret_key.items():
    decription_key[v] = k

#encryption part

for i in plain_text:
    if i == ' ':
        cipher_text += ' '
    else:
        cipher_text += secret_key[i]
    
print("Success")
with open("secret_key.txt","w") as file:
    file.write("--------------Encryption-------------- Key\n"+str(secret_key)+"\n")
with open("cipher_text.txt","w") as file:
    file.write("-----------Cipher Text------------\n"+cipher_text)

@app.route('/')
def d(): return send_file("cipher_text.txt", as_attachment=True)

if __name__ == '__main__':
    app.run()




#three problems
#1. choosing same substitution letters => solved by removing the randomly selected value every time
#2. space and special characters. solved by applying data cleaning first.
#3. I don't know how to make it secret from my self. 
    #solution 1. make it dynamic secret key.
    #solution 2. email my self and do not display on the console.
    #problem=> I don't know how to send email using python. 
       #better solution web hosting using flask to download the cipher text. 


