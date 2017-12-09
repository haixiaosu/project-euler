nums = {
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
    '10':'ten',
    '11':'eleven',
    '12':'twelve',
    '13':'thirteen',
    '14':'fourteen',
    '15':'fifteen',
    '16':'sixteen',
    '17':'seventeen',
    '18':'eighteen',
    '19':'nineteen',
    '20':'twenty',
    '30':'thirty',
    '40':'forty',
    '50':'fifty',
    '60':'sixty',
    '70':'seventy',
    '80':'eighty',
    '90':'ninety'
}

total_string = ""
for i in range(1, 1000):
    #print i
    str_i = str(i)
    length = len(str_i)
    if str_i in nums:
        total_string += nums[str_i]
    elif length == 2:
        str_tens = nums[str(i - int(str_i[1]))]
        total_string += str_tens + nums[str_i[1]]
        nums[str_i] = str_tens + nums[str_i[1]]
    elif length == 3:
        if i % 100 == 0:
            total_string += nums[str_i[0]] + "hundred"
        else:
            last_two = nums[str(int(str_i[1:]))]
            first = nums[str_i[0]] + "hundredand"
            total_string += first + last_two

total_string += "onethousand"
print(total_string)
print(len(total_string))
