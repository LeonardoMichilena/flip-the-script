function updateNavbarHTML(){

    document.getElementById("navbar").innerHTML = `
    <div class="logo-container" id="logo-container">
      <svg onclick="setNewColor()" id="logo" width="50" height="50" viewBox="0 0 50 50" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle r="23" transform="matrix(-1 0 0 1 25 25)" stroke="${currentMainColor}" stroke-width="4" />
        <path d="M14.4504 25.0336C14.4504 30.8414 19.1586 35.5496 24.9664 35.5496C30.7742 35.5496 35.4824 30.8414 35.4824 25.0336C35.4824 19.2258 30.7742 14.5176 24.9664 14.5176C19.1586 14.5176 14.4504 19.2258 14.4504 25.0336Z"
          stroke="${currentMainColor}" stroke-width="3" />
        <path d="M32.0426 8.48049L28.4718 13.7708L26.7337 13.9185L25.0333 13.6478L27.735 10.2521L30.1401 7.20951L30.4739 7.00925L30.6741 6.94249L30.8744 6.87574L31.0747 6.84236L31.3083 6.80898L31.542 6.84236L31.7781 6.9057L31.9091 7.076L31.9759 7.24289L32.0426 7.47654L32.076 7.64343L32.1094 7.87707V8.07734V8.17747V8.2776L32.076 8.37774L32.0426 8.48049Z"
          fill="${currentMainColor}" stroke="${currentMainColor}" />
        <path d="M17.557 41.4858L21.1278 36.1955L22.866 36.0479L24.5663 36.3185L21.8646 39.7142L19.4595 42.7568L19.1257 42.9571L18.9255 43.0238L18.7252 43.0906L18.5249 43.124L18.2913 43.1573L18.0577 43.124L17.8215 43.0606L17.6905 42.8903L17.6237 42.7234L17.557 42.4898L17.5236 42.3229L17.4902 42.0892V41.889V41.7888V41.6887L17.5236 41.5886L17.557 41.4858Z"
          fill="${currentMainColor}" stroke="${currentMainColor}" />
        <rect width="2.73698" height="9.21228" transform="matrix(-1 0 0 1 26.3687 10.3472)" fill="#EDEEEF" />
        <rect width="2.73698" height="9.21228" transform="matrix(-1 0 0 1 26.3687 31.4419)" fill="#F5F5F5" />
      </svg>
      <a class="title" href="/">Flip The Script</a>
    </div>
    <div class="list-container">
      <ul class="list">
  
        <li>
          <a href="/#why">Why It Matters</a>
        </li>
        <li>
          <a href="/#statistics">Statistics</a>
        </li>
        <li>
          <a href="/#predictor">Predictor</a>
        </li>
        <li>
          <a href="/#about">About Us</a>
        </li>
        <li>
          <a class="btn-start" style="background-color: ${currentMainColor};" href="/flip">Start Now</a>
        </li>
      </ul>
    </div>`;
}

function updateIntroHTML(){
    document.getElementById("intro").innerHTML = ` <h1>We Care About A Fair <span style="color: ${currentMainColor};">World</span></h1>
    <p>Creating Gender Neutral Texts</p>    
    <a class="btn-flip" style="background-color: ${currentMainColor};" href="/flip">Create Your Text Now</a>`;
}

function updateWhyHTML(){
    document.getElementById('why').innerHTML = ` <div id="title-container" class="text one slideshow-closed">
    <div class="why-titles">
      <h2 id="title1">Words form thoughts, </h2>
      <h2 id="title2"> and thoughts form words.</h2>
    </div>
    <p class="why-subtitle">imagine the following scenario:</p>
  </div>
  <div id="slideshow-box" class="slideshow-box-closed" onclick="toggleSlideshow('open')">
    ${insertSLideshowHTML()}
  </div>`;
}

function insertSLideshowHTML(){
    return `
    <!-- Slideshow container -->
    <div id="slideshow-container">
        <ul id="slideshow-list" style="background-color: ${convertHexToRGBA(currentSecondColor,0.5)};">

            <!-- Full-width images with number and caption text -->
            <li class="slide showing" onclick="nextSlide()">
                <div class="quotes-container">
                    <div class="quotes start">“</div>
                    <div class="text-in-quotes">
                        <p>A father and a son are in a horrible car crash that kills the dad. The son
                        is rushed to the hospital, just as he is about to go under the knife, the surgeon says: I can't operate,
                        that boy is my son!</p>
                    </div>
                    <div class="quotes end">”</div>
                </div>
            </li>
            <li class="slide" onclick="nextSlide()">
                <div>
                    <h1>How is this possible?</h1>
                </div>
            </li>

            <li class="slide" onclick="nextSlide()">
                <div>
                    <h3><span style="color: ${currentMainColor};">86% of people</span> didn't consider the surgeon was a <span style="color: ${currentMainColor};">woman</span></h3>
                </div>
            </li>

            <li class="slide" onclick="nextSlide()">
                <div>
                    <h3>Here's why</h3>
                    <div class="quotes-container">
                    <div class="quotes start">“</div>
                    <div class="text-in-quotes">
                        <p>A father and a son are in a horrible car crash that kills the dad. The son
                        is rushed to the hospital, just as he is about to go under the knife, the surgeon says: I can't operate,
                        that boy is my son!</p>
                    </div>
                    <div class="quotes end">”</div>
                </div>
                    <h3>7 Male pronouns</h3>
                    <h3>1 Neutral pronoun</h3>
                    <h3>0 Female pronouns</h3>

                </div>
            </li>
            <li class="slide" onclick="nextSlide()">
                <div>
                    <h3>What about this</h3>
                    <div class="quotes-container">
                        <div class="quotes start">“</div>
                        <div class="text-in-quotes">
                            <p>A father and daughter are in a horrible car crash that kills the dad. The
                            daughter is rushed to the hospital, just as she’s about to go under the knife, the surgeon says, I can’t
                            operate, that girl is my daughter!</p>
                        </div>
                        <div class="quotes end">”</div>
                    </div>
                    <h4>4 Male pronouns</h4>
                    <h4>1 Neutral pronoun</h4>
                    <h4>3 Female pronouns</h4>
                </div>
            </li>
            <li class="slide" onclick="nextSlide()">
                <div>
                    <h3>What about this</h3>
                    <p>adding less than half of female pronouns allows 24% more people to get it right.
                    </p>
                </div>
            </li>
            <li class="slide" onclick="nextSlide(); toggleSlideshow('close')">
                <div>
                    <p><a href="/why-it-matters#video-section">Learn more</a> on why this matters. </p>
                </div>
            </li>
        </ul>
        <div id="dot-container" style="text-align:center">
            <span class="dot active" onclick="currentSlide(0)"></span>
            <span class="dot" onclick="currentSlide(1)"></span>
            <span class="dot" onclick="currentSlide(2)"></span>
            <span class="dot" onclick="currentSlide(3)"></span>
            <span class="dot" onclick="currentSlide(4)"></span>
            <span class="dot" onclick="currentSlide(5)"></span>
            <span class="dot" onclick="currentSlide(6)"></span>
        </div>
    </div>`;
}

function updateStatisticsHTML(){
    document.getElementById('statistics').innerHTML = `<div class="part-one">
    <h1 style="color: ${currentMainColor};">Numbers,</h1>
    <p style="color: ${currentMainColor};">numbers</p>
</div>`;
}

function updateDidYouKnow(){


}