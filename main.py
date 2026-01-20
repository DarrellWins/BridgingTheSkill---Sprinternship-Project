import random
from word_bank import ACTION_VERBS, SKILL_KEYWORDS, EXPERIENCE_MAPPINGS

# ---------- CLEANING FUNCTIONS ---------- #
def clean_name(name):
    """Capitalizes each part of the name correctly"""
    return " ".join(word.capitalize() for word in name.strip().split())

def get_skill_keywords(role):
    """Get relevant skill keywords for a role"""
    role_lower = role.lower()
    
    # Check for exact match
    if role_lower in SKILL_KEYWORDS:
        keywords = SKILL_KEYWORDS[role_lower].copy()
        return random.sample(keywords, min(2, len(keywords)))
    
    # Check for partial matches
    for key in SKILL_KEYWORDS:
        if key in role_lower or role_lower in key:
            keywords = SKILL_KEYWORDS[key].copy()
            return random.sample(keywords, min(2, len(keywords)))
    
    # Generic keywords for unknown roles
    return ["professional development", "operational excellence"]

def normalize_experience(role):
    """Turns role into complete resume-ready phrases"""
    role_lower = role.lower()
    
    # Check for exact match
    if role_lower in EXPERIENCE_MAPPINGS:
        return EXPERIENCE_MAPPINGS[role_lower]
    
    # Check for partial matches
    for key in EXPERIENCE_MAPPINGS:
        if key in role_lower:
            return EXPERIENCE_MAPPINGS[key]
    
    # Generate grammatically correct phrase for unknown roles
    if 'manager' in role_lower or 'supervisor' in role_lower or 'director' in role_lower:
        return "team operations and organizational objectives"
    elif 'assistant' in role_lower or 'aide' in role_lower:
        return "daily operations and team support functions"
    elif 'associate' in role_lower or 'representative' in role_lower:
        return "customer needs and organizational services"
    elif 'coordinator' in role_lower or 'specialist' in role_lower:
        return "project initiatives and stakeholder requirements"
    else:
        return "organizational goals and professional responsibilities"

# ---------- BULLET GENERATION ---------- #
def generate_bullets(role, skill, n=5):
    """Generate professional resume bullet points with skill keywords"""
    bullets = []
    used_verbs = set()
    
    object_phrase = normalize_experience(role)
    keywords = get_skill_keywords(role)
    
    # Varied templates with better grammar and natural phrasing
    templates = [
        lambda v, o, k: f"{v} {o}",
        lambda v, o, k: f"{v} {o} to meet organizational standards",
        lambda v, o, k: f"{v} {o} while maintaining quality benchmarks",
        lambda v, o, k: f"{v} {o} through {k[0]}",
        lambda v, o, k: f"{v} {o} utilizing {k[0]} and {k[1]}",
        lambda v, o, k: f"{v} {o}, emphasizing {k[0]}",
        lambda v, o, k: f"{v} {o} in alignment with team objectives",
        lambda v, o, k: f"{v} {o} with focus on {k[0]}",
        lambda v, o, k: f"{v} {o} to enhance operational effectiveness",
        lambda v, o, k: f"{v} {o} by implementing {k[0]}"
    ]
    
    # Shuffle templates for variety
    random.shuffle(templates)
    
    for i in range(n):
        # Get a unique action verb
        verb = random.choice(ACTION_VERBS[skill])
        attempts = 0
        while verb in used_verbs and attempts < 20:
            verb = random.choice(ACTION_VERBS[skill])
            attempts += 1
        used_verbs.add(verb)
        
        # Select template
        template = templates[i % len(templates)]
        
        # Create bullet point
        bullet = template(verb, object_phrase, keywords)
        bullets.append(bullet)
    
    return bullets

# ---------- PROGRAM START ---------- #
print("=== Life Experience → Resume Translator ===")
print("By: Darrell Cox\n")

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
    
    bullets = generate_bullets(role, skill)
    
    print("\nSuggested bullet points:")
    for i, b in enumerate(bullets, 1):
        print(f"  {i}. {b}")
    
    # Allow user to select 2-3 bullets
    print("\nSelect 2-3 bullet points for this role.")
    selected_bullets = []
    
    while len(selected_bullets) < 3:
        try:
            if len(selected_bullets) >= 2:
                choice_input = input(f"Choose bullet #{len(selected_bullets) + 1} (1-5, or press Enter to finish): ").strip()
                if choice_input == "":
                    break
                choice = int(choice_input)
            else:
                choice = int(input(f"Choose bullet #{len(selected_bullets) + 1} (1-5): "))
            
            if 1 <= choice <= 5:
                if bullets[choice - 1] not in selected_bullets:
                    selected_bullets.append(bullets[choice - 1])
                else:
                    print("You already selected that bullet. Choose a different one.")
            else:
                print("Invalid choice. Please enter a number between 1-5.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1-5.")
    
    if len(selected_bullets) < 2:
        print("You must select at least 2 bullets. Adding first two by default.")
        selected_bullets = bullets[:2]
    
    # Add all selected bullets to experiences
    experiences.append({
        "category": category,
        "role": role,
        "bullets": selected_bullets
    })

# ---------- OUTPUT ---------- #
print("\n\n" + "="*50)
print("PROFESSIONAL RESUME - EXPERIENCE SECTION")
print("="*50 + "\n")
print(f"Name: {name}\n")

# Group and display by category, then by role
for cat in sorted(set(e["category"] for e in experiences)):
    print(f"--- {cat.upper()} ---\n")
    # Get all roles and their bullets within this category
    roles_in_category = [(e["role"], e["bullets"]) for e in experiences if e["category"] == cat]
    
    for role, bullets in roles_in_category:
        print(f"{role}")
        for bullet in bullets:
            print(f"  • {bullet}")
        print()

print("="*50)