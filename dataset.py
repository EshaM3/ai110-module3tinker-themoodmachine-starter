"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    "laughing",
    "yay",
    "yippee",
    "yipee",
    "stand",
    "thank",
    "tyty",
    "ty",
    "bright",
    "crushed",
    "hopeful",
    "glad",
    "slay",
    "poggers"
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    "bs",
    "nonsense",
    "dislike",
    "wrong",
    "annoying",
    "annoyed",
    "queasy",
    "bombed",
    "mad"
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")

SAMPLE_POSTS.append("What's wrong with you")
TRUE_LABELS.append("negative")
SAMPLE_POSTS.append("I crushed that test")
TRUE_LABELS.append("positive")
SAMPLE_POSTS.append("I bombed that test")
TRUE_LABELS.append("negative")
SAMPLE_POSTS.append("I'm feeling pretty queasy today 🤢")
TRUE_LABELS.append("negative")
SAMPLE_POSTS.append("What on Earth is that")
TRUE_LABELS.append("neutral")
SAMPLE_POSTS.append("Girl you're crazy 🤣")
TRUE_LABELS.append("positive")
SAMPLE_POSTS.append("That's wild 💀")
TRUE_LABELS.append("negative")
SAMPLE_POSTS.append("WHYYYY 😭")
TRUE_LABELS.append("negative")
SAMPLE_POSTS.append("That movie was mid")
TRUE_LABELS.append("neutral")
SAMPLE_POSTS.append("Bruh why do I keep forgetting my umbrella :(")
TRUE_LABELS.append("negative")
SAMPLE_POSTS.append("Got the internship!!! 😭✨")
TRUE_LABELS.append("positive")
SAMPLE_POSTS.append("I can't stand them")
TRUE_LABELS.append("negative")
SAMPLE_POSTS.append("YAY")
TRUE_LABELS.append("positive")
SAMPLE_POSTS.append("YIPPEE :D")
TRUE_LABELS.append("positive")
SAMPLE_POSTS.append("I love it")
TRUE_LABELS.append("positive")
SAMPLE_POSTS.append("Uhh idk man")
TRUE_LABELS.append("mixed")
SAMPLE_POSTS.append("I’m fine. Totally fine. Definitely fine.")
TRUE_LABELS.append("mixed")
SAMPLE_POSTS.append("I lowkey have no idea what that is")
TRUE_LABELS.append("neutral")
SAMPLE_POSTS.append("This weather is giving me life ☀️")
TRUE_LABELS.append("positive")
SAMPLE_POSTS.append("Who does he think he is")
TRUE_LABELS.append("negative")
SAMPLE_POSTS.append("Thank you :)")
TRUE_LABELS.append("positive")
SAMPLE_POSTS.append("tyty")
TRUE_LABELS.append("positive")
SAMPLE_POSTS.append("That was sooo useful 🙄")
TRUE_LABELS.append("negative")
SAMPLE_POSTS.append("That was so scary 😨")
TRUE_LABELS.append("negative")
SAMPLE_POSTS.append("feeling sad but kinda mad. happy but kinda queasy.")
TRUE_LABELS.append("mixed")
SAMPLE_POSTS.append("YIPPEE BEST DAY EVER")
TRUE_LABELS.append("positive")

#
# Remember to keep them aligned:
# print(len(SAMPLE_POSTS) == len(TRUE_LABELS))
