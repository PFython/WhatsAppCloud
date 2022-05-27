
## Send unlimited WhatsApp messages from Python for free

![](https://cdn-images-1.medium.com/max/5120/1*I08YdcuzGJ5qsjG_Ybs3Kw.jpeg)

It’s true — you really can send free messages to five (verified) phone numbers for free using Meta’s [**WhatsApp Business Cloud API**](https://developers.facebook.com/products/whatsapp/). The only proviso is that you agree to and follow their terms and conditions, especially regarding opting-in and acceptable use…

The good news for Pythonistas is that I’ve waded my way through the API docs and several published “works in progress” on Github, basically going down a few rat-holes so you won’t have to. The result is about 20 lines of Python (excluding comments and docstrings) which you can copy into your own scripts then sit back and enjoy outbound WhatsApp notifications without having to learn the quirks of yet another API from scratch. Or if you *do* want to get a deeper understanding, you can head over to my [**Github repository**](https://github.com/PFython/Whatsapp) where you’ll find a [**full Python package**](https://pypi.org/whatsappcloud) with tests and additional functions.

You can also install the full package using **pip** in the usual way:

    python -m pip install whatsappcloud --upgrade

Hopefully this article will fast-track your learning journey and get you using the WhatsApp Cloud API that much quicker.

### TLDR: Here’s the bare-bones code to get you up and running…

![](Screenshot%201.png)

>  **SOAP BOX ALERT!** A shocking number of API tutorials mix credentials and config data together in the same script. In my opinion and many others’, this is **bad practice** and not to be emulated, so let’s start with a better way right from the outset…

Here’s an example of a standalone config file you can use once you’ve created your first WhatsApp Cloud App on the developers’ portal (details below). You’ll just need to add your own credentials then save as ***config.py***:

![](Screenshot%202.png)

There are still a few steps to take before you can actually send messages, but once you’ve registered and created your Meta/Facebook App (see below), sending WhatApp messages in future will be as easy as this:

    from whatsappcloud import Whatsapp
    # If you've installed the full package e.g. using pip

    >>> Whatsapp()
    # Send a test message with test url (and preview) to your default contact

    >>> Whatsapp.text("Hello Monty", CONTACT[4])
    # Send "Hello Monty" to your fifth contact

    >>> Whatsapp.template("hello_world")
    # Send the pre-approved "hello_world" Template to your default contact

    >>> wa = Whatsapp(autosend=False)
    # Create a WhatsApp message object but don't send. Useful when testing/debugging and also if you intend to do any pre- or post- processing and want to control when a message is actually sent.

    >>> wa.send()
    # Send (or resend) a previously prepared message

## Getting Set Up

The process for registering a new Meta/Facebook app is mercifully easy to follow. Just follow Steps 1 and 2 of their **[‘Getting Started’](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started)** instructions. I don’t propose to walk through those steps in this article but if you do get stuck, there are several other tutorials online already which I’m sure you can find quite easily.

So, with the benefit of hindsight here are my suggestions/comments before you start working your way through the setup process yourself:

* I was surprised to discover you don’t *actually* have to create or verify a Facebook Business Account. At a certain point when you’re creating your new App you’ll be given the option of creating a Test Business Account. That’s all you need.

* If you want to unlock the full power of the WhatsApp Cloud API and run a proper production system, you can create or link to a verified Business Account later on. If you do that you currently get 1,000 ‘conversations’ free per month or in other words roughly 33 messages per day — one an hour plus a few spare. But unless you do something to get kicked off your Test Business Account, *unlimited* free messages to/from five phone numbers is very generous and seems ideal for developers and micro-businesses, so I’d suggest sticking with that for as long as possible.

* You don’t *have* to enable two factor authentication if you just want to dive in and start playing.

* Once you’ve created your five free contact phone numbers I don’t think there’s a way to change or delete them… so choose carefully and triple check they’re correct and properly formatted before you commit.

* As well as your **Token**, you’ll just need to copy/paste your **Phone number ID** and **App ID** into the config template above,*** ***then rename it ***config.py***. NB the **Phone number ID** is different from the actual (test) phone number. You won't need to copy the actual phone number across.

* The WhatsApp Business Platform describes itself as “*intended for people developing for themselves or their organization, not on behalf of a client”* and *“the platform is not open to those developing on behalf of clients.”* … but don’t let that put off. There’s plenty you can legitimately use the API for and the learning curve really isn’t steep considering you’ve already found this article!

* The prescribed way of initiating messages to phone contacts who have opted in to receive them is via a pre-approved “Template”. This is why the first test message in the documentation (sent by CURL) is a Template message rather than any other type (plain text, media etc). The only trouble with this is that you need to set up new Templates and *have them approved* via the Cloud API dashboard, *every* time you want a new form of message. Presumably if you're reading this you're already planning to generate messages and content yourself in Python, not fiddle around setting up server-side templates and passing variables into *them* every time. So IMHO a better starting point for understanding the API as a whole, and the basis for my Whatsapp class above is the simpler 'Send Messages' API which you can read more about [**here](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages)**.

* Before you can send an initial hello_world test message (Template) to a phone number you’ll need to verify it with a one-time-pass code. After receiving the first message, you’ll also need to “Allow” the Test Business number on each receiving phone to continue.

* You’ll probably be eager to send regular (non-template) messages as soon as possible, especially if you’re hoping to do something like sending notifications to yourself and team members directly from Python. In that case you’ll need to actually ***send a reply ***to the first message you receive on each phone, or in other words, engage in a ‘conversation’ from the receiving end. It took me ages to work out why I was getting success (200) messages from my outgoing API calls for non-template messages, but not seeing anything on the recipient’s phone(s). This was the reason! A ‘reaction’ to the initial message might do the trick too, but at the time of writing I haven’t tested that. Please let me know in the comments if you do?

* It also looks like conversations are reset after 24 hours, so you’ll either need to use Templates to get things going each day (initially), or keep the conversation going from the receiver’s side. I haven’t fully tested the restrictions in this regard, but one approach once a conversation is reset might be to add a nice interactive button to your Template message, but that’s beyond the scope of this article. Another perhaps easier option is using the free Business version of WhatsApp on your recipients’ phones and have them create an auto-reply or quick-reply.
>  By all means carry on to Steps 3 and 4 of the Getting Started instructions If you want to learn how to receive inbound messages using Webhooks and making things interactive, or upload and download files etc, but this article is all about providing 80% of the good stuff for 20% of the effort, and if you’re at all like me, you’ll be excited enough just at the prospect of sending free notifications from Python!

## The Code

* Unfortunately the [**API Documentation](https://developers.facebook.com/docs/whatsapp/cloud-api)** isn’t Python-friendly and just gives you CURL snippets to decipher. You can do what I did and use [**tools like this](https://reqbin.com/req/python/c-xgafmluu/convert-curl-to-python-requests)** to convert CURL into Python if you want to, or perhaps a smarter idea since I’ve done that step already would be to browse the function definitions and tests in my [**main repository](https://github.com/PFython/WhatsAppCloud)** and explore the various options and arguments there.

* My Whatsapp class at the start of this article was intentionally lightweight - just enough functionality to get you started and send a basic text message with a url and preview. The point of the additionalkwargs logic you see in __init__ however is to make things [**DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)** and easily extensible e.g. if you want to extend the class (as I’ve started to do) to handle more elaborate message types like audio, video, images, buttons, geolocation, stickers, contact cards, and yes, templates if you must. To do so, you just need to provide keyword arguments. If you're not familiar with things like function parameters, *args and **kwargs, have a look at [***test_whatsappcloud.py](https://github.com/PFython/WhatsAppCloud/blob/master/whatsappcloud/test_whatsappcloud.py)*** which I hope will give you some ideas about the available options and usage.

* The autosend keyword argument was included mainly to help with testing and debugging, but also helps if you want to do something else to the message before sending. That could include translation to another language, saving to file/database/cloud, creating a message 'factory' for multiple recipients, message approval workflows, sending messages according to a schedule, or responding to inbound messages types.

* Not strictly essential, but I’ve included my go-to helper class [**CleverDict](https://github.com/PFython/cleverdict)** in this code. If you're curious about it, it basically adds the ability to get and set dictionary values using the oh-so-convenient 'dot' notation e.g. data.type rather than dictionary["key"] notation, which makes things like tests much more readable and easier to type - one keystroke for . rather than [ + SHIFT + " ... + SHIFT + "+ ] which kills your little finger on a US/UK keyboard! You can easily strip out CleverDict and swap back to dictionary notation if you prefer to be completely dependency free, but it's a very lightweight package and worth checking out if you haven't used it before. It's also used extensively in ***test_whatsappcloud.py*** so if you do strip it out, you may need to refactor those tests too.

* For Test Business Accounts, the Token expires every 24 hours which is a bit of a pain, so you’ll either need to update your ***config.py*** manually or write a bit of code e.g. with **selenium** to log in to your Facebook Developer Dashboard and refresh and copy the Token. I’ve included **APP_ID** and **APP_URL** in ***config.py*** for that purpose, and if you add your scraping code into ***config.py*** it should run and update automatically whenever you import from it. If I get round to it first I’ll include something in the main package to help with that, hopefully soon…

## And finally…

If you’ve benefitted from reading this article and want to pay it forward, I’d be delighted if you’d STAR my [**Github](https://github.com/PFython/WhatsAppCloud)** page or…

![](https://cdn-images-1.medium.com/max/2000/0*UFfv__Fq-88tK4FE)

… or if you’re reading this on **Medium**, please give it a few claps?
>  Did you know you can press and hold the “clap” icon to give more than one clap? I double-dare you to find the maximum — try it now!

Finally, finally… if you want to contact me the best way is through [**Twitter](https://twitter.com/AWSOM_solutions)**, or feel free to raise an Issue or Pull Request on Github directly. Please note that I do work full time, I have a very needy dog, and also act as a carer, so please be patient if I don’t respond quickly. Enjoy.

*Originally published at [https://github.com](https://github.com/PFython/WhatsappCloud/blob/master/README.md).*
