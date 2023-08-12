## Docker Installation and Usage Documentation

### 1. Installing Docker


1. **For Linux:**
    ```bash
    $ sudo apt-get update
    $ sudo apt-get install docker-ce docker-ce-cli containerd.io
    ```

2. **For Mac and Windows:** 
   - Visit Docker's official site to download Docker Desktop for [Mac](https://docs.docker.com/desktop/mac/install/) or [Windows](https://docs.docker.com/desktop/windows/install/).

3. After installation, you can verify Docker's installation by:
    ```bash
    $ docker --version
    ```

### 2. Starting the Docker Containers

Navigate to the directory where your `docker-compose.yml` file is located. Then, run the following command to start the containers:

```bash
$ docker-compose up --build
```

This command will build the Docker images and then start the Docker containers based on the configurations specified in the `docker-compose.yml` file.

### 3. Accessing the API Endpoints

Once the Docker containers are up and running, you can access the API endpoints to fetch data:

1. **Fetching Profile IDs:**

   URL: `http://localhost:5000/profiles?page=1`
   
   Description: This endpoint fetches the profile IDs from the database, paginated by the page number provided as a query parameter.

2. **Fetching Profile Details:**

   URL Template: `http://localhost:5000/profiles/<id>`
   
   Description: Replace `<id>` with the actual profile ID to fetch detailed information about a specific profile from the database.

3. **Fetching Post IDs:**

   URL: `http://localhost:5000/posts?page=1`
   
   Description: This endpoint fetches the post IDs from the database, paginated by the page number provided as a query parameter.

4. **Fetching Post Details:**

   URL Template: `http://localhost:5000/posts/<id>`
   
   Description: Replace `<id>` with the actual post ID to fetch detailed information about a specific post from the database.

---

Remember to close the Docker containers when you're done:

```bash
$ docker-compose down
```

This command will stop and remove the running containers.