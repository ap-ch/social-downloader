# ![Social Downloader](https://i.imgur.com/Yid7oNy.png)
This is a full-stack application that lets the user download content easily from Social Networks. It's fully modular, so adding another is fairly simple. For the time being it only works with Telegram.

## Application Features
- Easy local deployment with Docker Compose
- Configuration with environment variables
- Authentication with OAuth2, using a bearer type token
- Backend written in Python using the FastAPI framework
- Long-term persistence of data per user with MongoDB
- Queuing of jobs per service with Celery and RabbitMQ
- Automatic handling of pagination
- Custom preferences per user
- Frontend using the SvelteKit framework (WIP)

## Services Available
### Telegram
Using the Telegram service, you can get:
- Your user
- Your chats
- A chat given its ID
- All messages or N messages of a chat given its ID
- More to be added

Moreover, the user can change the `telegram_login` preferences to switch the Telegram account they are using by setting a different phone number or bot token. Each Telegram account has a different cache directory so conflicts won't occur.


