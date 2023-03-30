# ChronoTrain

## Description

### Project Task Overview
[Task](task.md) (German)

---
This project was developed in [**Pycharm**](https://www.jetbrains.com/pycharm), which is inspired by Bootstrap, 
with the libraries:
- [**ttkbootstrap**](https://ttkbootstrap.readthedocs.io/en/latest)
- [**tkinter**](https://docs.python.org/3/library/tkinter.html)
- [**fpdf**](https://pyfpdf.github.io/fpdf2)

***ChronoTrain*** runs locally on the student's computers and uses a centralized SQLite3 database named `training.db`,
which shall be provided on a network drive within the house of the customer *PKN*.
The project was created in a `poetry` environment, and the
linter I used is called [**Ruff**](https://beta.ruff.rs/docs).

### Learnings
The project provided a great opportunity to learn about Graphical User Interfaces, PDF generation, and SQLite.
The user interface is intuitive and restrictive, preventing users from making incorrect inputs.

### Structure
**Login & Add Users**<br>
The program generates a login screen that allows trainees to log in, provided they have an account.
An account can only be created using an identification number (ID) provided by the training company.

**Daily Reports & time recording**<br>
Once logged in, the trainee can submit daily reports, but only after a minimum of 50 characters have been entered.
However, the report submission window is only unlocked after the trainee has started the daily time recording using a
button. Time recording can be stopped by clicking another button, which only becomes clickable after a minimum of
50 characters have been entered into the report submission window.

**Outputs of reports via PDF**<br>
In another tab, the user can select a period, after which a PDF is generated containing several data points,
including the daily report, the date the report was saved, the trainee's ID, and the start and end times of the
corresponding day. Now, the PDF is saved in the project's root folder, but a prompt for a save location
will be added.

## Way of realization
The project was developed iteratively, beginning with the GUI design of the login screen, followed by the creation of the SQLite database, and concluding with the development of the report storage feature. Finally, fpdf was used to create a clear and concise output that presents the reports in a tabular format, with information about the trainee and the associated times.

## Technologies Used
- Pycharm
- ttkbootstrap
- tkinter
- fpdf
- SQLite

## Installation

    - Clone the repository
    - Set up a virtual environment using poetry or any other package manager
    - Install the required packages using the package manager
    - Run the program using the following command: python main.py

## Usage

- Enter the identification number (ID) provided by the training company to create an account.
- Once logged in, start the daily time recording using the appropriate button.
- Enter a report of at least 50 characters.
- Stop the daily time recording using the appropriate button.
- Select a period to generate a PDF containing the daily report, the date the report was saved, the trainee's ID, 
and the start and end times of the corresponding day.

## Known Bugs
- There is no time calculation implemented yet. The butttons check the beginning and end of users time,
but do not calculate the difference.
- No date frame implemented by now. Therefore, you cannot choose a specific time frame for the PDF output.
Users get always all their corresponding reports.
- Password saved in clear text, as the software is not ready for shipment yet, no need for any security right now.
Planned for the next development iteration .

## Background
### Customer:
PKN company trains employees frequently, so there is a need for a time tracking tool that allows users to create training certificates based on their already recorded times.

### Contractor:
JIKU IT-Solutions GmbH in Stuttgart is an IT systems house

### Author
**HUDDEIJ Softworks** 

### Contact
[**chronotrain@huddeij.de**](mailto:chronotrain@huddeij.de) © 2023
