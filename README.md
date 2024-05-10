<div align="center">
  <a href="https://netflix-pro-3mjv.onrender.com/login/">
    <img alt="Netflix Pro" src="https://github.com/AlexIbasitas/Netflix-Pro/blob/main/demo_images/Netflix-Pro.gif">
    <h1>Netflix Pro</h1>
  </a>
</div>




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

https://user-images.githubusercontent.com/25078541/123811962-01474580-d8f4-11eb-83ba-66cded3f321f.mp4

<br/>

## 🎯 About

I have started this project with the purpose of learning how to structure a Web App of a mid-level complexity integrating the Redux logic.<br/>
I've tried to replicate the original layout as much as possible and I've also made some improvements in some sections inserting route animations and micro-interactions. I've also inserted a really close clone of Netflix's original splash animation (forked from a famous [codepen from Claudio Bonfati](https://codepen.io/claudio_bonfati/pen/mdryxPv)), made entirely with CSS, as well as the play animation. I have then sampled the original Netflix "ta-duummm" sound and I made it play along with the two animations.<br/>
I put a lot of effort into it and I hope that you could like it.<br/><br/>
The Web App redirects you to an authentication page, in which you can choose to sign up or to sign in: you can sign in with your custom account or with your Google account. Once you are logged in and after the splash animation, you will land on the homepage, in which you can find a mix of movies and series divided into rows.<br/>
Each row represents a movie/series category: you can click on it and you will be redirected to the selected category, a page that loads thousands of movies with an infinite scroll. You can also navigate to the movies page, series page, new & popular page (that contains the upcoming movies/series and the most popular ones) or you can navigate to your favorites page.<br/>
You can add/remove movies/series through the plus and minus buttons that you can find hovering each poster or opening a single movie's detail modal. If you click on the play button you can enjoy a custom CSS-only play animation with Netflix Pro's brand name.<br/>
You have also the option to search through TMDB's catalogue using the search functionality inside the fixed navbar: you can search by movie name, actor or movie director.<br/><br/>
Go try it and please let me know if you enjoyed it with a ⭐️, I would appreciate it a lot.

<br/>

## ▶️ Demo

Here you can find the demo link:

- [Demo](https://netflix-pro-3mjv.onrender.com/)

⭐ Please allow time for the Demo to load. Render spins down a Free web service that goes 15 minutes without receiving inbound traffic. Render spins the service back up whenever it next receives a request to process. Spinning up a service takes up to a minute, which causes a noticeable delay for incoming requests until the service is back up and running.

### Test credentials (for lazy users 😓)

> Username: test_user<br/>
> Password: password4test_user<br/>

You may also sign in with your Google account.

<br/>

## :sparkles: Features
:heavy_check_mark: &nbsp;&nbsp;Display "Netflix Wrapped"—data visualizations and insightful statistics based on users' viewing history
:heavy_check_mark: &nbsp;&nbsp;Display movies and series, old and upcoming, also from the real Netflix<br />
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

