<a href="https://fakeflix.th3wall.codes">
  <img alt="Fakeflix – Not the usual clone that you can find on the web" src="https://cdn.jsdelivr.net/gh/Th3Wall/assets-cdn/Fakeflix/Fakeflix_readme.png">
  <h1 align="center">Netflix Pro</h1>
</a>

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

- [TMDb API's](https://www.themoviedb.org/)
- [React](https://reactjs.org/)
- [React Hooks](https://reactjs.org/docs/hooks-intro.html)
- [React Hooks Form](https://react-hook-form.com/)
- [React Router](https://reactrouter.com/web/guides/quick-start)
- [Redux](https://redux.js.org/)
- [Redux Thunk](https://github.com/reduxjs/redux-thunk)
- [Redux Saga](https://redux-saga.js.org/)
- [Redux Persist](https://github.com/rt2zz/redux-persist)
- [Redux Logger](https://github.com/LogRocket/redux-logger)
- [Reselect](https://github.com/reduxjs/reselect)
- [Firebase](https://firebase.google.com/)
- [SCSS](https://sass-lang.com/)
- [SwiperJS](https://swiperjs.com/react)
- [Framer Motion](https://www.framer.com/motion/)
- [React Icons](https://react-icons.github.io/react-icons/)
- [Netlify](https://www.netlify.com) (have a look below) and [Vercel](https://vercel.com/) for the deploy and CI.

### Deploy configuration steps

1. Connect your GitHub account to Netlify
2. Select the project
3. In Settings → Build & Deploy → Set **Build command** to : **_npm run build_**
4. In Settings → Build & Deploy → Set **Publish directory** to : **_build_**
5. In Settings → Build & Deploy → Set **Environment variables** → Click on **Edit variables** and add yours (ie: TMBd's API key, Firebase configuration).

<br/>

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

- Go to the project directory

```bash
  cd fakeflix
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

[MIT](https://github.com/Th3Wall/Fakeflix/blob/main/LICENSE)

<br/>



<a href="https://www.buymeacoffee.com/th3wall" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="41" width="174" alt="Buy Me A Coffee" /></a>
