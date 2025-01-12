# Password Manager GUI App

## Overview
The **Password Manager GUI App** is a Python-based application designed to simplify and secure the process of managing your passwords. With an intuitive interface built using **Tkinter**, this app allows users to generate strong passwords, store them securely, and associate them with relevant websites and email accounts.

---

## Features
- **Password Generator**: Create strong, random passwords containing letters, numbers, and symbols.
- **Clipboard Copy**: Automatically copy generated passwords to the clipboard for easy use.
- **Password Storage**: Save passwords along with the associated website and email/username information in a text file (`data.txt`).
- **User-Friendly Interface**: Built with Tkinter for a clean and intuitive experience.
- **Pre-Filled Email**: Default email/username field populated for convenience.

---

## Requirements
To run the app, ensure you have the following installed:
- Python 3.x
- Tkinter (included in the standard Python library)
- [pyperclip](https://pypi.org/project/pyperclip/) (for clipboard functionality)

Install pyperclip using pip if not already installed:
```bash
pip install pyperclip
```

---

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/password-manager-gui.git
   ```
2. Navigate to the project directory:
   ```bash
   cd password-manager-gui
   ```
3. Run the Python script:
   ```bash
   python password_manager.py
   ```

---

## Usage
1. Launch the application.
2. Enter the website, email/username, and click **Generate Password** to create a strong password.
3. The generated password is copied to the clipboard and can be pasted as needed.
4. Click **Add** to save the website, email, and password to `data.txt`.

---

## Project Structure
```
password-manager-gui/
├── password_manager.py  # Main Python script
├── README.md            # Project documentation
├── data.txt             # Saved password data
├── logo.png             # Lock image used in the GUI
└── requirements.txt     # Dependencies file
```

---

## Contribution
Contributions are welcome! If you have ideas for enhancements or new features, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request on GitHub.

---

## Acknowledgements
- Developed using **Python** for its versatility and simplicity.
- GUI built with **Tkinter**, a reliable and straightforward library for Python GUI development.
- Clipboard functionality powered by **pyperclip**.

---

## Contact
For any questions or feedback, feel free to contact me at [your-email@example.com].

