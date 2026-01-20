import random
from word_bank import ACTION_VERBS, ROLE_OBJECTS, SKILL_KEYWORDS

# ---------- CLEANING ---------- #
def clean_name(name):
    return " ".join(word.capitalize() for word in name.strip().split())

# ---------- ROLE NORMALIZATION ---------- #
def normalize_experience(role):
    role_lower = role.lower()

    if role_lower in ROLE_OBJECTS:
        return ROLE_OBJECTS[role_lower]

    for key in ROLE_OBJECTS:
        if key in role_lower:
            return ROLE_OBJECTS[key]

    return "assigned responsibilities and team objectives"

# ---------- KEYWORD HANDLING ---------- #
def get_skill_keywords(role):
    role_lower = role.lower()

    if role_lower in SKILL_KEYWORDS:
        keywords = SKILL_KEYWORDS[role_lower]
        return random.sample(keywords, min(2, len(keywords)))

    return ["professional skills", "team collaboration"]

# ---------- BULLET GENERATION ---------- #
def generate_bullets(skill, role, n=5):
    bullets = []
    used_verbs = set()

    object_phrase = normalize_experience(role)
    keywords = get_skill_keywords(role)

    templates = [
        "{verb} {object}",
        "{verb} {object} to support organizational goals",
        "{verb} {object} while applying {keyword1}",
        "{verb} {object} in collaboration with team members",
        "{verb} {object} while developing {keyword1} and {keyword2}"
    ]

    for _ in range(n):
        verb = random.choice(ACTION_VERBS[skill])
        while verb in used_verbs and len(used_verbs) < len(ACTION_VERBS[skill]):
            verb = random.choice(ACTION_VERBS[skill])
        used_verbs.add(verb)

        template = random.choice(templates)

        bullet = template.format(
            verb=verb,
            object=object_phrase,
            keyword1=keywords[0],
            keyword2=keywords[1] if len(keywords) > 1 else "cross-functional collaboration"
        )

        bullets.append(bullet)

    return bullets

# ---------- PROGRAM START ---------- #
print("\n=== Life Experience → Resume Translator ===\n")

name = clean_name(input("Enter your full name: "))
experiences = []

while True:
    add = input("\nAdd an experience? (y/n): ").lower()
    if add not in ("y", "yes"):
        break

    category = input("Category (Work / Volunteer / Other): ").strip().title()
    role = input("Role / Position Title: ").strip()

    print("\nChoose the skill this experience highlights:")
    skills = list(ACTION_VERBS.keys())
    for i, s in enumerate(skills, 1):
        print(f"  {i}. {s}")

    try:
        skill_choice = int(input("Enter number: "))
        skill = skills[skill_choice - 1]
    except:
        skill = "Leadership"

    bullets = generate_bullets(skill, role)

    print("\nSuggested bullet points:")
    for i, b in enumerate(bullets, 1):
        print(f"  {i}. {b}")

    selected = []
    while len(selected) < 3:
        choice = input(f"Choose bullet #{len(selected)+1} (1–5, Enter to stop): ").strip()
        if choice == "":
            break
        try:
            idx = int(choice) - 1
            if bullets[idx] not in selected:
                selected.append(bullets[idx])
        except:
            pass

    experiences.append({
        "category": category,
        "role": role.title(),
        "bullets": selected
    })

# ---------- OUTPUT ---------- #
print("\n" + "="*50)
print("PROFESSIONAL RESUME – EXPERIENCE")
print("="*50)
print(f"\nName: {name}\n")

for cat in sorted(set(e["category"] for e in experiences)):
    print(f"--- {cat.upper()} ---\n")
    for e in experiences:
        if e["category"] == cat:
            print(e["role"])
            for b in e["bullets"]:
                print(f"  • {b}")
            print()

print("="*50)
