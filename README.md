# Get Daily Arxiv Notification E-mails

This repository is build based on [here](https://github.com/kobiso/get-daily-arxiv-noti) and [here](https://github.com/DongZhouGu/arxiv-daily)

Arxiv.org announces new submissions every day on fixed time as informed [here](https://arxiv.org/help/submit). You can subscribe to Arxiv notification service for paper categories as described [here](https://info.arxiv.org/help/subscribe.html).
But the arxiv e-mails has so many articles that impossible to browse. Sometimes it reach the maximum line number allowed by e-mail services.

This repository makes it easy to filter papers by keywords and follow-up new papers which are in your interests by creating an issue in a github repository.

- Subject: computer science (cs)
- Keywords: "human object interaction", "visual relation detection", "object detection", "transformer","scene understanding", "visual reasoning"

## Usage( github actions)

#### 0. ⭐Star⭐

#### 1.Clone this Repo and Create a Repo

- Create a repository to get notification via e-mail.
-  **click "Settings"->"Secrets and variables"->"Actions" -> New repository secret**

```python
Option-1 (connect mail via connection URL):
Name: MAIL_CONNECTION
Specify connection via URL (replaces server_address, server_port, secure, username and password)
Value Format:
* smtp://user:password@server:port
* smtp+starttls://user:password@server:port

Option-2(connect mail via username and password):
MAIL_SERVER
Value: smtp.domain.com

Name: MAIL_USERNAME
# Authentication for your e-mail
Value: yourusername

Name: MAIL_PASSWORD
# Authentication for your e-mail
Value: yourpassword
-----------

Name: MAIL_FROM
Value: Your Name <yourmail@domain.com>

Name: MAIL_TO
Value: yourmail@domain.com, anothermail@domain.com

Optional
Name: MAIL_CC
Value: yourmail@domain.com, anothermail@domain.com
```




#### 2. Edit python-package.yml

**update `python-package.yml` as your perferences.**





#### 3. Edit config.py
```python
# Set new submission url of subject
NEW_SUB_URL = 'https://arxiv.org/list/cs/new'

# Keywords to search
KEYWORD_LIST = ["changeme"]
```

#### 4.  Test

To test the functionality, you can click "Actions -> Arxiv Daily -> Run Workflow -> Run Workflow" for an immediate run.
