import random
from word_bank import ACTION_VERBS, SKILL_KEYWORDS

# ---------- CLEANING FUNCTIONS ---------- #
def clean_name(name):
    """Capitalizes each part of the name correctly"""
    return " ".join(word.capitalize() for word in name.strip().split())

def get_skill_keywords(role):
    """Get relevant skill keywords for a role"""
    role_lower = role.lower()
    
    # Check if we have specific keywords for this role
    if role_lower in SKILL_KEYWORDS:
        return random.sample(SKILL_KEYWORDS[role_lower], min(2, len(SKILL_KEYWORDS[role_lower])))
    
    # Default keywords if role not found
    return ["professional skills", "team collaboration"]

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
        "server": "customers with dining service and hospitality",
        "intern": "team members through internship responsibilities",
        "teacher": "students through educational instruction",
        "receptionist": "visitors and clients with administrative tasks",
        "sales associate": "customers with product selection and purchases",
        "camp counselor": "campers through recreational activities and supervision"
    }
    
    return mappings.get(sentence, sentence)
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
def generate_bullets(sentence, skill, role, n=3):
    """Generate professional resume bullet points with skill keywords"""
    bullets = []
    used_verbs = set()
    
    object_phrase = normalize_experience(sentence)
    keywords = get_skill_keywords(role)
    
    # Better templates with proper grammar and keyword integration
    templates = [
        "{verb} {object}",
        "{verb} and supported {object}",
        "{verb} {object} to achieve program goals",
        "{verb} {object}, utilizing {keyword1}",
        "{verb} {object} while developing {keyword1} and {keyword2}"
    ]
    
    for _ in range(n):
        # Get a unique action verb
        verb = random.choice(ACTION_VERBS[skill])
        while verb in used_verbs and len(used_verbs) < len(ACTION_VERBS[skill]):
            verb = random.choice(ACTION_VERBS[skill])
        used_verbs.add(verb)
        
        # Select template
        template = random.choice(templates)
        
        # Create bullet point with keywords if template uses them
        if "{keyword1}" in template:
            bullet = template.format(
                verb=verb,
                object=object_phrase,
                keyword1=keywords[0] if len(keywords) > 0 else "professional skills",
                keyword2=keywords[1] if len(keywords) > 1 else "team collaboration"
            )
        else:
            bullet = template.format(
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
    role = input("Role/Position title (e.g., 'Student Mentor', 'Cashier', 'Tutor'): ").strip().title()
    
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
    
    bullets = generate_bullets(role, skill, role)
    
    print("\nSuggested bullet points:")
    for i, b in enumerate(bullets, 1):
        print(f"  {i}. {b}")
    
    try:
        choice = int(input("Choose the best bullet (1-3): "))
        if 1 <= choice <= 3:
            experiences.append({
                "category": category,
                "role": role,
                "bullet": bullets[choice - 1]
            })
        else:
            print("Invalid choice. Using first option.")
            experiences.append({
                "category": category,
                "role": role,
                "bullet": bullets[0]
            })
    except ValueError:
        print("Invalid input. Using first option.")
        experiences.append({
            "category": category,
            "role": role,
            "bullet": bullets[0]
        })

# ---------- OUTPUT ---------- #
print("\n\n" + "="*50)
print("PROFESSIONAL RESUME - EXPERIENCE SECTION")
print("="*50 + "\n")
print(f"Name: {name}\n")

# Group and display by category, then by role
for cat in sorted(set(e["category"] for e in experiences)):
    print(f"--- {cat.upper()} ---\n")
    # Get all unique roles within this category
    roles_in_category = [(e["role"], e["bullet"]) for e in experiences if e["category"] == cat]
    
    for role, bullet in roles_in_category:
        print(f"{role}")
        print(f"  • {bullet}\n")

print("="*50)