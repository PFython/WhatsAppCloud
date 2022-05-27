# Send unlimited Whatsapp messages from Python - for free!

It's true - you really can send free messages to five (verified) phone numbers for free using Meta's [WhatsApp Business Cloud API](https://developers.facebook.com/products/whatsapp/). The only proviso is that you agree to and follow their terms and conditions, especially regarding opting-in and acceptable use.

The even better news is that I've waded my way through the API docs and several published "works in progress" on Github, basically going down a few rat-holes so you won't have to! The result is about 20 lines of actual Python which you can copy into your own scripts to enjoy outbound Whatsapp notifications without having to learn the quirks of yet another API from scratch yourself. Or if you _do_ want to get a deeper understanding, you can head over to my evolving [Github repository](https://github.com/PFython/Whatsapp) where you'll find a [fully installable PyPI package](https://pypi.org/whatsappcloud) to hopefully fast-track your journey and move you towards using the more advanced features that much quicker.  If you do, please spare a nano-second to click on the STAR button top right of the screen?  A little appreciation can be life-affirming, thank you!

## TLDR: Here's the essential Python GIST to get you up and running

![](Screenshot%201.png)
> https://github.com/PFython/WhatsappCloud/blob/master/whatsappcloud/gist.py


### You'll need to jump through a few (easy) hoops registering as a Meta/Facebook developer before you can actually send messages, but once you've done so, sending messages will be as easy as this:

```
>>> Whatsapp()
# Send a test message with test url (and preview) to your default contact

>>> Whatsapp.text("Hello Monty", CONTACT[4])
# Send "Hello Monty" to your fifth contact

>>> wa = Whatsapp(autosend=False)
# Create but don't send a message.  Useful when testing/debugging and also if you intend to do any pre- or post- processing and want to control when a message is actually sent.

>>> wa.send()
# Send (or resend) a previously prepared message
```

### And here's the config file you'll need to update and rename once you've created your first Whatsapp Cloud App on the developers' portal (details below):

![](Screenshot%202.png)
> https://github.com/PFython/WhatsappCloud/blob/master/whatsappcloud/config_template.py

> *SOAP BOX alert! For some reason so many API tutorials seems to mix credentials and config data together in the same script. This is officially, quinetessentially, metaphysically, didactically and canonically **bad practice** and not to be emulated, so let's start the right way from the outset!*


### As I say, the whole package is also installable from PyPI:

```
python -m pip install whatsappcloud --upgrade
```
____

# More details... if you're still reading!

## Getting Set Up

The WhatsApp Business Platform is intended _"for people developing for themselves or their organization, not on behalf of a client"_ and _"the platform is not open to those developing on behalf of clients."_ ... but don't let that put off!

Compared with getting up to speed with Google APIs and authentication, the Meta/Facebook documentation was generally so clear and easy to follow that I don't think you'll need me to walk you through it. Just follow Steps 1 and 2 of the ['Getting Started'](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started) instructions. You can go further if you want to learn how to receive inbound messages using Webhooks and making things interactive, or upload and download files etc, but this article is all about providing 80% of the good stuff for 20% of the effort, and if you're at all like me, you'll be tremendously excited just at the prospect of being able to send free notifications from your Python code to your phone (and four others).

My only other comments before you go off and start working your way through the docs yourself are:

- You don't actually have to create or verify a Facebook Business Account. At a certain point when you're creating your new App you'll be given the option of creating a Test Business Account. That's all you need.

- You don't _have_ to even enable two factor authentication if you just want to dive in and start playing.

- Once you've created your five free contact phone numbers I don't think there's a way to change or delete them... so choose carefully and triple check they're correct and properly formatted before you commit.

- As well as your **Token**, you'll just need to copy/paste your **Phone number ID** and **App ID** into `config_template.py` then rename it `config.py`. The **Phone number ID** is different from the actual (test) phone number, and you won't need to copy the actual phone number across.

   > **NB** *For Test Business Accounts, the Token expires every 24 hours so you'll either need to update your `config.py` manually or write a bit of code e.g. with `selenium` to log in to your Facebook Developer Dashboard and refresh and copy the Token.  I've included `APP_ID` and `APP_URL` in `config.py` for that purpose, and if you add your scraping code into `config.py` it should run and update automatically whenever your credentials are imported.  If I get to it first I'll include that in the main package, hopefully soon...*

- The official way of initiating messages to contacts who have opted in to receive them is via the Template message type which is why the first test message in the documentation (sent by CURL) uses a predefined template called `hello_world`.  The only trouble with this is that you need to set up new Templates and _have them approved_ via the Cloud API dashboard, every time you want a new form of message.  Presumably if you're reading this you're already thinking excitedly about freely generating messages and content yourself in Python, not necessarily fiddling around setting up server-side templates and passing variables into _them_ every time.  So IMHO a better starting point for understanding the API as a whole, and the basis for my `Whatsapp` class above is the simpler 'Send Messages' API which you can read more about [here](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages).

- As well as verifying each phone number before being able to send a first Template message to it, you'll need to "Allow" the test account on each receiving phone after receiving the first "hello_world" test message.  That should open the gates to initiating more 'conversations' from the Business side by sending further Template messages.

- You'll probably be eager to send regular Messages as soon as possible - especially if you're doing something like sending notifications and updates to yourself and team members programmatically.  In that case you'll need to actually **send a reply** to the Test Business number, or in other words, engage in a 'conversation' from the receiving end. It took me ages to work out why I was getting success (200) messages from my outgoing API calls but not receiving anything on the recipient's phone(s) other than Template messages. This was the reason, but the documentation didn't save me from learning the hard and slow way.  A 'reaction' might do the trick too, but at the time of writing I haven't tested that.  Please let me know?

- It also looks like conversations are reset every 24 hours, so you'll either need to use Templates to get things going each day (initially), or keep the conversation going from the receiver's side.  One approach is to add a nice interactive button to your daily Template message, but that's beyond the scope of this article.  Another perhaps easier option is using the free Business version of Whatsapp on your recipients' phones and have them create an auto-reply.

- If you want to unlock the full power fo the Whatsapp Cloud API and remove all restrictions, you'll need to create or link to a verified Business Account. If you do that you currently get 1,000 'conversations' free per month or in other words roughly 33 messages per day - one an hour plus a few spare. But unless you do something to get kicked off your Test Business Account, _unlimited_ free messages to/from five phone numbers is very generous and seems ideal for developers and micro-businesses.

## The Code

- Unfortunately the [Developer docs](https://developers.facebook.com/docs/whatsapp/cloud-api) aren't Python-friendly (unlike the Google API) and just give you CURL snippets to decode.  But never fear, you can use [tools like this](https://reqbin.com/req/python/c-xgafmluu/convert-curl-to-python-requests) to convert their CURL examples into Python if you want to, or you can just browse the function definitions and tests in my main repository to understand the various options and arguments.

- My `Whatsapp` class at the start of this article was intentionally minimalistic - just enough functionality to get you started and send a basic text message with a url and preview. The whole point of the `kwargs` logic you see in `__init__` however is to make it [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) and easily extensible e.g. if you want to specify more elaborate message types like audio, video, images, buttons, geolocation, stickers, contact cards, and yes, templates if you must. To do so, you would just provide a new keyword arguments. If you're not familiar with function parameters, `*args` and `**kwargs`, have a look at [`test_whatsappcloud.py`](https://github.com/PFython/WhatsappCloud/blob/master/whatsappcloud/test_whatsappcloud.py) which I hope will give you some ideas.

- The `autosend` keyword argument was included mainly to help  with testing and debugging, but also helps if you want to do something else to the message before sending.  That could include translation to another language, saving to file/database/cloud, creating a message 'factory' for multiple recipients, for message approval workflows, or for sending messages according to a schedule or in response to particular inbound messages.

- Not strictly essential, but I've included my go-to helper class [`CleverDict`](https://github.com/PFython/cleverdict) in the code.  If you're curious about it, it basically adds the ability to get and set dictionary values using the oh-so-convenient 'dot' notation e.g. `data.type` rather than `dictionary["key"]` notation, which makes things like tests much more readable and easier to type - one keystroke for `.` rather than `[ + SHIFT + " ... + SHIFT + "+ ]` which kills your little fingers!  You can easily strip out `CleverDict` and swap back to dictionary notation if you prefer to be completely dependency free, but it's a very lightweight package and worth checking out if you haven't used it before.  It's also used extensively in `test_whatsappcloud.py` so if you do strip it out, you may need to refactor those tests too.

## And finally...

I've always been a fan of "simple tools for busy people", so `whatsappcloud.py` and `config.py` are intentionally short and offered "bare-bones" for now. I don't doubt some excellent Python modules will come to the fore which wrap the Whatsapp Cloud API more comprehensively, but in the meantime if you feel the urge to build on this humble repository and want to suggest Pull Requests etc. I'd be happy to collaborate.

If you've benefitted from reading this and want to pay it forward, I'd be thrilled if you'd...

<a href="https://www.buymeacoffee.com/pfython" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="217px" ></a>

... or if you're reading this on **Medium**, please give it a few claps?  Did you know you can press and hold the "clap" icon to give more than one?  Try it now - I double-dare you to find the maximum!

Finally, finally... if you want to contact me the best ways are either through [Github](https://github.com/PFython) or [Twitter](https://twitter.com/AWSOM_solutions). Please note that I do work full time, I have a very needy dog, and also act as a carer, so please be patient if I don't respond quickly. Enjoy.
