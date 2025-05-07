# Library Management System

A comprehensive library management system built with Python and PyQt5 that helps manage students, books, and book loans in an educational institution.

## Features

### Student Management
- Add new students with detailed information
- Modify student details
- Delete student records
- Search and display student information
- Track student book loans

### Book Management
- Add new books to the library
- Modify book information
- Delete book records
- Search and display book information
- Track book availability

### Loan Management
- Create new book loans
- Return books
- Modify loan information
- Delete loan records
- Track active and completed loans

## Project Structure

```
├── UI/                    # User interface components
├── Save/                  # Data storage directory
├── fct/                   # Function modules
├── class_bibliotheque.py  # Main library class
├── class_etudiant.py      # Student class
├── class_livre.py         # Book class
├── class_emprunt.py       # Loan class
├── Menu_principale.py     # Main menu interface
└── Various function files for CRUD operations
```

## Technical Details

### Dependencies
- Python 3.x
- PyQt5
- SQLite (for data storage)

### Main Components

1. **Library Class (`class_bibliotheque.py`)**
   - Core functionality for managing the library
   - Handles all CRUD operations for students, books, and loans

2. **Student Management**
   - `ajouter_etudiant.py` - Add new students
   - `modifier_etudiant.py` - Modify student information
   - `supprimer_etudiant.py` - Delete student records
   - `afficher_etudiant.py` - Display student information

3. **Book Management**
   - `ajouter_livre.py` - Add new books
   - `modifier_livre.py` - Modify book information
   - `supprimer_livre.py` - Delete book records
   - `afficher_livre.py` - Display book information

4. **Loan Management**
   - `ajouter_emprunt.py` - Create new loans
   - `retour_emprunt.py` - Return books
   - `modifier_emprunt.py` - Modify loan information
   - `supprimer_emprunt.py` - Delete loan records
   - `afficher_emprunt.py` - Display loan information

## Getting Started

1. Clone the repository
2. Install the required dependencies:
   ```bash
   pip install PyQt5
   ```
3. Run the main application:
   ```bash
   python main.py
   ```

## Usage

1. Launch the application using the main menu
2. Navigate through the different sections using the menu interface
3. Perform operations on students, books, and loans as needed
4. All changes are automatically saved to the database

## Features in Detail

### Student Management
- Add students with: ID, name, surname, address, email, phone, section, and study level
- Search students by various criteria
- Modify student contact information
- Delete student records

### Book Management
- Add books with: reference, title, author, publication date, and quantity
- Search books by various criteria
- Modify book information
- Delete book records
- Track book availability

### Loan Management
- Create loans with student ID and book reference
- Track loan dates and return dates
- Modify loan information
- Delete loan records
- Automatic book quantity management

## Contributing

Feel free to submit issues and enhancement requests.
