# A. Import the sqlite library
import sqlite3

#######################################################
# 1. ADD PROJECT TO DB
#######################################################
def saveProjectDB(Title, Description, ImageFileName):
    #A. Make a connection to the database
    conn = None
    conn = sqlite3.connect("projects.db")

    #B. Write a SQL statement to insert a specific row (based on Title name)
    sql = 'INSERT INTO projects (Title, Description, ImageFileName) values (?,?,?)'

    # B. Create a workspace (aka Cursor)
    cur = conn.cursor()

    # C. Run the SQL statement from above and pass it 1 parameter for each ?
    cur.execute(sql, (Title, Description, ImageFileName, ))

    # D. Save the changes
    conn.commit()
    if conn:
        conn.close()

#######################################################
# 2. SHOW PROJECTS IN A TABLE
#######################################################
#   THIS RETURNS AS LIST OF DICTIONARIES
def getAllProjects():
    try:
        # A. Connection to the database
        conn = sqlite3.connect('projects.db')

        # B. Create a workspace (aka Cursor)
        cursorObj = conn.cursor()

        # D. Run the SQL Select statement to retrieve the data
        cursorObj.execute('SELECT Title, Description, ImageFileName, AdditionalImages, LiveDemo FROM projects;')

        # E. Tell Python to 'fetch' all of the records and put them in
        #     a list called allRows
        allRows = cursorObj.fetchall()

        projectListOfDictionaries = []

        for individualRow in allRows:
            # Make sure we have an image name
            if individualRow[2] is not None and individualRow[2] != "":
                Image = individualRow[2]
            else:
                Image = "placeholder.png"
            
            # Handle additional images
            AdditionalImages = individualRow[3] if individualRow[3] else ""
            LiveDemo = individualRow[4] if individualRow[4] else ""
            
            # Create a dictionary for each row
            p = {
                "Title": individualRow[0], 
                "Description": individualRow[1], 
                "Image": Image,
                "AdditionalImages": AdditionalImages,
                "LiveDemo": LiveDemo
            }
            projectListOfDictionaries.append(p)

        if conn:
            conn.close()

        return projectListOfDictionaries
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
        return [{"Title": "Error", "Description": "Database connection failed", "Image": "error.png"}]

#######################################################
# 3. CREATE DATABASE AND TABLE
#######################################################
def createDatabase():
    try:
        # A. Connection to the database
        conn = sqlite3.connect('projects.db')

        # B. Create a workspace (aka Cursor)
        cursorObj = conn.cursor()

        # C. Create the projects table
        cursorObj.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Title TEXT NOT NULL,
                Description TEXT NOT NULL,
                ImageFileName TEXT,
                AdditionalImages TEXT,
                LiveDemo TEXT
            )
        ''')

        # D. Save the changes
        conn.commit()
        
        if conn:
            conn.close()
            
        print("Database and table created successfully!")
        return True
    except Exception as e:
        print(f"An error occurred while creating the database: {e}")
        return False

def initializeSampleData():
    """Initialize the database with the original project data"""
    try:
        # Clear existing data first
        conn = sqlite3.connect('projects.db')
        cursorObj = conn.cursor()
        cursorObj.execute('DELETE FROM projects')
        
        # Add the original projects with full descriptions
        projects_data = [
            (
                "'Bloomington Parking Wizard' — Informatics Capstone Project",
                "The Bloomington Parking Wizard is the Capstone project my team and I worked on for seven months during our senior year to fulfill the final requirement for our Informatics degree at Indiana University. The goal was to tackle one of Bloomington's biggest everyday challenges: finding reliable parking. With thousands of students, faculty, and visitors commuting for classes, events, and activities, parking often becomes stressful and time-consuming.\n\nWe designed and developed a parking assistance website that helps users locate parking spots around the IU campus and downtown area. The site provides an interactive map that displays parking locations, real-time availability, hourly pricing, and operational hours. It also offers recommendations tailored to a user's needs (proximity to destination, preferred lot type, etc.).\n\nThis project combines user-centered design with live data integration to make the parking experience more efficient and less frustrating — helping reduce citations and improving how drivers navigate Bloomington's busy streets. The capstone was a full lifecycle team project: problem discovery, UX research, wireframing, implementation, testing, and deployment.",
                "parking-wizard-1.png",
                "parking-wizard-2.png",
                "https://zion.luddy.indiana.edu/info-capstone-2025/bloomington-parking-wizard"
            ),
            (
                "'The Bathroom Problem' — Informatics HCI Group Project",
                "This project was part of a Human-Computer Interaction (HCI) class focused on UX research, UI principles, wireframing, and prototyping. Over the semester our team designed a working prototype in Figma that addressed a common urban problem: finding a clean, accessible restroom nearby.\n\nWe called our app \"The Bathroom Problem\", and it's meant for people in Chicago who are younger and already somewhat familiar with apps that help them search and rate everyday places. Team members from Chicago informed the problem selection based on lived experience. Our goal was to help users quickly locate restrooms and trust recommendations via a rating system, improving convenience and confidence for users in public spaces.\n\nWe followed the full HCI design process: user research, wireframes, low-fidelity prototypes, iterative testing, and a high-fidelity prototype built in Figma. The project emphasized research-driven design and showed how iteration and testing refine solutions before development begins.",
                "bathroom-problem-1.png",
                "bathroom-problem-2.png",
                "https://zion.luddy.indiana.edu/i300-fa22/falak-bathroom-problem"
            )
        ]
        
        cursorObj.executemany('''
            INSERT INTO projects (Title, Description, ImageFileName, AdditionalImages, LiveDemo) 
            VALUES (?, ?, ?, ?, ?)
        ''', projects_data)
        
        conn.commit()
        conn.close()
        
        print("Sample data initialized successfully!")
        return True
    except Exception as e:
        print(f"An error occurred while initializing sample data: {e}")
        return False
