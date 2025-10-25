# FlaskConversion - Personal Website

A Flask-based personal website with database integration, Docker containerization, and automated testing.

## Features

- **Dynamic Projects Page**: Displays projects from SQLite database
- **Project Management**: Add new projects through web form
- **Responsive Design**: Modern, professional styling
- **Database Integration**: SQLite with Data Access Layer (DAL)
- **Docker Support**: Containerized application
- **Automated Testing**: CI/CD with GitHub Actions

## Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Containerization**: Docker
- **Testing**: Python unittest
- **CI/CD**: GitHub Actions

## Project Structure

```
FlaskConversion/
├── app.py                 # Flask application
├── DAL.py                # Data Access Layer
├── projects.db           # SQLite database
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
├── .dockerignore        # Docker ignore file
├── .gitignore          # Git ignore file
├── test_app.py         # Application tests
├── test_database.py    # Database tests
├── templates/          # HTML templates
├── css/               # Stylesheets
└── images/            # Static images
```

## Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd FlaskConversion
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open in browser**
   ```
   http://localhost:5000
   ```

### Docker

1. **Build the image**
   ```bash
   docker build -t flask-conversion-app .
   ```

2. **Run the container**
   ```bash
   docker run -p 5000:5000 flask-conversion-app
   ```

3. **Access the application**
   ```
   http://localhost:5000
   ```

### GitHub Codespaces

1. **Open in Codespaces**
   - Click the green "Code" button
   - Select "Create codespace on main"

2. **Run the application**
   ```bash
   python app.py
   ```

3. **Open in browser**
   - Click "Open in Browser" when prompted

## Testing

Run the test suite:

```bash
# Run all tests
python test_app.py
python test_database.py

# Run with verbose output
python -m unittest test_app.py -v
python -m unittest test_database.py -v
```

## Database Schema

The `projects` table includes:
- `id` (Primary Key)
- `Title` (Project title)
- `Description` (Project description)
- `ImageFileName` (Image filename)
- `AdditionalImages` (Additional image filenames)
- `LiveDemo` (Live demo URL)

## API Endpoints

- `GET /` - Home page
- `GET /projects` - Projects page (database-driven)
- `GET /contact` - Contact page
- `POST /contact` - Add new project or contact form
- `GET /about` - About page
- `GET /resume` - Resume page

## CI/CD

This project includes automated testing with GitHub Actions:
- Runs on every push to main branch
- Tests database functionality
- Tests Flask application
- Validates application startup

## Screenshots Required

For assignment submission:
1. Docker Desktop Images tab
2. Docker Desktop Containers tab  
3. Website running locally from container
4. GitHub repository main page
5. Website running in Codespaces
6. GitHub Actions screen

## Author

Nigel Stoltz - Personal Portfolio Website

## License

This project is for educational purposes.