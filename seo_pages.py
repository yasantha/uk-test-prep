"""Long-tail guide pages for the Life in the UK Test Prep website.

Used by build.py. Each page is plain data: slug, title, description, heading, lead, body HTML, FAQ pairs.
Facts follow the official handbook (3rd edition) and GOV.UK. Where a rule or fee can change, the page
says so and points to GOV.UK instead of quoting a number.
"""
from __future__ import annotations

GOV = "https://www.gov.uk/life-in-the-uk-test"

# ------------------------------------------------------------------ chapter guides
CHAPTERS = [
    dict(
        n=1, slug="life-in-the-uk-test-chapter-1-values-and-principles",
        name="The values and principles of the UK",
        title="Life in the UK Test Chapter 1: Values and Principles",
        desc="Chapter 1 of the Life in the UK handbook explained: democracy, the rule of law, liberty, tolerance and community life. Is it in the test?",
        lead="Chapter 1 is short and sets out the values the rest of the handbook builds on. Here is what it says and how to use it.",
        body="""
<h2>Is chapter 1 in the test?</h2>
<p>No. The questions in the Life in the UK Test come from chapters 2 to 5 of the handbook. Chapter 1 is not examined, but it explains the ideas behind the rest of the book, and it is worth a 15-minute read because it helps you understand why the later chapters say what they do.</p>
<h2>The fundamental principles</h2>
<p>The handbook describes the fundamental principles of British life as:</p>
<ul>
<li><b>Democracy:</b> people choose who governs them through free and fair elections.</li>
<li><b>The rule of law:</b> everyone, including the government, must obey the law, and the law applies to everyone equally.</li>
<li><b>Individual liberty:</b> people are free to live their lives as they choose, within the law.</li>
<li><b>Tolerance of those with different faiths and beliefs:</b> and respect for other people's rights.</li>
<li><b>Participation in community life:</b> taking part in society, for example by volunteering, joining a group or voting.</li>
</ul>
<h2>Becoming a permanent resident or citizen</h2>
<p>The chapter explains that people who settle in the UK are expected to respect these principles, and it describes the pledge new citizens make at a citizenship ceremony: to be loyal to the United Kingdom, respect its rights and freedoms, uphold its democratic values, obey its laws and fulfil the duties and obligations of a citizen.</p>
<h2>How to study it</h2>
<p>Read it once, quickly. The same ideas return in chapter 5 (government, the law and your role), where they are tested in more detail.</p>
""",
        quick=[
            ("Is chapter 1 part of the test?", "No. The test questions come from chapters 2 to 5."),
            ("Name two fundamental principles of British life.", "Examples: democracy, the rule of law, individual liberty, tolerance and participation in community life."),
        ],
    ),
    dict(
        n=2, slug="life-in-the-uk-test-chapter-2-what-is-the-uk",
        name="What is the UK?",
        title="Life in the UK Test Chapter 2: What is the UK? Key Facts",
        desc="Key facts from chapter 2 of the Life in the UK handbook: the four countries, capitals, patron saints, flags and devolution, with practice questions.",
        lead="Chapter 2 covers the geography and make-up of the UK. It is short, and the questions are very learnable.",
        body="""
<h2>UK, Great Britain and the British Isles</h2>
<p>These three terms are easy to mix up, and the test likes to ask about them.</p>
<ul>
<li>The <b>United Kingdom</b> is England, Scotland, Wales and Northern Ireland.</li>
<li><b>Great Britain</b> is England, Scotland and Wales only.</li>
<li>The <b>British Isles</b> include the UK, Ireland, the Isle of Man and the Channel Islands.</li>
<li>The <b>Channel Islands</b> and the <b>Isle of Man</b> are Crown dependencies. They are not part of the UK.</li>
</ul>
<h2>Capitals, patron saints and national days</h2>
<div class="tablewrap"><table>
<thead><tr><th>Country</th><th>Capital</th><th>Patron saint</th><th>Saint's day</th></tr></thead>
<tbody>
<tr><td>England</td><td>London</td><td>St George</td><td>23 April</td></tr>
<tr><td>Scotland</td><td>Edinburgh</td><td>St Andrew</td><td>30 November</td></tr>
<tr><td>Wales</td><td>Cardiff</td><td>St David</td><td>1 March</td></tr>
<tr><td>Northern Ireland</td><td>Belfast</td><td>St Patrick</td><td>17 March</td></tr>
</tbody></table></div>
<h2>The Union Flag</h2>
<p>The Union Flag, often called the Union Jack, combines the crosses of three saints: St George (England), St Andrew (Scotland) and St Patrick (Ireland). Wales is not represented separately on the flag.</p>
<h2>Devolution</h2>
<p>Scotland, Wales and Northern Ireland each have their own devolved parliament or assembly that makes decisions on some matters, such as education and health. These are the <b>Scottish Parliament</b>, the <b>Senedd</b> (the Welsh Parliament) and the <b>Northern Ireland Assembly</b>. The UK Parliament in London keeps control of areas such as defence and foreign affairs.</p>
<h2>Languages and landmarks</h2>
<ul>
<li>English is spoken throughout the UK. Welsh is widely spoken in Wales, and Scottish Gaelic and Irish are spoken in parts of Scotland and Northern Ireland.</li>
<li><b>Ben Nevis</b> in Scotland is the highest mountain in the UK.</li>
<li><b>Lough Neagh</b> in Northern Ireland is the largest lake in the UK.</li>
</ul>
<h2>How to study it</h2>
<p>Learn the table above by heart, then practise telling the UK, Great Britain and the British Isles apart. Those distinctions come up often.</p>
""",
        quick=[
            ("Which countries make up Great Britain?", "England, Scotland and Wales."),
            ("What is the capital of Wales?", "Cardiff."),
            ("Who is the patron saint of Scotland?", "St Andrew, whose day is 30 November."),
            ("Are the Channel Islands part of the UK?", "No. They are Crown dependencies."),
        ],
    ),
    dict(
        n=3, slug="life-in-the-uk-test-chapter-3-history",
        name="A long and illustrious history",
        title="Life in the UK Test Chapter 3: British History Key Dates",
        desc="A clear timeline for chapter 3 of the Life in the UK handbook: Romans, Normans, Tudors, Stuarts, two world wars and modern Britain, with practice questions.",
        lead="History is the longest chapter and where most people lose marks. Learn it as a timeline, not as separate dates.",
        body="""
<h2>An overview timeline</h2>
<div class="tablewrap"><table>
<thead><tr><th>Period or date</th><th>What to remember</th></tr></thead>
<tbody>
<tr><td>Stone Age to Iron Age</td><td>Early settlers, farming, and Stonehenge and Skara Brae from this time.</td></tr>
<tr><td>AD 43</td><td>The Romans invade Britain under Emperor Claudius. They build roads, towns and Hadrian's Wall.</td></tr>
<tr><td>After the Romans</td><td>The Anglo-Saxons settle, then the Vikings raid and settle.</td></tr>
<tr><td>1066</td><td>William of Normandy wins the Battle of Hastings and becomes king (the Norman Conquest).</td></tr>
<tr><td>1215</td><td>King John agrees to Magna Carta, limiting the power of the king.</td></tr>
<tr><td>1485 to 1603</td><td>The Tudors. Henry VIII breaks with the Roman Catholic Church and Elizabeth I defeats the Spanish Armada (1588).</td></tr>
<tr><td>1603 to 1714</td><td>The Stuarts. The Union of the Crowns (1603), the Civil War, the execution of Charles I (1649), the Restoration (1660), the Glorious Revolution (1688) and the Bill of Rights (1689).</td></tr>
<tr><td>1707</td><td>The Act of Union joins England and Scotland.</td></tr>
<tr><td>1700s to 1800s</td><td>The Industrial Revolution. The slave trade is abolished in 1807 and slavery in the British Empire in 1833.</td></tr>
<tr><td>1837 to 1901</td><td>Queen Victoria's reign.</td></tr>
<tr><td>1914 to 1918</td><td>The First World War.</td></tr>
<tr><td>1939 to 1945</td><td>The Second World War. Winston Churchill leads Britain as Prime Minister.</td></tr>
<tr><td>1948</td><td>The National Health Service (NHS) begins. The ship Empire Windrush arrives from the Caribbean.</td></tr>
</tbody></table></div>
<h2>People who often appear</h2>
<ul>
<li><b>William the Conqueror:</b> the Norman king after 1066.</li>
<li><b>King John:</b> agreed to Magna Carta in 1215.</li>
<li><b>Henry VIII:</b> six wives, and the break with Rome that led to the Church of England.</li>
<li><b>Elizabeth I:</b> Protestant queen, defeated the Spanish Armada in 1588.</li>
<li><b>Oliver Cromwell:</b> led the Parliamentary side in the Civil War and ruled as Lord Protector.</li>
<li><b>Winston Churchill:</b> Prime Minister during the Second World War.</li>
</ul>
<h2>Votes for women</h2>
<p>In 1918 women over 30 who met certain conditions won the vote. In 1928 women gained the vote on equal terms with men.</p>
<h2>How to study it</h2>
<p>Split it into three blocks: up to 1066, 1066 to 1714, and 1714 to today. Work through one block at a time, and test yourself after each. Keep a short list of the dates you keep forgetting and review it daily.</p>
""",
        quick=[
            ("In which year did the Normans win the Battle of Hastings?", "1066."),
            ("Which document did King John agree to in 1215?", "Magna Carta."),
            ("Which queen defeated the Spanish Armada in 1588?", "Elizabeth I."),
            ("When did slavery end in the British Empire?", "1833. The slave trade itself was abolished in 1807."),
        ],
    ),
    dict(
        n=4, slug="life-in-the-uk-test-chapter-4-modern-society",
        name="A modern, thriving society",
        title="Life in the UK Test Chapter 4: Modern Society and Culture",
        desc="Chapter 4 of the Life in the UK handbook explained: religion, customs and festivals, sport, arts and famous places, with key facts and practice questions.",
        lead="Chapter 4 describes everyday life, traditions and culture. Dates of festivals and famous names are the main things to learn.",
        body="""
<h2>Traditions and festivals</h2>
<div class="tablewrap"><table>
<thead><tr><th>Date</th><th>Event</th></tr></thead>
<tbody>
<tr><td>25 January</td><td>Burns Night in Scotland, in memory of the poet Robert Burns</td></tr>
<tr><td>14 February</td><td>St Valentine's Day</td></tr>
<tr><td>Spring</td><td>Easter, and Good Friday and Easter Monday as bank holidays</td></tr>
<tr><td>31 October</td><td>Halloween</td></tr>
<tr><td>5 November</td><td>Bonfire Night, remembering the Gunpowder Plot of 1605</td></tr>
<tr><td>11 November</td><td>Remembrance Day. People wear red poppies and remember those who died in war.</td></tr>
<tr><td>25 December</td><td>Christmas Day</td></tr>
<tr><td>31 December</td><td>Hogmanay in Scotland (New Year's Eve)</td></tr>
</tbody></table></div>
<p>The handbook also describes major religious festivals of other faiths, such as Diwali, Eid, Hanukkah and Vaisakhi, which are celebrated across the UK.</p>
<h2>Religion</h2>
<p>Christianity is the largest religion, and the UK has many other faiths. The Church of England is the established church in England and the Church of Scotland is the national church in Scotland. People are free to follow any religion or none.</p>
<h2>Sport, arts and famous places</h2>
<ul>
<li>Major sporting events include Wimbledon (tennis) and the Six Nations (rugby).</li>
<li>The handbook names writers, artists, composers, scientists and inventors from all periods, so learn what each person is known for.</li>
<li>It also lists famous places to visit across all four countries, from castles and cathedrals to national parks.</li>
</ul>
<h2>Everyday life</h2>
<ul>
<li>Education is compulsory for children up to age 16 in the UK, and in England young people must then stay in education or training until 18.</li>
<li>You must be 17 to drive a car. People drive on the left.</li>
<li>You must be 18 to vote in a general election.</li>
</ul>
<h2>How to study it</h2>
<p>Make a calendar of the festival dates above and learn it. For the people and places, use flash cards with one fact per name.</p>
""",
        quick=[
            ("What is celebrated on 25 January in Scotland?", "Burns Night."),
            ("What does Bonfire Night remember?", "The Gunpowder Plot of 1605."),
            ("What do people wear on Remembrance Day?", "Red poppies."),
            ("At what age can you drive a car in the UK?", "17."),
        ],
    ),
    dict(
        n=5, slug="life-in-the-uk-test-chapter-5-government-law-and-your-role",
        name="The UK government, the law and your role",
        title="Life in the UK Test Chapter 5: Government and the Law",
        desc="Chapter 5 of the Life in the UK handbook explained: the monarchy, Parliament, elections, courts, rights and responsibilities, with practice questions.",
        lead="Chapter 5 explains how the UK is governed and what is expected of residents and citizens. The facts are precise, so learn the numbers.",
        body="""
<h2>The constitution and the monarchy</h2>
<p>The UK is a <b>constitutional monarchy</b>. The King or Queen is head of state, but the government makes the decisions. The UK constitution is not written down in a single document.</p>
<h2>Parliament</h2>
<ul>
<li>The <b>House of Commons</b> is the elected house. It has 650 members, called MPs, each representing a constituency.</li>
<li>The <b>House of Lords</b> is the second house. Its members are not elected in general elections. It checks and suggests changes to new laws.</li>
<li>A general election must be held at least every five years.</li>
<li>The leader of the party with the most MPs, or who can command a majority in the Commons, usually becomes <b>Prime Minister</b>, and chooses the Cabinet.</li>
<li>You must be 18 to vote.</li>
</ul>
<h2>Devolved governments and local government</h2>
<p>The Scottish Parliament, the Senedd (Wales) and the Northern Ireland Assembly make decisions on devolved matters. Local councils, led by elected councillors, provide services such as rubbish collection, planning and libraries.</p>
<h2>The courts and the law</h2>
<ul>
<li>Serious crimes are tried in front of a judge and a <b>jury</b> of 12 people in England, Wales and Northern Ireland. Scotland also uses juries, and its juries have 15 members.</li>
<li>You can be called for jury service if you are on the electoral register and aged between 18 and 75.</li>
<li>The UK has a modern, independent police service. The police must treat everyone fairly.</li>
<li>Discrimination on grounds such as race, sex, religion, age or disability is against the law.</li>
</ul>
<h2>Rights and responsibilities</h2>
<p>As a resident you are expected to obey the law, pay your taxes, look after your family, respect the rights of others and help the police prevent crime. Taking part in community life, for example through volunteering, is encouraged.</p>
<h2>How to study it</h2>
<p>Learn the numbers (650 MPs, 5 years, 18 to vote, 12 jurors) first, then the roles of each institution. Practise the questions that ask you to choose two correct answers.</p>
""",
        quick=[
            ("How many MPs are there in the House of Commons?", "650."),
            ("How often must a general election be held?", "At least every five years."),
            ("What is the minimum voting age?", "18."),
            ("How many people are on a jury in England?", "12."),
        ],
    ),
]

# ------------------------------------------------------------------ topic guides
TOPICS = [
    dict(
        slug="life-in-the-uk-test-pass-mark",
        title="Life in the UK Test Pass Mark, Questions and Time Limit",
        desc="The Life in the UK Test has 24 questions, lasts 45 minutes and the pass mark is 75% (18 correct). See the question types and what a good mock score looks like.",
        h1="Life in the UK Test pass mark, questions and time",
        crumb="Pass mark and format",
        lead="The short answer: 24 questions, 45 minutes, and you need 18 correct to pass.",
        body="""
<div class="facts facts-3" aria-label="Test format">
<div><b>24</b><span>questions</span></div>
<div><b>45 min</b><span>time allowed</span></div>
<div><b>75%</b><span>pass mark (18 correct)</span></div>
</div>
<h2>What the test looks like</h2>
<p>The test is taken on a computer at an approved test centre. Questions are multiple choice. Most ask you to pick one answer, some ask you to pick two, and some are true or false statements. You see your result before you leave.</p>
<h2>What a good mock score is</h2>
<p>Passing needs 18 out of 24. For a safety margin, aim for <b>21 or more</b> in at least three full mock tests in a row before you sit the real test. Mock tests that use the same format, with 24 questions in 45 minutes, show you whether your timing is comfortable.</p>
<h2>Which chapters are tested</h2>
<p>The questions come from chapters 2 to 5 of the official handbook. See the guides for <a href="/life-in-the-uk-test-chapter-2-what-is-the-uk/">chapter 2</a>, <a href="/life-in-the-uk-test-chapter-3-history/">chapter 3</a>, <a href="/life-in-the-uk-test-chapter-4-modern-society/">chapter 4</a> and <a href="/life-in-the-uk-test-chapter-5-government-law-and-your-role/">chapter 5</a>.</p>
<h2>Is the pass mark ever different?</h2>
<p>The pass mark and format can be changed by the government. Check the <a href="%(gov)s">GOV.UK Life in the UK Test page</a> for the current rules before you book.</p>
""".replace("%(gov)s", GOV),
        faq=[
            ("How many questions are in the Life in the UK Test?", "24 multiple-choice questions."),
            ("How long is the Life in the UK Test?", "45 minutes."),
            ("What is the pass mark for the Life in the UK Test?", "75%, which means at least 18 of the 24 questions correct."),
        ],
    ),
    dict(
        slug="life-in-the-uk-test-booking-and-what-to-bring",
        title="How to Book the Life in the UK Test and What to Bring",
        desc="Step-by-step: how to book the Life in the UK Test on GOV.UK, which identification to bring, what happens on the day and how to get your result.",
        h1="How to book the Life in the UK Test and what to bring",
        crumb="Booking and what to bring",
        lead="Book through the official GOV.UK service only. Here is how it works and how to prepare for the day.",
        body="""
<h2>Booking steps</h2>
<ol>
<li>Go to the official <a href="%(gov)s">GOV.UK Life in the UK Test page</a> and start the booking. Use only GOV.UK. Other sites may charge extra or are not official.</li>
<li>Create an account and choose a test centre, date and time.</li>
<li>Pay the test fee. It is £50 at the time of writing; check the current amount on GOV.UK. Book at least 3 days before the test date.</li>
<li>Save your booking confirmation and check what identification you must bring.</li>
</ol>
<h2>What to bring</h2>
<p>You must bring the <b>same identification you used when booking</b>, in its original form. Copies and phone screenshots are not accepted, and the name on your booking must match your ID exactly. If it does not, you will not be allowed to sit the test and you will not get a refund.</p>
<p>According to GOV.UK, accepted identification includes:</p>
<ul>
<li>an <b>eVisa share code</b>, if you have an eVisa</li>
<li>a valid <b>passport</b></li>
<li>a valid national identity card from an EU country, Switzerland, Iceland, Liechtenstein or Norway</li>
<li>a valid photo travel document (not an emergency travel document)</li>
<li>a biometric residence permit or card, within the time limits GOV.UK sets</li>
</ul>
<p>Your photo is taken at the test centre. Children and other family members cannot come into the centre with you. Check the full, current list on GOV.UK a few days before your test.</p>
<h2>On the day</h2>
<ul>
<li>Arrive early. Test centres have identity checks before you start.</li>
<li>Follow the instructions of the staff. You will usually be asked to store your belongings.</li>
<li>Read each question twice, especially ones that ask for two answers.</li>
<li>You get your result at the end. If you pass, keep your pass notification letter safe, because you need its reference number for your application.</li>
</ul>
<h2>Language</h2>
<p>The test is normally taken in English. It can also be taken in Welsh or Scottish Gaelic at some centres. Check GOV.UK for availability.</p>
<h2>Prepare before you book</h2>
<p>Take full mock tests first. When you score 21 or more out of 24 consistently, you are ready to book. Try our <a href="/practice-questions/">free practice questions</a> or the <a href="/demo/">interactive demo</a>.</p>
""".replace("%(gov)s", GOV),
        faq=[
            ("Where do I book the Life in the UK Test?", "On the official GOV.UK Life in the UK Test page. Do not use unofficial booking sites."),
            ("What should I bring to the Life in the UK Test?", "The original identification you used when you booked, such as your passport or eVisa share code. The name must match your booking exactly. Copies and screenshots are not accepted."),
            ("Can I cancel my Life in the UK Test and get a refund?", "Yes, if you cancel at least 72 hours (3 days) before the test. Cancelling or changing it later than that means no refund."),
            ("Do I get my result straight away?", "Yes. You see your result before you leave the test centre."),
        ],
    ),
    dict(
        slug="life-in-the-uk-test-retake-rules",
        title="Failed the Life in the UK Test? Retake Rules and Next Steps",
        desc="What happens if you fail the Life in the UK Test: you can retake it, how soon, what it costs and how to fix your weak areas before the next attempt.",
        h1="Failed the Life in the UK Test? Retake rules and next steps",
        crumb="Retake rules",
        lead="Failing is common and not the end. You can take the test again. Here is what to do.",
        body="""
<h2>Can I retake the test?</h2>
<p>Yes. You can retake the Life in the UK Test as many times as you need. You must book and pay the £50 fee again each time, and you must book at least 3 days before the test. GOV.UK does not set a separate waiting period between attempts, but rules can change, so check the <a href="%(gov)s">GOV.UK Life in the UK Test page</a> before you rebook. Read our guide to the <a href="/life-in-the-uk-test-cost/">test cost, refunds and rebooking</a>.</p>
<h2>How to improve before the next attempt</h2>
<ol>
<li><b>Find your weak chapter.</b> Most people lose marks in history (chapter 3). Check which chapter your wrong answers came from.</li>
<li><b>Study the explanations.</b> For every question you miss, read why the right answer is right.</li>
<li><b>Re-test the same questions.</b> Come back to missed questions after a day, then after a week.</li>
<li><b>Take timed mocks.</b> Practise 24 questions in 45 minutes until you score 21 or more three times in a row.</li>
<li><b>Book when ready.</b> You do not have to book the earliest possible date.</li>
</ol>
<h2>Common reasons people fail</h2>
<ul>
<li>Trying to memorise dates without understanding the order of events.</li>
<li>Mixing up the UK, Great Britain and the British Isles.</li>
<li>Missing the "choose two answers" questions.</li>
<li>Not taking full mock tests under timed conditions.</li>
</ul>
<h2>Where to start</h2>
<p>Read the <a href="/study-guide/">study guide and 4-week plan</a>, then work through the <a href="/life-in-the-uk-test-guides/">chapter guides</a>.</p>
""".replace("%(gov)s", GOV),
        faq=[
            ("Can I retake the Life in the UK Test if I fail?", "Yes, as many times as needed. You book and pay again each time."),
            ("How long must I wait to retake the test?", "GOV.UK does not set a waiting period between attempts, but every booking must be made at least 3 days before the test, and you pay the £50 fee each time."),
        ],
    ),
    dict(
        slug="life-in-the-uk-test-for-ilr-and-citizenship",
        title="Life in the UK Test for ILR and Citizenship: Who Needs It?",
        desc="Who needs to pass the Life in the UK Test for indefinite leave to remain (settlement) or British citizenship, who is exempt, and what else you may need.",
        h1="Life in the UK Test for ILR and British citizenship",
        crumb="ILR and citizenship",
        lead="Most adults who apply for settlement or British citizenship must pass the test. Here is who needs it and who does not.",
        body="""
<h2>Who needs to pass</h2>
<p>If you are applying for <b>indefinite leave to remain (ILR, also called settlement)</b> or for <b>British citizenship by naturalisation</b>, you usually need to pass the Life in the UK Test and include your pass notification letter reference in your application.</p>
<h2>Who may not need to take it</h2>
<ul>
<li>People under 18 and people aged 65 or over.</li>
<li>Some people with a long-term physical or mental condition. You may need to provide evidence.</li>
</ul>
<p>Exemptions and routes differ, so confirm yours on GOV.UK or with a regulated immigration adviser.</p>
<h2>One test, two uses</h2>
<p>It is the same test for ILR and for citizenship. If you pass for one, the pass notification letter can usually be used for the other, because it does not expire. Keep the letter safe.</p>
<h2>What else you may need</h2>
<p>The Life in the UK Test is only one requirement. Applicants also usually need to show their level of English, for example at B1 on the CEFR scale, and meet residence and other requirements for their route. Rules change, so check the current guidance on GOV.UK before applying.</p>
<h2>Prepare for it</h2>
<p>Use the <a href="/study-guide/">study guide</a> and the <a href="/practice-questions/">free practice questions</a>, then take mock tests until you score 21 or more out of 24.</p>
<p><i>This page is general information, not legal advice. For your own case, use GOV.UK or an adviser regulated in the UK.</i></p>
""",
        faq=[
            ("Do I need the Life in the UK Test for ILR?", "Usually yes, unless you are exempt, for example because of your age or a long-term condition."),
            ("Is the test the same for citizenship and settlement?", "Yes. It is the same test."),
            ("Does the Life in the UK Test pass expire?", "No. Keep your pass notification letter safe."),
        ],
    ),
    dict(
        slug="how-long-to-study-for-the-life-in-the-uk-test",
        title="How Long Does It Take to Study for the Life in the UK Test?",
        desc="How long to study for the Life in the UK Test: a realistic timeline for different starting points, a 2-week crash plan and a 4-week plan with daily time.",
        h1="How long to study for the Life in the UK Test",
        crumb="How long to study",
        lead="There is no official figure, but most people need two to four weeks of short daily sessions.",
        body="""
<h2>A realistic timeline</h2>
<div class="tablewrap"><table>
<thead><tr><th>Your situation</th><th>Suggested time</th><th>Daily study</th></tr></thead>
<tbody>
<tr><td>Strong English, some knowledge of the UK</td><td>2 weeks</td><td>30 to 45 minutes</td></tr>
<tr><td>Strong English, new to UK history and culture</td><td>3 to 4 weeks</td><td>20 to 30 minutes</td></tr>
<tr><td>English is a second language</td><td>4 to 6 weeks</td><td>30 minutes, with read-aloud</td></tr>
</tbody></table></div>
<p>These are guides, not rules. What matters is that you score consistently high in timed mock tests.</p>
<h2>A 2-week plan</h2>
<ol>
<li><b>Days 1 to 3:</b> chapters 1 and 2, then questions.</li>
<li><b>Days 4 to 8:</b> chapter 3 (history) one period per day.</li>
<li><b>Days 9 to 11:</b> chapters 4 and 5.</li>
<li><b>Days 12 to 14:</b> a full mock test each day, then review every wrong answer.</li>
</ol>
<h2>How to know you are ready</h2>
<p>You are ready when you score <b>21 or more out of 24</b> in at least three timed mock tests in a row. A 75% pass mark leaves little room for a bad day, so a margin helps.</p>
<h2>Tips that save time</h2>
<ul>
<li>Study a little every day instead of one long weekend session.</li>
<li>Spend more time on chapter 3, which is the longest and has the most questions that catch people out.</li>
<li>Use questions as study tools. Read the explanation for each one you get wrong.</li>
</ul>
<p>The full 4-week plan is in our <a href="/study-guide/">study guide</a>.</p>
""",
        faq=[
            ("How many weeks does it take to prepare for the Life in the UK Test?", "Most people need two to four weeks of 20 to 45 minutes a day. People studying in a second language may need longer."),
            ("How do I know I am ready for the test?", "When you score 21 or more out of 24 in several timed mock tests in a row."),
        ],
    ),
    dict(
        slug="life-in-the-uk-test-cost",
        title="Life in the UK Test Cost 2026: £50 Fee, Refunds, Rebooking",
        desc="The Life in the UK Test costs £50. When you can get a refund, what happens if you cancel or rebook, and how to avoid paying twice.",
        h1="How much does the Life in the UK Test cost?",
        crumb="Test cost and refunds",
        lead="The test fee is £50, paid when you book on GOV.UK. Here is when you can get it back and how to avoid paying twice.",
        body="""
<div class="facts facts-3" aria-label="Test cost">
<div><b>£50</b><span>test fee</span></div>
<div><b>3 days</b><span>minimum notice to book</span></div>
<div><b>72 hours</b><span>notice to cancel for a refund</span></div>
</div>
<h2>The fee</h2>
<p>It costs <b>£50</b> to book the Life in the UK Test. You pay online when you book through the official <a href="%(gov)s">GOV.UK Life in the UK Test page</a>. If you need to take the test again, you pay the £50 fee again each time. Fees can change, so always check the current amount on GOV.UK before you book.</p>
<h2>Book only on GOV.UK</h2>
<p>Some websites offer to book the test for you or charge a "booking fee". You do not need them. The official booking service is on GOV.UK, and booking there costs only the test fee.</p>
<h2>Cancelling and refunds</h2>
<ul>
<li>Cancel <b>at least 72 hours (3 days)</b> before your test and you get a refund to the card you paid with.</li>
<li>If you cancel or rearrange your test <b>less than 3 days</b> before it, you do not get a refund.</li>
<li>If the <b>test centre cancels</b>, you can ask for a refund within 3 months of the test date.</li>
</ul>
<h2>When you will not get your money back</h2>
<p>GOV.UK says you will not get a refund if you cannot take the test because:</p>
<ul>
<li>you bring the wrong identification, or the name on your booking does not exactly match your ID</li>
<li>you arrive late or do not turn up</li>
<li>you are ill on the day</li>
<li>you refuse to have your photo taken at the centre</li>
</ul>
<p>Double-check your ID and booking name against our <a href="/life-in-the-uk-test-booking-and-what-to-bring/">booking and what to bring guide</a> before the day.</p>
<h2>The cheapest way to pass: once</h2>
<p>Every failed attempt costs another £50. Practise with timed mock tests until you score <b>21 or more out of 24</b> three times in a row, then book. Start with our <a href="/practice-questions/">free practice questions</a>.</p>
""".replace("%(gov)s", GOV),
        faq=[
            ("How much does the Life in the UK Test cost?", "£50, paid when you book on GOV.UK. Check GOV.UK for the current fee."),
            ("Do I pay again if I fail?", "Yes. You pay the £50 fee each time you book the test."),
            ("Can I get a refund on the Life in the UK Test?", "Yes, if you cancel at least 72 hours before the test, or if the test centre cancels. Not if you cancel later, bring the wrong ID, arrive late or are ill."),
        ],
    ),
    dict(
        slug="life-in-the-uk-test-exemptions",
        title="Life in the UK Test Exemptions: Who Doesn't Need to Take It?",
        desc="Who is exempt from the Life in the UK Test: under 18s, people aged 65 or over, people who have already passed and some with a long-term condition.",
        h1="Life in the UK Test exemptions: who does not need to take it",
        crumb="Exemptions",
        lead="Most adults applying for settlement or citizenship must pass the test, but some people do not need to take it.",
        body="""
<h2>You do not need to take the test if you are</h2>
<ul>
<li><b>under 18</b></li>
<li><b>65 or over</b></li>
<li>someone who has <b>already passed it</b>, for example when you applied for settlement</li>
<li>someone with a <b>long-term physical or mental condition</b> that stops you taking it</li>
</ul>
<h2>Exemption for a long-term condition</h2>
<p>If a long-term physical or mental condition means you cannot take the test, you must send evidence with your application. GOV.UK says this should be either an <b>exemption form</b> or a <b>letter from a doctor</b> confirming your condition. Check the current form and guidance on the <a href="%(gov)s">GOV.UK Life in the UK Test page</a>.</p>
<h2>Already passed? You do not take it again</h2>
<p>If you passed the test for indefinite leave to remain, you do not need to sit it again when you apply for British citizenship. Use the unique reference number you got when you passed. Read more about your <a href="/life-in-the-uk-test-results-and-reference-number/">result and reference number</a>.</p>
<h2>Need help to take the test instead?</h2>
<p>Being exempt is different from needing support. If you have a disability, you can ask for reasonable adjustments when you book, such as extra equipment or help getting into the test centre.</p>
<h2>Other requirements still apply</h2>
<p>An exemption from the Life in the UK Test does not automatically exempt you from other requirements, such as showing your knowledge of English. Each route has its own rules, so check GOV.UK or ask an immigration adviser regulated in the UK.</p>
<p><i>This page is general information, not legal advice.</i></p>
""".replace("%(gov)s", GOV),
        faq=[
            ("Who is exempt from the Life in the UK Test?", "People under 18, people aged 65 or over, people who have already passed it, and people with a long-term physical or mental condition who provide an exemption form or a doctor's letter."),
            ("Do I need to take the test again for citizenship if I passed for ILR?", "No. If you have already passed, you use the same pass and do not take it again."),
            ("Can I get help to take the test if I have a disability?", "Yes. You can ask for reasonable adjustments, such as extra equipment or help accessing the centre, when you book."),
        ],
    ),
    dict(
        slug="life-in-the-uk-test-results-and-reference-number",
        title="Life in the UK Test Results and Unique Reference Number",
        desc="How you get your Life in the UK Test result, what the unique reference number is, how to use it for ILR or citizenship and what to do if you lose your letter.",
        h1="Life in the UK Test results and your unique reference number",
        crumb="Results and reference number",
        lead="You need 75% to pass. If you pass, you get a unique reference number, which you need for your application.",
        body="""
<h2>Getting your result</h2>
<p>The pass mark is <b>75%</b>, which means at least 18 of the 24 questions correct. You find out your result at the test centre after you finish.</p>
<h2>Your unique reference number</h2>
<p>When you pass, you get a <b>unique reference number</b>. You need this number when you apply for <b>indefinite leave to remain (settlement)</b> or <b>British citizenship</b>, so keep it somewhere safe, such as a note on your phone and a printed copy at home.</p>
<p>If you passed before <b>17 December 2019</b>, you were given a <b>pass notification letter</b> with a test reference ID instead. You use that letter in your application.</p>
<h2>One pass, two applications</h2>
<p>If you passed when you applied for settlement, you do not need to take the test again for citizenship. Use the same pass. See who else does not need to sit the test on our <a href="/life-in-the-uk-test-exemptions/">exemptions page</a>.</p>
<h2>What if I lose my pass letter?</h2>
<p>If you have lost your pass notification letter, GOV.UK says to write a letter explaining this and send it with your citizenship or settlement application. Include as many details of your test as you can, such as the date and the test centre.</p>
<h2>If you did not pass</h2>
<p>You can book again and pay the fee again. Use your result to find your weak areas. Our <a href="/life-in-the-uk-test-retake-rules/">retake guide</a> explains a plan for the next attempt.</p>
""",
        faq=[
            ("When do I get my Life in the UK Test result?", "At the test centre, after you finish the test."),
            ("What is the Life in the UK Test unique reference number?", "The number you get when you pass. You need it for your settlement or citizenship application."),
            ("What if I lost my Life in the UK Test pass letter?", "Write a letter explaining that you lost it and send it with your application, as GOV.UK advises."),
        ],
    ),
]

HUB = dict(
    slug="life-in-the-uk-test-guides",
    title="Life in the UK Test Guides: Chapter Summaries and Answers",
    desc="Free Life in the UK Test guides: every handbook chapter, pass mark, cost, booking, exemptions, results, retakes and how long to study.",
)
