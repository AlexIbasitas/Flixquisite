<div align="center">
  <a href="https://netflix-pro-3mjv.onrender.com/login/">
    <img alt="Netflix Pro" src="https://github.com/AlexIbasitas/Netflix-Pro/blob/main/demo_images/Netflix-Pro.gif">
    <h1>Netflix Pro</h1>
  </a>
</div>




Uploading netflix_pro_demo.mp4…



<p align="center">
  An expanded platform modeled after Netflix—one that not only delivers captivating content but also provides users with personalized data       visualizations and insightful statistics based on their viewing history
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/alexibasitas/">
    LinkedIn
  </a>
</p>

<p align="center">
  <a href="#-about"><strong>About</strong></a> ·
  <a href="#%EF%B8%8F-demo"><strong>Demo</strong></a> ·
  <a href="#sparkles-features"><strong>Features</strong></a> ·
  <a href="#rocket-technologies"><strong>Technologies</strong></a> ·
  <a href="#-screenshots"><strong>Screenshots</strong></a> ·
  <a href="#-run-locally"><strong>Run Locally</strong></a> ·
  <a href="#white_check_mark-requirements"><strong>Requirements</strong></a> ·
  <a href="#-license"><strong>License</strong></a> ·
</p>
<br/>

![Netflix Pro Demo](https://github.com/AlexIbasitas/Netflix-Pro/raw/main/demo_images/netflix_pro_demo.mp4)


<br/>

## 🎯 About

I have started this project with the purpose of learning how to structure a Web App and learn more about how Netflix written in Django might work. I was inspired to build this expanded Netflix-inspired platform while completing the Netflix Pathways Summer Bootcamp 2023.<br/>

The Web App redirects you to an sign in page, in which you can choose to sign up or to sign in: you can sign in with your custom account, sign in with the test account provided below, or sign in with your Google account. Once you are logged in, you will land on the homepage, in which you can find movies and series on each row<br/>

In the navigation bar, you may click the "Genre" dropdown menu in order to look at movies sorted by genre. You may also click the "My List" button to view movies/series that have been added to your favorited list.<br/>

You can add/remove movies/series through the "Add to My List" button found in each movie modal. Press the play button to view the title.<br/>

Click the "Netflix Wrapped" button in the navigation bar to view visualizations and statistics related to your watch history. This button will redirect you to a landing page where you may select from a variety of options. You may selec the period of time included in the generated "Netflix Wrapped" and choose to either view Alex's Netflix Wrapped or Upload your own.<br/>

<br/>

## ▶️ Demo

Here you can find the demo link:

- [Demo](https://netflix-pro-3mjv.onrender.com/)

⭐ Please allow time for the Demo to load. Render spins down a Free web service that goes 15 minutes without receiving inbound traffic. Render spins the service back up whenever it next receives a request to process. Spinning up a service takes up to a minute, which causes a noticeable delay for incoming requests until the service is back up and running.

### Test credentials

> Username: test_user<br/>
> Password: password4test_user<br/>

You may also sign in with your Google account.

<br/>

## :sparkles: Features
:heavy_check_mark: &nbsp;&nbsp;Generate "Netflix Wrapped"—data visualizations and insightful statistics based on users' viewing history<br />
:heavy_check_mark: &nbsp;&nbsp;Select the time frame for Netflix Wrapped, ranging from 3 to 12 months of viewing history.<br />
:heavy_check_mark: &nbsp;&nbsp;Watch movies and series, old and upcoming<br />
:heavy_check_mark: &nbsp;&nbsp;Search by title, actor, genrer<br />
:heavy_check_mark: &nbsp;&nbsp;Add/Remove to/from "My list" functionality<br />
:heavy_check_mark: &nbsp;&nbsp;Detail modal with extra informations about the selected movie/series<br />
:heavy_check_mark: &nbsp;&nbsp;Category related pages<br />
:heavy_check_mark: &nbsp;&nbsp;Google OAuth login<br />
:heavy_check_mark: &nbsp;&nbsp;User Sign In & User Sign Up<br />
:heavy_check_mark: &nbsp;&nbsp;Favourites list persistence (PostgreSQL database hosted on Amazon RDS)<br />
:heavy_check_mark: &nbsp;&nbsp;Scroll movies list<br />

<br/>

## :rocket: Technologies


- [Django](https://www.djangoproject.com/)
- [Django Whitenoise](https://whitenoise.readthedocs.io/en/stable/django.html) a middleware to handle static files
- [Django Social Auth](https://python-social-auth.readthedocs.io/en/latest/configuration/django.html) for setting up social authentication
- [Netflix API](https://www.netflix.com/viewingactivity)
- [Plotly](https://plotly.com/) a Python data visualization library
- [Google OAuth](https://cloud.google.com/apigee/docs/api-platform/security/oauth/access-tokens)
- [Psycopg2](https://pypi.org/project/psycopg2/) a PostgreSQL database adapter for Python 
- [Tailwind CSS](https://tailwindcss.com/)
- [PostgreSQL](https://www.postgresql.org/) for database
- [AWS](https://aws.amazon.com/) for hosting database
- [Render](https://render.com/) for the deploy and CI.
- [TMDB](https://www.themoviedb.org/) for movie information

## 📸 Screenshots

**Sign In**
![Screenshot of Netflix Pro Sign In](https://github.com/AlexIbasitas/Netflix-Pro/blob/main/demo_images/login_page.png)
<br/>

**Sign Up**
![Screenshot of Netflix Pro Sign Up](https://github.com/AlexIbasitas/Netflix-Pro/blob/main/demo_images/sign_up_page.png)
<br/>

**Homepage**
![Screenshot of Netflix Pro Homepage](https://github.com/AlexIbasitas/Netflix-Pro/blob/main/demo_images/home_page.png)
<br/>

**Modal Detail**
![Screenshot of Netflix Pro Modal Detail](https://github.com/AlexIbasitas/Netflix-Pro/blob/main/demo_images/modal.gif)
<br/>

**Netflix Wrapped Landing Page**
![Screenshot of Netflix Pro Wrapped Landing Page](https://github.com/AlexIbasitas/Netflix-Pro/blob/main/demo_images/netflix_wrapped_landing_page.png)
<br/>

**Netflix Wrapped**
![Screenshot of Netflix Pro Wrapped](https://github.com/AlexIbasitas/Netflix-Pro/blob/main/demo_images/netflix_wrapped.gif)
<br/>

## 👨🏻‍💻 Run Locally

- Clone the project

```bash
  git clone https://github.com/AlexIbasitas/Netflix-Pro.git
```

- Go to the project's root directory

```bash
  cd Netflix_Pro
```

- Install dependencies

```bash
  npm install
  pip3 install -r requirements.txt
```

- Configure your PostgreSQL database in settings.py

- Start the server

```bash
  python3 manage.py runserver
```

<br/>

## :white_check_mark: Requirements

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Node](https://nodejs.org/en/) installed.

<br/>

## 📝 License

[MIT](https://github.com/AlexIbasitas/Netflix-Pro/blob/main/LICENSE.bib)

<br/>

