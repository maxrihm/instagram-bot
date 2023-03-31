## Instagram Bot with Python and Selenium
This is a Python script that uses Selenium to automate actions on Instagram. The script has several modules:

1. **Subscription Manager**: This module manages your subscriptions to other users. It checks if you have a mutual subscription with the user, and if not, it unfollows them.
2. **Like Photos**: This module likes photos of the accounts that you are following.
3. **Like Photos by Tags**: This module likes photos in your news feed with the tags that you have provided in a text file.
4. **Create Subscription Chains**: This module subscribes to other users' accounts and creates a chain of subscriptions.

The bot runs for a specified time that you can specify in the `time.txt` file, and it will turn off automatically.

### How to Use
1. Clone the repository.
2. Install the dependencies using pip:
```
pip install selenium
```
3. Download the [ChromeDriver](https://sites.google.com/chromium.org/driver/) executable and place it in the project directory.
4.Create a .env file in the project directory and add your Instagram username and password:
```
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password
```
5. Run the script using the following command:
```
python contoller.py
```
6. Choose the module that you want to run.
7. Follow the instructions on the console.

### Note
This script is for educational purposes only. Use it at your own risk. Instagram may block or ban your account if you use this script excessively or inappropriately.
