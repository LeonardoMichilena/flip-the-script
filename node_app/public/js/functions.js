let originalText;
let responseText;
let responseArray;
let flippedWords;
let flippedWordsArray;


function init(){

    originalText = document.getElementById('newArticle').value;
    
    if( document.getElementById('response-text') != null)     {
        responseText = document.getElementById('response-text').innerText;
        responseArray = responseText.split(" ");

        flippedWords = document.getElementById('flipped-words').innerText;
        flippedWordsArray = flippedWords.split(",");

        cleanFLippedWordsArray();

        if(responseText){
            addHTMLResponse();
        }
    }

}

function cleanFLippedWordsArray(){
    for(i=0; i<flippedWordsArray.length;i++){
        if(flippedWordsArray[i].length <= 1) flippedWordsArray.splice(i,1);
    }
}

function addHTMLResponse() {

    let responseBox = document.getElementById("response-box");
    let k;
    
    for(i=0;i<responseArray.length;i++){
       for(j=0;j<flippedWordsArray.length;j++){
           k =j;
            if(checkForMatchingWord(i,j)){
                responseBox.innerHTML += `<span class="pinky"> ${responseArray[i]} </span> `;
                break;
            }
       }
       if(!checkForMatchingWord(i,k))responseBox.innerHTML += `<span> ${responseArray[i]} </span> `;
    }
} 

function checkForMatchingWord(i,j){

    if(responseArray[i].search(flippedWordsArray[j]) == 0) {
       //Checks for an equal length or +1 (punctuation mark) an returns true
        if(responseArray[i].length == flippedWordsArray[j].length) return true;
        else  if(responseArray[i].length == flippedWordsArray[j].length+1) return true;
        else false;
    } else false;
}