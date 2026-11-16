
def NLP(list2,common=0):
    '''NLP Counts unique words in a string and optionally displays the most frequently occurring words.'''
    list2=list2.lower() 
    mylist=list2.split()
    #common_num=[]
    unique_words=[]
    for i in mylist:
        if i not in unique_words:    ##to avoid counting duplicates, if the word is not in the unique list we add it. it it exists list, we skip it
            unique_words.append(i)
    unique=len(unique_words)       #len of the list is the number of unique words with no repetition 

    if common!=0:    #common!=0 ex common ==3: display 3 words with the highest count
        for j in range(common):
            highest = 0
            most_common = ""
            for i in mylist:
                if mylist.count(i) > highest:
                    highest = mylist.count(i)
                    most_common = i
            print("Most common word:\"", most_common,"\" appeared:", highest, "times")
            while most_common in mylist:
                mylist.remove(most_common)
    return print("there is:",unique,"unique word") 

print('1st test')
NLP("It was many and many a year ago In a kingdom by the sea That a maiden there lived whom you may know By the name of Annabel Lee And this maiden she lived with no other thought Than to love and be loved by me",2)

print('2nd test')
NLP("I was a child and she was a child. In this kingdom by the sea. But we loved with a love that was more than love. I and my Annabel Lee. With a love that the winged seraphs of Heaven. Coveted her and me")

print('3rd test')
NLP('''And this was the reason that long ago
In this kingdom by the sea
A wind blew out of a cloud chilling
My beautiful Annabel Lee
So that her highborn kinsmen came
And bore her away from me
To shut her up in a sepulchre
In this kingdom by the sea''')

print('4th test')
NLP('''The angels not half so happy in Heaven
Went envying her and me
Yes that was the reason as all men know
In this kingdom by the sea
That the wind came out of the cloud by night
Chilling and killing my Annabel Lee''')

print("5th test")
NLP('''But our love it was stronger by far than the love
Of those who were older than we
Of many far wiser than we
And neither the angels in Heaven above
Nor the demons down under the sea
Can ever dissever my soul from the soul
Of the beautiful Annabel Lee''')
print('6th test')
NLP('''For the moon never beams without bringing me dreams
Of the beautiful Annabel Lee
And the stars never rise but I feel the bright eyes
Of the beautiful Annabel Lee
And so all the night-tide I lie down by the side
Of my darling my darling my life and my bride
In her sepulchre there by the sea
In her tomb by the sounding sea''')

##########whole Poem###########
print("whole poem: ")
NLP('''It was many and many a year ago
In a kingdom by the sea
That a maiden there lived whom you may know
By the name of Annabel Lee
And this maiden she lived with no other thought
Than to love and be loved by me

I was a child and she was a child
In this kingdom by the sea
But we loved with a love that was more than love
I and my Annabel Lee
With a love that the winged seraphs of Heaven
Coveted her and me

And this was the reason that long ago
In this kingdom by the sea
A wind blew out of a cloud chilling
My beautiful Annabel Lee
So that her highborn kinsmen came
And bore her away from me
To shut her up in a sepulchre
In this kingdom by the sea

The angels not half so happy in Heaven
Went envying her and me
Yes that was the reason as all men know
In this kingdom by the sea
That the wind came out of the cloud by night
Chilling and killing my Annabel Lee

But our love it was stronger by far than the love
Of those who were older than we
Of many far wiser than we
And neither the angels in Heaven above
Nor the demons down under the sea
Can ever dissever my soul from the soul
Of the beautiful Annabel Lee

For the moon never beams without bringing me dreams
Of the beautiful Annabel Lee
And the stars never rise but I feel the bright eyes
Of the beautiful Annabel Lee
And so all the night-tide I lie down by the side
Of my darling my darling my life and my bride
In her sepulchre there by the sea
In her tomb by the sounding sea''')