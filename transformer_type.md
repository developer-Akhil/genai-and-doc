# Transformer
A Transformer is a deep learning model architecture introduced by Google researchers in 2017 in a paper titled. It was designed to handle sequential data (like text, speech, or time series) more efficiently than older models such as **RNNs (Recurrent Neural Networks)** and **LSTMs (Long Short-Term Memory networks)**.

**Core Idea**\
The Transformer replaces recurrence (RNNs) and convolution (CNNs) with a mechanism called self-attention, which allows the model to:\
Look at all words in a sentence simultaneously\
Learn contextual relationships between them\
Capture long-range dependencies efficiently

**Transformer Type**\
A Transformer in AI is a type of neural network architecture designed for processing sequential data, such as text, by learning context and tracking relationships between sequence elements using mechanisms called attention and self-attention. Transformers are the foundation for modern natural language processing (NLP) models like GPT (Generative Pretrained Transformer), BERT, and Gemini, and have also been \ adapted for computer vision, audio, and multimodal AI applications.

**Embedding**\
Embedding converts discrete data (like words or sentences) into meaningful numerical vectors so that similar items are close together in vector space.

**Why Do We Need Embeddings?**\
Machine learning models cannot process raw text directly.
They require numerical input.\
Embeddings solve this by:
* Converting tokens into vectors
* Capturing semantic meaning
* Enabling similarity search
* Supporting clustering and retrieval

**Embedding Layer:**\
An Embedding Layer is a neural network layer that converts words (or tokens) into numbers (vectors) — specifically, into dense numerical representations that capture the meaning or context of the words.
The embedding layer in a transformer neural network converts discrete tokens, such as words or subwords, into dense numerical vectors called embeddings that represent both their semantic meaning and positional information within a sequence. This enables the model to process raw input text as continuous data, making it suitable for neural computation.

In short: \
➡️ **Words → Vectors (numbers)** \
so the model can understand and process them. \
**Why do we need it?** \
Computers can’t understand words directly — they only understand numbers. \
So before processing text, we must represent each word numerically. \
Older methods used:
  * One-hot encoding: e.g. “dog” → [0, 0, 1, 0, 0] (problem: very large and sparse vectors — no sense of meaning or similarity).\

The **Embedding Layer** solves this by learning compact, meaningful numerical representations.

Example
Let’s say we have three words:
* “cat”
* “dog”
* “apple”

The embedding layer might learn something like:
| Word  |	Embedding Vector (example) |
|-------|-----------------|
| cat	  | [0.2, 0.1, 0.7] |
| dog	  | [0.3, 0.2, 0.6] |
| apple |	[0.9, 0.8, 0.1] |

Notice how **“cat”** and **“dog”** have similar vectors — meaning the model has learned that they are related (both animals).
But **“apple”** is quite different — it’s a fruit.

**How it works inside a model**
  1.	The model takes a sentence (e.g., “The cat sat on the mat”).
  2.	Each word is converted to a token ID (like an index).\
     The → 1, cat → 2, sat → 3, ...
  3.	The Embedding Layer looks up each token ID in a table of learned vectors (called the embedding matrix).
  4.	These vectors are passed into the next layers of the model (like attention layers).

**In Transformers**
Transformers use **positional embeddings** too —\
because unlike RNNs, Transformers don’t process text sequentially. \
Positional embeddings tell the model **where each word appears in a sentence**. \
So the total input embedding = Word embedding + Positional embedding 

**Summary Table:**
|Feature |	Description |
|-------|-----------------|
|Purpose |	Convert words or tokens into dense numeric vectors |
|Learns	| Word meanings and relationships |
|Output |	A matrix of real-valued vectors |
|Used in	| NLP models like GPT, BERT, T5, etc. |
|Advantage |	Captures similarity — similar words have similar embeddings |

**GPT**
GPT, or Generative Pre-trained Transformer, is a type of large language model (LLM) developed using the transformer architecture for deep learning. GPTs are notable for their ability to generate human-like text and perform a wide variety of natural language processing tasks such as answering questions, summarizing content, translation, and more.

It’s a type of **AI language model** that can **understand and generate human-like text**.
Developed by **OpenAI**, GPT is based on the **Transformer architecture**

**Let’s break down the name:**

|Part|	Meaning|
|-------|-----------------|
|Generative|	It can generate new text — like writing essays, emails, poems, or code.|
|Pre-trained|	It’s trained in advance on a huge amount of text from the internet, books, and articles — before being fine-tuned for specific tasks.|
|Transformer|	The neural network architecture it’s built on — based on self-attention (helps the model understand context and relationships in text).|

**How GPT works (in simple steps)**
1.	Training phase (Pre-training):
*	GPT reads massive amounts of text (billions of words).
*	It learns patterns of language, grammar, facts, and context.
*	The goal: predict the next word in a sentence.
**Example:**
**“The sky is ___” → likely “blue”.**
2.	Fine-tuning (or instruction tuning):
*	The model is later trained with human feedback (like instructions, question-answering, reasoning).
*	This makes GPT useful for practical conversation and problem-solving (like ChatGPT).
3.	Inference (using it):
*	You give it a prompt, and GPT generates text word-by-word (token-by-token), predicting what comes next logically and contextually.







