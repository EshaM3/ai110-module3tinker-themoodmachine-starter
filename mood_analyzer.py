# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS

import string
import re


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.

        TODO: Improve this method.

        Right now, it does the minimum:
          - Strips leading and trailing whitespace
          - Converts everything to lowercase
          - Splits on spaces

        Ideas to improve:
          - Remove punctuation
          - Handle simple emojis separately (":)", ":-(", "🥲", "😂")
          - Normalize repeated characters ("soooo" -> "soo")
        """

        # Handle simple emojis separately
        SIMPLE_EMOJI_MAP = {
          ":)": "happy",
          ":-)": "happy",
          ":(": "sad",
          ":-(": "sad",
          ">:(": "angry",
          ":D": "excited",
          ">:D": "fun",
          "D:": "sad",
          "😄": "happy",
          "😊": "happy",
          "😆": "laughing",
          "😂": "laughing",
          "🤣": "laughing",
          "🥲": "sad",
          "😢": "sad",
          "😔": "sad",
          "😞": "sad",
          "❤️": "love",
          "💗": "love",
          "💘": "love",
          "💝": "love",
          "💖": "love",
          "💓": "love",
          "💞": "love",
          "💕": "love",
          "😡": "angry",
          "😠": "angry",
          "🤬": "angry",
          "🙄": "annoyed",
          "☀️": "bright",
          "🤢": "queasy"
        }
        for emoji, replacement in SIMPLE_EMOJI_MAP.items():
            text = text.replace(emoji, f" {replacement} ")

        # lowercase + remove leading/trailing spaces
        text = text.strip().lower()

        # normalize stretched out words like soooooo to just soo
        text = re.sub(r'(.)\1{2,}', r'\1\1', text)

        # handle emotive abbreviations separately
        text = text.replace("lol", "laughing")
        text = text.replace("lmao", "laughing")
        
        # make contractions negations for easier scoring
        CONTRACTIONS = {
          "can't": "can not",
          "won't": "will not",
          "don't": "do not",
          "doesn't": "does not",
          "isn't": "is not",
          "wasn't": "was not",
          "didn't": "did not",
          "wouldn't": "would not",
          "couldn't": "could not",
          "shouldn't": "should not",
        }
        for contraction, expanded in CONTRACTIONS.items():
            text = text.replace(contraction, expanded)

        # Attempts to target sarcastic phrasing
        SARCASTIC_PHRASES = {
            "love getting stuck in traffic": "hate traffic",
            "love mondays": "hate mondays",
            "love being ignored": "hate being ignored",
            "oh great": "bad",
            "yeah right": "disbelief",
            "just wonderful": "bad",
            "oh fantastic": "bad",
        }

        for phrase, replacement in SARCASTIC_PHRASES.items():
            text = text.replace(phrase, replacement)


        # Remove punctuation
        cleaned = "".join(filter(lambda x: x not in string.punctuation, text))
        
        # tokenize
        tokens = cleaned.split()

        # Remove stop/filler words
        STOPWORDS = {"the", "a", "an", "is", "it", "in", "on", "at", "to", "and", "or", "but", "i", "you", "we", "they", "just", "really", "kinda", "of", "sorta", "feeling", "feelin", "too"}

        tokens = [t for t in tokens if t not in STOPWORDS]

        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> tuple[int, bool]:
        """
        Compute a numeric "mood score" for the given text.

        Positive words increase the score.
        Negative words decrease the score.

        TODO: You must choose AT LEAST ONE modeling improvement to implement.
        For example:
          - Handle simple negation such as "not happy" or "not bad"
          - Count how many times each word appears instead of just presence
          - Give some words higher weights than others (for example "hate" < "annoyed")
          - Treat emojis or slang (":)", "lol", "💀") as strong signals
        """
        # TODO: Implement this method.
        #   1. Call self.preprocess(text) to get tokens.
        #   2. Loop over the tokens.
        #   3. Increase the score for positive words, decrease for negative words.
        #   4. Return the total score.
        #
        # Hint: if you implement negation, you may want to look at pairs of tokens,
        # like ("not", "happy") or ("never", "fun").
        
        tokens = self.preprocess(text)
        score = 0
        i = 0
        # if there is the presence of negative or positive
        # words rather than neither, a text is "mixed"
        # instead of "neutral"
        could_be_mixed = False

        while i < len(tokens):
            if (tokens[i] == "not" or tokens[i] == "never") and i < len(tokens)-1:
                if tokens[i+1] in NEGATIVE_WORDS:
                    score += 1
                    could_be_mixed = True
                elif tokens[i+1] in POSITIVE_WORDS:
                    score -= 1
                    could_be_mixed = True
                i += 1
            else:
                if tokens[i] in NEGATIVE_WORDS:
                    score -= 1
                    could_be_mixed = True
                elif tokens[i] in POSITIVE_WORDS:
                    score += 1
                    could_be_mixed = True
            i+=1

        return score, could_be_mixed
    
    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn the numeric score for a piece of text into a mood label.

        The default mapping is:
          - score > 0  -> "positive"
          - score < 0  -> "negative"
          - score == 0 -> "neutral"

        TODO: You can adjust this mapping if it makes sense for your model.
        For example:
          - Use different thresholds (for example score >= 2 to be "positive")
          - Add a "mixed" label for scores close to zero
        Just remember that whatever labels you return should match the labels
        you use in TRUE_LABELS in dataset.py if you care about accuracy.
        """
        # TODO: Implement this method.
        #   1. Call self.score_text(text) to get the numeric score.
        #   2. Return "positive" if the score is above 0.
        #   3. Return "negative" if the score is below 0.
        #   4. Return "neutral" otherwise.
        score, could_be_mixed = self.score_text(text)
        if score > 0:
            return "positive"
        elif score < 0:
            return "negative"
        elif could_be_mixed:
            return "mixed"
        else:
            return "neutral"

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        TODO:
          - Look at the tokens and identify which ones counted as positive
            and which ones counted as negative.
          - Show the final score.
          - Return a short human readable explanation.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        The current implementation is a placeholder so the code runs even
        before you implement it.
        """
        tokens = self.preprocess(text)

        positive_hits: List[str] = []
        negative_hits: List[str] = []
        score = 0

        for token in tokens:
            if token in self.positive_words:
                positive_hits.append(token)
                score += 1
            if token in self.negative_words:
                negative_hits.append(token)
                score -= 1

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )
