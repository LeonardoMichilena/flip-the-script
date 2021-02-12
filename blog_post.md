# Introduction
</br>

We are Stephanie, Leticia, Leonardo and Luciana, a team of four motivated and engaged participants of TechLabs Berlin. We started Flip The Script because we recognized an issue in the way society sees gender. The way language works in our conscious and subconscious mind is often underestimated, and so is the way it affects how we perceive gender.

Flip The Script is aimed to be used as a tool for change and education about our language use by offering users the option to consciously decide for a fairer language. Furthermore, we want to offer visitors the option to learn more about language use and patters and why it is important. You can find, on the statistics page, our results from collecting and analyzing news articles from various sources across the web.

The MVP that we are presenting is a web app that essentially takes a user submitted text and flips the pronouns in the text to either the opposite gender's pronouns, or to gender neutral pronouns. While this is a centering topic of our MVP, it is not the only feature that our app provides. We have several different processes that make up our app, including a machine learning module, an analysis of data we collected over the duration of the project phase, and special design features.

Here, you will find a deep dive into the process of building the app, the challenges we faced, and an explanation about the deliverable we created.

# Front-end

After our first meeting we agreed on what each our roles in the project will be, and visualise, after some brainstorming, what our first MVP should aim for. Although I was following the back-end Web Dev learning path. We decided that I could take care of the front-end part of the project along with Luciana, our UI/UX designer. And since I had some previous experience and I love front-end, I was quite happy to do so.
All my previous experience was mostly just me, coding. So I was happy to be part of a smart and easy-going team that effectively worked together on bringing results week by week.
Once we defined that first MVP, we still had no idea about what it even should look like or how exactly it should work. I couldn’t start to code yet. So I started to learn a bit from our designer about all the research that should be done before even starting to design anything. I was helping with some ideas and questions that we used in order to get some feedback from potential users.
Even though at the beginning our project was just an idea and seemed difficult for it to take form. Each of our team members worked towards making this idea the real and solid project that we now have.
Once our data-science experts Leticia and Paula (one of the members who had to leave the project) got the core functionalities working in python, I started to code with Angular which I previously knew and it seemed just the right thing to do.
After a couple of days I stopped and started all over. Since this is a project for and about learning. I decided that I wanted to try to code for the first time with Express, which is what I learnt on my track, so I could put to practice some of the recent acquired knowledge.
Express is mostly used for building APIs and was fundamental for our project to work, and although It was taught in my back-end learning path, I used express only to code the front-end, because we already had Stephanie M as a our back-end lead who took care of transmitting the data back and forth the python and node apps, and to help me understand and fix the data flow whenever I had problems when creating a new functionality.
Once I got right and practiced all the basics about working with express as a front-end framework, I started to slowly make improvements to the code and apply new functionalities with the “magic” of HTML,CSS and JavaScript working together.
I like to spend my time trying out all kinds of different code, and our project gave me just the perfect challenges for me to explore many of the endless possibilities of JavaScript.
The biggest challenges I had were:
2. Show the response with a special highlighting format meanwhile conserving the original line breaks.
3. Make the original text to stay in the box once the POST request was sent.
4. The random not repeating changing color functionality
5. Transforming the predictor simple form, into the pretty slideshow-like form from the designs
6. Git -> I had to forget about the way I had been using git and GitHub for my personal projects, and learn to work as a part of a team.
In a nutshell, this project has been a real taste of what working as a developer in a team feels like. And all I can say is: I’M READY FOR IT.

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

## Other insights of the project phase
One of the major challenges that I came across what figuring out how to extract data from the python functions. At first, I nested all of the functions in the HTTP routes located in the app.py file. As the functions and dictionaries became more extensive, it became clear that the functions needed to reside in an python file outside of the app.py file that was making the HTTP calls. My challenge here was learning how to put the functions in a new file, and learning how to link the two python files together, as well as extract the correct data for sending to the Express app. </br>
- Image one: how to import certain functions from an outside python file to another.
- Image two: the route for the gender_converter. Here, from the files called gender_function.py, there are two functions that are imported into app.py. The data from the Express app is passed through each function, going from data, to textData, and so on, to finally be returned as text_converted to the Express app. You can refer to the [final working version](# Final-working-version) to explore what happens to the data.

![app_pyimports](https://user-images.githubusercontent.com/60686512/107756991-4132d500-6d25-11eb-89b9-9465ca81ff1f.PNG)
![httpcall](https://user-images.githubusercontent.com/60686512/107757189-85be7080-6d25-11eb-8d32-cc060bc6f962.PNG)

</br>
### Machine learning module
Finally, my last challenge was figuring out how to pass data from user to the machine module and back. Leticia set up the module to accept an array of numbers [1, 1, 1], for example. Three critereas: the news source, the topic, and the authors gender. My challenge was to create a form to return numbers that matched Leticia's machine module. I created a form that returned numbered values (which can be seen in the node_app/public/js/html.js file, under the updatePredictorResultHTML function). </br>
I was able to send to flask an array of three numbers. The challenged I encountered, was that because the array went through the json.loads function, it was turned into a string, instead of array of numbers. So, the array because ['1', '1', '1'], and the machine would not accept this. </br>
After some research I discovered how to transform an array of strings to an array of numbers in python.
- Image one: You can see in the image below, on line 37, the function that casts the variables to integers. This was challenging to figure out the logic and syntax, but again, looking back, it looks very simple. </br>
- Image two: The path in the Express app, that sends an array of data from the user submitted form to Flask. After Flask returns the response from the machine learning module, the response is sent to its corresponding EJS file.
![arraypython](https://user-images.githubusercontent.com/60686512/107758578-61639380-6d27-11eb-96a2-7f3272a1cfa1.PNG)
![indexjsmachine](https://user-images.githubusercontent.com/60686512/107758924-d9ca5480-6d27-11eb-8fe1-80d5143ea9e0.PNG)

## Side notes
Because we lost a DS member of our team, I helped Leticia collect the articles for building our dataset. I started to organize the data into different tables, in hopes to collect more insights into the data for our users. I used SQL in Excel to structure and filter the data. Unfortunately, due to our time constraints and my lack of knowledge in data science, we were not able to use the data that I collected. This data includes all articles filtered by male versus female authors, organized by topics, and defined by what gender the author is writing about. In the future, as we build our data sets, we will also build our data visuals and statistics, to further explore how gender is represented in media.

## Final thoughts
Looking at this code and where I am now with my understanding of it, I am in a much different mindset than when I began. Through this process, I was able to grasp the concept of REST API's and how to pass data through the response and request objects. I am also very thankful to have been able to experiment with python and Flask, as this helped reinforce the different types of REST API frameworks and how to extract and send data from one to the other.

# Data Science
From our first meeting, I could better understand our target and what we wanted from Flip-The-Script. On the same day I started developing a function and doing some research. There were some algorithms related to the subject but as I thought, they covered part of our MVP and not all the requirements.

RegEx was the key in the functions, therefore, I had to learn it. After the first implementations, I realized that the program ran faster and without any problem. Basically the function used a long string as a dictionary and by every match with the text (user input), the function delivered the conversion. This applied morphological and orthographic distinctions, and provided a conversion in accordance to these rules.

The next day I could deliver screenshots to show that it was possible to create a gender converter so with that the other members could start doing their tasks. My first steps in this project were as a Software Developer more than as a Data Scientist.

Following the same line, I started developing the neutral converter and at the same time made the gender converter robuster. Since I took the lead in Software development, a project model was necessary to avoid any inconsistencies. As a beginner, the "Trial and Error" model was the best choice to be implemented and Kanban list was the tool that we used as a group. In order to define my milestones and to show what I was currently doing, I actively used it.

The way of thinking for the neutral converter was different. A switch function was not an option because the conversion didn’t require a reversed feature. Thus, I created a dictionary and developed a function that by every match with the text (user input) delivered a conversion. The complexity of the neutral converter lied in the units, some of the conversion had more than one word so a RegEx pattern was not the best option to be implemented.

Having both converters, the module test phase was the next step. My idea was to use it as a reference for the dictionary articles from well-known news media. From the first samples, the first bugs came to light. There was an issue when the program converted the pronoun "he" or "she" into "they". The verb, which follows, remains the same (3rd person singular). If I would have tried to change every verb, I would have had to create a dictionary with every converted verb.

With the neutral converter, I thought about how to create a data analysis using articles. I found a dataset on Kaggle (article_news.csv) and started using it to get some insights. Nevertheless, the quantity of words of the title and headlines were not enough to give them. Therefore, I started analyzing news articles with at least 200 words and recorded them in my own dataset. I noticed that the most insightful article was a particular case about a person (topic: local news). News articles about politics or health (Covid-19) do not use female or male articles or pronouns to a great extent.

By the end of December, there was a beta version for gender converter (adding new words) and a beta version with disclaimer (verbs - morphological rules) for neutral converter. We decided as a group to not push the dataset on GitHub due to legal terms and added another attribute called "gender_author" to the dataset in order to make a distinction between male and female authors. I set a milestone, that by January 17 a hundred analyzed articles should be included in the dataset. In connection with Linguistics, I started documenting the most significant conversions included in the dictionaries so this page should be included as "References" on the website.

In early January I defined the three main attributes, which should be used for prediction (Machine Learning):

*Sources: 'abc news', 'al jazeera', 'bbc news', 'cnbc', 'cnn', 'deutsche welle', 'newsweek', 'npr', 'reuters', 'science', 'the irish times', 'the new york times'*

*Topics: 'business', 'culture', 'food and drinks', 'health', 'local news', 'people', 'politics', 'social science', 'sports', 'technology', 'travel', 'world'*

*Author's Gender: 'male', 'female', 'none'*

I used the Counter library, created another functions for text analysis and categorized the units, which were converted, grammatically into ten groups:

1. *'female personal pronoun (she)',*
2. *'male personal pronoun (he)',*
3. *'feminine determiners (her, herself)',*
4. *'masculine determiners (him, his, himself)',*
5. *'masculine nouns',*
6. *'femenine nouns',*
7. *'adjectives with masculine connotation',*
8. *'adjectives with femenine connotation',*
9. *'male title',*
10. *'female title'.*

I registered in the dataset: the number of words per article, the number of words converted, the number of words converted as per grammatical and morphological category, a list with the words converted, and six lists with words converted to analyze possible bias according to the following categories: *'masculine nouns', 'femenine nouns', 'adjectives with masculine connotation', 'adjectives with femenine connotation', 'male title', 'female title'*.

After reaching 100 analyzed articles, I started plotting. For this purpose, I used Streamlit in order to see all the data and get insights. With the first plots, I explained the insights to front end since they were in charge of plotting graphics for the website. However, the first insights were used as a reference since the 100 articles represented only 37% of total analysis.

In late January I completed the analysis of 276 articles, the dataset was done. In this way, I could finish my plots for machine learning and some of them are similar to the following ones:

   ![plots](https://user-images.githubusercontent.com/73216174/107207077-264c2200-6a00-11eb-81c4-570a762e7bad.png)

The next step was to develop a prediction using an algorithm from scikitlearn. Due to the nature of the dataset "categorical data", I decided on using KNeighbors. All the steps I took were through troubleshooting. I created another csv file, where I labeled every article according to some parameters that I established. Mean() was the key function for every calculation and after getting these values, I crossed information according to three attributes: Topic, Source and Global mean (all articles). The labels were established as below:

*Non-biased: Equal to 0,*

*Slightly biased: More than 0 and less than the mean value,*

*Biased: Equal to or more than the mean value.*

After comparing the three labels from the three aforementioned attributes, I assigned one unique label, which summarized the other three and was the most frequently occurring label.

Having this labeled csv file, I got many errors related to the type of data when creating the model. Then I used KNeighbors from scratch (euclidean distance) and successfully got predictions. As our mentor recommended me, I tried once again with scikitlearn and I could successfully get predictions with the following scores:

*Accuracy of test set: 0.51*

*Accuracy of training set: 0.41*

*Accuracy of set: 0.48*

The dataset didn’t have enough attributes in order to increase accuracy. At the beginning, my model had a 63% accuracy without splitting data into train and test. Nevertheless, when I talked about the model in the weekly meeting, as a group we decided to add two extra options for author's gender: "non-binary" and "I don't know", which were summarized in "none". There are few articles in the dataset, which don't include gender. In this way, the model must predict data that doesn't exist in the dataset. Splitting was a must. I tuned the model with: StandardScale(), GridSearchCV(), which resulted in:

*Best leaf_size: 1*

*Best p: 1*

*Best n_neighbors: 15*

Finally I used the library Pickle in order to save the model as a sav file and implement it in production.

The estimates delivered by the algorithm should be used as a reference since the dataset is not large enough to set a precedent. The research consisting of: 276 articles from 12 sources about 12 topics most of them published between December 2020 and the first week of February 2021, can give an insight that gendered language does exist in the media and varies according to source, topic and author's gender. Future studies and extension of the dataset will help the algorithm to be robust and a link between the neutral converter and the model could provide a direct bias prediction with higher accuracy using units converted and categories.

These softwares together with the algorithm were intended to encourage users to reflect about these questions.

Gender converter:

* Does the reversed text show a difference in relation to the original one? Does the meaning change? (semantic differences)

Neutral converter:

* Does the meaning of the text change when using the software? (semantic and morphosyntactic differences)
* Is it necessary to define the gender of a person through pronouns, nouns, determiners, titles, etc. in a text?
* Is it necessary to define the gender of an expression through adverbs or adjectives in a text?

Model:

* Is there a reason why the media use certain words instead of neutral options?
* Do topics or the author's gender have an influence on how articles are written?

# UX

# Conclusion
