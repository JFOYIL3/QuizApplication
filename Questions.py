import random

question_list = ["What is the name of Anakin Skywalker's mother?",
                 "How many languages does C-3PO speak?",
                 "What is the name of Obi-Wan's diner friend?",
                 "What does AT-AT stand for?",
                 "What docking bay was the Millenium Falcon docked in A New Hope?",
                 "In the \"asteroid\", what animals attach themselves to the Millenium Falcon in Empire Strikes Back?",
                 "What was Count Dooku also known as?",
                 "Who was Count Dooku's padawan?",
                 "Who first ordered the creation of the clone army?",
                 "Who said this: \"From here, you will witness the final destruction of the Alliance and the end of your insignificant rebellion.\"?",
                 "In the Mos Eisley's Cantina, what is the genre of music that plays?",
                 "What planet did Princess Leia say that the Rebel base was supposedly at when confessing to Grand Moff Tarkin not to blow up Alderaan?",
                 "What year was the first Star Wars film released?",
                 "In what planet were younglings sent to mine kyber crystals to construct their light sabers as part of their training?",
                 "Who was Shmi married to in Attack of the Clones?",
                 "How big was the the exhaust port on the first Death Star? (Hint: about the same as a Womp Rat)",
                 "What species is Admiral Ackbar?",
                 "What is the sickness that makes Han Solo temporarily blind in Return of the Jedi?",
                 "Who said this: \"Who’s the more foolish; the fool, or the fool who follows him?\"",
                 "Where was Luke going to get power converters in A New Hope?",
                 "\"Star Wars V: The Empire Strikes Back\" was the first appearance of Boba Fett",
                 "Of whom did Jabba the Hutt say: \"This bounty hunter is my kind of scum ... fearless and inventive\"?",
                 "In which Star Wars film was the movie filmed entirely in a studio?",
                 "What creature was Obi-Wan mimicking when scaring off the sand people?",
                 "Why did Yoda say he didn't want to train Luke Skywalker?",
                 "Who wiped out all of the information about Kamino from the Jedi Temple archives?",
                 "What was the job that Finn told Han Solo he had at Starkiller base?",
                 "Who freed Princess Leia from her chains at Jabba's palace?",
                 "What was the diameter of the first Death Star?",
                 "How old was Yoda when Luke came back to complete his training?",
                 "Who spoke first in A New Hope?",
                 "What color lasers do Tie Fighters shoot?",
                 "On what planet was Han Solo born on?",
                 "How many systems did this guy have the death sentence on?",
                 "What was the name of Lando's co-pilot in Return of the Jedi?",
                 "What was Finn's stormtrooper designation number?",
                 "What is the only lightsaber color to appear in every movie?",
                 "What does the \"TIE\" in Tie Fighter stand for?",
                 "What was the name of the Imperial Shuttle Han and his strike team took to the forrest moon of Endor?",
                 "What was the name of the creatures that escape in Han Solo's ship in The Force Awakens?"] # twin ion engine, twin ignitor engine, two ion emmiter, twin ion emitter

question_guesses = []

question_desc = ["You are the most usesless character. Watto is more interesting than you. You should feel bad...",
                 "At least as a Toydarian, you won't succumb to Jedi Mindtricks so easily.",
                 "You have just started your journey, but with more training, you might soon become a Jedi Knight.",
                 "You are a bit more experienced with your training, but there is more work to be done!",
                 "You are a smooth talking scoundrel willing to do what they want, if the price is right, of course.",
                 "You are ruthless, and are experienced in tracking down your targets. But if it pays off with credits, who cares?",
                 "You are an experienced Jedi Knight, guardians of peace in the galaxy. But we do not grant you the rank of Jedi Master...",
                 "Evil to the core, you have begun training with the dark side of the force.",
                 "The dark side of the force is a pathway to many abilities some consider to be unnatural.",
                 "You have perfected your abilities as a Jedi Knight, and are part of the Jedi Council.",
                 "You have been stricken down, however, you are more powerful than you could possibly imagine."]

question_corrects = ["a", "b", "c", "a", "c", "b", "d", "b", "c", "b", "c", "c", "b", "d", "c", "a", "c", "a", "b", "c",
                     "b", "b", "b", "a", "d", "a", "b", "c", "c", "d", "a", "b", "c", "d", "b", "a", "d", "c", "b", "b"]

question_images = ["images/shmi.png", "images/c3po.png", "images/dex.png", "images/atat.png", "images/dockingbay.png",
                   "images/Mynock.png", "images/Count_Dooku.png", "images/padawan.png", "images/clone army.png",
                   "images/padawan.png", "images/jizz.png", "images/alderaan.png", "images/newhope.png",
                   "images/younglings.png", "images/cliegg.png", "images/death star.png", "images/ackbar.png",
                   "images/hibernation.png", "images/padawan.png", "images/tosche.png", "images/Bobafett.png",
                   "images/padawan.png", "images/star wars logo.png",
                   "images/SandPeople.png",
                   "images/YodaLuke.png",
                   "images/padawan.png",
                   "images/HanFinn.png",
                   "images/SlaveLeia.png",
                   "images/DeathStar.png",
                   "images/YodaRest.png",
                   "images/padawan.png",
                   "images/TieFighter.png",
                   "images/HanSoloPlanet.png",
                   "images/DeathSentence.png",
                   "images/Nien.png",
                   "images/Finn.png",
                   "images/LightSaber.png",
                   "images/TieFighter.png",
                   "images/Shuttle.png",
                   "images/Rathtar.png",]

question_rank = ["Jar Jar", "Toydarian", "Youngling", "Padawan", "Smuggler", "Bounty Hunter", "Jedi Knight",
                 "Darth *Insert Name*", "The Senate", "Jedi Master", "Force Ghost"]

a_answers = ["Shmi", "More than 5 Million", "Debster Jenster", "All Terrain Armored Transport", "87", "Triclocks",
             "Darth Levdus", "Mace Windu", "Count Dooku", "Grand Moff Tarkin", "jazz", "Tatooine", "1975", "Hoth",
             "Owen Lars", "2 meters", "Don Sushimi", "Hibernation Sickness", "Qui-Gon-Jinn", "Bosche Station", "True",
             "Boba Fett", "Attack of the Clones", "Krayt Dragon", "Luke was too old", "Count Dooku", "Patrol", "C-3PO",
             "100 kilometers", "600", "C-3PO", "Red", "Coruscant", "10", "Wicket", "FN-2187", "Blue",
             "Twin Ignitor Engine", "Tyberium", "Blurrg"]

b_answers = ["Padme", "More than 6 Million", "Dexter Jemster", "All Terrain Auxillary Transport", "83", "Mynocks",
             "Darth Bane", "Qui-Gon-Jinn", "Finis Valorum", "Emperor Palpatine", "fizz", "Yavin 4", "1977", "Corellia",
             "Zeeg Lars", "3 meters", "Don Schwarmi", "Resurrection Sickness", "Obi-Wan", "Posche Station", "False",
             "Princess Leia", "Revenge of the Sith", "Tusken Raider", "Yoda didn't have the time", "Palpatine",
             "Sanitation", "Luke Skywalker", "110 kilometers", "700", "Captain Antilles", "Green", "Naboo", "13",
             "Nien Nunb", "FN-2178", "Green", "Twin Ion Emmiter", "Tydirium", "Rathtar"]

c_answers = ["Leia", "More than 8 Million", "Dexter Jettster", "All Terrain Advanced Transport", "94", "Cybocks",
             "Darth Bandon", "Plo Koon", "Sifo-Dyas", "Darth Vader", "jizz", "Dantooine", "1979", "Ryloth",
             "Cliegg Lars", "4 meters", "Mon Calamari", "Resurrection Syndrome", "Yoda", "Tosche Station", "NULL",
             "Han Solo", "The Phantom Menace", "Wampa", "Yoda sensed the darkside in Luke", "Sifo-Dyas", "Maintenance",
             "R2D2", "120 kilometers", "800", "Darth Vader", "Blue", "Corellia", "15", "Bib Fortuna", "FN-2718", "Purple",
             "Twin Ion Engine", "Tylerium", "Acklay"]

d_answers = ["Boss Nass", "More than 9 Million", "Daxter Jemster", "Ass Titties Ass Tittes", "65", "Mysocks",
             "Darth Tyranus", "Kit Fisto", "Yaddle", "Boba Fett", "dizz", "Ansion", "1980", "Ilum", "Drez Lars",
             "5 meters", "Mon Sushimi", "Hibernation Syndrome", "Han Solo", "Phosche Station", "NULL", "Luke Skywalker",
             "Return of the Jedi", "Bantha", "Luke lacked patience", "Darth Maul", "Pilot", "Chewbacca", "130 kilometers",
             "900", "Princess Leia", "Yellow", "Ryloth", "12", "Wedge", "FN-2781", "Red", "Two Ion Emmiter", "Tybirius",
             "Rancor"]

correct_answers_sounds = ["sounds/Correct.mp3", "sounds/yahoo.mp3", "sounds/hellothere.mp3", "sounds/good.mp3"]

max_number_of_questions = 40


def get_true_or_false(number):
    return a_answers[number]


def get_hint(number):
    return question_corrects[number]


def get_rank(number_right):
    global max_number_of_questions

    if number_right / max_number_of_questions < 0.10:
        rank = question_rank[0]
        rank_description = question_desc[0]
        rank_image = "images/JarJar_rank.png"
        return rank, rank_description, rank_image
    elif 0.10 <= number_right / max_number_of_questions < 0.20:
        rank = question_rank[1]
        rank_description = question_desc[1]
        rank_image = "images/watto_rank.png"
        return rank, rank_description, rank_image
    elif 0.20 <= number_right / max_number_of_questions < 0.30:
        rank = question_rank[2]
        rank_description = question_desc[2]
        rank_image = "images/youngling_rank.png"
        return rank, rank_description, rank_image
    elif 0.30 <= number_right / max_number_of_questions < 0.40:
        rank = question_rank[3]
        rank_description = question_desc[3]
        rank_image = "images/padawan_rank.png"
        return rank, rank_description, rank_image
    elif 0.40 <= number_right / max_number_of_questions < 0.50:
        rank = question_rank[4]
        rank_description = question_desc[4]
        rank_image = "images/smuggler_rank.png"
        return rank, rank_description, rank_image
    elif 0.50 <= number_right / max_number_of_questions < 0.60:
        rank = question_rank[5]
        rank_description = question_desc[5]
        rank_image = "images/bounty_hunter.png"
        return rank, rank_description, rank_image
    elif 0.60 <= number_right / max_number_of_questions < 0.70:
        rank = question_rank[6]
        rank_description = question_desc[6]
        rank_image = "images/jedi_knight.png"
        return rank, rank_description, rank_image
    elif 0.70 <= number_right / max_number_of_questions < 0.80:
        rank = question_rank[7]
        rank_description = question_desc[7]
        rank_image = "images/Darth_rank.png"
        return rank, rank_description, rank_image
    elif 0.80 <= number_right / max_number_of_questions < 0.90:
        rank = question_rank[8]
        rank_description = question_desc[8]
        rank_image = "images/thesenate_rank.png"
        return rank, rank_description, rank_image
    elif 0.90 <= number_right / max_number_of_questions < 1:
        rank = question_rank[9]
        rank_description = question_desc[9]
        rank_image = "images/jedimaster_rank.png"
        return rank, rank_description, rank_image
    elif number_right == max_number_of_questions:
        rank = question_rank[10]
        rank_description = question_desc[10]
        rank_image = "images/forceghost_rank.png"
        return rank, rank_description, rank_image


def get_image(number):
    if number < max_number_of_questions:
        return question_images[number]


def get_question(number):
    if number < max_number_of_questions:
        return question_list[number]


def store_answer(letter):
    question_guesses.append(letter)


def get_a_answers(number):
    if number < max_number_of_questions:
        return a_answers[number]


def get_b_answers(number):
    if number < max_number_of_questions:
        return b_answers[number]


def get_c_answers(number):
    if number < max_number_of_questions:
        return c_answers[number]


def get_d_answers(number):
    if number < max_number_of_questions:
        return d_answers[number]


def compare_answers():
    number_correct = 0
    i = 0
    while i < max_number_of_questions:
        if question_guesses[i] == question_corrects[i]:
            number_correct += 1
            i += 1
        elif question_guesses[i] != question_corrects[i]:
            i += 1
    return number_correct


def check_if_correct(number, string):
    if question_corrects[number] == string:
        if number == 15:
            sound = "sounds/t16.mp3"
            return "That is correct", "null", sound
        elif number == 33:
            sound = "sounds/DeathSentence.mp3"
            return "That is correct", "null", sound
        else:
            sound = random.choice(correct_answers_sounds)
            return "That is correct", "null", sound
    elif question_corrects[number] != string:
        if number == 15:
            sound = "sounds/t16.mp3"
            return "That is incorrect", question_corrects[number], sound
        elif number == 33:
            sound = random.choice(correct_answers_sounds)
            return "That is incorrect", question_corrects[number], sound
        else:
            sound = "sounds/JarJar.mp3"
            return "That is incorrect", question_corrects[number], sound
