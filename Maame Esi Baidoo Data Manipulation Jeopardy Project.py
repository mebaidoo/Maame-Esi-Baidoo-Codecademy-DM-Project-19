import pandas as pd
import datetime
pd.set_option('display.max_colwidth', -1)
#Loading the csv data into a pandas dataframe
jeopardy = pd.read_csv("jeopardy.csv")
print(jeopardy)
#Inspecting the different columns the df has
print(jeopardy.columns)
print(jeopardy[" Air Date"].head())
print(jeopardy[" Round"].head())
print(jeopardy[" Category"].head())
print(jeopardy[" Value"].head())
print(jeopardy[" Question"].head())
#Filter the questions column to return only questions containing the words, "King" and "England"
def filter_column(dataf, column_name, word1, word2):
    return dataf[(dataf[column_name].str.contains(word1)) & (dataf[column_name].str.contains(word2))]
    #return dataf[dataf[column_name].isin(words_list)]
filtered_questions_king = filter_column(jeopardy, " Question", "King", "England")
print(filtered_questions_king)
print(len(filtered_questions_king))
#Converting everything in the Questions column so all questions containing "king" and "england" will be selected as the first selection only selected those with these words in title case format
jeopardy[" Question"] = jeopardy[" Question"].str.lower()
print(jeopardy[" Question"])
#Convert the Value column to float to be able to perform aggregate statistics on it
print(jeopardy[" Value"].head(30)) 
jeopardy["Converted Values"] = jeopardy[" Value"].apply(lambda x: x if x == "None" else float(x.replace("$", "").replace(",", "")))
print(jeopardy["Converted Values"])
def filter_column2(dataf, column_name, word):
    return dataf[(dataf[column_name].str.contains(word))]
#Filtering the questions column for questions containing "king"
filtered_questions_king2 = filter_column2(jeopardy, " Question", " king ")
print(filtered_questions_king2[" Question"])
print(len(filtered_questions_king2))
#Find the average value of questions that contain the word "king" in determining the difficulty level of questions containing certain words using the values placed on them
avg_king_value = filtered_questions_king2[filtered_questions_king2["Converted Values"] != "None"].mean()
print("The average value of questions that contain the word \"king\" is " + str(avg_king_value["Converted Values"]))
#Finding the average value of questions containing another word
filtered_questions_president = filter_column2(jeopardy, " Question", " president ")
print(filtered_questions_president[" Question"])
print(len(filtered_questions_president))
avg_president_value = filtered_questions_president[filtered_questions_president["Converted Values"] != "None"].mean()
print("The average value of questions that contain the word \"president\" is " + str(avg_president_value["Converted Values"]))
if avg_king_value["Converted Values"] > avg_president_value["Converted Values"]:
    print("Questions containing \"king\" have a higher difficulty level than questions containing \"president\".")
else:
    print("Questions containing \"president\" have a higher difficulty level than questions containing \"king\".")
#Finding the number of answers to questions containing "king" that contain "Henry VIII"
king_answers_count = filtered_questions_king2[" Answer"].value_counts()
print("This is the count of each answer to questions containing \"king\": " + "\n" + str(king_answers_count))
#Finding out if there were more or less questions from the 90s containing "computer" than in the 2000s
grouped_90s = jeopardy[jeopardy[" Air Date"].str.contains("199")]
print(grouped_90s)
grouped_90s_computer = grouped_90s[grouped_90s[" Question"].str.contains(" computer ")]
print(grouped_90s_computer[" Question"])
grouped_2000s = jeopardy[jeopardy[" Air Date"].str.contains("20")]
print(grouped_2000s)
grouped_2000s_computer = grouped_2000s[grouped_2000s[" Question"].str.contains(" computer ")]
print(grouped_2000s_computer[" Question"])
if len(grouped_90s_computer) > len(grouped_2000s_computer):
    print("Questions containing \"computer\" were more in the 90s than in the 2000s.")
else:
    print("Questions containing \"computer\" were more in the 2000s than in the 90s.")
#Determining if there is a connection between the round and category columns by checking if there are more literature categories in the rounds, jeopardy or double jeopardy
jeopardy.rename(columns = {"Show Number": "ShowNumber", " Category": "Category"}, inplace = True)
by_literature = jeopardy[jeopardy.Category == "LITERATURE"]
print(by_literature["Category"])
groupby_round = by_literature.groupby(" Round").ShowNumber.count()
print(groupby_round)