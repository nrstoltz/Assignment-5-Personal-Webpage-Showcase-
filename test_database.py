#!/usr/bin/env python3
"""
Test file for database operations in FlaskConversion
Tests the Data Access Layer (DAL) functionality
"""

import unittest
import os
import sqlite3
import sys

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from DAL import getAllProjects, saveProjectDB, createDatabase

class TestDatabaseOperations(unittest.TestCase):
    """Test cases for database operations"""
    
    def setUp(self):
        """Set up test environment"""
        # Ensure we have a clean database for testing
        if os.path.exists('test_projects.db'):
            os.remove('test_projects.db')
    
    def test_database_connection(self):
        """Test that we can connect to the database"""
        conn = sqlite3.connect('projects.db')
        cursor = conn.cursor()
        cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')
        tables = cursor.fetchall()
        conn.close()
        
        # Should have at least the projects table
        table_names = [table[0] for table in tables]
        self.assertIn('projects', table_names)
    
    def test_projects_table_structure(self):
        """Test that the projects table has the correct structure"""
        conn = sqlite3.connect('projects.db')
        cursor = conn.cursor()
        cursor.execute('PRAGMA table_info(projects)')
        columns = cursor.fetchall()
        conn.close()
        
        # Check that we have the required columns
        column_names = [col[1] for col in columns]
        required_columns = ['id', 'Title', 'Description', 'ImageFileName']
        
        for col in required_columns:
            self.assertIn(col, column_names)
    
    def test_get_all_projects_returns_list(self):
        """Test that getAllProjects returns a list"""
        projects = getAllProjects()
        self.assertIsInstance(projects, list)
    
    def test_get_all_projects_has_data(self):
        """Test that getAllProjects returns projects with data"""
        projects = getAllProjects()
        self.assertGreater(len(projects), 0)
        
        # Check first project structure
        if projects:
            first_project = projects[0]
            required_keys = ['Title', 'Description', 'Image']
            for key in required_keys:
                self.assertIn(key, first_project)
    
    def test_save_project_functionality(self):
        """Test that saveProjectDB works without errors"""
        test_title = "Database Test Project"
        test_description = "This project tests database save functionality"
        test_image = "test-image.png"
        
        # This should not raise an exception
        try:
            saveProjectDB(test_title, test_description, test_image)
            success = True
        except Exception as e:
            success = False
            print(f"Error saving project: {e}")
        
        self.assertTrue(success)
    
    def test_project_data_integrity(self):
        """Test that project data is stored and retrieved correctly"""
        # Get initial project count
        initial_projects = getAllProjects()
        initial_count = len(initial_projects)
        
        # Add a test project
        test_title = "Data Integrity Test"
        test_description = "Testing data integrity in database operations"
        test_image = "integrity-test.jpg"
        
        saveProjectDB(test_title, test_description, test_image)
        
        # Get projects after adding
        updated_projects = getAllProjects()
        updated_count = len(updated_projects)
        
        # Should have one more project
        self.assertEqual(updated_count, initial_count + 1)
        
        # Check that our test project is in the list
        project_titles = [p['Title'] for p in updated_projects]
        self.assertIn(test_title, project_titles)

class TestFlaskIntegration(unittest.TestCase):
    """Test cases for Flask integration with database"""
    
    def setUp(self):
        """Set up test client"""
        from app import app
        self.app = app.test_client()
        self.app.testing = True
    
    def test_projects_page_uses_database(self):
        """Test that the projects page uses database data"""
        response = self.app.get('/projects')
        self.assertEqual(response.status_code, 200)
        
        # Should contain project data from database
        response_text = response.data.decode('utf-8')
        self.assertIn('Projects', response_text)
    
    def test_contact_page_has_project_form(self):
        """Test that the contact page has the project addition form"""
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)
        
        response_text = response.data.decode('utf-8')
        self.assertIn('Add New Project', response_text)
        self.assertIn('project-title', response_text)

if __name__ == '__main__':
    unittest.main()
