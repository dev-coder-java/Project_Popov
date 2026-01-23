def party_guests(guest_list):
    if len(guest_list) == 0:
        return 'Никто не пришёл на вечеринку.'
    elif len(guest_list) == 1:
        return f'На вечеринке {guest_list[0]}'
    elif len(guest_list) == 2:
        return f'{guest_list[0]} и {guest_list[1]} пришли на вечеринку.'
    else:
        first_two = ', '.join(guest_list[:2])
        others_count = len(guest_list) - 2
        return f'{first_two} и ещё {others_count} других пришли на вечеринку.'

n = [input()]
print(party_guests(n))
print(party_guests([]))
print(party_guests(['Иван']))
print(party_guests(['Иван', 'Марина']))
print(party_guests(['Иван', 'Марина', 'Сергей']))