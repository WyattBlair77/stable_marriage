class Woman():
    def __init__(self, name, pref=[]):
        # preference list, from most attractive to least
        self.pref = pref
        self.name = name
        self.suitors = []
        self.stable = False
        self.rej_count_prior = 0
        self.rej_count = 0

    def __str__(self):
        return self.name

    def print_suitors(self):
        print(self.name + "'s suitor: ", end='')
        for suitor in self.suitors:
            print(suitor.name, end='')
        print()

    def receive(self, man):
        self.suitors.append(man)

    def remove_suitor(self, suitor):
        while self.suitors.count(suitor):
            self.suitors.remove(suitor)

    def evaluate(self):

        reject_count = 0

        if len(self.suitors) != 0:
            first_choice = self.suitors[0]
            for suitor in self.suitors:

                if self.pref.index(suitor) < self.pref.index(first_choice):

                    first_choice.reject(self)
                    reject_count += 1
                    self.remove_suitor(first_choice)

                    first_choice = suitor

                elif self.pref.index(suitor) == self.pref.index(first_choice):

                    first_choice = suitor

                else:

                    suitor.reject(self)
                    reject_count += 1
                    self.remove_suitor(suitor)

        if len(self.suitors) > 1:
            self.suitors = [self.suitors[0]]

        if reject_count == 0:
            self.stable = True
        else:
            self.stable = False
            self.rej_count_prior = self.rej_count
            self.rej_count += reject_count

        self.print_suitors()

    def update_pref(self, pref):
        self.pref = pref



