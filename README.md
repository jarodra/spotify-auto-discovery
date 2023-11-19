# spotify-auto-discovery
Personal project to learn spotify api through python's spotipy library, authentications and different deployment applications. 

Currently is usable and several platforms are possible to be used
- [x] Manual
- [x] Docker
- [x] Docker-compose
- [X] Kubernetes Cronjob
- [X] Google Cloud Platform: Cloud Run + Cloud Scheduler
  
### Clone the repository
Clone the repository which the following command

    git clone https://github.com/Durgrim/spotify-auto-discovery.git

### Before starting
Install the dependencies.  
Use virtual environments as this will be deployed on docker.  
If you can to use the script in your local machine, just install the requirements.  

    python3 -m venv env
    source env/bin/activate
    cd app
    python3 -m pip install -r requirements.txt

Create an .env file with the following [Spotify developer](https://developer.spotify.com/) infomation.
[Use the recommended (http://localhost:8080) to automatic refresh of authentication token](https://github.com/spotipy-dev/spotipy/blob/587baec9b95da6c45e45f0f8e5b2577bda780980/spotipy/oauth2.py#L374..L383)

    SPOTIPY_CLIENT_ID="your_spotify_developer_id"
    SPOTIPY_CLIENT_SECRET="your_spotify_developer_secret"
    SPOTIPY_REDIRECT_URI="your_spotify_developer_redurect_uri"
    SPOTIFY_USER="your_spotify_user_name"
    DISCOVER_WEEKLY_ID="discover_playlist_id"

### First uses
Execute in your local machine the following commands:

    cd app
    python3 main.py

On this first time call the program and it will prompt a URI.  
This authorization is required as we're using Authorization Code flow on Spotipy through SpotifyOAuth.
Copy, paste it, and paste it back to your terminal.  
It will create a .cache file with the access token, and it will refresh authomaticaly.  
The following steps should be done after the .cache file has been created.  

### Following uses

#### Manual use
If you can to use the script manually in your local machine, just repeat the previous step.  

#### Docker/Docker-compose with cron deployment
For image deployment there's a Dockerfile with an alpine distribution implemented.  
This Dockerfile has a cron job authomatized to run the python script once every Monday at 8:00.

    docker build --tag spotify-auto-discovery .
    docker run -d spotify-auto-discovery

If you prefer to use Docker Compose just use `docker compose up -d` or `docker compose down`.  

#### Kubernetes cronjob deployment
If you prefer to user a local kubernetes cluster:

    docker build -t spotify-auto-discovery-kubernetes -f Dockerfile-kubernetes .
    kubectl apply -f cronjob.yaml

#### Cloud Deployment
An option to deploy the app and not depend on your own resourses is to use a Cloud Provider as Google, AWS or Azure.
Most of them have a free tier option that should be enough to cover the app requirements.

In this particular case I will deploy it within Google Cloud Platform and use Cloud Run jobs.
I will use Artifact Registry as Docker image registry.

**DISCLAIMER:**
In terms of security this is not the best case scenario as we will use the .cache and .env straigh into the container.
Please be careful on the IAM and project visibility.
It could be a nice idea to use env variables during the creation of the cloud run job, but I am not doing as this is a simple project to learn.

Note: In order to be able to use the cloud scheduler tools can the manifest "Dockerfile-kubernetes" can be used instead the default one as it already has a local cron configured (the container will keep running instead).

   docker build -t spotify-auto-discovery -f Dockerfile-kubernetes .

Follow the next steps if you want to try it on your own:
- Install [gcloud CLI](https://cloud.google.com/sdk/docs/install).
- Authenticate with your GCP account:
   ```
     gcloud auth login
   ```
- Set your project:
   ```
     gcloud config set project PROJECT_ID
   ```
- Create the repository into Artifact Registry:
   ```
    gcloud artifacts repositories create REPOSITORY_NAME --repository-format=docker --location=LOCATION --async
   ```
- Adds the Docker credentials entry to Docker's configuration file:
   ```
     gcloud auth configure-docker REGION-docker.pkg.dev
   ``` 
- Build (with the Dockerfile-kubernetes manifest as it will implement the cron afterwards) or tag the image if you already created it.
   - Build the image:
       ```
         docker build . -f Dockerfile-kubernetes -t LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE
       ``` 
   - Or if you already build the image locally, tag the existing image:
       ```
         docker tag spotify-auto-discovery-kubernetes LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE
       ``` 
- Upload the image to Artifact Registry:
    ```
      docker push LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE
    ``` 
- Create the Cloud Run job:
    ```
      gcloud run jobs create JOB_NAME --image=LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE
    ```
- Get your project number:
    ```
      gcloud projects describe PROJECT_ID --format="value(projectNumber)"
    ``` 
- Create the Cloud Scheduler:
    ```
        gcloud scheduler jobs create http SCHEDULE_NAME \
            --location SCHEDULER_REGION \
            --schedule="0 8 * * 1" \
            --uri="https://CLOUD_RUN_REGION-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/PROJECT_ID/jobs/CLOUD_RUN_JOB_NAME:run" \
            --http-method POST \
            --oauth-service-account-email PROJECT-NUMBER-compute@developer.gserviceaccount.com
    ```
