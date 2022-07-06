# start on line 34 teb
"""
def word_to_int(string):
    answer = ""
    wordlist = string.split(" ")
    print(wordlist)
    for word in wordlist:
        print(word)
        if word == "one" or word == "ten":
            answer += "1"
        elif word == "two" or word == "twenty":
            answer += "2"
        elif word == "three" or word == "thirty":
            answer += "3"
        elif word == "four" or word == "fourty":
            answer += "4"
        elif word == "five" or word == "fifty":
            answer += "5"
        elif word == "six" or word == "sixty":
            answer += "6"
        elif word == "seven" or word == "seventy":
            answer += "7"
        elif word == "eight" or word == "eighty":
            answer += "8"
        elif word == "nine" or word == "ninety":
            answer += "9"
        else:
            pass
    print(answer)

# word_to_int("six hundred and thirty two")
"""
#################################################################################################
def int_to_word(number):
    numberdict = {
        "1" : "one",
        "2" : ["two", "twenty"],
        "3" : ["three" "thirty"],
        "4" : ["four", "fourty"],
        "5" : ["five", "fifty"],
        "6" : ["six", "sixty"],
        "7" : ["seven", "seventy"],
        "8" : ["eight", "eighty"],
        "9" : ["nine", "ninety"],
        "0" : ""
    }
    specialtens = {
        "10" : "ten",
        "11" : "eleven",
        "12" : "twelve",
        "13" : "thirteen",
        "14" : "fourteen",
        "15" : "fifteen",
        "16" : "sixteen",
        "17" : "seventeen",
        "18" : "eighteen",
        "19" : "nineteen",
    }
    numbersyntax = ["millions", "hundred_thousands", "ten_thousands", "thousands", "hundreds", "tens", "ones"]
    stringify = str(number)
    answerlist = []
    for i, num in enumerate(stringify):
        for index, x in enumerate(numbersyntax[-len(stringify):]):
            if i == index:
                if (x == "ones" or x == "thousands" or x == "millions") and stringify[i-1:(i+1)] not in specialtens:
                    if num != "0":
                        answerlist.append(f'{numberdict[num][0]}')
                        if x == "thousands":
                            answerlist.append("thousand")
                        if x == "millions":
                            answerlist.append("million")
                elif x == "tens" or x == "ten_thousands":
                    # if tens place is 10-19
                    if stringify[i:(i+2)] in specialtens:
                        answerlist.append(f'{specialtens[stringify[i:(i+2)]]}')
                        if x == "ten_thousands":
                            answerlist.append("thousand")
                    # if tens place is anything else
                    else:
                        answerlist.append(f'{numberdict[num][1]}')
                elif x == "hundreds" or x == "hundred_thousands":
                    if num != "0":
                        answerlist.append(f'{numberdict[num][0]}')
                        answerlist.append("hundred")
    while "" in answerlist:
        answerlist.remove("")
    print(f'{number} reads as: {" ".join(answerlist)}')

int_to_word(7022222)


biglist = ["big", "small", "tiny", "yikes"]

print(", ".join(biglist))