story_1 = {
    "start": {"Kai, your typical high schooler, got infected in a nearby resort, whilst on vacation with his family, this turned his whole life upside down"},
    "middle": {"One day, an alert popped up in the local news and Kai. A unusual foe, by the name 'the plunger', appeared"},
    "end": {"As, he entered the realm of crime fighting, he realised, he has become, Captain Underpants, and defeated most of his enemies and yearns for more action'"},
}
# prints out the story in the terminal in a linear fashion
print(story_1)

# prints out the type of method that is used
print(type(story_1))

# displays all the keys that is listed in the dict
print(story_1.keys())

# displays all the values that us listed in the dict
print(story_1.values())

# prints out all the value pairs
print(story_1["start"])
print(story_1["middle"])
print(story_1["end"])

# displays the key/value pairs in a tuple
print(story_1.items())

# updates the dict to add another key-value pair
story_1.update({
    "hero": "Captain Underpants"
})
# prints the entire updated dict
print(story_1)