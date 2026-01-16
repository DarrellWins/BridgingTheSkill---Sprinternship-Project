# word_bank.py
ACTION_VERBS = {
    "Problem Solving": [
        "Analyze", "Anticipate", "Compare", "Compile", "Consolidate",
        "Correlate", "Diagnose", "Evaluate", "Examine", "Expedite",
        "Identify", "Implement", "Improve", "Inspect", "Investigate",
        "Research", "Resolve", "Review", "Revise", "Survey",
        "Systematize", "Troubleshoot", "Update", "Validate", "Verify"
    ],

    "Communication": [
        "Advise", "Communicate", "Conduct", "Confer", "Consult",
        "Correspond", "Counsel", "Disseminate", "Edit", "Explain",
        "Inform", "Instruct", "Interpret", "Notify", "Present",
        "Propose", "Recommend", "Report", "Request", "Respond",
        "Summarize", "Transcribe", "Write"
    ],

    "Leadership": [
        "Administer", "Assign", "Authorize", "Coordinate", "Delegate",
        "Determine", "Direct", "Dispatch", "Drive", "Endorse",
        "Enforce", "Ensure", "Execute", "Facilitate", "Instruct",
        "Lead", "Maintain", "Manage", "Oversee", "Plan",
        "Prioritize", "Promote", "Represent", "Supervise"
    ],

    "Human Relations": [
        "Advise", "Assist", "Collaborate", "Cooperate",
        "Coordinate", "Facilitate", "Guide", "Participate", "Promote"
    ],

    "Creative": [
        "Adapt", "Arrange", "Assemble", "Create", "Design",
        "Develop", "Devise", "Draft", "Establish",
        "Generate", "Initiate", "Innovate", "Prepare", "Produce"
    ],

    "Taking Action": [
        "Assemble", "Circulate", "Collate", "Collect", "Distribute",
        "Furnish", "Obtain", "Operate", "Organize", "Perform",
        "Proceed", "Process", "Provide", "Retrieve", "Secure",
        "Select", "Solicit", "Submit", "Train"
    ]
}

# Optional: small mapping of past-tense to base verbs
PAST_TO_BASE = {
    "Made": "Create",
    "Created": "Create",
    "Developed": "Develop",
    "Led": "Lead",
    "Managed": "Manage",
    "Assisted": "Assist",
    "Organized": "Organize",
    "Implemented": "Implement",
    "Designed": "Design",
    "Generated": "Generate",
    "Produced": "Produce",
    "Facilitated": "Facilitate",
    "Performed": "Perform",
    "Prepared": "Prepare"
}
