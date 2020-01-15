from Man import Man
from Woman import Woman

Adam = Man(name='1')
Bob = Man(name='2')
Carl = Man(name='3')
Dan = Man(name='4')

Abby = Woman(name='A', pref=[Bob, Carl, Dan, Adam])
Bette = Woman(name='B', pref=[Carl, Dan, Adam, Bob])
Carol = Woman(name='C', pref=[Dan, Adam, Bob, Carl])
Daisy = Woman(name='D', pref=[Adam, Bob, Carl, Dan])

Adam.update_pref([Abby, Bette, Carol, Daisy])
Bob.update_pref(([Bette, Carol, Abby, Daisy]))
Carl.update_pref([Carol, Abby, Bette, Daisy])
Dan.update_pref(([Abby, Bette, Carol, Daisy]))

men = [Adam, Bob, Carl, Dan]
women = [Abby, Bette, Carol, Daisy]

count = 0
stable = False

while count < 16 and not stable:
    print('-------------\n\nDay ', count+1, ": \n\n")
    print('Proposals: ')
    for man in men:
        man.propose()
    print()
    print('Evaluations: ')
    for woman in women:
        woman.evaluate()
        print('Rejects:', woman.rej_count_prior)
        print('- - - -')
    print()
    print('Preference lists: ')
    for man in men:
        print(man.name+': ', end='')
        for woman in man.pref:
            print(woman.name + ", ", end='')
        print()
    print()

    stability = []
    for woman in women:
        stability.append(woman.stable)
    if False not in stability:
        stable = True

    count += 1