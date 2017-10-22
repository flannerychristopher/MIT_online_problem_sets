# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz

#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self._guid = guid
        self._title = title
        self._description = description
        self._link = link
        self._pubdate = pubdate
    
    def get_guid(self):
        return self._guid
    def get_title(self):
        return self._title
    def get_description(self):
        return self._description
    def get_link(self):
        return self._link
    def get_pubdate(self):
        return self._pubdate
    
#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        Trigger.__init__(self)
        self.phrase = phrase.lower()
    
    def get_phrase(self):
        return self.phrase
        
    def clean_string(self, input):
        clean_string = input[:].lower()
        for p in string.punctuation:
            clean_string = clean_string.replace(p, ' ')
        clean_string = ' '.join(clean_string.split())
        return clean_string
    
    def is_phrase_in(self, text):
        clean_phrase = self.clean_string(self.get_phrase())
        clean_text = self.clean_string(text)

        flag = True
        if clean_phrase not in clean_text:
            flag = False
        for word in clean_phrase.split(' '):
            if word not in clean_text.split(' '):
                flag = False
        return flag
   
# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
        
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())

# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
    
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
#        format time to: 3 Oct 2016 17:00:10 
class TimeTrigger(Trigger):
    def __init__(self, time):
        Trigger.__init__(self)
        self._time = self.format_time(time)
    
    def format_time(self, time):
        formatted_time = datetime.strptime(time, "%d %b %Y %H:%M:%S")
        return formatted_time
    
    def get_time(self):
        return self._time

# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def __init__(self, time):
        TimeTrigger.__init__(self, time)
        
    def evaluate(self, story):
        time = self.get_time()
        try:
            return time > story.get_pubdate()
        except:
            time = time.replace(tzinfo=pytz.timezone("EST"))
            return time > story.get_pubdate()
            
class AfterTrigger(TimeTrigger):
    def __init__(self, time):
        TimeTrigger.__init__(self, time)
        
    def evaluate(self, story):
        time = self.get_time()
        try:
            return time < story.get_pubdate()
        except:
            time = time.replace(tzinfo=pytz.timezone("EST"))
            return time < story.get_pubdate()
    
# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, T):
        self._T = T
    def evaluate(self, story):
        return not self._T.evaluate(story)

# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, T1, T2):
        self._T1, self._T2 = T1, T2
    def evaluate(self, story):
        return self._T1.evaluate(story) and self._T2.evaluate(story)

# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, T1, T2):
        self._T1, self._T2 = T1, T2
    def evaluate(self, story):
        return self._T1.evaluate(story) or self._T2.evaluate(story)

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    story_matches = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) and story not in story_matches:
                story_matches.append(story)
    return story_matches

#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    t_map = {    "TITLE": TitleTrigger,
                 "DESCRIPTION": DescriptionTrigger,
                 "AFTER": AfterTrigger,
                 "BEFORE": BeforeTrigger,
                 "NOT": NotTrigger,
                 "AND": AndTrigger,
                 "OR": OrTrigger        }
    trigger_dict = {}
    trigger_list = [] 

    def line_reader(line):
        data = line.split(',')
        if data[0] != "ADD":
            if data[1] == "OR" or data[1] == "AND":
                trigger_dict[data[0]] = t_map[data[1]](trigger_dict[data[2]], trigger_dict[data[3]])
            else:
                trigger_dict[data[0]] = t_map[data[1]](data[2])
        else: 
            trigger_list[:] += [trigger_dict[t] for t in data[1:]]

    for line in lines:
        line_reader(line)
    return trigger_list

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
#        t1 = TitleTrigger("election")
#        t2 = DescriptionTrigger("Trump")
#        t3 = DescriptionTrigger("Clinton")
#        t4 = AndTrigger(t2, t3)
#        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

