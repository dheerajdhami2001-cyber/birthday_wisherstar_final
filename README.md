# Automated Birthday Wisher

A Python script that automatically sends a personalized birthday email to friends and family. This project uses `smtplib` for sending emails, `pandas` for managing a list of birthdays from a CSV file, and the `datetime` module to check the current date.

The script checks a list of birthdays every day. If it finds a birthday matching the current day, it selects a random letter template, personalizes it with the person's name, and sends them a happy birthday email right at midnight.

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
    git clone https://github.com/dheerajdhami2001-cyber/birthday_wisherstar_final.git
    ```

2.  **Navigate into the project directory:**
    ```bash
    cd birthday_wisherstar_final
    ```

3.  **Install the required dependency:**
    ```bash
    pip install pandas
    ```

### 3. Customize for Your Use

1.  **Update the Birthday List:**
    Open the `birthdays.csv` file. Edit it to include the names, email addresses, and birth dates of the people you want to send wishes to. **Ensure the column headers (`name,email,year,month,day`) remain the same.**

2.  **Edit or Add Email Templates:**
    Navigate to the `letter_templates` directory. You can modify the existing `letter_1.txt`, `letter_2.txt`, etc., or add your own. The script will randomly pick one. Make sure you keep the `[NAME]` placeholder.

### 4. Set Up Your Email Credentials (IMPORTANT)

This script uses Gmail. For security reasons, you cannot use your regular Gmail password directly. You must generate a special **"App Password"**.

**How to Generate a Google App Password:**

1.  **Enable 2-Step Verification:**
    -   Go to your Google Account settings: [myaccount.google.com](https://myaccount.google.com/).
    -   Go to the "Security" tab.
    -   Enable **"2-Step Verification"**. You cannot create an App Password without this.

2.  **Create the App Password:**
    -   On the same "Security" page, click on **"App passwords"**.
    -   Select "Mail" for the app and "Other (Custom name)" for the device. Name it "Python Birthday App".
    -   Click **"Generate"**.

3.  **Save Your App Password:**
    -   Google will show you a **16-character password**. Copy this immediately.

4.  **Update the Script:**
    -   Open `main.py`.
    -   Replace `"testingcode@gmail.com"` with your Gmail address.
    -   Replace `"abcd efgh ijkl mnon"` with the **16-character App Password** you just generated.

## Deployment to the Cloud (PythonAnywhere)

To make this script truly automatic, host it on a cloud service.

**Recommended Schedule Time:** To be the first to send a wish, schedule the script to run once a day at **12:00 AM UTC (midnight)**.

**Steps to Deploy:**

1.  **Create a free PythonAnywhere account.**
2.  **Upload Your Files:**
    -   Go to the "Files" tab and upload `main.py`, `birthdays.csv`, and the `letter_templates` folder.
3.  **Set Up a Scheduled Task:**
    -   Go to the "Tasks" tab and create a new "Daily task".
    -   Set the time to `00:00` UTC.
    -   Enter the command: `python3 /home/YourUsername/main.py` (replace `YourUsername` with your PythonAnywhere username).

### A Crucial Extra Step for Google Security

Often, Google's security will block the first login attempt from a new server like PythonAnywhere. To fix this, you need to manually authorize the connection **one time**.

1.  **Run the Task Manually:**
    -   After setting up the task, go to your "Tasks" tab on PythonAnywhere and click the "▶️" (Run) button. It will most likely fail, and this is expected.

2.  **Authorize the Login Attempt:**
    -   Check your Gmail inbox for a **"Critical security alert"** email from Google.
    -   Open the email and click the **"Check activity"** button.
    -   On the next page, confirm that **"Yes, it was me"**. This tells Google that the login attempt from the PythonAnywhere server was legitimate.
    -   Alternatively, you can proactively visit Google's [Display Unlock Captcha](https://accounts.google.com/b/0/DisplayUnlockCaptcha) page and click "Continue" to allow access from new devices.

3.  **Re-run the Task:**
    -   Go back to PythonAnywhere and run the task again. It should now succeed.

Your script is now live and will run automatically every day at midnight.

## Acknowledgments

This project was inspired by and completed with the guidance of the **[100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)** by Dr. Angela Yu.
