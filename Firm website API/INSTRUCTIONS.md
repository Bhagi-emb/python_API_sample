#   Python website sample - flask

## Purpose
An accounting firm website offering a wide range of services — we can create a clean and professional layout using Flask + HTML in VS Code.

## Instructions
**1. STEP one : Installation** 
    - Install Python
        Go to python.org and download the latest version.
        During installation, check the box that says: “Add Python to PATH”.
    (or)    
    -Install VS Code
        Download it from code.visualstudio.com
        - Install the Python extension for VS Code
            Open VS Code and go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by pressing `Ctrl+Shift+X`.
            Search for "Python" and install the extension provided by Microsoft.
        - Install Flask
            Open a terminal in VS Code (`` Ctrl+` ``) and run:
            ```bash
            pip install Flask
            ```

**2. STEP two : Creating project ** : 
    Create a new folder for your project
    - Open VS Code and create a new folder for your project.
    - Open the terminal in VS Code (`` Ctrl+` ``) and navigate to your project folder.
    (or)
    - Naviagate/open project folder
    - open terminal by right clicking on explorer
    - Now enter the command code .

**3. STEP three : Creating a Flask app** 
    - Create a new file named `app.py` in your project folder.
    - Open `app.py` and add the code 

**4. STEP four : Creating HTML templates** 
    - Create a new folder named `templates` in your project folder.
    - Inside the `templates` folder, create a new file named `base.html`, `contact.html`, `home.html` and `services.html`.
    - Open `base.html` and add the HTML code.  
    - Open `contact.html` and add the HTML code.
    - Open `home.html` and add the HTML code.
    - Open `services.html` and add the HTML code.
    - Open `app.py` and add the code to render the templates.

    **purpose of each file**
    - `app.py`: This is the main Flask application file that handles routing and rendering templates.
    - `base.html`: This is the base template that contains the common layout for all pages.
    - `contact.html`: This template displays the contact form and handles form submission(Form with name, email, phone, and message).
                    - Optional: Office address, phone number, and Google Map
    - `home.html`: This template displays the home page with a welcome message,Brief intro about the firm,Highlight key services,Contact button.
    - `services.html`: This template displays the services offered by the accounting firm.


**4. STEP  : RUNNING THE CODE**
    - run this command on command terminal ``python3 app.py`` 



## Notes
- Tip 1
- Tip 2




