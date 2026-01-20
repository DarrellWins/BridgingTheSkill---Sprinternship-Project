# word_bank.py
# Expanded role intelligence + action verbs + skill keywords

ACTION_VERBS = {
    "Leadership": [
        "Led", "Directed", "Coordinated", "Supervised",
        "Managed", "Mentored", "Facilitated", "Guided"
    ],
    "Communication": [
        "Communicated", "Presented", "Advised", "Consulted",
        "Engaged", "Collaborated", "Instructed"
    ],
    "Problem-Solving": [
        "Analyzed", "Developed", "Designed", "Implemented",
        "Improved", "Resolved", "Streamlined"
    ],
    "Teamwork": [
        "Collaborated", "Partnered", "Supported",
        "Contributed", "Assisted", "Aided"
    ],
    "Creative": [
        "Created", "Designed", "Produced",
        "Developed", "Generated", "Conceptualized"
    ],
    "Taking Action": [
        "Executed", "Initiated", "Completed",
        "Delivered", "Launched", "Implemented"
    ]
}

# Role → Resume Object (CRITICAL)
ROLE_OBJECTS = {
    "tech intern": "technical projects and team initiatives",
    "software intern": "software development tasks and team projects",
    "data intern": "data analysis and reporting tasks",
    "intern": "assigned projects and operational responsibilities",

    "math tutor": "students in core mathematics concepts",
    "tutor": "students through individualized academic instruction",

    "student mentor": "students through structured mentoring programs",
    "mentor": "peers through professional development support",

    "cashier": "customers with transactions and point-of-sale operations",
    "sales associate": "customers with product selection and service",

    "research assistant": "data collection, analysis, and research documentation",
    "volunteer": "community members through service initiatives",
    "caregiver": "individuals with daily living and personal support",

    "teacher": "students through instructional planning and delivery",
    "coach": "team members through training and performance development",
    "camp counselor": "campers through supervised activities and programs"
}

# Skill keywords for enrichment
SKILL_KEYWORDS = {
    "tech intern": ["industry best practices", "technical documentation"],
    "intern": ["project collaboration", "professional communication"],
    "tutor": ["personalized learning strategies", "academic progress tracking"],
    "mentor": ["goal setting", "professional development"],
    "volunteer": ["community outreach", "program coordination"],
    "research assistant": ["data accuracy", "analytical methodologies"]
}
