from tkinter import *
from Questions import *
import playsound
import winsound
import time
import os
import random


# moving "Current Song" animation
def moving_song():
    global song_animation
    global song_title_move_count

    if song_title_move_count == 0:
        song_title_move_count += 1
        song_title_label.place(x=5, y=900)
    elif song_title_move_count == 1:
        song_title_move_count += 1
        song_title_label.place(x=10, y=900)
    elif song_title_move_count == 2:
        song_title_move_count += 1
        song_title_label.place(x=15, y=900)
    elif song_title_move_count == 3:
        song_title_move_count += 1
        song_title_label.place(x=20, y=900)
    elif song_title_move_count == 4:
        song_title_move_count += 1
        song_title_label.place(x=15, y=900)
    elif song_title_move_count == 5:
        song_title_move_count += 1
        song_title_label.place(x=10, y=900)
    elif song_title_move_count == 6:
        song_title_move_count += 1
        song_title_label.place(x=5, y=900)
    elif song_title_move_count == 7:
        song_title_move_count = 0
        song_title_label.place(x=0, y=900)
    song_animation = root.after(120, moving_song)


# have the song title flash colors
def flashing_song_text():
    global song_color_count

    if song_color_count == 0:
        current_song.config(fg="red")
        song_color_count += 1
    elif song_color_count == 1:
        current_song.config(fg="orange")
        song_color_count += 1
    elif song_color_count == 2:
        current_song.config(fg="yellow")
        song_color_count += 1
    elif song_color_count == 3:
        current_song.config(fg="green")
        song_color_count += 1
    elif song_color_count == 4:
        current_song.config(fg="blue")
        song_color_count += 1
    elif song_color_count == 5:
        current_song.config(fg="indigo")
        song_color_count = 0
    root.after(150, flashing_song_text)


def skip_check():
    global skip_song
    global run

    if skip_song:
        root.after_cancel(run)
        skip_song = False
        song_clip()
    elif not skip_song:
        song_clip()


def song_clip():
    global song_count
    global run

    if song_count == 1:
        winsound.PlaySound("sounds/JediRocks.wav", winsound.SND_ASYNC)
        current_song.config(text="♫ Jedi Rocks ♫")
        song_count += 1
        run = root.after(63000, skip_check)
    elif song_count == 2:
        winsound.PlaySound("sounds/Cantina2.wav", winsound.SND_ASYNC)
        current_song.config(text="♫ Cantina Song 1 ♫")
        song_count += 1
        run = root.after(81000, skip_check)
    elif song_count == 3:
        winsound.PlaySound("sounds/LaptiNek.wav", winsound.SND_ASYNC)
        current_song.config(text="♫ Lapti Nek ♫")
        song_count += 1
        run = root.after(87000, skip_check)
    elif song_count == 4:
        winsound.PlaySound("sounds/IzizCantina.wav", winsound.SND_ASYNC)
        current_song.config(text="♫ Iziz Cantina ♫")
        song_count = 0
        run = root.after(53000, skip_check)
    elif song_count == 0:
        winsound.PlaySound("sounds/Cantina.wav", winsound.SND_ASYNC)
        current_song.config(text="♫ Cantina Song 2 ♫")
        song_count += 1
        run = root.after(63000, skip_check)


def lando_clip(event):
    global lando_counter
    global sound

    # get lando sound clip
    sound = os.path.join(script_dir, "sounds/WorseAllTheTime.mp3")
    playsound.playsound(sound, False)

    # hide the click me text
    dont_click.config(text="")

    # every time lando has been clicked
    lando_counter += 1

    if lando_counter == 5:
        dont_click.config(text="PLZ STOP")
        dont_click.place(x=1860, y=995)

    elif lando_counter == 10:
        dont_click.config(text="STOP!")


def call_a_friend_clip(event):
    global palpatine_count

    # play palpatine sound clip
    playsound.playsound("sounds/Faith.mp3", False)

    # turn off the luke, han, leia widgets and replace them with palpatine
    label_luke.place_forget()
    label_han.place_forget()
    label_leia.place_forget()
    phone_friend.config(text="Fool")
    phone_friend.place(x=175)
    label_palpatine.place(x=150, y=60)
    palpatine_count += 1


def phone_a_sith_dooku(event):
    global sith_check
    global dooku_check

    dooku_check = True
    if sith_check:
        playsound.playsound("sounds/LookingForward.mp3", False)
        correct_answer = get_hint(count)
        dooku_answer.config(text="\"I have no doubt that the correct answer is " + correct_answer + ".\"")
        dooku_answer.place(x=0, y=600)
        dooku_label.place_forget()
        dooku_label_gray.place(x=150, y=60)
        vader_answer.place_forget()
        maul_answer.place_forget()
        boba_check()
        boba_details.config(text="Boba Fett will retrieve a random Sith that has already been called (" + str(sith_credits) + " Credits)")


def phone_a_sith_vader(event):
    global sith_check
    global vader_check

    vader_check = True
    if sith_check:
        correct_answer = get_hint(count)
        answers = ["a", "b", "c", "d"]
        check_t_or_f = get_true_or_false(count)
        while True:
            if check_t_or_f == "True":
                playsound.playsound("sounds/TooEasy.mp3", False)
                break
            else:
                vader_random_answer = random.choice(answers)
                if vader_random_answer == correct_answer:
                    continue
                elif vader_random_answer != correct_answer:
                    playsound.playsound("sounds/VaderBreathing.mp3", False)
                    vader_answer.config(text="\"The answer is definitely not " + vader_random_answer + ".\"")
                    vader_answer.place(x=0, y=600)
                    # vader_label.place_forget()
                    vader_label_gray.place(x=40, y=60)
                    dooku_answer.place_forget()
                    maul_answer.place_forget()
                    boba_check()
                    boba_details.config(text="Boba Fett will retrieve a random Sith that has already been called (" + str(sith_credits) + " Credits)")
                    break


def phone_a_sith_maul(event):
    global sith_check
    global sith_credits
    global maul_check

    maul_check = True
    if sith_check:
        correct_answer = get_hint(count)
        answers = ["a", "b", "c", "d"]
        answers.remove(correct_answer)
        check_t_or_f = get_true_or_false(count)
        while True:
            if check_t_or_f == "True":
                playsound.playsound("sounds/TooEasy.mp3", False)
                break
            else:
                playsound.playsound("sounds/Revenge.mp3", False)
                maul_answers = [correct_answer, random.choice(answers)]
                maul_guess = random.choice(maul_answers)
                maul_answer.config(text="\"The answer is " + maul_guess + "\".")
                maul_answer.place(x=0, y=600)
                maul_label.place_forget()
                maul_label_gray.place(x=260, y=60)
                vader_answer.place_forget()
                dooku_answer.place_forget()
                boba_check()
                boba_details.config(text="Boba Fett will retrieve a random Sith that has already been called (" + str(sith_credits) + " Credits)")
                break


def boba_check():
    global sith_credits
    global boba_count

    boba_count += 1
    if boba_count == 1:
        sith_credits = 150
    elif boba_count == 2:
        sith_credits = 100
    elif boba_count == 3:
        sith_credits = 50


def call_bounty_boba(event):
    global credits_count
    global boba_count
    global vader_check
    global dooku_check
    global maul_check
    global sith_credits
    global boba_check_if_active
    global check_if_enough_credits

    if boba_check_if_active:

        if credits_count >= sith_credits:
            # 150 credits for boba
            if sith_credits == 150 and credits_count >= 150:
                sith_credits = 0
                if vader_check:
                    vader_label_gray.place_forget()
                    credits_count -= 150
                    credits_label.config(text="Credits: " + str(credits_count))
                    boba_count -= 1
                elif dooku_check:
                    dooku_label_gray.place_forget()
                    credits_count -= 150
                    credits_label.config(text="Credits: " + str(credits_count))
                    boba_count -= 1
                elif maul_check:
                    maul_label_gray.place_forget()
                    credits_count -= 150
                    credits_label.config(text="Credits: " + str(credits_count))
                    boba_count -= 1

                playsound.playsound("sounds/BobaQuote.mp3", False)

            # 100 credits for boba
            elif sith_credits == 100 and credits_count >= 100:
                sith_credits = 150
                numbers = [1, 2]
                get_number = random.choice(numbers)

                # vader and dooku
                if vader_check and dooku_check:
                    if get_number == 1:
                        vader_label_gray.place_forget()
                        credits_count -= 100
                        credits_label.config(text="Credits: " + str(credits_count))
                        boba_count -= 1
                    elif get_number == 2:
                        dooku_label_gray.place_forget()
                        credits_count -= 100
                        credits_label.config(text="Credits: " + str(credits_count))
                        boba_count -= 1

                # vader and maul
                elif vader_check and maul_check:
                    if get_number == 1:
                        vader_label_gray.place_forget()
                        credits_count -= 100
                        credits_label.config(text="Credits: " + str(credits_count))
                        boba_count -= 1
                    elif get_number == 2:
                        maul_label_gray.place_forget()
                        credits_count -= 100
                        credits_label.config(text="Credits: " + str(credits_count))
                        boba_count -= 1

                # dooku and maul
                elif dooku_check and maul_check:
                    if get_number == 1:
                        dooku_label_gray.place_forget()
                        credits_count -= 100
                        credits_label.config(text="Credits: " + str(credits_count))
                        boba_count -= 1
                    elif get_number == 2:
                        maul_label_gray.place_forget()
                        credits_count -= 100
                        credits_label.config(text="Credits: " + str(credits_count))
                        boba_count -= 1

                playsound.playsound("sounds/BobaQuote.mp3", False)

            # 50 credits for boba
            elif sith_credits == 50 and credits_count >= 50:
                sith_credits = 100
                numbers = [1, 2, 3]
                get_number = random.choice(numbers)
                if get_number == 1:
                    vader_label_gray.place_forget()
                    credits_count -= 50
                    credits_label.config(text="Credits: " + str(credits_count))
                    boba_count -= 1
                elif get_number == 2:
                    dooku_label_gray.place_forget()
                    credits_count -= 50
                    credits_label.config(text="Credits: " + str(credits_count))
                    boba_count -= 1
                elif get_number == 3:
                    maul_label_gray.place_forget()
                    credits_count -= 50
                    credits_label.config(text="Credits: " + str(credits_count))
                    boba_count -= 1

                playsound.playsound("sounds/BobaQuote.mp3", False)

                # update the number of credits boba needs
                boba_details.config(text="Boba Fett will retrieve a random Sith that has already been called (" + str(sith_credits) + " Credits)")

            else:
                playsound.playsound("sounds/OutLeague.mp3", False)

    elif not boba_check_if_active:
        playsound.playsound("sounds/OutLeague.mp3", False)


def call_bounty_greedo(event):
    global credits_count

    if credits_count >= 50:
        playsound.playsound("sounds/Maclunky.mp3", False)
        credits_count -= 50
        credits_label.config(text="Credits: " + str(credits_count))


def call_bounty_bossk(event):
    global credits_count
    global song_count
    global skip_song
    global regular_song

    if credits_count >= 70:
        skip_song = True
        skip_check()
        credits_count -= 70
        credits_label.config(text="Credits: " + str(credits_count))


def time_count():
    global time_counter
    global minute
    global count

    # calculate the time
    if count < max_number_of_questions:
        label_timer.place(x=925, y=1035)
        if time_counter < 60:
            if time_counter < 10:
                label_timer.configure(text=str(minute) + ":0" + str(time_counter), font=("Courier", 25))
                time_counter += 1
            elif time_counter >= 10:
                label_timer.configure(text=str(minute) + ":" + str(time_counter), font=("Courier", 25))
                time_counter += 1
        elif time_counter == 60:
            minute += 1
            time_counter = 0
            label_timer.configure(text=str(minute) + ":0" + str(time_counter), font=("Courier", 25))
            time_counter += 1
        root.after(1000, time_count)


def check_answer_a():
    global count
    global credits_count
    global sith_check

    # make sure cannot use phone sith when answered
    sith_check = False

    statement, correct, correct_sound = check_if_correct(count, "a")
    store_answer("a")
    count += 1
    button_a.place_forget()
    button_b.place_forget()
    button_c.place_forget()
    button_d.place_forget()

    # play sound if correct or not
    playsound.playsound(os.path.join(script_dir, correct_sound), False)
    if statement == "That is correct":
        answer_a.config(bg="green")
        correct_label.config(text="That is correct")
        correct_label.place(x=808, y=900)
        credits_count += 10
        credits_label.config(text="Credits: " + str(credits_count))
    elif statement == "That is incorrect":
        answer_a.config(bg="red")
        correct_label.config(text="That is incorrect")
        correct_label.place(x=790, y=900)
        if correct == "b":
            answer_b.config(bg="green")
        elif correct == "c":
            answer_c.config(bg="green")
        elif correct == "d":
            answer_d.config(bg="green")

    if count == max_number_of_questions:
        next_button.config(text="Finish Quiz!")
    next_button.place(x=850, y=950)


def check_answer_b():
    global count
    global credits_count
    global sith_check

    # make sure cannot use phone sith when answered
    sith_check = False

    statement, correct, correct_sound = check_if_correct(count, "b")
    store_answer("b")
    count += 1
    button_a.place_forget()
    button_b.place_forget()
    button_c.place_forget()
    button_d.place_forget()

    # play sound if correct or not
    playsound.playsound(os.path.join(script_dir, correct_sound), False)
    if statement == "That is correct":
        answer_b.config(bg="green")
        correct_label.config(text="That is correct")
        correct_label.place(x=808, y=900)
        credits_count += 10
        credits_label.config(text="Credits: " + str(credits_count))
    elif statement == "That is incorrect":
        answer_b.config(bg="red")
        correct_label.config(text="That is incorrect")
        correct_label.place(x=790, y=900)
        if correct == "a":
            answer_a.config(bg="green")
        elif correct == "c":
            answer_c.config(bg="green")
        elif correct == "d":
            answer_d.config(bg="green")
    if count == max_number_of_questions:
        next_button.config(text="Finish Quiz!")
    next_button.place(x=850, y=950)


def check_answer_c():
    global count
    global credits_count
    global sith_check

    # make sure cannot use phone sith when answered
    sith_check = False

    statement, correct, correct_sound = check_if_correct(count, "c")
    store_answer("c")
    count += 1
    button_a.place_forget()
    button_b.place_forget()
    button_c.place_forget()
    button_d.place_forget()

    # play sound if correct or not
    playsound.playsound(os.path.join(script_dir, correct_sound), False)
    if statement == "That is correct":
        answer_c.config(bg="green")
        correct_label.config(text="That is correct")
        correct_label.place(x=808, y=900)
        credits_count += 10
        credits_label.config(text="Credits: " + str(credits_count))
    elif statement == "That is incorrect":
        answer_c.config(bg="red")
        correct_label.config(text="That is incorrect")
        correct_label.place(x=790, y=900)
        if correct == "a":
            answer_a.config(bg="green")
        elif correct == "b":
            answer_b.config(bg="green")
        elif correct == "d":
            answer_d.config(bg="green")
    if count == max_number_of_questions:
        next_button.config(text="Finish Quiz!")
    next_button.place(x=850, y=950)


def check_answer_d():
    global count
    global credits_count
    global sith_check

    # make sure cannot use phone sith when answered
    sith_check = False

    statement, correct, correct_sound = check_if_correct(count, "d")
    store_answer("d")
    count += 1
    button_a.place_forget()
    button_b.place_forget()
    button_c.place_forget()
    button_d.place_forget()

    # play sound if correct or not
    playsound.playsound(os.path.join(script_dir, correct_sound), False)
    if statement == "That is correct":
        answer_d.config(bg="green")
        correct_label.config(text="That is correct")
        correct_label.place(x=808, y=900)
        credits_count += 10
        credits_label.config(text="Credits: " + str(credits_count))
    elif statement == "That is incorrect":
        answer_d.config(bg="red")
        correct_label.config(text="That is incorrect")
        correct_label.place(x=790, y=900)
        if correct == "a":
            answer_a.config(bg="green")
        elif correct == "b":
            answer_b.config(bg="green")
        elif correct == "c":
            answer_c.config(bg="green")
    if count == max_number_of_questions:
        next_button.config(text="Finish Quiz!")
    next_button.place(x=850, y=950)


def display_rank(number):
    global main_logo
    global max_number_of_questions

    rank, description, image = get_rank(number)
    title.config(text="You got " + str(number) + " out of " + str(max_number_of_questions) + " correct")
    question.config(text="Your rank: " + rank)
    main_logo = PhotoImage(file=image)
    label_main.config(image=main_logo)
    Label(root, text=description, bg="black", fg="white", font=("Courier", 25), wraplength=1000).pack()
    Button(root, text="Goodbye!", command=root.destroy, bg="orange", font=("Courier", 9, "bold"), width=30, height=3).place(x=850, y=900)


def next_question():
    global count
    global main_logo
    global label_main
    global lando_counter
    global palpatine_count
    global main_picture
    global max_number_of_questions
    global pack_check
    global sith_check
    global run
    global boba_check_if_active

    # hide the next button and correct label as well as the sith answers
    next_button.place_forget()
    correct_label.place_forget()
    dooku_answer.place_forget()
    vader_answer.place_forget()
    maul_answer.place_forget()

    if count == 0:
        # play fun begins sound clip
        playsound.playsound("sounds/FunBegins.mp3", False)

        # start the timer
        time_count()

        # destroy the start button
        button_main.destroy()

        # place lando face
        dont_click.place(x=1800, y=995)
        label_lando.place(x=1860, y=1020)

        # place phone a friend images
        label_luke.place(x=40, y=60)
        label_leia.place(x=150, y=60)
        label_han.place(x=260, y=60)
        phone_friend.place(x=0, y=0)

        # pay a bounty
        bounty_title.place(x=1331, y=0)
        greedo_label.place(x=1550, y=60)
        bossk_label.place(x=1660, y=60)
        boba_label.place(x=1770, y=60)
        credits_label.place(x=1300, y=60)
        greedo_details.place(x=1535, y=250)
        bossk_details.place(x=1523, y=280)
        boba_details.place(x=1555, y=325)

        # song title
        song_title_label.place(x=0, y=900)
        current_song.place(x=0, y=945)
        moving_song()

    if count < max_number_of_questions:
        # change the picture and which question you are on
        main_picture = get_image(count)
        main_logo = PhotoImage(file=main_picture)
        label_main.config(image=main_logo)
        title.config(text="Question " + str(count + 1) + "/" + str(max_number_of_questions), fg="yellow", relief=RIDGE, bd=10)

        # get next question
        question.config(text=get_question(count), font=("Courier", 25, "bold"), fg="yellow")

        # make sure sith check is ready
        sith_check = True

        # see if it is a true or false question
        if get_true_or_false(count) == "True":

            answer_a.config(text="a) " + get_a_answers(count), bg="black")
            # update the true or false answers
            answer_b.config(text="b) " + get_b_answers(count), bg="black")

            # just have two buttons and two answers
            button_a.place(x=860, y=900)
            button_b.place(x=1060, y=900)
            button_c.place_forget()
            button_d.place_forget()
            answer_c.pack_forget()
            answer_d.pack_forget()

            # makes sure that the next question will have the answers again
            pack_check = True

        else:
            if pack_check:
                answer_c.pack()
                answer_d.pack()
                pack_check = False
            # update the answers
            answer_a.config(text="a) " + get_a_answers(count), bg="black")
            answer_b.config(text="b) " + get_b_answers(count), bg="black")
            answer_c.config(text="c) " + get_c_answers(count), bg="black")
            answer_d.config(text="d) " + get_d_answers(count), bg="black")

            # buttons to press
            button_a.place(x=760, y=900)
            button_b.place(x=860, y=900)
            button_c.place(x=1060, y=900)
            button_d.place(x=1160, y=900)

        # gets rid of palpatine after clicked and displays phone a sith function
        if palpatine_count == 1:
            # palpatine_count += 1
            label_palpatine.place_forget()
            phone_friend.place(x=0, y=0)
            phone_friend.config(text="Would you like to phone a sith?")

            vader_label.place(x=40, y=60)
            dooku_label.place(x=150, y=60)
            maul_label.place(x=260, y=60)

            vader_details.place(x=0, y=200)
            dooku_details.place(x=0, y=230)
            maul_details.place(x=0, y=260)

            boba_details.config(text="Boba Fett will retrieve a random Sith that has already been called (" + str(sith_credits) + " Credits)")
            boba_details.place(x=1515, y=325)
            boba_check_if_active = True



    if count == max_number_of_questions:
        # stop the main song and purge the playlist
        winsound.PlaySound(None, winsound.SND_PURGE)
        root.after_cancel(run)
        root.after_cancel(song_animation)

        # get number of answers correct
        number_correct = compare_answers()

        # destroy/hide widgets
        # buttons
        button_a.destroy()
        button_b.destroy()
        button_c.destroy()
        button_d.destroy()

        # answer options
        answer_a.destroy()
        answer_b.destroy()
        answer_c.destroy()
        answer_d.destroy()

        # "phone a friend"
        label_luke.place_forget()
        label_leia.place_forget()
        label_han.place_forget()
        label_palpatine.place_forget()
        phone_friend.place_forget()

        # phone a sith
        vader_label.place_forget()
        vader_label_gray.place_forget()
        dooku_label.place_forget()
        dooku_label_gray.place_forget()
        maul_label.place_forget()
        maul_label_gray.place_forget()
        vader_details.place_forget()
        maul_details.place_forget()
        dooku_details.place_forget()

        # pay a bounty
        greedo_label.place_forget()
        bossk_label.place_forget()
        boba_label.place_forget()
        bounty_title.place_forget()
        greedo_details.place_forget()
        bossk_details.place_forget()
        boba_details.place_forget()

        # credits
        credits_label.place_forget()

        # current song
        current_song.place_forget()
        song_title_label.place_forget()

        # hide that stupid lando face
        label_lando.place_forget()

        # call display rank function
        display_rank(number_correct)

        # display final time
        Label(root, text="Final Time:", bg="black", fg="white", font="Times").place(x=920, y=780)
        label_timer.place(x=913, y=800)

        # display times lando has been clicked
        dont_click.place_forget()
        if lando_counter > 0:
            Label(root, text="Times Lando has been clicked: " + str(lando_counter), bg="black", fg="white").place(x=1740, y=1060)

        # play ending song
        time.sleep(0.5)
        if number_correct / max_number_of_questions < 0.10:
            playsound.playsound("sounds/Darth Vader Noooo.mp3", False)
        elif 0.80 <= number_correct / max_number_of_questions < 0.90:
            playsound.playsound("sounds/Power.mp3", False)
        elif number_correct == max_number_of_questions:
            playsound.playsound("sounds/ForceBeWithYou.mp3", False)
        playsound.playsound("sounds/EndSong.wav", False)


# create the window
root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.attributes('-fullscreen', True)
root.config(background="black")
root.title("Star Wars Quiz Show")

# initialize the main file path
script_dir = os.path.dirname(__file__)

# set the maximum number of questions
max_number_of_questions = 40

main_picture = os.path.join(script_dir, "images/main_logo1.png")

# initialize the count
count = 0

# initialize sound variable
sound = "null"

# title
title = Label(root, text="Welcome to the Star Wars Quiz Show!", bg="black", fg="white")
title.config(font=("Courier", 44), fg="yellow")
title.pack()

# create the logo
main_logo = PhotoImage(file=main_picture)
label_main = Label(root, image=main_logo, bg="blue")
label_main.pack(pady=6)

# button to start the quiz
button_main = Button(root, text="Start the Quiz!", font=("Courier", 15, "bold"), command=next_question, bg="black", fg="yellow", cursor="hand2")
button_main.pack(pady=40)
button_main.config(height=10, width=30)

# question to ask
question = Label(root, bg="black", fg="white", font=("Courier", 24), wraplength=1000)
question.pack()

# create the answers
answer_a = Label(root, bg="black", fg="white", font=("Courier", 24), wraplength=1000)
answer_a.pack()
answer_b = Label(root, bg="black", fg="white", font=("Courier", 24), wraplength=1000)
answer_b.pack()
answer_c = Label(root, bg="black", fg="white", font=("Courier", 24), wraplength=1000)
answer_c.pack()
answer_d = Label(root, bg="black", fg="white", font=("Courier", 24), wraplength=1000)
answer_d.pack()

pack_check = False

# create the answer buttons
button_a = Button(root, text="a", command=check_answer_a, width=1, height=1, font=("Courier", 25, "bold"), bg="black", fg="red", cursor="hand2")
button_b = Button(root, text="b", command=check_answer_b, width=1, height=1, font=("Courier", 25, "bold"), bg="black", fg="green", cursor="hand2")
button_c = Button(root, text="c", command=check_answer_c, width=1, height=1, font=("Courier", 25, "bold"), bg="black", fg="yellow", cursor="hand2")
button_d = Button(root, text="d", command=check_answer_d, width=1, height=1, font=("Courier", 25, "bold"), bg="black", fg="blue", cursor="hand2")

# create the next button and display if correct or not
next_button = Button(root, text="Next Question", command=next_question, width=30, height=3, bg="purple")
correct_label = Label(root, font=("Courier", 25), bg="black", fg="white")

# exit button
Button(root, text="E X I T", command=root.destroy, bg="black", fg="red", font="bold", cursor="hand2").place(x=5, y=1045)

# the lando face
lando_picture = os.path.join(script_dir, "images/landoface.png")
lando_face = PhotoImage(file=lando_picture)
label_lando = Label(root, image=lando_face, bg="pink", cursor="hand2")
label_lando.bind("<Button-1>", lando_clip)
dont_click = Label(root, text="Please don't click me", bg="black", fg="white")
lando_counter = 0

# add a timer
time_counter = 0
minute = 0
label_timer = Label(root, text=time_counter, fg="white", bg="black")

# add call a friend images
# luke
luke_picture = os.path.join(script_dir, "images/Luke.png")
luke_image = PhotoImage(file=luke_picture)
label_luke = Label(root, image=luke_image, bg="white", cursor="hand2")
label_luke.bind("<Button-1>", call_a_friend_clip)

# leia
leia_picture = os.path.join(script_dir, "images/Leia.png")
leia_image = PhotoImage(file=leia_picture)
label_leia = Label(root, image=leia_image, bg="white", cursor="hand2")
label_leia.bind("<Button-1>", call_a_friend_clip)

# han
han_picture = os.path.join(script_dir, "images/Han.png")
han_image = PhotoImage(file=han_picture)
label_han = Label(root, image=han_image, bg="white", cursor="hand2")
label_han.bind("<Button-1>", call_a_friend_clip)

# phone a friend label
phone_friend = Label(root, text="Would you like to phone a friend?", bg="black", fg="white", font=("Courier", 18))

# palpatine image
palpatine_picture = os.path.join(script_dir, "images/Palpatine.png")
palpatine_image = PhotoImage(file=palpatine_picture)
label_palpatine = Label(root, image=palpatine_image)
palpatine_count = 0

# phone a sith images
vader_image = PhotoImage(file="images/DarthVader.png")
dooku_image = PhotoImage(file="images/Dooku.png")
maul_image = PhotoImage(file="images/DarthMaul.png")
vader_label = Label(root, image=vader_image, cursor="hand2")
dooku_label = Label(root, image=dooku_image, cursor="hand2")
maul_label = Label(root, image=maul_image, cursor="hand2")
dooku_label.bind("<Button-1>", phone_a_sith_dooku)
vader_label.bind("<Button-1>", phone_a_sith_vader)
maul_label.bind("<Button-1>", phone_a_sith_maul)

# phone a sith details
sith_check = False
vader_check = False
dooku_check = False
maul_check = False
vader_details = Label(root, text="Vader will always give an incorrect answer", bg="black", fg="red", font="Courier")
dooku_details = Label(root, text="Dooku will always give the correct answer", bg="black", fg="green", font="Courier")
maul_details = Label(root, text="Maul will always give the correct answer 70% of the time", bg="black", fg="orange", font="Courier", wraplength=450)

# phone a sith grayed out images
vader_image_gray = PhotoImage(file="images/DarthVaderGray.png")
dooku_image_gray = PhotoImage(file="images/DookuGray.png")
maul_image_gray = PhotoImage(file="images/DarthMaulGray.png")
vader_label_gray = Label(root, image=vader_image_gray)
dooku_label_gray = Label(root, image=dooku_image_gray)
maul_label_gray = Label(root, image=maul_image_gray)

# sith answers
dooku_answer = Label(root, "", bg="black", fg="white", font="Courier", wraplength=400)
vader_answer = Label(root, "", bg="black", fg="white", font="Courier")
maul_answer = Label(root, "", bg="black", fg="white", font="Courier")

# pay off a bounty hunter
bounty_title = Label(root, text="Would you like to pay off a bounty hunter?", bg="black", fg="white", font=("Courier", 18))

# bounty hunter images
# bossk
skip_song = False
run = None
bossk_image = PhotoImage(file="images/Bossk.png")
bossk_label = Label(root, image=bossk_image, cursor="hand2")
bossk_details = Label(root, text="Bossk will change the music to the next track. (70 Credits)", bg="black", fg="white", font="Courier", wraplength=400)
bossk_label.bind("<Button 1>", call_bounty_bossk)

# greedo
greedo_image = PhotoImage(file="images/Greedo.png")
greedo_label = Label(root, image=greedo_image, cursor="hand2")
greedo_label.bind("<Button-1>", call_bounty_greedo)
greedo_details = Label(root, text="Greedo will go \"Maclunky\" (50 Credits)", bg="black", fg="white", font="Courier")

# boba
sith_credits = 0
boba_count = 0
boba_check_if_active = False
check_if_enough_credits = False
boba_image = PhotoImage(file="images/Boba.png")
boba_label = Label(root, image=boba_image, cursor="hand2")
boba_details = Label(root, text="Boba cannot be used right now . . . ", bg="black", fg="white", font="Courier", wraplength=400)
boba_label.bind("<Button-1>", call_bounty_boba)

# credits
credits_count = 0
credits_label = Label(root, text="Credits: " + str(credits_count), bg="black", fg="white", font="Courier")

# song title
song_color_count = 0
song_title_label = Label(root, text="Current Song: ", bg="black", fg="purple", font=("Courier", 25, "bold"))
current_song = Label(root, text="", bg="black", fg="white", font=("Courier", 25, "italic"))

# play main song (KEEP AT BOTTOM)
song_animation = None
flashing_song_text()
song_count = 0
song_clip()
song_title_move_count = 0

# keep the window running
root.mainloop()

""""
TODO:
"""