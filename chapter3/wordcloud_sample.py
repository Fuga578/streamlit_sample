from wordcloud import WordCloud


word_cloud = WordCloud()
prob = {"a": 10, "b": 100, "c": 20, "d": 40}
img = word_cloud.fit_words(prob)
pil = img.to_image()

pil.show()
