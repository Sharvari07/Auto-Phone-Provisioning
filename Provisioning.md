# Auto Phone Provisioning
 An application that monitors and stores the live state of provisioned phones in Metroleads using the inbuilt phone application created using Python(Django).
 
 ## Table of Content
 * [Motivation](#motivation)
* [General info](#general-info)
* [Technologies](#technologies)
* [Reasons to choose the technology](#reason-to-choose-the-technology)
*  [Getting Started](#getting-started)
* [Launch](#launch)
* [Scope of functionalities](#scope-of-functionalities)
* [References](#References)

## Motivation
There are a lot of telephony lines used in the telephonic services of any industry. These phones help the company for better client interactions, service management etc. Since, there are a number of customers/consumers of the company's services, there's also a huge amount of data collected daily. In such conditions, there is a need of an application which can store all this huge data and then separate it on the basis of it's Mac/Registered line name. After, all the storage procedurea are done, there still exist a problem of looking up to the data for a specific phone and it's logs. So, this project tries to retrieve that data from the database and show it on a page with each of the phones different space and recent logs, hence reducing the company's constant need of looking up to the log details in the database. Now, it can view all of it's telephonic data at once with the required number of logs for each.



## General Info
The application creates a server on the localhost which receives data pushed by the client in the XML format. This data is then parsed using the *XML.etree.ElementTree* module in the python libraries and hence stored in the Database created in the django framework. The data here, is received from a number of provisioned phones and conatins information like the Phone's IP, MAC address, called party name, calling party name, call duration etc. There is a large amount of data that is recieved, processed and stored, which inturn is segregated over the calling party name attribute and all the recent five logs of that person including the rest, are displayed over the web page. 

## Technologies
Project is created with the help of:
* Visual Studio Code version: 1.36.1
* Python version: 3.7.1
* Django version: 2.2
* SQL lite version: 3
* Boot Strap version: 3.4
* Html version: 5

## Reasons to choose the Technology
The reasons for choosing the following technologies are:
### **Visual Studio Code**
* **Edit, build and Debug**: When it comes to programming, Visual Studio Code features a lightning fast source code editor. With support for hundreds of languages, VS Code helps you be instantly productive with syntax highlighting, bracket-matching, auto-indentation, box-selection, snippets, and more.
* **Extensible**: VS Code is very extensible and you can install Extensions for almost all the popular programming languages. You do not have to download these “convoluted” **IDEs** for each programming language you are working with
* **Faster**: Unlike IDEs and other editors that become slow the more you install addons, VS Code still runs faster, even with twenty or more plugins.

### **Django**
* **Build**: One of the main reasons to choose Django, is because it is built with python which means that it inherits some of the key benefits of the programming language and hence it is dynamic.
* **All you need**: It has got “batteries included”, which means that it comes with most of the libraries and tools required for common use cases (such as Django ORM, Authentication, HTTP libraries, Multi-site support, Django Admin, template engine, and many more).
* **Secure**: It is one of the best out-of-the-box security systems out there, and it helps developers avoid common security issues (such as clickjacking, cross-site scripting, and SQL injection).
* **DRY Principal**(Don’t Repeat Yourself): This makes it possible to reuse existing code and focus on the unique one. As a matter of fact, Django enables fast development.
* **Scalable and Reliable**: Since it’s a popular and well-maintained framework, which is now widely used across the industries, cloud providers are striving to provide support to run Django applications easily and quickly on cloud platforms.

### **Boot Strap**
* **Ease of Use**: It is extremely an easy and speedy procedure to begin with Bootstrap. You can utilize Bootstrap along with CSS, or LESS, or also with Sass.
* **Speed of Development**: Bootstrap lets you to use ready-made coding blocks in order to assist you in setting up. You can blend that along with CSS-Less functionality and cross-browser compatibility that can give way to saving of ample hours of coding 
* **Simple Integration**:Bootstrap can be simply integrated along with distinct other platforms and frameworks, on existing sites and new ones too. You can also utilize particular elements of Bootstrap along with your current CSS. 

## Getting Started
#### Creating the project
First, change to the specified folder you want to create your projrct in and to start the project type in 
```
$ cd ../
$ django-admin startproject provisioning
``` 
#### Writing the functionalities
Second, we need to create an app for creating a server, recieve and store the data.
```
$ python manage.py startapp pull
```
Now, all the functions are wriiten in *views.py* and the database is created in the *models.py* subsections of the app.

## Launch
Inorder to run this project we need to setup a local environment and enter our IP address in the VVX (XXX) telephony event notification setting, inorder to recieve the push notifications sent by the phone to the specified server. We can run this project by:
```
$ cd ../provisioning
$ python manage.py runserver
```
## Scope of Functionalities

* Acts as a server
* Parses an XML file and stores the data into a database
* Displays the provisioned data in an overview fashion.

## References
1. Phone guide: https://www.gamma.co.uk/wp-content/uploads/2016/12/polycom-vvx201-full-user-guide-v10.pdf
2. Http server: https://www.afternerd.com/blog/python-http-server/
3. Web scrapping: https://www.edureka.co/blog/web-scraping-with-python/
4. Beautifulsoup error: https://stackoverflow.com/questions/5663980/importerror-no-module-named-beautifulsoup
5. Requests: https://www.edureka.co/blog/python-requests-tutorial/
6. Simple http server: https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7
7. POst requests: https://instructobit.com/tutorial/110/Python-3-urllib:-making-requests-with-GET-or-POST-parameters
8. Creating Models and inheriting: https://docs.djangoproject.com/en/2.2/topics/db/models/
9. Parsing through XML documents: https://www.geeksforgeeks.org/xml-parsing-python/
10. Etree: https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.append
11. Parsing from url in etree: https://stackoverflow.com/questions/21713527/xml-parsing-from-web-response
12. dictionary reference: https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/
13. Reseting migrations: https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html
14. Deleting a record from django models :https://stackoverflow.com/questions/3805958/how-to-delete-a-record-in-django-models
15. Slicing through the data: https://stackoverflow.com/questions/47428403/how-to-get-the-last-10-item-data-in-django
16. Styling the table: https://www.w3schools.com/howto/howto_css_table_responsive.asp
17. date time: https://stackoverflow.com/questions/127803/how-do-i-parse-an-iso-8601-formatted-date



