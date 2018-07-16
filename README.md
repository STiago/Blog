The purpose of this service is to accept a blog url (with URL validation), store the blog url entered into the form, fetch and store the UPA and PDA values return by the Moz API.

Requirements:

- Install Django (1.10) & Postgres and create a Django project
- Make a model, view, form and templates to accept a blog url (with URL validation)
- Make a temporary account with https://moz.com/products/mozscape/access to use their API
- Store the Blog url entered into the form, and fetch (and store) the UPA and PDA values return by the API (https://moz.com/help/guides/moz-api/mozscape/api-reference/url-metrics)
- Create an admin page to display the blog urls entered, and show the UPA and PDA values in the list display


How to run the service and the tests: docker-compose up

Before running this service or its tests:
  - Ensure you have installed the following packages: python3, docker, docker-compose
  - In the directory The_Blogger_Programe, execute the following command: docker-compose build

Endpoints:

- http://localhost:8000/add_blog_url/ -> Register a new blog url
- http://localhost:8000/ -> Home: Shows a list with the blog url registered.
- http://localhost:8000/admin_view/ -> Admin view: Shows a list of blogs with the blog url, UPA and PDA registered.
- http://localhost:8000/delete/<id> -> Delete a blog
