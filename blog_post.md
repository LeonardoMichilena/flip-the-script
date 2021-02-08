# Introduction
</br>

We are Stephanie, Leticia, Leonardo and Luciana, a team of four motivated and engaged participants of TechLabs Berlin. We started Flip The Script because we recognized an issue in the way society sees gender. The way language works in our conscious and subconscious mind is often underestimated, and so is the way it affects how we perceive gender.

Flip The Script is aimed to be used as a tool for change and education about our language use by offering users the option to consciously decide for a fairer language. Furthermore, we want to offer visitors the option to learn more about language use and patters and why it is important. You can find, on the statistics page, our results from collecting and analyzing news articles from various sources across the web.

The MVP that we are presenting is a web app that essentially takes a user submitted text and flips the pronouns in the text to either the opposite gender's pronouns, or to gender neutral pronouns. While this is a centering topic of our MVP, it is not the only feature that our app provides. We have several different processes that make up our app, including a machine learning module, an analysis of data we collected over the duration of the project phase, and special design features.

Here, you will find a deep dive into the process of building the app, the challenges we faced, and an explanation about the deliverable we created.

# Front-end

# Back-end
After our first meeting, discussing vaguely what an MVP could look like, it became apparent that NodeJS alone would not work. The data scientists are working in python and writing functions that are necessary for working with the web page in real time. This includes the dictionaries and converting functions that scan an article and flip the words. Meike informed us that in order for python functions to work with the NodeJS app, we would need to find a way to connect the two languages.
Being brand new to coding and the concepts of back-end, I understood quickly that I had a lot to learn.
So, to complete my first task of the project, I had to find a way to connect the NodeJS app with python. Flask seemed like the best option.

This is a point in the project that was one of the most difficult for me. I knew I had to not only grasp the concept of the NodeJS express app and what it meant to set up http entry points, but to also learn a new framework as well as learn some basic python coding (as my coding knowledge up to this point was only JavaScript).

I felt over my head and was nervous about what my capabilities were. NodeJS was already foreign enough, but learning how to set up a Flask server seemed even more confusing.

So, what I did was start small; a method I learned as a way to tackle larger coding problems and will subsequently always apply in the future. My goal was a classic "hello world" app.
After I read the Flask documentation and watched some videos to learn some basic python, I set up a path in the Flask app that would return the string 'hello world'. This was one of the most challenging parts of the projects, yet now, looking back, it seems so simple. The experience serves as another insight I learned over the course of the project; that sometimes, challenges seem big and impossible, but once they are solved, look tiny and simple.

When the first completed python function was pushed to GitHub, I began my next challenge. This was passing text data from a user form, in the NodeJS app, to the python function in the Flask app and then the converted data back to the NodeJS app.
It was during this process that I learned I could not send data with Flask and Express only, but also needed the help of Axios. So, I read the documentation to Axios and watched some online courses that would help me understand how to use it.

It was also during this challenge that I learned python does not use JSON data, which happened to be the data that NodeJS was sending to the Flask app. I mentioned earlier my big challenge of setting up the "hello world" app between Flask and NodeJS. Finding out how to pass usable information to python was my next biggest challenge. It took me a couple days to figure this one out, and just like the previous, it seems just as simple in hindsight.

It was during this challenge that I learned about python's request library and how to parse JSON data in the Flask app. Eventually, in the final form of the app, I implemented the command json.loads(request.data) that would parse the JSON data.

The process was challenging and the resulting code was messy, but I was able to set up a working app in which a user could submit text in a form and it would return to them converted. Below are some images of the first versions of the app.
You will see, that my API calls are circular and I am not using GET and POST requests correctly.

## First working version:

Below are four images that show the (incorrect) use of REST APIs. While they did work for its intended purpose, they are redundant, circular, and incorrect.

- Image one: The Flask app (which uses localhost:5000) uses a GET method to grab data from the express app (localhost:3000).
- Image two: In the Express app, GET and POST routes for user submitted articles.
- Image three: Using Axios incorrectly to set up a port to pass data from the Express app to the Flask App.
- Image four: The Express app calling the Flask server for the data that has been converted.
![FlaskVersion1](https://user-images.githubusercontent.com/60686512/107198524-7f628880-69f5-11eb-9a82-2f3df6bae247.PNG)

  ![nodereversepostandget](https://user-images.githubusercontent.com/60686512/107198602-943f1c00-69f5-11eb-9df2-549f407c5240.PNG)

  ![nodereversewraptoflask](https://user-images.githubusercontent.com/60686512/107198609-9608df80-69f5-11eb-8062-59c7868aef52.PNG)

  ![NodeReverse1post](https://user-images.githubusercontent.com/60686512/107198595-930def00-69f5-11eb-9e65-0ab49ec97080.PNG)

## Final working version:

After I received feedback that the GET and POST requests were not correct, I spent some more time reviewing documentation for Flask, NodeJS, and Axios, as well as review online tutorials I could find on REST routes.  Below are some images of the final version, which will show the corrected routes.    

Below is the final version of the paths that send data to the gender_function (to flip the pronouns in the text to the opposite gender) and back.

- Image one: Represents the form element that a user can choose whether to flip their text using the gender_converter or the neutral_converter. This is done by using the POST method in the form element, as well as the formaction attribute in the button element. Notice there are two different paths. The example I am providing will use the "/articles" path, which represents the gender_converter function.
- Image two: Represents the API call that posts to Flask and returns data back to NodeJS. A modification from the earlier version of the app, the Axios POST method is nested within the express POST method. Three API calls are done in this one block of code. First, the data from the form element is posted to "/articles". Next, the object req.body is deconstructed to pass the "article" property to Flask, through a POST request using Axios. After Flask processes the data (refer to image three for an explanation), it is returned in the response object. The converted article resides under repsonse.data and is extracted. Here, you will notice that the variable differentWords is given a value. The value is referencing the fucntion convertedWordsArray (explained in image four). DifferentWords is the array of words that have been converted. Finally, the data, which includes the DifferentWords array, the user submitted article(firstArticle), and the converted article(response.data), is sent to the "flip" ejs page and formatted to the page.
- Image three: The Flask method is now a POST. Therefore, the request.get is no longer necessary and the data sent from NodeJS is represented as request.data.
Next, it is important to convert the data from JSON with json.loads and continuing to extract the necessary data from the object. Finally, the actual python file that holds the converter functions, pre_gender_converter and pron_converter, resides in another file and is being called from def jsInfo(). Once the text is converted, it is returned.
- Image four: The function that finds the array of words that have been changed. This is important for the purpose of the highlighting feature, which will highlight the words in the converted text that have been altered. The function calls for two arguments. In this case, the two arguments are the converted article(response.data) and the original article(firstArticle). Next, a for/of loop checks to see if any words from the first and second article are different using the indexOf() method. An if loop notifies, that if the terms are different (equal to -1), to push them to an array. Then, the array of different terms are returned.
   ![formFinal](https://user-images.githubusercontent.com/60686512/107198579-8f7a6800-69f5-11eb-9cc4-a6001a884a32.PNG)

  ![nodeFinal](https://user-images.githubusercontent.com/60686512/107198588-91442b80-69f5-11eb-8826-52127db3766c.PNG)

  ![Flaskfinal2](https://user-images.githubusercontent.com/60686512/107198556-8b4e4a80-69f5-11eb-875a-8dca599d4c8b.PNG)

  ![flipFUnction](https://user-images.githubusercontent.com/60686512/107198571-8e493b00-69f5-11eb-84f6-01702b5c77d9.PNG)










# Data Science

# UX

# Conclusion
