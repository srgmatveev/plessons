#!/usr/bin/env python
import cgi
reshtml = '''Content-Type: text/html\n
<HTML><HEAD><TITLE>
Friends CGI Demo (dynamic screen)
</TITLE></HEAD>
<BODY><H3>Friends list for: <I>{0}</I></H3>
Your name is: <B>{0}</B><P>
You have <B>{1}</B> friends.
</BODY></HTML>'''
form = cgi.FieldStorage()
who = form['person'].value
howmany = form['howmany'].value
print(reshtml.format(who, howmany))
