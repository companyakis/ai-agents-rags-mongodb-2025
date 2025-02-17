from transformers import pipeline

summarizer = pipeline(task="summarization", model="cnicu/t5-small-booksum")

output = summarizer(long_text, max_length=50)

print(output[0]["summary_text"])
