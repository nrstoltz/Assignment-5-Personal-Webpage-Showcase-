#!/usr/bin/env python3
"""
Test file for FlaskConversion Flask application
Tests basic functionality of the web application
"""

import unittest
import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app
from DAL import getAllProjects, saveProjectDB

class TestFlaskApp(unittest.TestCase):
    """Test cases for the Flask application"""
    
    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_home_page(self):
        """Test that the home page loads successfully"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>', response.data)
    
    def test_projects_page(self):
        """Test that the projects page loads successfully"""
        response = self.app.get('/projects')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Projects', response.data)
    
    def test_contact_page(self):
        """Test that the contact page loads successfully"""
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contact', response.data)
    
    def test_about_page(self):
        """Test that the about page loads successfully"""
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About', response.data)
    
    def test_resume_page(self):
        """Test that the resume page loads successfully"""
        response = self.app.get('/resume')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Resume', response.data)

class TestDatabase(unittest.TestCase):
    """Test cases for database functionality"""
    
    def test_get_all_projects(self):
        """Test that we can retrieve projects from the database"""
        projects = getAllProjects()
        self.assertIsInstance(projects, list)
        self.assertGreater(len(projects), 0)
        
        # Check that each project has required fields
        for project in projects:
            self.assertIn('Title', project)
            self.assertIn('Description', project)
            self.assertIn('Image', project)
    
    def test_save_project(self):
        """Test that we can save a project to the database"""
        # Test data
        test_title = "Test Project for Unit Testing"
        test_description = "This is a test project created during unit testing"
        test_image = "nigel.jpg"
        
        # Save the project
        saveProjectDB(test_title, test_description, test_image)
        
        # Verify it was saved by getting all projects
        projects = getAllProjects()
        project_titles = [p['Title'] for p in projects]
        self.assertIn(test_title, project_titles)

if __name__ == '__main__':
    unittest.main()
