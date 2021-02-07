function updateNavbarHTML() {

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
          <a href="/why-it-matters">Why It Matters</a>
        </li>
        <li>
          <a href="/statistics">Statistics</a>
        </li>
        <li>
          <a href="/predictor">Predictor</a>
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

function updateIntroHTML() {
    document.getElementById("intro").innerHTML = ` <h1>We Care About A Fair <span style="color: ${currentMainColor};">World</span></h1>
    <p>Creating Gender Neutral Texts</p>    
    <a class="btn-flip" style="background-color: ${currentMainColor};" href="/flip">Create Your Text Now</a>`;
}

function updateWhyHTML() {
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

function insertSLideshowHTML() {
    return `
    <!-- Slideshow container -->
    <div id="slideshow-container">
        <ul id="slideshow-list" style="background-color: ${convertHexToRGBA(currentSecondColor, 0.5)};">

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
            <li class="slide two" onclick="nextSlide()">
                <div>
                    <h1>How is this possible?</h1>
                </div>
            </li>

            <li class="slide three" onclick="nextSlide()">
                <div>
                    <h3><span style="color: ${currentThirdColor};">86% of people</span> didn't consider the surgeon was a <span style="color: ${currentThirdColor};">woman</span></h3>
                </div>
            </li>

            <li class="slide four" onclick="nextSlide()">
                <h3>Here's why</h3>
                <div class="quotes-container">
                    <div class="quotes start">“</div>
                    <div class="text-in-quotes">
                        <p>A <span style="color: ${currentThirdColor};">father</span> and <span style="color: ${currentThirdColor};">son</span> are in a horrible car crash that kills the <span style="color: ${currentThirdColor};">dad</span>. The <span style="color: ${currentThirdColor};">son</span>
                        is rushed to the hospital, just as <span style="color: ${currentThirdColor};">he's</span> about to go under the knife, the surgeon says: I can't operate,
                        that <span style="color: ${currentThirdColor};">boy</span> is my <span style="color: ${currentThirdColor};">son</span>!</p>
                    </div>
                    <div class="quotes end">”</div>
                </div>
                <div>
                    <h3>7 Male pronouns</h3>
                    <h3><span style="color: ${currentThirdColor};">1</span> Neutral pronoun</h3>
                    <h3><span style="color: ${currentThirdColor};">0</span> Female pronouns</h3>
                </div>
            </li>
            <li class="slide five" onclick="nextSlide()">
                <h3>What about this...</h3>
                <div class="quotes-container">
                    <div class="quotes start">“</div>
                    <div class="text-in-quotes">
                        <p>A father and <span style="color: ${currentThirdColor};">daughter</span> are in a horrible car crash that kills the dad. The
                        <span style="color: ${currentThirdColor};">daughter</span> is rushed to the hospital, just as <span style="color: ${currentThirdColor};">she’s</span> about to go under the knife, the surgeon says, I can’t
                        operate, that <span style="color: ${currentThirdColor};">girl</span> is my <span style="color: ${currentThirdColor};">daughter</span>!</p>
                    </div>
                    <div class="quotes end">”</div>
                </div>
                <div>
                    <h4>4 Male pronouns</h4>
                    <h4><span style="color: ${currentThirdColor};">1</span> Neutral pronoun</h4>
                    <h4><span style="color: ${currentThirdColor};">3</span> Female pronouns</h4>
                </div>
            </li>
            <li class="slide six" onclick="nextSlide()">
                <div>
                    <h3>Adding less than half of female pronouns allows <span style="color: ${currentThirdColor};">24% more people</span> to get it right.</h3>
                </div>
            </li>
            <li class="slide seven" onclick="nextSlide(); toggleSlideshow('close')">
                <div>
                    <h3><a href="/why-it-matters#video-section" style="text-decoration-color: ${currentThirdColor};"><span style="color: ${currentThirdColor};">Learn more</span></a> on why this matters. </h3>
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

function updateStatisticsHTML() {
    document.getElementById('statistics').innerHTML = `
    <div class="title">
        <h1 style="color: ${currentMainColor};">Numbers,</h1>
        <p style="color: ${currentMainColor};">numbers</p>
    </div>
    <div class="statistics-content">
        <div class="charts-area">
            <canvas id="myChartDoughnut"></canvas>
            <canvas id="myChartBars"></canvas>
        </div>
        <div class="text-area">
            <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Rem perspiciatis at labore doloremque ex in consectetur voluptate eligendi sint distinctio illo quaerat incidunt, dolore vel repellendus aliquid voluptatibus saepe ullam.</p>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis rerum quam est recusandae? Ducimus at nobis sapiente quaerat, quam rerum laborum temporibus ea explicabo a tempora! Dolor sequi quae quod.</p>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis rerum quam est recusandae? Ducimus at nobis sapiente quaerat, quam rerum laborum temporibus ea explicabo a tempora! Dolor sequi quae quod.</p>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis rerum quam est recusandae? Ducimus at nobis sapiente quaerat, quam rerum laborum temporibus ea explicabo a tempora! Dolor sequi quae quod.</p>
            <a class="btn-learn-more" style="background-color: ${currentMainColor};" href="/statistics">Learn More</a>
        </div>
    </div>  
    `;
}

function updateDidYouKnow() {


}

function updatePredictorHTML(){
    document.getElementById('predictor-section').style.backgroundColor = convertHexToRGBA(currentThirdColor,0.5);
    document.getElementById('predictor-section').innerHTML = `
    <form method="POST">

    <div class="predictor-slideshow">
        <ul class="predictor-slideshow-list">
            <li class="predictor-slide showing">
                <h1>Predictions, Predictions</h1>
                <p>to know how likely it is that an article is gender biased, please select the source:
                </p>
                <div class="source-container">
                    <label for="source"></label>
                    <select class="form-select" aria-label="Default" name="source" id="source">
                        <option value="1">ABC News</option>
                        <option value="2">Al Jazeera</option>
                        <option value="3">BBC news</option>
                        <option value="4">CNN</option>
                        <option value="5">Deutsche Welle</option>
                        <option value="6">Newsweek</option>
                        <option value="7">Reuters</option>
                        <option value="8">The Irish Times</option>
                        <option value="9">The New York Times</option>
                        <option value="10">Science Mag</option>
                        <option value="11">CNBC</option>
                        <option value="12">NPR</option>
                    </select>
                </div>
                <button style="background-color:${currentMainColor}" class="btn-next" type="button" onclick="predictorNextSlide()">Next</button>

            </li>
            <li class="predictor-slide">
                <h1>What's The Topic Of The Article?</h1>
                <div class="topic-container">
                    <label for="topic"></label>
                    <select name="topic" id="topic">
                        <option value="1">Business</option>
                        <option value="2">Culture</option>
                        <option value="3">Food and Drinks</option>
                        <option value="4">Health</option>
                        <option value="5">Local News</option>
                        <option value="6">People</option>
                        <option value="7">Politics</option>
                        <option value="8">Sports</option>
                        <option value="9">Technology</option>
                        <option value="10">Travel</option>
                        <option value="11">World</option>
                        <option value="12">Social Science</option>
                    </select>
                </div>
                <button class="btn-next" style="background-color:${currentMainColor}" type="button" onclick="predictorNextSlide()">Next</button>

            </li>
            <li class="predictor-slide">
                <h1>What's The Gender Of The Author?</h1>
                <!-- <div class="gender-container">
                    <button class="btn-next" name="sex" style="background-color:${currentMainColor}" type="submit" formaction="/neutralarticle" onclick="predictorNextSlide()">Female</button>
                    <button class="btn-next" name="sex" style="background-color:${currentMainColor}" type="submit" formaction="/neutralarticle" onclick="predictorNextSlide()">Male</button>
                    <button class="btn-next" style="background-color:${currentMainColor}" type="submit" formaction="/neutralarticle" onclick="predictorNextSlide()">Non-Binary</button>
                    <button class="btn-next" style="background-color:${currentMainColor}" type="submit" formaction="/neutralarticle" onclick="predictorNextSlide()">Unknown</button>
                </div> -->
                <div class="gender-container">
                    <input type="radio" id="male" name="sex" value="0">
                    <label for="male">Male</label> 
                    <input type="radio" id="female" name="sex" value="1">
                    <label for="female">Female</label>
                </div>
                <button class="btn-skip" type="submit" onclick="predictorNextSlide()" formaction="/neutralarticle"><span style="color:${currentThirdColor}">Check the results</span></button>
            </li>
            <li class="predictor-slide">
                <h1>The Predictor says this article might be:</h1>
                <div class="response-container">
                </div>
                <a class="btn-next" href="/predictor"><span style="color:${currentThirdColor}">New Prediction</span></a>
            </li>
        </ul>
    </div>
</form>
    `;

}

function updateAboutHTML() {}

function updateTeamHTML() {}

function updateFooterHTML(){
    document.getElementById('footer').innerHTML = `
    <div class="footer-main-container" style="background-color: ${currentSecondColor}">
    <div class="logo-container" id="logo-container">
        <svg onclick="setNewColor()" id="logo" width="50" height="50" viewBox="0 0 50 50" fill="none"
            xmlns="http://www.w3.org/2000/svg">
            <circle r="23" transform="matrix(-1 0 0 1 25 25)" stroke="${currentMainColor}" stroke-width="4" />
            <path
                d="M14.4504 25.0336C14.4504 30.8414 19.1586 35.5496 24.9664 35.5496C30.7742 35.5496 35.4824 30.8414 35.4824 25.0336C35.4824 19.2258 30.7742 14.5176 24.9664 14.5176C19.1586 14.5176 14.4504 19.2258 14.4504 25.0336Z"
                stroke="${currentMainColor}" stroke-width="3" />
            <path
                d="M32.0426 8.48049L28.4718 13.7708L26.7337 13.9185L25.0333 13.6478L27.735 10.2521L30.1401 7.20951L30.4739 7.00925L30.6741 6.94249L30.8744 6.87574L31.0747 6.84236L31.3083 6.80898L31.542 6.84236L31.7781 6.9057L31.9091 7.076L31.9759 7.24289L32.0426 7.47654L32.076 7.64343L32.1094 7.87707V8.07734V8.17747V8.2776L32.076 8.37774L32.0426 8.48049Z"
                fill="${currentMainColor}" stroke="${currentMainColor}" />
            <path
                d="M17.557 41.4858L21.1278 36.1955L22.866 36.0479L24.5663 36.3185L21.8646 39.7142L19.4595 42.7568L19.1257 42.9571L18.9255 43.0238L18.7252 43.0906L18.5249 43.124L18.2913 43.1573L18.0577 43.124L17.8215 43.0606L17.6905 42.8903L17.6237 42.7234L17.557 42.4898L17.5236 42.3229L17.4902 42.0892V41.889V41.7888V41.6887L17.5236 41.5886L17.557 41.4858Z"
                fill="${currentMainColor}" stroke="${currentMainColor}" />
            <rect width="2.73698" height="9.21228" transform="matrix(-1 0 0 1 26.3687 10.3472)" fill="transparent" />
            <rect width="2.73698" height="9.21228" transform="matrix(-1 0 0 1 26.3687 31.4419)" fill="transparent" />
        </svg>
        <a class="title" href="/">Flip The Script</a>
    </div>
    <div class="links">
        <div class="information">
            <ul>
                <li>
                    <h3>Information</h3>
                </li>
                <li><a href="/#about">About</a></li>
                <li><a href="/contact-us">Contact Us</a></li>
                <li><a href="/why-this-matters">Why This Matters</a></li>
            </ul>
        </div>
        <div class="actions">
            <ul>
                <li>
                    <h3>Actions</h3>
                </li>
                <li><a href="/flip">Flip Your Script</a></li>
                <li><a href="/predictor">Predictions</a></li>
                <li><a href="/statistics">Statistics</a></li>
            </ul>
        </div>
    </div>
</div>
<div class="social-links" style="background-color: ${currentThirdColor}">
    <a href="#"><img class="social-icons" src="/img/facebook" alt="Facebook Icon"></a>
    <a href="#"><img class="social-icons" src="/img/instagram" alt="Instagram Icon"></a>
    <a href="#"><img class="social-icons" src="/img/tumblr" alt="Tumblr Icon"></a>
</div>
    `;
}
