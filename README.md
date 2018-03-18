<h1 align="center">
  <img src="https://i.imgur.com/9HtMAdT.png" width="250">
  <br>
  MyBB-Automation
</h1>

Automate simple tasks with Python. Get your PM's, detect SPAM and even get recent threads in your own console.
It was mainly created for the forum "Greysec", however you can change the code and make it work for other websites.
<br>
It is as simple as changing the xpath!

This is not the final release, I plan on adding a notification system via SMTP or Telegram.


<h4>
Requirements
</h4>
<p>
      In order to run the tool you will need python and the dependencies found in requirements.txt, they can be automatically installed with </p>
```
pip install -r requirements.txt
```
<p>
Note that keyring is not mandatory (if set to manual) as it requires Mac OS X Keychain, Freedesktop Secret Service, KWallet or Windows Credential Locker</p>

<h4>
Current working features
</h4>
<ul style="list-style-type:disc">
  <li>Get threads and check if they are new</li>
  <li>Search for spam looking for keywords in threads</li>
  <li>Login system using keychains/manual</li>
  <li>Reload app every x seconds</li>
</ul>  

<h4>
TO-DO
</h4>
<ul style="list-style-type:disc">
  <li>Send alerts if SPAM is found</li>
  <li>Send alerts if new PM's are found</li>
  <li>Automatic responses to PM's</li>
  <li>Mark all PM's as read</li>
</ul>  

### Previews:

#### New threads

![New threads](https://i.imgur.com/8w5LRaR.png)

#### General Screenshot
![Login](https://i.imgur.com/oxZG6CG.png)
![General Screenshot](https://i.imgur.com/NiGUF4X.png)
