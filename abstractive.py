#install pytorch
#install transformers

# import dependencies
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

# create tokenizer
tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")

# load the model
model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")


# start summarization
text = """
Kobe Bean Bryant (/koʊbi/ KOH-bee; August 23, 1978  January 26, 2020) was an 
American professional basketball player. A shooting guard, he spent his entire 20-year
 career with the Los Angeles Lakers in the National Basketball Association (NBA). Widely 
 regarded as one of the greatest basketball players of all time, Bryant won five NBA championships 
 and was an 18-time All-Star, a 15-time member of the All-NBA Team, a 12-time member of the
  All-Defensive Team, the 2008 NBA Most Valuable Player (MVP), and a two-time NBA Finals MVP. 
  Bryant also led the NBA in scoring twice and ranks fourth in league all-time regular season 
  and postseason scoring. He was posthumously voted into the Naismith Memorial Basketball Hall 
  of Fame in 2020 and named to the NBA 75th Anniversary Team in 2021.
"""

# tokenize
tokens = tokenizer(text, truncation=True, padding="longest",return_tensors="pt")

print(tokens)