
# CryptoSignals

CryptoSignals is a cryptocurrency fluctuation notifier. It is build on Django and currently supports Slack. It has an interface for managing settings and subscription. 

## Getting Started

The below instructions will help in setting up the project in local machine.

### Prerequisites

Need `virtualenv` and `python3` for creating isolated environment.

```
sudo apt-get install virtualenv
```

### Installation

1. Clone the project into the machine.
2. Go to project root and create `virtualenv`. 
```virtualenv -p python3 venv```
3. Activate virtualenv.
```source venv/bin/activate```
4. Install dependencies.
```pip3 install -r requirements.txt```
5. Execute migrations.
```python3 manage.py migrate```
6. Create superuser
```python3 manage.py createsuperuser```
7. Run the server
```python3 manage.py runserver```
The server will be starting at `127.0.0.1:8000`.

### Post setup
Setup a cron to execute `/api/hotload/` at max 1 time  for every minute.

## Usage

CryptoSignals need slack token and channel name for sending notifications. 
1. To create a slack token, Login to the slack in browser and go to the legacy-token page by clicking [here](https://api.slack.com/custom-integrations/legacy-tokens). Now generate token by clicking `Generate token` button under `Legacy information` tab. Save the `token` for later purpose. 
2. Choose existing channel or create a new channel and save the channel name for later purpose.
3. Login to `CryptoSignals` and go to the settings, provide `token` and `channel` name  and check subscription box and hit update button.
4. Go to the homepage and click any coin card and hit subscribe button to get its notifications.
Note: Channel name is absolute. So while providing channel name it should be along with the `#` example `#general`, `#random` etc..

## Deployment

The application has been deployed on heroku . Go to [https://cryptosupport.herokuapp.com/login/](https://cryptosupport.herokuapp.com/login/) for live.

## Built With

* [Django](https://www.djangoproject.com/) - A python based web framework.
* [cron-job.org](https://cron-job.org/en/) - External API cron service.
* [koinex](https://koinex.in/) - India's leading cryptocurrency platform.

