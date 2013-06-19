# coding: utf-8
play = True

while play:
    print 'Hi, Palomi!  I made you a program. Press enter to start!'
    raw_input()

    adj = raw_input('Enter an adjective: ')
    verb_ed  = raw_input('Enter a verb ending in ed: ')
    p_noun = raw_input('Enter a plural noun: ')
    liq = raw_input('Enter a liquid: ')
    p_noun2 = raw_input('Enter a plural noun: ')
    famous  = raw_input('Enter the name of a famous person: ')
    place = raw_input('Enter the name of a place: ')
    occupation = raw_input('Enter an occupation: ')
    noun = raw_input('Enter a noun: ')
    nationality = raw_input('Enter a nationality: ')
    fem_celeb = raw_input('Enter a female celebrity: ')
    noun2 = raw_input('Enter a noun: ')
    fem_friend = raw_input('Enter the name of a female friend: ')
    p_noun3 = raw_input('Enter a plural noun: ')
    number = raw_input('Enter a number: ')
    adj2 = raw_input('Enter an adjective: ')

    string = "I enjoy long, %s walks on the beach, getting %s in the rain and serendipitous \
    encounters with %s. I really like pina coladas mixed with %s, and romantic, \
    candle-lit %s. I am well-read from Dr. Seuss to %s. I travel frequently, \
    especially to %s, when I am not busy with work. (I am a %s.) I am looking for %s \
    and beauty in the form of a %s goddess. She should have the physique of %s and the\
     %s of %s. I would prefer if she knew how to cook, clean, and wash my %s. I know \
     I’m not very attractive in my picture, but it was taken %s days ago, and I have \
     since become more %s."

    print string % (adj,verb_ed,p_noun,liq,p_noun2,famous,place,occupation,noun,
                    nationality,fem_celeb,noun2,fem_friend,p_noun3,number,adj2)

    y_or_n = raw_input('\n Want to play again? (y/n) : ')
    if y_or_n == "n":
        play = False