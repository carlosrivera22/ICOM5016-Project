from flask import jsonify
from data.credit_card import CreditCardData

class CreditCardHandler:

    def getAllCreditCards(self):
        credit_card = CreditCardData()
        return jsonify(credit_card.getAllCreditCart())

    def getCreditCardById(self, credit_card_id):
        credit_card = CreditCardData()
        result = credit_card.getCreditCardById(credit_card_id)
        return jsonify(result)

    def getCreditCardByCreditCardNumber(self, credit_card_number):
        credit_card = CreditCardData()
        result = credit_card.getCreditCardByCreditCardNumber(credit_card_number)
        return jsonify(result)

    def getCreditCardByNameOnCard(self, name_on_card):
        credit_card = CreditCardData()
        result = credit_card.getCreditCardByNameOnCard(name_on_card)
        return jsonify(result)

    def getCreditCardByExpDate(self, exp_date):
        credit_card = CreditCardData()
        result = credit_card.getCreditCardByExpDate(exp_date)
        return jsonify(result)

    def getCreditCardByCVS(self, cvs):
        credit_card = CreditCardData()
        result = credit_card.getCreditCardByCVS(cvs)
        return jsonify(result)

    def getCreditCardByVictimId(self, victim_id):
        credit_card = CreditCardData()
        result = credit_card.getCreditCardByVictimId(victim_id)
        return jsonify(result)

    def searchCreditCart(self, args):
        credit_card_id = args.get('credit_card_id')
        credit_card_number = args.get('credit_card_number')
        name_on_card = args.get('name_on_card')
        exp_date = args.get('exp_date')
        cvs = args.get('cvs')
        victim_id = args.get('victim_id')

        if len(args) == 1 and credit_card_id:
            if credit_card_id:
                return self.getCreditCardById(int(credit_card_id))
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and credit_card_number:
            if credit_card_number:
                return self.getCreditCardByCreditCardNumber(credit_card_number)
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and name_on_card:
            if name_on_card:
                return self.getCreditCardByNameOnCard(name_on_card)
            else:
                return jsonify(Error="Malformed search string."), 400

        elif len(args) == 1 and exp_date:
            if exp_date:
                return self.getCreditCardByExpDate(exp_date)
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and cvs:
            if cvs:
                return self.getCreditCardByCVS(cvs)
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and victim_id:
            if victim_id:
                return self.getCreditCardByVictimId(victim_id)
            else:
                return jsonify(Error="Malformed search string."), 400
        else:
            return jsonify(Error="Malformed search string"), 400

