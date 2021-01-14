import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

news = pd.read_csv("table_newsanalysis.csv", index_col=0)

print("Flip the script - Neutral Converter")

print("# Displaying Data")

df = pd.DataFrame(news)
print(df.head(10))

plt.style.use('ggplot')

print("# Original vs. Neutral")
plt.subplot(3, 2, 1)
plt.plot(news['words_count'], color='mediumaquamarine', label='Words in total')
plt.plot(news['words_converted'], color='mediumorchid', label='Words converted')
plt.ylabel("Quantity of words")
plt.xlabel('Quantity of articles')
plt.legend(loc='upper left')
#plt.show()

print("# Ratio of conversions per topic")
plt.subplot(3, 2, 2)
sns.scatterplot(x=news['rate'], y=news['topic'], alpha=0.5, hue=news['words_count'], size=news['words_count'], sizes=(50,500), palette="mako") 
plt.xlim(0, 10)
plt.ylabel("Topics")
plt.xlabel('Converted words ratio')
plt.title('Ratio = Neutral * % / Original')
plt.legend(loc='lower right')
#plt.show()

print("# Author's gender")
plt.subplot(3, 2, 3)
sns.barplot(x=news['gender_author'], y=news['rate'], alpha=0.5, hue=news['gender_author'], palette="hls") #rocket, hls 
plt.ylabel('Converted words ratio')
plt.xlabel("Author's gender")
plt.legend(loc='upper right')
#plt.show()

print("# Ratio of conversions per source")
plt.subplot(3, 2, 4)
sns.scatterplot(x=news['rate'], y=news['source_name'], alpha=0.5, hue=news['words_count'], size=news['words_count'], sizes=(50,500), palette="rocket")
plt.xlim(0, 10)
plt.ylabel("Source")
plt.xlabel('Converted words ratio')
plt.title('Ratio = Neutral * % / Original')
plt.legend(loc='lower right')
#plt.show()

print("# Residual of a regression")
plt.subplot(3, 2, 5)
sns.residplot(data=news, x="words_converted", y="words_count", color="indianred")
#plt.show()

print("# Higher-order regressions")
plt.subplot(3, 2, 6)
plt.scatter(news['words_converted'], news['words_count'], label='News articles', color='mediumslateblue', marker='o')
sns.regplot(data=news, x="words_converted", y="words_count", color="tomato", scatter=None, label= "First order")
sns.regplot(data=news, x="words_converted", y="words_count", color="limegreen", scatter=None, order=2, label= "Second order")
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()