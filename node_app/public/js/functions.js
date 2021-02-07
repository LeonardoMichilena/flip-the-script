
///////////////Response array and hightligh 

//Variables
let originalText;
let responseText;
let responseArrayPar;
let responseArray;
let flippedWords;
let flippedWordsArray;



/**
 * Executes automatically once the page is loaded (body > onload atributte)
 */
function initHome() {


    updateNavbarHTML();
    updateIntroHTML();
    updateStatisticsHTML();
    updateWhyHTML();
    updateFooterHTML();


    drawCanvas();
}
function initWhy() {
    updateNavbarHTML();
    updateWhyHTML();
    updateFooterHTML();

}

function initStatistics() {
    updateNavbarHTML();
    updateStatisticsHTML();
    updateFooterHTML();
    drawCanvas();

}
function initPredictor() {

    updateNavbarHTML();
    document.getElementById('predictor-section').style.backgroundColor = currentSecondColor;
    updateFooterHTML();

}

function initAbout(){
    updateNavbarHTML();
    updateAboutHTML();
    updateFooterHTML();
}

function initFlip() {

    updateNavbarHTML();


    //Checks if the response box is not empty and executes the code
    if (document.getElementById('response-text') != null) {

        //Gets the original text from the Post request response (firstArticle)
        originalText = document.getElementById('newArticle').value;

        //Gets the converted text from the Post request response (response)
        responseText = document.getElementById('response-text').innerText;

        //Splits the responseText into an array separating it by every line break "\n" found
        responseArrayPar = responseText.split("\n");

        //Splits the each responseArrayPar items into another array separating it by every empty space found
        for (i = 0; i < responseArrayPar.length; i++) {
            responseArrayPar[i] = responseArrayPar[i].split(" ");
        }

        //Gets the flipped words text from the Post request response (flippedArray)
        flippedWords = document.getElementById('flipped-words').innerText;

        //Splits the flippedWords text into an array separating it by every comma "," found
        flippedWordsArray = flippedWords.split(",");

        //Cleans empty spaces in the flippedWordsArray
        cleanFLippedWordsArray();

        if (responseText) {
            addHTMLResponse();
        }
    }

}

/**
 *  When separating the flippedWords by every ",", there were sometimes empty indexes in the 
 * array made when the split method finds two commas ",,", so that needed to be gone with this function
 */
function cleanFLippedWordsArray() {
    for (i = 0; i < flippedWordsArray.length; i++) {
        if (flippedWordsArray[i].length <= 1) flippedWordsArray.splice(i, 1);
    }
}

/**
 * The HTML that will appear as a response on the front end response's box
 */
function addHTMLResponse() {

    //Selects the response-box 
    let responseBox = document.getElementById("response-box");

    let k;

    //Checks if first the i word from the responseArray is similar to any of the words in the flippedWordsArray
    for (l = 0; l < responseArrayPar.length; l++) {
        // responseBox.innerHTML += `<p>`;
        for (i = 0; i < responseArrayPar[l].length; i++) { //here the responseArrayPar[l] will start looping
            for (j = 0; j < flippedWordsArray.length; j++) { //here that word will loop to check every word inside the flippedWordsArray[j]
                k = j; //Asings the j value to the k, to not lose it when finishing the loop

                //Checks if the word is matching to execute the code
                if (checkForMatchingWord(l, i, j)) {
                    // Applies special HTML and adds up to the innerHTML from the response box and then ends the loop
                    responseBox.innerHTML += `<span style="color: ${currentThirdColor}"> ${responseArrayPar[l][i]} </span>`;
                    break;
                }
            }
            //When first loop (j) is finished, checks if the word was not a match and applies normal HTML and adds it up to the response's box
            if (!checkForMatchingWord(l, i, k)) responseBox.innerHTML += `<span> ${responseArrayPar[l][i]} </span>`;
        }
        responseBox.innerHTML += `<br>`;
    }

}

/**
 * Checks if the word of the first array[i] matches with the word form the other array[j]
 * @param {number} l index of the responseArray 
 * @param {number} i index of the flippedWordsArray
  * @param {number} j index of the flippedWordsArray
 */
function checkForMatchingWord(l, i, j) {

    //Searches if the word is found inside the other word, if yes, returns 0. And the code will be executed otherwise returns false
    if (responseArrayPar[l][i].search(flippedWordsArray[j]) == 0) {
        //Checks for an equal length or +1 (punctuation mark) an returns true, if not then returns false
        // (for Example by words that contain the first word but is part of a larger word (like man and manual))
        if (responseArrayPar[l][i].length == flippedWordsArray[j].length) return true;
        else if (responseArrayPar[l][i].length == flippedWordsArray[j].length + 1) return true;
        else false;
    } else false;
}

///////////////Slideshow

//Variables
let totalSlides = 7;
let slideCounter = 0;

/**
 * Toggles the slideshow to open and close
 * @param {string} mode: this should be "open" or "close"
 */
function toggleSlideshow(mode) {

    //Get both elements of the section in order to manipulate them later
    let titleBox = document.getElementById('title-container');
    let slideShowBox = document.getElementById('slideshow-box');
    let title1 = document.querySelector("#title1");
    let title2 = document.querySelector("#title2");



    //If the mode "open" was passed to the function then this code will execute
    if (mode == 'open') {
        //Deletes the onclick atributte so it doesn't interfere with the slideshow
        document.getElementById('slideshow-box').removeAttribute('onclick');

        //Deletes the closed classes and adds the open classes
        titleBox.classList.toggle('slideshow-closed');
        slideShowBox.classList.toggle('slideshow-box-closed');

        title1.classList.toggle('title-shrink');
        title2.classList.toggle('title-shrink');


        titleBox.classList.toggle('slideshow-open');
        slideShowBox.classList.toggle('slideshow-box-open');
    }

    //If the mode "close" was passed to the function then this code will execute
    if (mode == "close") {
        //Deletes the open classes and adds the closed classes
        titleBox.classList.toggle('slideshow-open');
        slideShowBox.classList.toggle('slideshow-box-open');
        titleBox.classList.toggle('slideshow-closed');
        slideShowBox.classList.toggle('slideshow-box-closed');

        title1.classList.toggle('title-shrink');
        title2.classList.toggle('title-shrink');


        //Sets the onclick atributte after the animation is closed, so we can start over
        setTimeout(function () { document.getElementById('slideshow-box').setAttribute("onclick", "toggleSlideshow('open')"); }, 200);
    }

}

/**
 * Changes to the next slide
 */
function nextSlide() {

    //Sets the current slide and dot given the global slideCounter variable
    let currentSlide = document.querySelectorAll('#slideshow-container .slide')[slideCounter];
    let currentDot = document.querySelectorAll('#dot-container .dot')[slideCounter];

    //Toggles the classes for the slide and dots to not be the current anymore
    currentSlide.classList.toggle('showing');
    currentDot.classList.toggle("active");

    //Sets the slideCounter on the next slide available, if it's the last slide, starts from the beginning
    slideCounter = (slideCounter + 1) % totalSlides;

    //Sets the new current slide and dot
    currentSlide = document.querySelectorAll('#slideshow-container .slide')[slideCounter];
    currentDot = document.querySelectorAll('#dot-container .dot')[slideCounter];

    //Togggles the classes to be the current or active slides
    currentSlide.classList.toggle('showing');
    currentDot.classList.toggle("active");

}



///////////////Send post on textarea Onchange


function toggleConverter(mode) {

    if (mode == "reverse") {

    } else if (mode == "neutral") {

    }
}

/////////////////Color change

let backgroundColor = "f5f5f5";
let darkColor = "121212";

let mainColors = ["#FF83A8", "#76EEC6", "#FFCC00", "#9966FF", "#6699FF", "#F57B7B", "#33CCCC"];
let secondColors = ["#F8D2EB", "#A0E1BA", "#FCE68E", "#C3B1E9", "#A5C9FF", "#FFB2B2", "#91DCDC"];
let thirdColors = ["#F5428D", "#35E9AD", "#E5B800", "#7530FF", "#3E7DFB", "#FF6666", "#3BBBBF"];

let colorCounter = Math.floor(Math.random() * 7);

let currentMainColor = mainColors[colorCounter];
let currentSecondColor = secondColors[colorCounter];
let currentThirdColor = thirdColors[colorCounter];

/**
 * Returns a random number that is different to the actual number between 0-6
 * @param {number} a Number to be compared with the next random
 */
function nextRandomNum(a) {
    let randomNum = Math.floor(Math.random() * 7);
    console.log(a, randomNum);
    if (randomNum != a) {
        colorCounter = randomNum;
    } else nextRandomNum(a);
}
/**
 * Changes the color palette to a new color form the 3 colors arrays
 */
function setNewColor() {

    //Sets a new random number(color)
    nextRandomNum(colorCounter);

    currentMainColor = mainColors[colorCounter];
    currentSecondColor = secondColors[colorCounter];
    currentThirdColor = thirdColors[colorCounter];

    let pathName = document.location.pathname;

    console.log(pathName);

    if (pathName == "/flip") {
        initFlip();
    } else if (pathName == "/why-it-matters") {
        initWhy();
    } else if (pathName == "/statistics") {
        initStatistics();
    } else if (pathName == "/predictor") {
        initPredictor();
    } else if (pathName == "/") {
        initHome();
    }

}




function convertHexToRGBA(hex, alpha) {
    let c;
    if (/^#([A-Fa-f0-9]{3}){1,2}$/.test(hex)) {
        c = hex.substring(1).split('');
        if (c.length == 3) {
            c = [c[0], c[0], c[1], c[1], c[2], c[2]];
        }
        c = '0x' + c.join('');
        return 'rgba(' + [(c >> 16) & 255, (c >> 8) & 255, c & 255].join(',') + ',' + alpha + ')';
    }
}



/////Statistics charts

//variables

let ctx;
let myChart;


function drawCanvas() {

    ctx1 = document.getElementById('myChartDoughnut').getContext('2d');

    myChartDoughnut = new Chart(ctx1, {
        type: 'doughnut',
        data: {
            labels: ['Male converted words', 'Female converted words'],
            datasets: [{
                label: '% of converted words by gender neutralizer',
                data: [65, 35],
                backgroundColor: [
                    currentMainColor,
                    convertHexToRGBA(currentSecondColor, 0.5)
                ]
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    display: false,
                }],
                yAxes: [{
                    display: false,
                }],
            },
            animation: {
                duration: 4000,
            }
        }
    });

    ctx2 = document.getElementById('myChartBars').getContext('2d');

    myChartBars = new Chart(ctx2, {
        type: 'horizontalBar',
        data: {
            labels: ["Male personal pronouns","Masculine determiners","Female personal pronouns","Masculine nouns","Femenine determiners","Femenine nouns","Male titles","Adjectives with female connotation","Female titles","Adjectives with male connotation"],
            datasets: [{
                label: 'Ratio of words converted from all articles',
                data: [3,2.1,1.5,1.1,0.9,0.9,0.3,0.1,0.1,0.02],
                    backgroundColor: [
                    currentMainColor,
                    currentMainColor,
                    convertHexToRGBA(currentSecondColor, 0.5),
                    currentMainColor,
                    convertHexToRGBA(currentSecondColor, 0.5),
                    convertHexToRGBA(currentSecondColor, 0.5),
                    currentMainColor,
                    convertHexToRGBA(currentSecondColor, 0.5),
                    convertHexToRGBA(currentSecondColor, 0.5),
                    currentMainColor
                ]
            }]
        },
        options: {
            scales: {
                xAxes: [{
                }],
                yAxes: [{
                }],
            },
            animation: {
                duration: 5000,
            }
        }
    });

} 