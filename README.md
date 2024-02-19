# spotify-auto-discovery
Personal project to learn spotify api through python's spotipy library, authentications and different deployment applications. 

This branch allows the start up with GitHub Actions
- [x] Manual
- [x] Docker
- [ ] GitHub actions
  - [ ] Artifact Registry
  - [ ] Cloud Run
  - [ ] Cloud Scheduler

### Setting up the environment
Define the following variables:
```
    SPOTIPY_CLIENT_ID="your_spotify_developer_id"
    SPOTIPY_CLIENT_SECRET="your_spotify_developer_secret"
    SPOTIPY_REDIRECT_URI="your_spotify_developer_redurect_uri"
    SPOTIFY_USER="your_spotify_user_name"
    DISCOVER_WEEKLY_ID="discover_playlist_id"
```

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
#### GitHub actions CI
An option to deploy the app and not depend on your own resourses is to use a Cloud Provider as Google, AWS or Azure.

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
