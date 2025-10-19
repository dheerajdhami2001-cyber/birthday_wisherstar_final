# Automated Birthday Wisher

A Python script that automatically sends a personalized birthday email to friends and family. This project uses `smtplib` for sending emails, `pandas` for managing a list of birthdays from a CSV file, and the `datetime` module to check the current date.

The script checks a list of birthdays every day. If it finds a birthday matching the current day, it selects a random letter template, personalizes it with the person's name, and sends them a happy birthday email.

## Key Features

-   **Fully Automated:** Runs daily to check for birthdays without any manual intervention.
-   **Personalized Emails:** Merges the birthday person's name into a letter template for a personal touch.
-   **Customizable Templates:** Easily add or edit email templates in the `letter_templates` directory.
-   **Easy Contact Management:** Add or remove birthdays by simply editing the `birthdays.csv` file.
-   **Cloud-Ready:** Designed to be deployed on a cloud service like PythonAnywhere for scheduled daily execution.

## Project Setup & Configuration

Follow these steps carefully to get the script running.

### 1. Prerequisites

-   Python 3.x
-   A Google Account (Gmail)
-   `pip` (Python package installer)

### 2. Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/dheerajdhami2001-cyber/your-repo-name.git
    ```
    *(Remember to replace `your-repo-name` with your actual repository name.)*

2.  **Navigate into the project directory:**
    ```bash
    cd your-repo-name
    ```

3.  **Install the required dependency:**
    ```bash
    pip install pandas
    ```

### 3. Customize for Your Use

1.  **Update the Birthday List:**
    Open the `birthdays.csv` file. Edit it to include the names, email addresses, and birth dates of the people you want to send wishes to. **Ensure the column headers (`name,email,year,month,day`) remain the same.**

2.  **Edit or Add Email Templates:**
    Navigate to the `letter_templates` directory. You can modify the existing `letter_1.txt`, `letter_2.txt`, etc., or add your own. The script will randomly pick one. Make sure you keep the `[NAME]` placeholder, as this is where the person's name will be inserted.

### 4. Set Up Your Email Credentials (IMPORTANT)

This script uses Gmail to send emails. For security reasons, you cannot use your regular Gmail password directly in the code. You must generate a special **"App Password"**.

**How to Generate a Google App Password:**

1.  **Enable 2-Step Verification:**
    -   Go to your Google Account settings: [myaccount.google.com](https://myaccount.google.com/).
    -   Navigate to the "Security" tab.
    -   Under "Signing in to Google," click on **"2-Step Verification"** and follow the on-screen steps to enable it. You cannot create an App Password without this.

2.  **Create the App Password:**
    -   On the same "Security" page, click on **"App passwords"** (this option will appear after you enable 2-Step Verification).
    -   You may be asked to sign in again.
    -   Under "Select app," choose **"Mail"**.
    -   Under "Select device," choose **"Other (Custom name)"**. Name it something descriptive, like "Python Birthday App".
    -   Click **"Generate"**.

3.  **Save Your App Password:**
    -   Google will show you a **16-character password**. This is your App Password.
    -   **Copy this password immediately and save it somewhere safe.** You will not be able to see it again.

4.  **Update the Script:**
    -   Open `main.py`.
    -   Find the lines for `my_email` and `password`.
    -   Replace `"testingcode@gmail.com"` with your own Gmail address.
    -   Replace `"abcd efgh ijkl mnon"` with the **16-character App Password** you just generated.

## Deployment to the Cloud (PythonAnywhere)

To make this script truly automatic, you should host it on a cloud service that can run it on a schedule. PythonAnywhere is a great free option for this.

**Recommended Schedule Time:** To be the first to send a wish, schedule the script to run once a day at **12:00 AM UTC (midnight)**.

**Steps to Deploy on PythonAnywhere:**

1.  **Create a free PythonAnywhere account.**
2.  **Upload Your Files:**
    -   Go to the "Files" tab.
    -   Upload `main.py`, `birthdays.csv`, and the entire `letter_templates` folder.
3.  **Set Up a Scheduled Task:**
    -   Go to the "Tasks" tab.
    -   Create a new "Daily task".
    -   Set the time you want the script to run (e.g., `00:00` UTC).
    -   In the command box, enter the command to run your script: `python3 /home/YourUsername/main.py` (replace `YourUsername` with your PythonAnywhere username).
    -   Click "Create task".

Your script is now live and will run automatically every day at midnight.

## Acknowledgments

This project was inspired by and completed with the guidance of the **[100 Days of Code: The Complete Python Pro Bootcamp](https://www.du.ac.in/)** by Dr. Angela Yu.

```
