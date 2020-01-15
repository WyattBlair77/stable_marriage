class Man():
    def __init__(self, name, pref=[]):
        # preference list, from most attractive to least
        self.pref = pref
        self.name = name

    def __str__(self):
        return self.name

    def propose(self):
        print(self.name + ': proposes to', self.pref[0].name)
        self.pref[0].receive(self)

    def reject(self, woman):
        print(woman.name + ': rejects', self.name)
        self.pref.remove(woman)

    def update_pref(self, pref):
        self.pref = pref



