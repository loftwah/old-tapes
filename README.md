# old-tapes
Small script to get all links shared on your facebook feed.


## Getting access to users data:
1. Create facebook app
2. Using GraphAPIExplorer generate access token and pass it as env variable to `old_tapes` 
3. Get user_id


## Installation

```bash
git clone https://github.com/szewczykmira/old-tapes.git
cd old-tapes
virtualenv -p python3 old-tapes
poetry install
# Here is the time to gather access token and user id from facebook SDK
python -m old_tapes
```