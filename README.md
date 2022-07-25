# Upturt Backend

Uses cron job to periodically poll status of websites (stored at `.websites` at root directory)

Folder structure as recommended [here](https://guicommits.com/organize-python-code-like-a-pro/)

## Pre-requisites
1. Airtable setup
2. `.websites` file
3. Environment variables
```
export AIRTABLE_API_KEY=xxx
export AIRTABLE_STATUS_TABLE_NAME=xxx
export AIRTABLE_BASE_ID=xxx
```
Save them in `.env-dev` file


