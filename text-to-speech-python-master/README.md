# Text to Speech Python Starter Application

The [Text to Speech][service_url] service uses IBM's speech synthesis capabilities to convert English or Spanish text to an audio signal. The audio is streamed back to the client with minimal delay. The service can be accessed via a REST interface.

Give it a try! Click the button below to fork into IBM DevOps Services and deploy your own copy of this application on Bluemix.

[![Deploy to Bluemix](https://bluemix.net/deploy/button.png)](https://bluemix.net/deploy?repository=https://github.com/watson-developer-cloud/text-to-speech-python)

## Getting Started

1. Create a Bluemix Account

    [Sign up][sign_up] in Bluemix, or use an existing account. Watson Services in Beta are free to use.

2. Download and install the [Cloud-foundry CLI][cloud_foundry] tool

3. Edit the `manifest.yml` file and change the `<application-name>` to something unique.
  ```none
  applications:
  - name: text-to-speech-python
    command: python server.py
    path: .
    memory: 256M
    services:
    - text-to-speech-service
  ```

    The name you use will determinate your application url initially, e.g. `<application-name>.mybluemix.net`.

4. Connect to Bluemix in the command line tool
  ```sh
  $ cf api https://api.ng.bluemix.net
  $ cf login -u <your user ID>
  ```

5. Create the Text to Speech service in Bluemix

  ```sh
  $ cf create-service text_to_speech free text-to-speech-service
  ```

6. Push it live!

  ```sh
  $ cf push
  ```

  See the full [Getting Started][getting_started] documentation for more details, including code snippets and references.

## Running locally
  The application uses [Python](https://www.python.org) and [pip](https://pip.pypa.io/en/latest/installing.html) so you will have to download and install them as part of the steps below.

1. Copy the credentials from your `text-to-speech-service` service in Bluemix to `app.js`, you can see the credentials using:

  ```sh
  $ cf env <application-name>
  ```
    Example output:
  ```sh
  System-Provided:
  {
  "VCAP_SERVICES": {
    "text_to_speech": [{
        "credentials": {
          "url": "<url>",
          "password": "<password>",
          "username": "<username>"
        },
      "label": "text_to_speech",
      "name": "text-to-speech-service",
      "plan": "text_to_speech_free_plan"
   }]
  }
  }
  ```

    You need to copy `username`, `password` and `url`.

2. Install [Python 2.7.9 or later](https://www.python.org/downloads/)
3. Go to the project folder in a terminal and run:
  `pip install -r requirements.txt`
4. Start the application
  `python server.py`
5. Go to
  `http://localhost:3000`


## Troubleshooting

To troubleshoot your Bluemix app the main useful source of information are the logs, to see them, run:

  ```sh
  $ cf logs <application-name> --recent
  ```

## License

  This sample code is licensed under Apache 2.0. Full license text is available in [LICENSE](LICENSE).

## Contributing

  See [CONTRIBUTING](CONTRIBUTING.md).

## Open Source @ IBM
  Find more open source projects on the [IBM Github Page](http://ibm.github.io/)

[service_url]: http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/text-to-speech.html
[cloud_foundry]: https://github.com/cloudfoundry/cli
[getting_started]: http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/doc/getting_started/
[sign_up]: https://apps.admin.ibmcloud.com/manage/trial/bluemix.html?cm_mmc=WatsonDeveloperCloud-_-LandingSiteGetStarted-_-x-_-CreateAnAccountOnBluemixCLI
