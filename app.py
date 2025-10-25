from flask import Flask, render_template, request, redirect, url_for

# Import the DAL functions
from DAL import getAllProjects, saveProjectDB

# Serve static files (css/ and images/) from project root so existing folders work as-is.
app = Flask(__name__, static_folder='.', static_url_path='')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    # Get all projects from the database
    projectList = getAllProjects()
    return render_template('projects.html', projects=projectList)


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Check if this is a project addition form or contact form
        if 'project-title' in request.form:
            # This is a project addition form
            title = request.form.get('project-title')
            description = request.form.get('project-description')
            image_filename = request.form.get('image-filename')
            
            # Basic validation
            if not title or not description:
                return render_template('contact.html', error='Please complete required project fields.')
            
            # Save the project to database
            saveProjectDB(title, description, image_filename)
            
            # Redirect to projects page to show the new project
            return redirect(url_for('projects'))
        else:
            # This is the original contact form
            first = request.form.get('first-name')
            last = request.form.get('last-name')
            email = request.form.get('email')
            # Basic required-field check
            if not first or not last or not email:
                # Re-render the form for simplicity; client-side JS will usually prevent this.
                return render_template('contact.html', error='Please complete required fields.')
            return redirect(url_for('thankyou'))
    return render_template('contact.html')


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
