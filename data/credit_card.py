class CreditCardData:

    credit_cart = [

        {
            'credit_card_id': 1,
            'credit_card_number': '4359 4839 3849 3499',
            'name_on_card': 'Mikael Del Valle',
            'exp_date': '17/12/2022',
            'cvs': 123,
            'victim_id': 1
        },

        {
            'credit_card_id': 2,
            'credit_card_number': '4543 4534 1356 9829',
            'name_on_card': 'Edgardo Rivera',
            'exp_date': '12/04/2025',
            'cvs': 456,
            'victim_id': 2
        },

        {
            'credit_card_id': 3,
            'credit_card_number': '4935 3829 5543 5422',
            'name_on_card': 'Carlos Geronimo',
            'exp_date': '14/08/2021',
            'cvs': 789,
            'victim_id': 3
        },

        {
            'credit_card_id': 4,
            'credit_card_number': '4359 4839 3849 3499',
            'name_on_card': 'Mikael Del Valle',
            'exp_date': '14/08/2021',
            'cvs': 456,
            'victim_id': 1
        },

    ]

    def getAllCreditCart(self):
        return self.credit_cart

    def getCreditCardById(self, credit_card_id):
        for c in self.credit_cart:
            if c['credit_card_id'] == credit_card_id:
                return c
        return 'No Credit Card Found'

    def getCreditCardByCreditCardNumber(self, credit_card_number):
        for c in self.credit_cart:
            if c['credit_card_number'] == credit_card_number:
                return c
        return 'No Credit Card Found'

    def getCreditCardByCreditCardNumber(self, credit_card_number):
        for c in self.credit_cart:
            if c['credit_card_number'] == credit_card_number:
                return c
        return 'No Credit Card Found'

    def getCreditCardByNameOnCard(self, name_on_card):
        results = []
        for c in self.credit_cart:
            if c['name_on_card'] == name_on_card:
                results.append(c)
        return results

    def getCreditCardByExpDate(self, exp_date):
        results = []
        for c in self.credit_cart:
            if c['exp_date'] == exp_date:
                results.append(c)
        return results

    def getCreditCardByCVS(self, cvs):
        results = []
        for c in self.credit_cart:
            if c['cvs'] == cvs:
                results.append(c)
        return results

    def getCreditCardByVictimId(self, victim_id):
        results = []
        for c in self.credit_cart:
            if c['victim_id'] == victim_id:
                results.append(c)
        return results
