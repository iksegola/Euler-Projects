#Problem 17
#The problem of counting numbers

numbers  = ['one', 'two', 'three', 'four', 'five']


nums_as_dict = {1: 'one',
                2: 'two',
                3:'three',
                4:'four',
                5:'five'

}

length = [len(x) for x in numbers]
summish = sum(length)
print (length, summish)