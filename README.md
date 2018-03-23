# Candy Machine With Feelings

![Screenshot](http://i.imgur.com/1hPcd1O.png)

The project is originally created by [Josh Zheng](https://www.ibm.com/blogs/watson/2016/07/build-candy-machine-feelings/) to build a candy machine that could understand speech and dispense different types of candy based on the sentiment of the words using Watson Speech to Text with Watson AlchemyLanguage. We added an Arabic version to the project using Watson Language Translator.

## About

This repository contains the web application that runs on a Raspberry Pi connected to Candy Dispensers through Arduino.

The front end (client.js) uses the [Watson Javascript Speech To Text SDK](https://github.com/watson-developer-cloud/speech-javascript-sdk) to communicate with the Watson Speech to Text service via WebSocket.  The back end uses the [Watson Developer Cloud Python SDK](https://github.com/watson-developer-cloud/python-sdk) to access the AlchemyLanguage endpoints.

## Steps

1. Clone or download the repository
2. Login to your IBM Cloud account, if you don't have one already you can [sign up for IBM Cloud](https://console.bluemix.net/registration/).
3. Create `Speech to Text`,`AlchemyLanguage` and `Language Translator` services from Watson catalog in IBM Cloud.  
4. Update `.env` file with your service credentials
   ```
    STT_USERNAME=*your watson speech to text service credential*  
    STT_PASSWORD=*your watson speech to text service credential*  
    ALCHEMY_API_KEY=*your alchemy api key*
    LT_USERNAME=*your watson language translator service credential*
    LT_PASSWORD=*your watson language translator service credential*
    ```
5. Run the following command in the terminal to run the application

   `python server.py`

   If there is an Arduino board connected, run the following command instead.

   `python server.py arduino`

   *Note: by default it will run on localhost:5000*
<br><br>

If you want to learn more about the candy machine, here is the [complete tutorial on Medium](https://medium.com/@joshzheng/how-to-build-a-candy-machine-with-feelings-922285a475c8#.hncnebk0v) on how to put build the candy machine

## Contribution
AlchemyLanguage service has been deprecated and will remain supported till Mar 7, 2018. You can contribute to the project by using Watson Natural Language Understanding service instead to tap into the same powerful text analytics.

## Contributors

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
| [<img src="https://avatars2.githubusercontent.com/u/9212117?s=400&u=e8e8f322cb3d83a5442fe372c64884b7ffa1ee3c&v=4" width="100px;"/><br /><sub><b>Deema Alamer</b></sub>](https://twitter.com/deemaalamer)<br />[💻](#Contributors "Code") | [<img src="https://avatars3.githubusercontent.com/u/31738704?s=400&v=4" width="100px;"/><br /><sub><b>Nailah ALTayyar</b></sub>](https://twitter.com/naila_musaid)<br/>[💻](#Contributors "Code") | [<img src="https://avatars0.githubusercontent.com/u/17964781?s=460&v=4" width="100px;"/><br /><sub><b>Nora AlNashwan</b></sub>](https://twitter.com/xnorax)<br/>[💻](#Contributors "Code") [📖](#Contributors "Documentation")
| :---: | :---: | :---: |

This project follows the [all-contributors][all-contributors] specification.
Contributions of any kind are welcome!

## License
This project is licensed under the terms of the **MIT** license. You can check out the full license [here](https://opensource.org/licenses/MIT).

[all-contributors]: https://github.com/kentcdodds/all-contributors
