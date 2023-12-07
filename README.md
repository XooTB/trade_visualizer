# Trade visualizer

This project is built with [django](https://www.djangoproject.com/) and [python](https://www.python.org/). I built this project as a submission for a job application. So the next parts are aimed towards them.

- Live Site: [jackdawson.pythonanywhere.com/](https://jackdawson.pythonanywhere.com/)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Challenges & Solutions](#challenges)

## Installation

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the project dependencies using `pip install -r requirements.txt`.
4. Run database migrations using `python manage.py migrate`.
5. Start the development server using `python manage.py runserver`.

## Usage

1. Access the application at `http://localhost:8000`.
2. Follow the instructions to use the features of the application.

## Challenges

The main challenged faced while working on this project was that, I've never built anything using `Django` in the past. I learnt a bit of Python in class, but that was it. I always focused on being a JavaScript developer. So when I saw that this project needed to be built with Django and Python, I saw it as a big challenge.

I hopped onto [Youtube](https://www.youtube.com/) and taught myself some Django basics before I could even start. So it took me some time to finish this project.

The second challenge would be the huge amount of data. The data provided had almost **16 Thousand** entries. Which was a bit of problem while serving over the web. The loading times were really bad. So I had to get creative and group the data together so that the loading times of the website would be somewhat acceptable.

Instead of showing each entry individually, they are grouped up together. More detailed history of the tradecode can be found in the detailed pages.

Charts and graphs can also be found in the individual detailed page for each company. As putting them on top of the table makes it look really ugly.

Please checkout the detailed pages for each company to see how their stocks price is doing.
