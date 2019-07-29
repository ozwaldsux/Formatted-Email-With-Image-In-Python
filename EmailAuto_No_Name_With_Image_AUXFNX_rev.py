import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

host = "smtp.gmail.com"
port = 587
username = "wrigglemusic@gmail.com"
password = "fitzguber"
from_email = "wrigglemusic@gmail.com"
to_list = [""]

class MessageUser():
    user_details = []
    messages = []
    email_messages = []
    base_message = """\
<html>
  <head></head>
  <body>
    <p>Hi,<br><br>

Hope you're well today.<br><br>

I wanted to get in touch about a very exciting new release on our label, <b>Wriggle</b>. Experimental hip hop & jazz producer, multi-instrumentalist and DJ, <b>Auxiliary Phoenix</b> has returned
to his solo project,this time teaming up with emerging Irish rapper <b>Leo Miyagee</b> to deliver the superb <b>'If We Could Build'</b> Ep. This brilliant four-track release features
three forward-thinking instrumentals and a deadly vocal collaboration.<br><br>

We were wondering if you'd be interested in running a <b>feature</b> or <b>review</b> of <b>'If We Could Build"</b>?<br><br>

I've included some more information on the release below.<br><br>

Thanks<br><br>


<b>Artist</b>: Auxiliary Phoenix<br>
<b>Title</b>: If We Could Build <br>
<b>Label</b>: Wriggle <br>
<b>Release Date</b>: 4/6/2019 <br>
<a href="https://soundcloud.com/wriggledublin/sets/auxiliary-phoenix-if-we-could-build-ep/s-gSB0Q">Stream/Download</a> 
<br> <br>


<b>Press Release:</b><br>

Known for his forward-thinking sound that at times defies definition, Auxiliary Phoenix draws from a vast pool of influences, most notably Jazz and Hip-Hop, to create music that is truly unique. His inimitable 
style has been shown love throughout the music world, from icons such as <b>Thundercat</b> (for a solo bass piece) and <b>Mike Gao</b> (For BRB on Wriggle Vol 1) to grime visionary 
<b>Murlo</b> and <b>RTÉ 2FM DJ Dan Hegarty</b>. He has also worked with the likes of celebrated innovators of their respective scenes, <b>Divine Styler</b> and <b>Jon Anderson</b> of <b>Yes</b>. 
The ‘If We Could Build EP’ is Auxiliary Phoenix’s first foray into the ‘UK Bass’ sphere to be released, and the project could be seen as an interpretation of the Wriggle palette, which his sound has
since become encompassed within.<br><br>

Wasting no time, ‘A Distance’ launches us into a journey of contemporary jazz sculpted in the image of a footwork track, effortlessly lending live instrumentation with footwork sounds and oozing with math-rock 
influence, with guitar work harkening to the likes of Animals As Leaders and Tera Melos, and beats nodding to artists such as Kode9 and Mono/Poly. This is followed by the title track 'If We Could Build' which has 
been a staple Wriggle dub since its creation, and proposes a harmonious hybrid of R’n’G and UK Funky influences, driven by a striking lead vocal sample. Just as we’re beginning to feel safe, ’Summer Smack Aqua’ 
emerges from the deep to lead us on a wonky, dark adventure on a creaking pirate ship held together with duct tape. A remarkable exercise in sampling and sound design, Aquatic Smack was crafted around sound effects 
and foley samples taken from various movies. Wrapping up the release is ‘Tarmac Practice’. Being dropped into an Irish rap landscape where established artists don’t tend to sonically stray far from their
predecessors, ’Tarmac Practice’ throws down the gauntlet to any of the island’s rappers/ producers lacking innovation, seeking to inspire the creation of a new Irish sound. Featuring vocal performances from Leo Miyagee, 
Qboi Skew and Sambeau, this track is a departure from traditional rap sounds in Dublin, marking the shift towards a more innovative future.
<br><br>
<img src="cid:image1">
<img src="cid:image2">
<br><br>

    </p>
  </body>
</html>
"""

        
    def add_user(self, name, amount, email=None):
        amount = "%.2f" %(amount)
        detail = { 
        "name": name,
        "amount": amount,
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        if email is not None:
            detail['email'] = email
        self.user_details.append(detail)
    def get_details(self):
        return self.user_details
    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(
                    name=name,
                    date=date,
                    total=amount
                    )
                user_email = detail.get("email")
                if user_email:
                    user_data = {
                        "email": user_email,
                        "message": new_msg
                    }
                    self.email_messages.append(user_data)
                else:
                    self.messages.append(new_msg)
            return self.messages
        return[]
    def send_email(self):
        self.make_messages()
        if len(self.email_messages) > 0:
            for detail in self.email_messages:
                user_email = detail['email']
                user_message = detail['message']
                try:
                    email_conn = smtplib.SMTP(host, port)
                    email_conn.ehlo()
                    email_conn.starttls()
                    email_conn.login(username, password)
                    the_msg = MIMEMultipart("alternative")
                    the_msg['Subject'] = "Irish Producer, Auxiliary Phoenix Returns To Wriggle"
                    the_msg["From"] = str('Wriggle <wrigglemusic@gmail.com>')
                    the_msg['To'] = user_email 
                    part_1 = MIMEText(user_message, 'html')
                    the_msg.attach(part_1)
                    # This example assumes the image is in the current directory
                    fp = open('/Users/keithhazley/Documents/AUX_FNX_Press/if_we_could_build_cover5.png', 'rb')
                    msgImage = MIMEImage(fp.read())
                    fp.close()
                    fp2 = open('/Users/keithhazley/Documents/AUX_FNX_Press/press2.jpg', 'rb')
                    msgImage2 = MIMEImage(fp2.read())
                    fp.close()
                    # Define the image's ID as referenced above
                    msgImage.add_header('Content-ID', '<image1>')
                    msgImage2.add_header('Content-ID', '<image2>')
                    the_msg.attach(msgImage)
                    the_msg.attach(msgImage2)
                    email_conn.sendmail(from_email, [user_email], the_msg.as_string())
                    email_conn.quit()
                except smtplib.SMTPException:
                    print("error sending message")
            return True
        return False

    

obj = MessageUser()
obj.add_user('', 123.32, email='newmusic@goldenplec.com')
obj.add_user('', 123.32, email='info@hotpress.ie')
obj.add_user('', 123.32, email='info@electronicsound.co.uk')
obj.add_user('', 123.32, email='daryl@exclaim.ca')
obj.add_user('', 123.32, email='reiss.bruin@gmail.com')
obj.add_user('', 123.32, email='kristoffer@groove.de')
obj.add_user('', 123.32, email='soulivity@soulivity.com')
obj.add_user('', 123.32, email='laurenceremila@gmail.com')
obj.add_user('', 123.32, email='Laurie@thequietus.com')
obj.add_user('', 123.32, email='Rory@Thequietus.com')
obj.add_user('', 123.32, email='anna@thequietus.com')
obj.add_user('', 123.32, email='clubs@timeoutny.com')
obj.add_user('', 123.32, email='bittles.mag@titel-kulturmagazin.net')
obj.add_user('', 123.32, email='monvilleq@gmail.com')
obj.add_user('', 123.32, email='javimar@djmag.es')
obj.add_user('', 123.32, email='admin@djmag.fr')
obj.add_user('', 123.32, email='andrea@love-boat.org')
obj.add_user('', 123.32, email='press@jtvrecordings.com')
obj.add_user('', 123.32, email='info@djmagla.com')
obj.add_user('', 123.32, email='promo@djmag.nl')
obj.add_user('', 123.32, email='artem@djmag.ua')
obj.add_user('', 123.32, email='griboedoff@djmag.ua')
obj.add_user('', 123.32, email='yevgeniy@djmag.ua')
obj.add_user('', 123.32, email='djmagreviews@yahoo.com')
obj.add_user('', 123.32, email='alexcdnb@gmail.com')
obj.add_user('', 123.32, email='jeromerobins@me.com')
obj.add_user('', 123.32, email='erin.sharoni@djmag.com')
obj.add_user('', 123.32, email='boconnor@testa.com')
obj.add_user('', 123.32, email='jtremayne@testa.com')
obj.add_user('', 123.32, email='marcus@freshguide.de')
obj.add_user('', 123.32, email='promo@fuzz-mag.be')
obj.add_user('', 123.32, email='info@infusion.ae')
obj.add_user('', 123.32, email='feedback@intro.de')
obj.add_user('', 123.32, email='news@intro.de')
obj.add_user('', 123.32, email='christian.steinbrink@intro.de')
obj.add_user('', 123.32, email='sean@mixmagmedia.net')
obj.add_user('', 123.32, email='dave@dontstayin.com')
obj.add_user('', 123.32, email='digby@mixmag.net')
obj.add_user('', 123.32, email='nickdc@mixmag.net')
obj.add_user('', 123.32, email='chris@sixsix.asia')
obj.add_user('', 123.32, email='dave@sixsix.asia')
obj.add_user('', 123.32, email='c.hertler@partysan.net')
obj.add_user('', 123.32, email='weekender@virgilioclassics.com')
obj.add_user('', 123.32, email='v@clubbingbible.net')
obj.add_user('', 123.32, email='promo@emmagazine.be')
obj.add_user('', 123.32, email='g.hagmeier@partysan.net')
obj.add_user('', 123.32, email='rok.radobuljac@partysan.net')
obj.add_user('', 123.32, email='v.dore@partysan.net')
obj.add_user('', 123.32, email='redactie@djmag.nl')
obj.add_user('', 123.32, email='john@thequietus.com')
obj.add_user('', 123.32, email='l.rieul@traxmag.com')
obj.add_user('', 123.32, email='hello@viciousmagazine.com')
obj.add_user('', 123.32, email='promos@viciousmagazine.com')



obj.get_details()

obj.send_email()

