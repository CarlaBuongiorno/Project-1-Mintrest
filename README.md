# Project 1: Mintrest

This is a Flask project. The main goals are to learn the basics of client-server principles, getting a basic website served, and adding new posts via a form.

This project
- is version controlled and available in GiHub
- uses a virtualenv and has a requirements.txt
- has a README.md that explains how to work with it
- has automated tests

## Mintrest

Mintrest is a two-page, extremely minimal version of Pintrest.

There is a root page `(/)`, which contains a logo at the top, and a link to the "new post" page. The rest of the page is a series of posts, each with an image, title, description and date. This list is ordered with the newest posts first.

The New Post page `(/newpost/)` also contains the logo at the top, but this page is a form with three fields:
- _IMAGE_: this allows the user to enter a link to an image
- _TITLE_: a brief description of the post
- _DESCRIPTION_: a full description of the post

There is also a button to allow the user to submit the post. If the submission succeeds, the website redirects the user to the root page, where the new post is visible.