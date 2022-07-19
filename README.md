# Costco/Amazon Price Scraper

## How to use:
Install dependencies with using:
```shell
pip -r requirements.txt
```
Set up environment variables in a `.env` file (example in `.env_Sample`)  
Configure `HOST_ADDRESS` and `PORT` in `sendEmail.py` if not using Outlook/Hotmail.  
**NOTE:** Gmail is unsupported as of May 30, 2022 ([Link to Google](https://support.google.com/accounts/answer/6010255?hl=en&visit_id=637896899107643254-869975220&p=less-secure-apps&rd=1#zippy=%2Cuse-an-app-password))

Run with:
```shell
python main.py [file of links].txt
```