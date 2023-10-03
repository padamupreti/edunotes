# EduNotes

Educational blogging platform built with [Django](https://www.djangoproject.com/ 'Django Website'). Uses
[Tailwind CSS](https://tailwindcss.com/ 'Tailwind CSS Website') and
[htmx](https://htmx.org/ 'htmx Website').

## Requirements

-   [Python](https://python.org/downloads/ 'Download Python') (with pip)

## Setup

First clone the repository. Then, to install dependencies, navigate to project root in the terminal and run:

```
pip install -r requirements.txt
```

EduNotes uses [Natural Language Toolkit](https://www.nltk.org/ 'NLTK Website') tokenizer and stopwords. These
need to be downloaded. To do this, invoke Python shell from the terminal with `python` or `python3` command and run the
following:

```python
import nltk

nltk.download('punkt')
nltk.download('stopwords')
```

Create database migrations and perform migration:

```
python manage.py makemigrations
```

```
python manage.py migrate
```

## Running the development server

After successful completion of setup steps above, the development server can be run with:

```
python manage.py runserver 8000
```

If above command does not produce errors,
[localhost:8000](http://localhost:8000/ 'localhost port 8000') can be visited to view the running application.
