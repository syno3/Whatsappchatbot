### whatsapp chatbot

### Requirements

Python 3.6 or newer. If your operating system does not provide a Python interpreter, you can go to python.org to download an installer.

Flask. We will create a web application that responds to incoming WhatsApp messages with it.

ngrok. We will use this handy utility to connect the Flask application running on your system to a public URL that Twilio can connect to. This is necessary for the development version of the chatbot because your computer is likely behind a router or firewall, so it isn’t directly reachable on the Internet. If you don’t have ngrok it installed, you can download a copy for Windows, MacOS or Linux.

A smartphone with an active phone number and WhatsApp installed.

A Twilio account. If you are new to Twilio create a free account now. You can review the features and limitations of a free Twilio account.