'''
A custom trainer to train according to the Devfest Questions.
'''

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
chatterbot = ChatBot("Training our VIT Bot with some tests.")
chatterbot.set_trainer(ListTrainer)
chatterbot.train([
    "Hey",
    "Hello! How may I help you?",
])

chatterbot.train([
    "Which university is this?",
    "This is Vellore Institute of Technology.",
])

chatterbot.train([
    "Can you please tell me about VIT?",
    "VIT was established with the aim of providing quality higher education on par with international standards. It persistently seeks and adopts innovative methods to improve the quality of higher education on a consistent basis.The campus has a cosmopolitan atmosphere with students from all corners of the globe. Experienced and learned teachers are strongly encouraged to nurture the students. The global standards set at VIT in the field of teaching and research spur us on in our relentless pursuit of excellence. In fact, it has become a way of life for us. The highly motivated youngsters on the campus are a constant source of pride. Our Memoranda of Understanding with various international universities are our major strength. They provide for an exchange of students and faculty and encourage joint research projects for the mutual benefit of these universities. Many of our students, who pursue their research projects in foreign universities, bring high quality to their work and esteem to India and have done us proud. With steady steps, we continue our march forward. We look forward to meeting you here at VIT.",
])

chatterbot.train([
    "Facts about VIT?",
    "Over 2,23,000 appeared for the VIT Engineering Entrance Examination (VITEEE) in 2017\nThe institution offers 36 Undergraduate, 31 Post graduate, 4 Integrated and 3 Research Programmes.\nNAAC has re-accredited VIT with an 'A' grade.\nA 360-acre eco-friendly campus with over 50.83 lakh sq.ft. built-up space at Vellore.\nA 170 acre eco-friendly second campus at Chennai.\nOver 35,000 students, with nearly 1/3rd of them women\nStudents from 60 countries as well as from every state in India\nOver 1400 faculty and 1413 staff.\nVIT has been accredited by TCS, Wipro and Cognizant for academic collaboration and placements.\nEntered the Limca Book of Records for Campus Recruitment.",
])

#Schools in VIT

chatterbot.train([
    "Schools in vit",
    "There are several schools in VIT.\nSchool of Advanced Science (SAS)\nSchool of Architecture (V-SPARC )\nSchool of Bio Sciences & Technology (SBST)\nSchool of Civil and Chemical Engineering (SCALE)\nSchool of Computer Science and Engineering (SCOPE)\nSchool of Electrical Engineering (SELECT)\nSchool of Electronics Engineering (SENSE)\nSchool of Information Technology & Engineering (SITE)\nSchool of Mechanical Engineering(SMEC)\nSchool of Social Sciences & Languages\nVIT Business School (VIT BS)\nVIT Law School",
])
#Train if user says Bye! :/

chatterbot.train([
	'Bye',"Bye! I'll miss you!"])
