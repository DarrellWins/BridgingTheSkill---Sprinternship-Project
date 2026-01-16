import random

# Action verbs organized by skill category
ACTION_VERBS = {
    "Leadership": [
        "Coordinated", "Directed", "Facilitated", "Guided", 
        "Led", "Managed", "Mentored", "Supervised", "Organized"
    ],
    "Communication": [
        "Advised", "Collaborated", "Consulted", "Presented",
        "Communicated with", "Engaged", "Counseled", "Instructed"
    ],
    "Problem-Solving": [
        "Analyzed", "Assessed", "Developed", "Implemented",
        "Improved", "Resolved", "Streamlined", "Designed"
    ],
    "Teamwork": [
        "Assisted", "Contributed to", "Partnered with", 
        "Supported", "Cooperated with", "Helped", "Aided"
    ]
}

# ---------- CLEANING FUNCTIONS ---------- #
def clean_name(name):
    """Capitalizes each part of the name correctly"""
    return " ".join(word.capitalize() for word in name.strip().split())

def normalize_experience(sentence):
    """Turns short phrases into complete resume-ready bullet points"""
    sentence = sentence.strip().lower()
    
    # Common experience mappings
    mappings = {
        "student mentor": "students through academic mentoring programs",
        "mentor": "peers through one-on-one mentoring sessions",
        "volunteer": "community members through volunteer service initiatives",
        "tutor": "students with challenging academic coursework",
        "caregiver": "individuals with daily caregiving and personal assistance",
        "babysitter": "children with childcare and educational activities",
        "coach": "team members through sports coaching and training",
        "cashier": "customers with transactions and store operations",
        "server": "customers with dining service and hospitality"
    }
    
    return mappings.get(sentence, sentence)

# ---------- BULLET GENERATION ---------- #
def generate_bullets(sentence, skill, n=3):
    """Generate professional resume bullet points"""
    bullets = []
    used_verbs = set()
    
    object_phrase = normalize_experience(sentence)
    
    # Better templates with proper grammar
    templates = [
        "{verb} {object}",
        "{verb} and supported {object}",
        "{verb} {object} to achieve program goals"
    ]
    
    for _ in range(n):
        # Get a unique action verb
        verb = random.choice(ACTION_VERBS[skill])
        while verb in used_verbs and len(used_verbs) < len(ACTION_VERBS[skill]):
            verb = random.choice(ACTION_VERBS[skill])
        used_verbs.add(verb)
        
        # Create bullet point
        bullet = random.choice(templates).format(
            verb=verb,
            object=object_phrase
        )
        bullets.append(bullet)
    
    return bullets

# ---------- PROGRAM START ---------- #
print("=== Life Experience → Resume Translator ===\n")

# Get name with proper capitalization
name = clean_name(input("Enter your full name: "))

experiences = []

# Collect experiences
while True:
    add = input("\nAdd an experience? (y/n): ").lower()
    if add not in ("y", "yes"):
        break
    
    category = input("Category (Work / Volunteer / Other): ").strip().title()
    sentence = input("Describe your experience (e.g., 'student mentor', 'cashier', 'tutor'): ")
    
    print("\nChoose the skill this experience highlights:")
    skills = list(ACTION_VERBS.keys())
    for i, s in enumerate(skills, 1):
        print(f"  {i}. {s}")
    
    try:
        skill_choice = int(input("Enter number (1-4): "))
        if 1 <= skill_choice <= len(skills):
            skill = skills[skill_choice - 1]
        else:
            print("Invalid choice. Defaulting to Leadership.")
            skill = skills[0]
    except ValueError:
        print("Invalid input. Defaulting to Leadership.")
        skill = skills[0]
    
    bullets = generate_bullets(sentence, skill)
    
    print("\nSuggested bullet points:")
    for i, b in enumerate(bullets, 1):
        print(f"  {i}. {b}")
    
    try:
        choice = int(input("Choose the best bullet (1-3): "))
        if 1 <= choice <= 3:
            experiences.append({
                "category": category,
                "bullet": bullets[choice - 1]
            })
        else:
            print("Invalid choice. Using first option.")
            experiences.append({
                "category": category,
                "bullet": bullets[0]
            })
    except ValueError:
        print("Invalid input. Using first option.")
        experiences.append({
            "category": category,
            "bullet": bullets[0]
        })

# ---------- OUTPUT ---------- #
print("\n\n" + "="*50)
print("PROFESSIONAL RESUME - EXPERIENCE SECTION")
print("="*50 + "\n")
print(f"Name: {name}\n")

# Group and display by category
for cat in sorted(set(e["category"] for e in experiences)):
    print(f"--- {cat.upper()} ---")
    for e in experiences:
        if e["category"] == cat:
            print(f"  • {e['bullet']}")
    print()

print("="*50)