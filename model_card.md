# Model Card: Mood Machine

This model card is for the Mood Machine project, which includes **two** versions of a mood classifier:

1. A **rule based model** implemented in `mood_analyzer.py`
2. A **machine learning model** implemented in `ml_experiments.py` using scikit learn

You may complete this model card for whichever version you used, or compare both if you explored them.

## 1. Model Overview

**Model type:**  

I used both the rule based model and the ML model to compare them.

**Intended purpose:**  

This model is attempting to classify social media posts into one of four mood categories: positive, negative, neutral, mixed.

**How it works (brief):**  

Rule based:
The scoring rules will first see if there are more negative words
than positive or vice versa. If there is a negative word present, it
will subtract one point from the score. If there is a positive word present, it will add one point to the score. If there is a score less than 0 by the end, the mood is negative. If the score is greater than 0, it is positive. If it is 0, the score rule will first check if any negative or positive word was present in the phrase. If so, the mood is mixed (since it was a balance of differing moods). If not, the mood is just neutral.

ML:
Sample words are provided with corresponding words for the model to use apply similar logic on new data that it will receive in the testing phase. This could include how certain words add more weight to the mood determination.


## 2. Data

**Dataset description:**  

There are 32 posts in `SAMPLE_POSTS`. I added new ones that would have sarcasm, emojis, slang, casual vocabulary and casual grammar. I also tried to have words and phrases with double meanings.

**Labeling process:**  

Most of these labels were chosen just based on how they would be construed in everyday life contexts. But it's hard because even posts like "That was so scary 😨" could be completely sarcastic, but that can't be easily seen without context. Or posts with this emoji ✨ could be both positive ("Got the internship!!! 😭✨") or sassy/sarcastic/negative ("Yeah that gross gorey movie was ✨delightful✨"). The same goes for the 😭 emoji which can have several different meanings (gratitude/overwhelming joy, laughing at something ridiculous, relating to something ridiculous, sobbing, etc.).

**Important characteristics of your dataset:**   

- Contains slang and emojis  
- Includes sarcasm  
- Some posts express mixed feelings  

**Possible issues with the dataset:**  

Rule-based:
- Missing more vocabulary
- Missing logic to differentiate between double-meaning words like "like"
- Missing logic to add more weight to certain words than others
- Loooooove could be read as loove which is not in `POSITIVE_WORDS`
- Missing more sarcastic phrases

ML:
- Not enough training examples for more accurate input-based testing performance

## 3. How the Rule Based Model Works (if used)

**Your scoring rules:**  

- How positive and negative words affect score
- "Mixed" category and its associated logic for the score  
- Breaking contractions for negation
- Negation rules
- Removing 'stop' or 'filler' words to both make negation work better and also improve performance efficiency
- Emoji and "lol"/"lmao" handling
- Minor sarcastic phrase handling
- Removing punctuation

**Strengths of this approach:**  
Where does it behave predictably or reasonably well?

Any time you follow the rules.
For example: "I don't love how today is going for me 😔"
will read as negative because of the negation in "don't love" and the emoji "😔".

**Weaknesses of this approach:**  

Whenever you have sarcasm that doesn't fit into the `SARCASTIC_PHRASES` list.
For example: "Oh yeah. They did a real good job there by basically destroying the whole woodworking project" will be read as positive.

Or some slang like "poggers champions" could be read as neutral if not found in the `POSITIVE_WORDS` list.

## 4. How the ML Model Works (if used)

**Features used:**  

Bag of words using CountVectorizer.
This reads how many times a word appears in text that is assigned a certain mood label to be used as prediction by the Logistic Regression model.


**Training data:**  

The model trained on `SAMPLE_POSTS` and `TRUE_LABELS`.

**Training behavior:**  

More examples drastically changed the model. It is very sensitive on how many of each type of label exists in the training data because there is so little training data.

At first, I was only getting "negative" reads for everything unless I specifically typed a positive-labeled sample post that it was fed. After adding a few more positive posts, it gave slightly more positive reads. But it was still a bit inaccurate a lot of the time.

**Strengths and weaknesses:**  

Strengths:
- learning patterns quickly without needing explicit rules for every use case

Weaknesses:
- Incorrect correlations sometimes
- Very reliant on large training data set

## 5. Evaluation

**How you evaluated the model:**  

Rule-Based Model: 0.79 accuracy during training.

ML Model: 1.00 accuracy during training (this is only because it was just memorizing the training data)

**Examples of correct predictions:**  

- "I feel so enamored with life :)" -> positive
- "im so happy hehe" -> positive

This likely happened because I added a few more positive sample posts that made the number of positive posts equal to the number of negative posts in the training sample data (before I was only getting negative reads on anything I said). The sample size is very small so many assumptions based on word count for each word can be made for this to occur.

**Examples of incorrect predictions:**  

- "today i wanna float on a beautiful cloud" -> negative
- what a great day!! -> negative

Once again, the sample size is very small so many assumptions based on word count for each word can be made for this to occur.

This is quite inaccurate, and it is hard to understand the root of the problem compared to the rule-based model which has a much more predictable error pool.

## 6. Limitations

- The dataset is small   
- It depends heavily on the words you chose or labeled
- Limited feature types (Bag of Words but no other analysis tool like TF-IDF weighting, n-grams, character-level features, sentiment scores, etc.)

## 7. Ethical Considerations

- Misclassifying a message expressing distress as something positive 
- Misinterpreting mood for certain language communities  
- Privacy considerations if analyzing personal messages

## 8. Ideas for Improvement 

- Add more labeled data  
- Use TF IDF instead of CountVectorizer 
- Use more features in general 
- Add more extensive preprocessing for emojis, slang, and more vocabulary
- Use a small neural network or transformer model  
- Add a real test set instead of training accuracy only (80/20 rule)
