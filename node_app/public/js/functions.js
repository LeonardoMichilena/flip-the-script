
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
function init(){

    //Checks if the response box is not empty and executes the code
    if( document.getElementById('response-text') != null)     {

        //Gets the original text from the Post request response (firstArticle)
        originalText = document.getElementById('newArticle').value;

        //Gets the converted text from the Post request response (response)
        responseText = document.getElementById('response-text').innerText;

        //Splits the responseText into an array separating it by every line break "\n" found
        responseArrayPar = responseText.split("\n");

        //Splits the each responseArrayPar items into another array separating it by every empty space found
        for(i=0;i<responseArrayPar.length;i++){
            responseArrayPar[i] = responseArrayPar[i].split(" ");
        }
        
        //Gets the flipped words text from the Post request response (flippedArray)
        flippedWords = document.getElementById('flipped-words').innerText;
        
        //Splits the flippedWords text into an array separating it by every comma "," found
        flippedWordsArray = flippedWords.split(",");

        //Cleans empty spaces in the flippedWordsArray
        cleanFLippedWordsArray();

        if(responseText){
            addHTMLResponse();
        }
    }

}

/**
 *  When separating the flippedWords by every ",", there were sometimes empty indexes in the 
 * array made when the split method finds two commas ",,", so that needed to be gone with this function
 */
function cleanFLippedWordsArray(){
    for(i=0; i<flippedWordsArray.length;i++){
        if(flippedWordsArray[i].length <= 1) flippedWordsArray.splice(i,1);
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
    for(l=0;l<responseArrayPar.length;l++){
       // responseBox.innerHTML += `<p>`;
        for(i=0;i<responseArrayPar[l].length;i++){ //here the responseArrayPar[l] will start looping
            for(j=0;j<flippedWordsArray.length;j++){ //here that word will loop to check every word inside the flippedWordsArray[j]
                k =j; //Asings the j value to the k, to not lose it when finishing the loop
     
                //Checks if the word is matching to execute the code
                 if(checkForMatchingWord(l,i,j)){
                     // Applies special HTML and adds up to the innerHTML from the response box and then ends the loop
                     responseBox.innerHTML += `<span class="pinky"> ${responseArrayPar[l][i]} </span>`;
                     break;
                 }
            }
            //When first loop (j) is finished, checks if the word was not a match and applies normal HTML and adds it up to the response's box
            if(!checkForMatchingWord(l,i,k)) responseBox.innerHTML += `<span> ${responseArrayPar[l][i]} </span>`;
         }
        responseBox.innerHTML += `<br>`;
    }
   
} 

/**
 * Checks if the word of the first array[i] matches with word form the other array[j]
 * @param {number} l index of the responseArray 
 * @param {number} i index of the flippedWordsArray
  * @param {number} j index of the flippedWordsArray
 */
function checkForMatchingWord(l,i,j){

    //Searches if the word is found inside the other word, if yes, returns 0. And the code will be executed otherwise returns false
    if(responseArrayPar[l][i].search(flippedWordsArray[j]) == 0) {
       //Checks for an equal length or +1 (punctuation mark) an returns true, if not then returns false
       // (for Example by words that contain the first word but is part of a larger word (like man and manual))
        if(responseArrayPar[l][i].length == flippedWordsArray[j].length) return true;
        else  if(responseArrayPar[l][i].length == flippedWordsArray[j].length+1) return true;
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
function toggleSlideshow(mode){

    //Get both elements of the section in order to manipulate them later
    let titleBox = document.getElementById('title-container');
    let slideShowBox = document.getElementById('slideshow-box');
    let title1 = document.querySelector("#title1");
    let title2 = document.querySelector("#title2");



    //If the mode "open" was passed to the function then this code will execute
    if(mode =='open') {
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
    if(mode == "close") {
        //Deletes the open classes and adds the closed classes
        titleBox.classList.toggle('slideshow-open');
        slideShowBox.classList.toggle('slideshow-box-open');
        titleBox.classList.toggle('slideshow-closed');
        slideShowBox.classList.toggle('slideshow-box-closed');

        title1.classList.toggle('title-shrink');
        title2.classList.toggle('title-shrink');


        //Sets the onclick atributte after the animation is closed, so we can start over
        setTimeout(function(){document.getElementById('slideshow-box').setAttribute("onclick","toggleSlideshow('open')");},200);
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
    currentSlide.className = 'slide';
    currentDot.classList.toggle("active");

    //Sets the slideCounter on the next slide available, if it's the last slide, starts from the beginning
    slideCounter = (slideCounter+1)%totalSlides;

    //Sets the new current slide and dot
    currentSlide = document.querySelectorAll('#slideshow-container .slide')[slideCounter];
    currentDot = document.querySelectorAll('#dot-container .dot')[slideCounter];

    //Togggles the classes to be the current or active slides
    currentSlide.className = 'slide showing';
    currentDot.classList.toggle("active");

}



///////////////Send post on Change


function toggleConverter(mode){

    if(mode == "reverse"){

    }else if(mode == "neutral"){

    }


}
