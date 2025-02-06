import numpy as np
import torch
import transformers
from tqdm.auto import tqdm
from sklearn.model_selection import train_test_split

features = ids_list.drop('pos', axis=1)
train_X, train_y, test_X, test_y = train_test_split(features, ids_list['pos'], test_size=0.5)

tokenizer = transformers.BertTokenizer.from_pretrained('bert-base-uncased')
example = 'It is very handy to use transformers'
ids = tokenizer.encode(example, add_special_tokens=True,
                       max_length=5, truncation=True)
print(ids)

n = 512
padded = np.array(ids[:n] + [0]*(n-len(ids)))
print(padded)

attention_mask = np.where(padded != 0, 1, 0)

ids_list = []
attention_mask_list = []

max_length = 512

for input_text in corpus[:200]:
    ids = tokenizer.encode(
        input_text.lower(),
        add_special_tokens=True,
        truncation=True,
        max_length=max_length,
    )
    padded = np.array(ids + [0] * (max_length - len(ids)))
    attention_mask = np.where(padded != 0, 1, 0)
    ids_list.append(padded)
    attention_mask_list.append(attention_mask)

config = BertConfig.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

batch_size = 100
embeddings = []

for i in tqdm(range(len(ids_list) // batch_size)):
    ids_batch = torch.LongTensor(ids_list[batch_size*i:batch_size*(i+1)])
    attention_mask_batch = torch.LongTensor(attention_mask_list[batch_size*i:batch_size*(i+1)])
    with torch.no_grad():
        batch_embeddings = model(ids_batch, attention_mask=attention_mask_batch)
    embeddings.append(batch_embeddings[0][:,0,:].numpy())

remaining = len(ids_list) % batch_size
if remaining > 0:
    ids_batch = torch.LongTensor(ids_list[-remaining:])
    attention_mask_batch = torch.LongTensor(attention_mask_list[-remaining:])
    with torch.no_grad():
        batch_embeddings = model(ids_batch, attention_mask=attention_mask_batch)
    embeddings.append(batch_embeddings[0][:, 0, :].numpy())

features = np.concatenate(embeddings)

# The Film Junky Union, a new edgy community for classic movie enthusiasts, 
# is developing a system for filtering and categorizing movie reviews. 
# The goal is to train a model to automatically detect negative reviews. 
# You'll be using a dataset of IMBD movie reviews with polarity labelling to build a model for classifying positive and negative reviews. 
# It will need to reach an F1 score of at least 0.85.

# Project Instructions
# Load the data.
# Preprocess the data, if required.
# Conduct an EDA and make your conclusion on the class imbalance.
# Preprocess the data for modeling.
# Train at least three different models for the given train dataset.
# Test the models for the given test dataset.
# Compose a few of your own reviews and classify them with all the models.
# Check for differences between the testing results of models in the above two points. Try to explain them.
# Present your findings.

# Project Evaluation
# We’ve put together the evaluation criteria for the project. Read them carefully before moving on to the task:

# The text data has been loaded and pre-processed for vectorization.
# The text data has been transformed to vectors.
# The models have been defined, trained, and tested.
# The metric's threshold has been reached.
# All the code cells are arranged in the order of their execution.
# All the code cells can be executed without errors.
# You have made conclusions.
# Our reviewers will also look at the overall quality of your project:
# 
# Did you stick to the project structure?
# Did you keep your code neat?
# Have you managed to avoid code duplication?
# What are your findings?