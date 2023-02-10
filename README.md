### Telegram bot - Calendarbot

#### Setup
1. Setup your bot with Botfather bot in Telegram
2. Put your Telegram API key into .env file in root dir
3. Put your credentials.json from Google Console to credentials.json in root dir
4. poetry install
5. poetry shell
6. poetry run start

#### TODO:
- add ability to answer different users - done
- add SQL - done
- add calendar subscription from it's url - in the process
- add versioning
- make project build startup inside of a docker containers (postgre and bot app)
- draw a banner for this README!
- produce text messages with neural network (not related to main direction of using Google Calendar API
- add instruction on how to get credentials and API keys from google and tg to README
- update secrets or erase them from commit history