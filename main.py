import random
from word_bank import ACTION_VERBS, PAST_TO_BASE

def best_verb(sentence, skill):
    words = sentence.split()
    for w in words:
        base = PAST_TO_BASE.get(w.capitalize(), w.capitalize())
        if base in ACTION_VERBS[skill]:
            return base
    return random.choice(ACTION_VERBS[skill])

def generate_bullets(sentence, skill, n=3):
    bullets = []
    used_verbs = set()
    adverbs = ["Successfully", "Effectively", "Efficiently", "Collaboratively", "Proactively"]
    templates = [
        "{verb} {adverb} {sentence}",
        "{verb} {sentence} to achieve results",
        "{verb} {adverb} by {sentence_lower}",
        "{verb} {adverb} in {sentence_lower}"
    ]
    
    sentence_lower = sentence.lower()  # precompute lowercase version
    
    for _ in range(n):
        verb = best_verb(sentence, skill)
        # avoid repeating verbs
        while verb in used_verbs and len(used_verbs) < len(ACTION_VERBS[skill]):
            verb = random.choice(ACTION_VERBS[skill])
        used_verbs.add(verb)
        
        adverb = random.choice(adverbs)
        template = random.choice(templates)
        
        # format the bullet
        bullet = template.format(verb=verb, adverb=adverb, sentence=sentence, sentence_lower=sentence_lower)
        bullets.append(bullet)
    
    return bullets


# Collect personal info
name = input("Enter your full name: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")

experiences = []

while True:
    add_exp = input("\nDo you want to add an experience? (y/n): ").lower()
    if add_exp != "yes" and add_exp != "y":
        break

    category = input("Enter category (Work/Volunteer/Other): ")
    sentence = input("Describe your experience in 1-2 sentences: ").strip()
    
    print("Choose the main skill this experience highlights:")
    for i, skill in enumerate(ACTION_VERBS.keys(), 1):
        print(f"{i}. {skill}")
    
    skill_choice = int(input("Enter the number of the skill: "))
    skill = list(ACTION_VERBS.keys())[skill_choice - 1]

    bullets = generate_bullets(sentence, skill, n=3)
    
    print("\nHere are 3 suggested bullet points for this experience:")
    for i, b in enumerate(bullets, 1):
        print(f"{i}. {b}")
    
    choice = int(input("Choose the number of the bullet you like best: "))
    chosen_bullet = bullets[choice - 1]

    experiences.append({
        "category": category,
        "bullet": chosen_bullet
    })

# Print resume
print("\n\n===== LIFE EXPERIENCE RESUME =====\n")
print(f"Name: {name}")
print(f"Email: {email} | Phone: {phone}")

categories = set([exp["category"] for exp in experiences])
for cat in categories:
    print(f"\n--- {cat.upper()} ---")
    for exp in experiences:
        if exp["category"] == cat:
            print(f" - {exp['bullet']}")
