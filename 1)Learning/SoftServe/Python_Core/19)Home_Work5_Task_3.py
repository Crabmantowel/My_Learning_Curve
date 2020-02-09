def filter_words(st):
    return ' '.join(st.capitalize().split())


loud_words = 'ThEre MusT be SomeThinG Wrong, ITs      OkaY  tHoUgh!'
#print(loud_words.capitalize())
print(filter_words(loud_words))
