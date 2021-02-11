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
          <a href="/about">About Us</a>
        </li>
        <li>
          <a class="btn-start" style="background-color: ${currentMainColor};" href="/flip">Start Now</a>
        </li>
      </ul>
    </div>`;
}

function updateIntroHTML() {
    document.getElementById("intro").innerHTML = ` <img src="../img/blackDeco.png" alt=""><h1>We Care About A Fair <span style="color: ${currentMainColor};">World</span></h1>
    <p>Creating Gender Neutral Texts</p>    
    <a class="btn-flip" style="background-color: ${currentMainColor};" href="/flip">Create Your Text Now</a>
`;
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
                    <div id="bubleSlide2">${bubleSlide2SVG()}</div>
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

                <h4>7 Male pronouns</h4>
                <h4><span style="color: ${currentThirdColor};">1</span> Neutral pronoun</h4>
                <h4><span style="color: ${currentThirdColor};">0</span> Female pronouns</h4>

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
                <div id="bubleSlide7">${bubleSlide7SVG()}</div>
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
    <img src="../img/blackDeco.png" alt="">
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
            <p>Our data scientist Leti conducted a research analysing different articles applying our gender neutralizer. She found out that 65% of the gendered words converted were male. The biggest part of it being male personal pronouns, followed by male determiners. </br>
        
            The research was made with 270  different articles from 12 different sources. </br>
            
            Do you want to check out more numbers?
            
            <a class="btn-learn-more" style="background-color: ${currentMainColor};" href="/statistics">Learn More</a>
        </div>
    </div>  
    `;
}

function updateDidYouKnow() {

}

function updateAboutHTML() {

    document.getElementById('about').style.backgroundColor = backgroundColor;
    document.getElementById('about').innerHTML = `
    <h2 id="title1">We believe, </h2>
    <h2 id="title2"> we can all make change <span style="color: ${currentMainColor};"> happen.<span></h2>
        <link rel="stylesheet" href="/css/about.css">
          
        <div id="text-box two" class="text-contain">

            <p>We are Stephanie, Leticia, Leonardo and Luciana, a team of four motivated and engaged participants of TechLabs Berlin. We started Flip The Script because we recognized an issue in the way society sees gender.The way language works in our conscious and subconscious mind is often underestimated, and so is the way it affects how we perceive gender. 38% of the world’s population speaks a gendered language as a native speaker. World Bank economist Owen Ozier delivered, in 2019, a crash course on linguistics and its relationship to gender norms. According to Ozier, existing research has already hinted at a link between grammar and gender. Recent experiments in political science have shown that gendered languages that classify nouns as female, male, or neutral are associated with more regressive gender attitudes. How is it, then, that even though English, a language spoken by 1.5 billion people, isn't a gendered language, yet is highly pointed for being a biased language? The reason is, grammatical gender is only one among many of the linguistic structures we use that influences the way we see our society through a gendered lens.</p>
            <p id="hidden-text1" class="d-none">Research made by Janet A. Sniezek and Christine H. Jazwinski in the Journal of Applied Social Psychology found that “generic” masculine nouns, pronouns, and adjectives function similarly to gender specific masculine terms. That certain grammatically “neutral” terms are in fact rated as relatively masculine. This evidence demonstrates that the use of “generic” masculine and even other grammatically neutral terms in effect serves to exclude women and not binary people from the English language. This can be observed when an identifying noun, such as policemen, is used to identify a group of police officers. In effect, anyone who does not identify as a man is erased from the statement. Another example can be observed when a gender neutral word, such as scientist, is perceived with a male connotation. As a result, we often hear and read about "female scientists", as though scientists are all men and women are just an exception. The resulting masculine bias in our language reflects and reinforces the pattern that the male form is the default.</p>
            <p id="hidden-text2" class="d-none">But we want to change this. And we understand that we can all create change because we all use language. Flip The Script is aimed to be used as a tool for change and education about our language use by offering users the option to consciously decide for a fairer language. Furthermore, we want to offer visitors the option to learn more about language use and patters and why it is important. You can find, on the statistics page, our results from collecting and analyzing news articles from various sources across the web.</p>
            <a class="btn-start" id="contact-button" style="background-color: ${currentMainColor};" href="/contact">Contact Us</a>
            
        
        </div>
        <div id="about-people">
        ${people1SVG()}
        </div>
    `;
}


function updatePredictorHTML() {
    document.getElementById('predictor-section').style.backgroundColor = convertHexToRGBA(currentSecondColor, 0.5);
    document.getElementById('predictor-section').innerHTML = `
    <form id="predictor-form" method="POST">

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
              
                <div class="gender-container">
                <button type="button" onclick="checkGenderForm(id)" id="male-btn" class='btn-next'>Male</button>
                <button type="button" onclick="checkGenderForm(id)" id="female-btn" class='btn-next'>Female</button>

                    <input class="d-none" type="radio" id="male" name="sex" value="0">
                    <label class="d-none"for="male">Male</label> 
                    <input class="d-none"type="radio" id="female" name="sex" value="1">
                    <label class="d-none" for="female">Female</label>
                </div>
                <button id="btn-results" class="btn-skip v-hidden" formaction="articlecat"><span style="color:${currentThirdColor}">Check the results</span></button>
            </li>
        </ul>
    </div>
</form>
    `;
}

function updatePredictorResultHTML() {
    document.getElementById('predictor-result-section').style.backgroundColor = convertHexToRGBA(currentThirdColor, 0.5);
    document.getElementById('predictor-result-section').innerHTML = `<ul class="predictor-slideshow-list">
<li class="predictor-slide">
    <h1>The Predictor says this article might be:</h1>
    <div class="response-container" id="response-container">
    </div>
    <a class="btn-next" href="/predictor" style="background-color:${currentMainColor}">New Prediction</a>
</li>
</ul>`;

}


function updateTeamHTML() {

    document.getElementById('team-section').style.backgroundColor = convertHexToRGBA(currentSecondColor, 0.5);
    document.getElementById('team-section').innerHTML = `
    <div class="title-container">
        <h1>The Team</h1>
        <h2>Behind <span style="color:${currentThirdColor};">Flip The Script</span></h2>
    </div>
    <div class="team-container">
    <div class="row">
        <div class="col">
            <img src="../img/member3.png" alt="">
            <div class="description">
                <p>Hi!, I am Luciana, born in Bogota and based in Berlin. 
                I am the designer of the team. I enjoy designing for users, but more than that I enjoy designing for people. Currently studying Computer Science and I have a passion for design, art and dance. Trying to save the world by redesigning it bit by bit.</p> 
            </div>
        </div>
        
        
            <div class="col">
            <img src="../img/member2.png" alt="">
            <div class="description">
                <p>Hello! I am Leticia, Data Scientist and Software Developer of the team. My academic background is Applied Linguistics and currently I'm an aspiring IT specialist living in Berlin. 
                It fascinates me how words shape people and the impact of language on our lives. In this digital age where our information diet is overwhelmed by the media, I want to create tools with which people can be aware of objectivity. When not programming, I enjoy hiking, blogging and doing kusudamas.</p>   
            </div>
            </div>
        
            <div class="col">
            <img src="../img/member1.png" alt="">
            <div class="description">
                <p>Hello! I am Stephanie and am currently studying software development. I am passionate about broadening the world of tech to be more inclusive and available for everyone. I also believe that tech is a force that is changing society and want to use it for positive change and to give back to communities.</p>  
            </div>
        </div>
        <div class="col">
            <img src="../img/leo.jpg" alt="">
            <div class="description">
                <p>Hi there! I'm Leonardo, an a frontend developer of the team. I love bringing designs to life and developing software that can help others. Although my past was not as a Web Dev, I am sure that my future will be all about it!</p>
            </div>
            </div>
        </div>
    </div>
    `;
}

function updateFlipHTML(){

}
function updateFooterHTML() {
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
                <li><a href="/about">About</a></li>
                <li><a href="/contact-us">Contact Us</a></li>
                <li><a href="/why-it-matters">Why This Matters</a></li>
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
<svg width="99" height="22" viewBox="0 0 99 22" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M0.849365 4.86572C0.849365 3.80486 1.27079 2.78744 2.02094 2.0373C2.77108 1.28715 3.7885 0.865723 4.84937 0.865723H16.8494C17.9102 0.865723 18.9276 1.28715 19.6778 2.0373C20.4279 2.78744 20.8494 3.80486 20.8494 4.86572V16.8657C20.8494 17.9266 20.4279 18.944 19.6778 19.6941C18.9276 20.4443 17.9102 20.8657 16.8494 20.8657H4.84937C3.7885 20.8657 2.77108 20.4443 2.02094 19.6941C1.27079 18.944 0.849365 17.9266 0.849365 16.8657V4.86572ZM4.84937 2.86572C4.31893 2.86572 3.81022 3.07644 3.43515 3.45151C3.06008 3.82658 2.84937 4.33529 2.84937 4.86572V16.8657C2.84937 17.3962 3.06008 17.9049 3.43515 18.2799C3.81022 18.655 4.31893 18.8657 4.84937 18.8657H10.8494V11.8657H9.84937C9.58415 11.8657 9.32979 11.7604 9.14226 11.5728C8.95472 11.3853 8.84937 11.1309 8.84937 10.8657C8.84937 10.6005 8.95472 10.3462 9.14226 10.1586C9.32979 9.97108 9.58415 9.86572 9.84937 9.86572H10.8494V8.36572C10.8494 7.43746 11.2181 6.54723 11.8745 5.89085C12.5309 5.23447 13.4211 4.86572 14.3494 4.86572H14.9494C15.2146 4.86572 15.4689 4.97108 15.6565 5.15862C15.844 5.34615 15.9494 5.60051 15.9494 5.86572C15.9494 6.13094 15.844 6.38529 15.6565 6.57283C15.4689 6.76037 15.2146 6.86572 14.9494 6.86572H14.3494C14.1524 6.86572 13.9573 6.90452 13.7753 6.9799C13.5934 7.05529 13.428 7.16577 13.2887 7.30506C13.1494 7.44435 13.0389 7.60971 12.9635 7.7917C12.8882 7.97369 12.8494 8.16874 12.8494 8.36572V9.86572H14.9494C15.2146 9.86572 15.4689 9.97108 15.6565 10.1586C15.844 10.3462 15.9494 10.6005 15.9494 10.8657C15.9494 11.1309 15.844 11.3853 15.6565 11.5728C15.4689 11.7604 15.2146 11.8657 14.9494 11.8657H12.8494V18.8657H16.8494C17.3798 18.8657 17.8885 18.655 18.2636 18.2799C18.6387 17.9049 18.8494 17.3962 18.8494 16.8657V4.86572C18.8494 4.33529 18.6387 3.82658 18.2636 3.45151C17.8885 3.07644 17.3798 2.86572 16.8494 2.86572H4.84937Z" fill="black"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M35.8494 4.86572C35.8494 3.80486 36.2708 2.78744 37.0209 2.0373C37.7711 1.28715 38.7885 0.865723 39.8494 0.865723H51.8494C52.9102 0.865723 53.9276 1.28715 54.6778 2.0373C55.4279 2.78744 55.8494 3.80486 55.8494 4.86572V16.8657C55.8494 17.9266 55.4279 18.944 54.6778 19.6941C53.9276 20.4443 52.9102 20.8657 51.8494 20.8657H39.8494C38.7885 20.8657 37.7711 20.4443 37.0209 19.6941C36.2708 18.944 35.8494 17.9266 35.8494 16.8657V4.86572ZM39.8494 2.86572C39.3189 2.86572 38.8102 3.07644 38.4352 3.45151C38.0601 3.82658 37.8494 4.33529 37.8494 4.86572V16.8657C37.8494 17.3962 38.0601 17.9049 38.4352 18.2799C38.8102 18.655 39.3189 18.8657 39.8494 18.8657H51.8494C52.3798 18.8657 52.8885 18.655 53.2636 18.2799C53.6387 17.9049 53.8494 17.3962 53.8494 16.8657V4.86572C53.8494 4.33529 53.6387 3.82658 53.2636 3.45151C52.8885 3.07644 52.3798 2.86572 51.8494 2.86572H39.8494ZM45.8494 7.86572C45.0537 7.86572 44.2907 8.18179 43.728 8.7444C43.1654 9.30701 42.8494 10.0701 42.8494 10.8657C42.8494 11.6614 43.1654 12.4244 43.728 12.987C44.2907 13.5497 45.0537 13.8657 45.8494 13.8657C46.645 13.8657 47.4081 13.5497 47.9707 12.987C48.5333 12.4244 48.8494 11.6614 48.8494 10.8657C48.8494 10.0701 48.5333 9.30701 47.9707 8.7444C47.4081 8.18179 46.645 7.86572 45.8494 7.86572ZM40.8494 10.8657C40.8494 9.53964 41.3761 8.26787 42.3138 7.33019C43.2515 6.39251 44.5233 5.86572 45.8494 5.86572C47.1754 5.86572 48.4472 6.39251 49.3849 7.33019C50.3226 8.26787 50.8494 9.53964 50.8494 10.8657C50.8494 12.1918 50.3226 13.4636 49.3849 14.4013C48.4472 15.3389 47.1754 15.8657 45.8494 15.8657C44.5233 15.8657 43.2515 15.3389 42.3138 14.4013C41.3761 13.4636 40.8494 12.1918 40.8494 10.8657ZM51.3494 6.86572C51.7472 6.86572 52.1287 6.70769 52.41 6.42638C52.6913 6.14508 52.8494 5.76355 52.8494 5.36572C52.8494 4.9679 52.6913 4.58637 52.41 4.30506C52.1287 4.02376 51.7472 3.86572 51.3494 3.86572C50.9515 3.86572 50.57 4.02376 50.2887 4.30506C50.0074 4.58637 49.8494 4.9679 49.8494 5.36572C49.8494 5.76355 50.0074 6.14508 50.2887 6.42638C50.57 6.70769 50.9515 6.86572 51.3494 6.86572Z" fill="black"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M74.8494 0.865723C73.7885 0.865723 72.7711 1.28715 72.0209 2.0373C71.2708 2.78744 70.8494 3.80486 70.8494 4.86572V16.8657C70.8494 17.9266 71.2708 18.944 72.0209 19.6941C72.7711 20.4443 73.7885 20.8657 74.8494 20.8657H86.8494C87.9102 20.8657 88.9276 20.4443 89.6778 19.6941C90.4279 18.944 90.8494 17.9266 90.8494 16.8657V4.86572C90.8494 3.80486 90.4279 2.78744 89.6778 2.0373C88.9276 1.28715 87.9102 0.865723 86.8494 0.865723H74.8494ZM72.8494 4.86572C72.8494 4.33529 73.0601 3.82658 73.4352 3.45151C73.8102 3.07644 74.3189 2.86572 74.8494 2.86572H86.8494C87.3798 2.86572 87.8885 3.07644 88.2636 3.45151C88.6387 3.82658 88.8494 4.33529 88.8494 4.86572V16.8657C88.8494 17.3962 88.6387 17.9049 88.2636 18.2799C87.8885 18.655 87.3798 18.8657 86.8494 18.8657H74.8494C74.3189 18.8657 73.8102 18.655 73.4352 18.2799C73.0601 17.9049 72.8494 17.3962 72.8494 16.8657V4.86572ZM80.8494 6.36572C80.8494 6.10051 80.744 5.84615 80.5565 5.65862C80.3689 5.47108 80.1146 5.36572 79.8494 5.36572C79.5841 5.36572 79.3298 5.47108 79.1423 5.65862C78.9547 5.84615 78.8494 6.10051 78.8494 6.36572V7.86572H77.8494C77.5841 7.86572 77.3298 7.97108 77.1423 8.15862C76.9547 8.34615 76.8494 8.60051 76.8494 8.86572C76.8494 9.13094 76.9547 9.38529 77.1423 9.57283C77.3298 9.76037 77.5841 9.86572 77.8494 9.86572H78.8494V12.7557C78.8494 15.2007 81.2914 16.8927 83.5794 16.0327L84.1954 15.8027C84.4437 15.7095 84.6449 15.5214 84.7546 15.2799C84.8643 15.0383 84.8736 14.7631 84.7804 14.5147C84.6871 14.2663 84.4991 14.0652 84.2575 13.9555C84.016 13.8458 83.7407 13.8365 83.4924 13.9297L82.8764 14.1597C82.6496 14.2448 82.4056 14.2737 82.1652 14.244C81.9249 14.2143 81.6953 14.1268 81.4961 13.989C81.2969 13.8512 81.134 13.6673 81.0214 13.4528C80.9088 13.2384 80.8497 12.9999 80.8494 12.7577V9.86572H83.3494C83.6146 9.86572 83.8689 9.76037 84.0565 9.57283C84.244 9.38529 84.3494 9.13094 84.3494 8.86572C84.3494 8.60051 84.244 8.34615 84.0565 8.15862C83.8689 7.97108 83.6146 7.86572 83.3494 7.86572H80.8494V6.36572Z" fill="black"/>
</svg>
</div>
    `;
}
