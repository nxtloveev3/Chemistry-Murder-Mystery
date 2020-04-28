import random
def conversationGeneration(message,weapon,nervous):
    dictionary={"STA":{"questions":["what","do","you","know","about","sta"],
                       "answers":["I do not know.","Yeah, they make pans.","Never heard of it."]},
                "knife":{"questions":["do","you","cook","what","happened","your","hand","finger","cut"],
                         "answers":["Yeah, I cook and I cut myself accidentally."]},
                "pillow":{"questions":["do","you","know","what","happened","pillow","stain","on"],
                        "answers":["I splashed water on it.","I don't know maybe Nico drool?"]},
                "GHB":{"questions":["what","do","you","know","about","ghb"],
                       "answers":["I take them to help me sleep.","I know that it makes people sleepy","I am not sure."]},
                "general":{"questions":["who","wants","him","nico","dead"],
                           "answers":["Not I know of.","I think the STA company.","Nico is trying to bring the STA company down. So..."]},
                "general2":{"questions":["why","do","you","work","here"],
                            "answers":["This job pays great.","I just got the job from my job agency"]},
                "general3":{"questions":["what","do","you","think","about","nico","love","your"],
                            "answers":["I think he is really nice.","I love him so much."]},
                "general4":{"questions":["you","do","know","effect"],
                            "answers":["Yes","It makes you sleepy"]},
                "general5":{"questions":["are","you","guilty","killing","nico"],
                            "answers":["No","How could I","Absolutely not"]},
                "general6":{"questions":["why","are","you","in","bedroom",],
                            "answers":["I just trying to help clean.","I saw pillow on the ground so I put it back."]},
                "general7":{"questions":["don't","butler","cook","for","you"],
                            "answers":["I kinda just felt need to cook for myself","Butler don't know my taste in food that well"]},
                "general8":{"questions":["what","knife","use","you","did","used","cook","cooking"],
                            "answers":["The large one.","Always,the large one"]},
                "general9":{"questions":["what","you","think","about","molly","marriage","their","nico"],
                            "answers":["I don't think they love each other","They are not that close."]},
                "general10":{"questions":["what","you","think","about","john","butler","cook"],
                            "answers":["He is a great cheif.","I heard he works for STA before.","He doesn't talk that much."]},
                "general11":{"questions":["what","do","you","think","about","marlin","gardener"],
                            "answers":["He is strong.","He is not that hardworking","He is really clumpsy."]},
                "general12":{"questions":["what","red","on","your","arm","mark","happened"],
                             "answers":["Oh, you know from work.","Sometimes you just got them when you are clumpsy.","I don't recall getting them"]},
                "general13":{"questions":["do","you","know","passward","key","storage"],
                             "answers":["Nope","I have no idea","Only Nico knows","I know that he put it on a paper",]}
                             }

    wordList = []
    message = message.lower()
    for word in message.split(' '):
        wordList.append(word)
    wincount = 0
    winelem = None
    for elem in dictionary:
        count = 0
        questionWord = dictionary[elem]["questions"]
        for word in wordList:
            if word in questionWord:
                count += 1
        if count > wincount:
            wincount = count
            winelem = elem
        elif count == wincount:
            winelem = None
    if winelem != None:
        if weapon == "GHB" and not nervous:
            answer = dictionary[winelem]["answers"][-1]
        elif weapon == "GHB" and nervous:
            answer = random.choice(dictionary[winelem]["answers"][:-1])
        else: 
            answer = random.choice(dictionary[winelem]["answers"])
    else:
        answer = "I do not know."
    return answer


    