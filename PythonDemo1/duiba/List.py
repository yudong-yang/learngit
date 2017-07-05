def get_formatted_name(first_name, last_name, middle_name=''):

    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
            full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)



def address(privence, city, county=''):
    if county:
        address = privence + ': ' + city + ': ' + county
    else:
        address = privence + ': ' + city + ' '
    return address.title()


def address_format(privence, city, county=''):
    if county:
        address = {'省份:':privence, '市:':city , '区县:' : county}
    else:
        address = {'省份:':privence, '市:':city}
    return address


formataddr = address_format('河南省', '开封市')
print(formataddr)

formataddr = address('浙江省','杭州市','西湖区')


print(formataddr)


def build_person(first_name, last_name, age=''):

    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)