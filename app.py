from flask import Flask, render_template

app = Flask(__name__)

# Context Processor for global contact info
@app.context_processor
def inject_contact_info():
    return dict(contact_info={
        'name': 'Rishabh Kumar',
        'title': 'Robotics Engineer & Product Manager',
        'email': 'rkumar23@uw.edu',
        'phone': {
            'us': '+1-206-302-9094',
            'india': '+91 7503536147'
        },
        'location': 'Seattle, WA, USA',
        'social_links': [
            {'platform': 'linkedin', 'url': 'https://www.linkedin.com/in/your-linkedin/'},
            {'platform': 'portfolio', 'url': 'https://hellorishabh.wixsite.com/hello'}
        ]
    })

EXPERIENCES = [
    {
        'title': 'Senior Technical Product Manager - Robot Autonomy',
        'company': 'Clutterbot Technologies, Bengaluru',
        'period': "Dec '23 - Sept '24",
        'achievements': [
            'Led end-to-end product development from MVP to Beta, facilitating user testing and customer feedback loops.',
            'Unveiled 7+ innovative product features using deep customer insights, optimizing usability and experience (UX), including AI-driven navigation and vision-based autonomous features.',
            'Improved 5 key product performance metrics by aligning cross-functional collaboration, focusing on product discovery and data-driven insights.',
            'Owned and authored detailed Product Requirement Documents (PRDs) for autonomy software systems, reducing development time by 20% through technical feasibility assessments of ML models and prioritization.',
            'Engaged with customer researchers to design user studies and extract valuable insights from data for prioritization strategies; resulting in 40% improvement in key metric and positive customer feedback.'
        ]
    },
    {
        'title': 'Product Manager - Mobile Robotics',
        'company': 'Adverb Technologies, Noida',
        'period': "May '22 - Dec '23",
        'achievements': [
            'Defined product vision, strategy and roadmap with comprehensive market research, competitor analysis, user requirements, and customer feedback for 5+ variants of Zippy product family.',
            'Streamlined the product development lifecycle using Agile and Stage Gate methodologies, reducing time to market by 30%.',
            'Collaborated with sales, engineering, legal and customer success teams to prioritize features and deliver customer centric solutions that resulted in 5+ repeat orders across Europe, Americas, Asia and Australia.',
            'Spearheaded product lifecycle management for Fleet Management Software, adding features and simulation capability, improving solution turn-around time by 60% through API integration and process automation.'
        ]
    },
    {
        'title': 'Engineer - Mobile Robotics',
        'company': 'Noida, India and Melbourne, Australia',
        'period': "July '19 - May '22",
        'achievements': [
            'Led R&D initiatives for new software modules and prototyping; with product demos and planning.',
            'Spearheaded robot system integration and design development, enhancing automated QA testing processes.',
            'Managed and delivered project for successful large-scale deployment of mobile robots, infrastructure, software suite setup and User Acceptance Testing (UAT) in Melbourne, achieving a 98% up time.'
        ]
    }
]

EDUCATIONS = [
    {
        'degree': 'Masters of Science Innovation Technology',
        'institution': 'University of Washington',
        'year': "Sept '24 - March '26",
        'details': 'Courses in Technology Strategy, Entrepreneurship, Design Thinking, Programming, Prototyping'
    },
    {
        'degree': 'Bachelors of Technology in Mechanical Engineering',
        'institution': 'Delhi Technological University, Delhi',
        'year': "Aug '15 - May '19",
        'details': ''
    }
]

SKILLS = [
    {
        'category': 'Product Management and Development',
        'items': [
            'Scrum & Agile Frameworks', 'OKRs & KPIs setting', 'Market Analysis',
            'Product Planning', 'Road-Mapping', 'User Research', 'Go-To-Market & Product Launch strategies'
        ]
    },
    {
        'category': 'PM Tools',
        'items': [
            'Jira', 'Azure DevOps', 'Miro', 'ProdPad', 'Dovetail', 'MS Office Suite'
        ]
    },
    {
        'category': 'Technical Skills and Tools',
        'items': [
            'C/C++', 'Python', 'ROS/ROS2', 'Git', 'SolidWorks', 'Autodesk Fusion'
        ]
    }
]

ADDITIONAL_INFO = [
    {
        'title': 'Advance Certificate in Product Management from XLRI, Virtual Interactive Learning',
        'year': "March '22 - Jan '23"
    },
    {
        'title': 'Udacity Nanodegree in C++ Programming',
        'year': "April '20 - July '20"
    },
    {
        'title': 'Shortlisted for Phase D of Indian Air Force, MBC for FOD detection using Drone swarm',
        'year': "Feb '23"
    },
    {
        'title': 'Excellence award for best international team, Robocon 2018, Wuhan, China',
        'year': "July '18"
    }
]

portfolio_items = [
    {
        "title": "Meher Baba Competition 2022",
        "description": "One of the most prestigious technological innovation challenges in the country, organized by the Indian Air Force. The problem statement combines technologies such as swarm, UAV autonomy, robotics, AI, ML, and computer vision to solve a practical problem and push the limits of technology and innovation in India.",
        "image": "Meher Baba Competition 2022.jpg"
    },
    {
        "title": "Soft Robotics",
        "description": "My master's thesis in the year 2019 was based in fabrication of Soft Robotics Actuators using 3D printing and their study to propose new applications.",
        "image": "Soft Robotics.jpg"
    },
    {
        "title": "Product Management",
        "description": "Along with my technical skills, I also have experience in product management. I have led several projects from ideation to launch, ensuring that they met the customer requirements and were delivered on time. My skills in product management have helped me understand the business side of robotics and have enabled me to develop a holistic approach towards problem-solving.",
        "image": "Product Management.jpg"
    },
    {
        "title": "Industrial Mobile Robots",
        "description": "I have extensive experience in the design and development of mobile robots. I have worked on the drive system—sensor integration and selection, hardware-software integration, controllers and planners, and robot dynamics.",
        "image": "Industrial Mobile Robots.jpg"
    },
    {
        "title": "Consumer Robotics",
        "description": "My experience in consumer robotics revolves around developing intelligent behaviors for human-robot interaction. I worked with robotics and Machine Learning teams to harness the power of robot autonomy and Artificial Intelligence for household application of robots.",
        "image": "Consumer Robotics.jpg"
    },
    {
        "title": "DTU Altair Projects",
        "description": "I was the captain and co-founder of the robotics technical group at Delhi Technological University. The team DTU Altair (Advance Lean in Technology and Intelligent Robotics), was started with the motivation of bringing students from diverse engineering fields together to work on multidisciplinary projects and research.",
        "image": "DTU Altair Projects.jpg"
    }
]

# Routes with unique function names
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", portfolio_items=portfolio_items)

@app.route("/resume")
def resume():
    return render_template("resume.html",
        experiences=EXPERIENCES,
        educations=EDUCATIONS,
        skills=SKILLS,
        additional_info=ADDITIONAL_INFO
    )

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
