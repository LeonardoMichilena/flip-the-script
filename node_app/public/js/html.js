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
    <a href="#"><img class="social-icons" src="/img/facebook.png" alt="Facebook Icon"></a>
    <a href="#"><img class="social-icons" src="/img/instagram.png" alt="Instagram Icon"></a>
    <a href="#"><img class="social-icons" src="/img/tumblr.png" alt="Tumblr Icon"></a>
</div>
    `;
}
