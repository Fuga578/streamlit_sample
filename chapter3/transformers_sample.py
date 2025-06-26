from transformers import pipeline


pipe = pipeline("sentiment-analysis")

res = pipe("May the force be with you.")
print(res)
