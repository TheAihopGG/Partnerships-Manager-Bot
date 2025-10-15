# Partnership Manager Bot Technical specification

## General

Guild-install-bot is designed to manage list of partnerships of a discord guild. The bot will provide CRUD functional for partnerships.

## Technologies

* **python3.14**
* **sqlalchemy** (database orm)
* **psycopg** (sqlalchemy dialect)
* **alembic** (database migrations)
* **fastapi** (api to interact with nats server)
* **nats** (events server)
* **docker compose**

## Bot commands

### Partnerships

* `add partnership <partner id> <guild id> <text> <invite link> [strict=false]`
  
  For administrators and PR managers

  **Parameters:**
  * `strict` If partner leaves the guild, the bot will break the connection

* `remove partnership <guild id> [reason="no reason"]`

  For administrators and PR managers

  Requires button confirmation

* `update partnership <guild id> [<new partner id> <new text> <new invite link> <strict>]`

  For administrators and PR managers

* `get partnership info <guild id>`

  For administrators and PR managers

  Returns information about partnership, created at, updated at, text, partner id, invite link

* `get partnerships list`

  Returns an organized list of partnerships

### Settings

* `get settings`

  For administrators

* `set prm role <role>`

  For administrators

### General

* `help`

  Returns help message with sections organized in drop select view