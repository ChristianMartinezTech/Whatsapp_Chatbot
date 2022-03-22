# _Aprende con Michi 🐱_ - Capstone proyect
![](https://fv9-3.failiem.lv/thumb_show.php?i=8qfjk78a6&view)

------------

#### “WhatsApp Bot for sharing OER (Open Educational Resources) for Colombia’s Preschool and Primary school education”

------------
## Our challenge:
This portfolio project is intended to solve the current lack of direct access to educational resources by preschool and primary school students in Colombia, due to a poor internet access infrastructure in remote areas and common problems such as low income in most Colombian families or absence of a computer at home.

### Who will help and users:
The users of the WhatsApp bot are the parents of children in Preschool or Primary school. However, their children would be the ones that benefit from it.



#### _Technical Risks what could have:_

- **HTTP Requests overload**: Our server would have to support too many requests, so a solution could be to optimize this by adding another server that supports requests that overload our first server.
- **Flask implementation**: Flask is not intended for deployment, only for testing and development. So we’ll need to use a different technology such as Gunicorn and uWSGI to deploy.

#### _Non-technical Risks what could have:_

**Twilio Membership Expiration**: The platform we will use for our chatbot is a paid platform, at the time we started this project we had a balance of $65 (sixty-five dollars) which was given to us by the GitHub Education resource. The solution is to pay to continue with the project.

## Infrastructure:
- According to documentation, we chose to use Feature Branching. Being BackEnd and DevOps the starting branches and as the portfolio project carries on, additional branches may be created as new features are needed. Also the Merging strategy we chose to use is Manual Code Review and Merge.
- Strategy for deployment: Recreate, it implies downtime of the service depending on both shutdown and boot duration of the application.
- We’ll upload files on SSH by using the *scp* command. Additionally, - We’ll storage the files following the same Chatbot content structure.
- We’ll use Pycodestyle for a consistent styling in Python files, unitests to test the correct functioning of Python scripts, periodical updates (and upgrades) to Linux servers, and lastly, we’ll manually test the Chatbot.


## Technologies:
- Twilio: we use Twilio due to its extensive documentation, online tutorials, and free price tag.
- Python: we use Python because most documentation of WhatsApp Boots use Python, Also, we’re familiar with Python and its libraries.
- Flask: we use Flask for testing the boot during development.
- nGrok: we use this utility to connect the Flask application running on our local systems to a public URL that Twilio can connect to.
- Nginx: for the server. We are familiar with configuring and deploying Nginx servers.

## Existing Solutions to our Challenge:
There are multiple websites and apps with educational resources: Colombia Aprende, Eduki, Aulap, etc.

The difference between Apps and Websites that provide educational resources is the easy entry barrier, ease of use, and more importantly, the low internet consumption in WhatsApp.

Easy entry barrier: WhatsApp is widely used in Latam. Almost everyone with a phone uses WhatsApp. There’s no need to download an App, nor register on a Website.

Ease of use: very clear and simple instructions.

Low Internet consumption: WhatsApp is the main communication channel in Colombia (With Facebook). There’s free internet.


## Team:
- Christian Martinez:  **DevOps Developer**
- Yael Uribe: **Backend Developer**
- Laura Cadavid: **Content Curator and Backend Developer**
- Ibethe Ramada: **Content Curator and DevOps Developer**

_________
###### This portfolio project is not solving issues like providing a mobile phone, improving ISP services or infrastructure. Also, it’s oriented towards specific assignments and grades, it doesn’t cover all Preschool nor Elementary school assignments.
