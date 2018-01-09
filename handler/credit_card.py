from flask import jsonify
from dao.credit_card import CreditCardData

class CreditCardHandler:

    def build_creditcard_dict(self,row):
        result = {}
        result['credit_card_id'] = row[0]
        result['victim_id'] = row[1]
        result['credit_card_number'] = row[2]
        result['name_on_card'] = row[3]
        result['exp_date'] = row[4]
        result['cvs'] = row[5]
        return result

    def build_victim_dict(self,row):
        result = {}
        result['user_id'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['email'] = row[3]
        result['phone'] = row[4]
        result['password'] = row[5]
        return result


    #funciona
    def getAllCreditCards(self):
        data = CreditCardData()
        credit_card_list = data.getAllCreditCards()
        result_list = []
        for row in credit_card_list:
            result = self.build_creditcard_dict(row)
            result_list.append(result)
        return jsonify(CreditCards=result_list)

    #funciona
    def getCreditCardById(self, credit_card_id):
        data = CreditCardData()
        row = data.getCreditCardById(credit_card_id)
        if not row:
            return jsonify(Error="Credit Card Not Found")
        else:
            credit_card = self.build_creditcard_dict(row)
        return jsonify(CreditCard=credit_card)

    #funciona
    def getCreditCardByCreditCardNumber(self, credit_card_number):
        data = CreditCardData()
        row = data.getCreditCardByCreditCardNumber(credit_card_number)
        if not row:
            return jsonify(Error="Credit Card Not Found")
        else:
            credit_card = self.build_creditcard_dict(row)
        return jsonify(CreditCard=credit_card)

    #funciona
    def getCreditCardByNameOnCard(self, name_on_card):
        data = CreditCardData()
        credit_card_list = data.getCreditCardByNameOnCard(name_on_card)
        result_list = []
        for row in credit_card_list:
            result = self.build_creditcard_dict(row)
            result_list.append(result)
        return jsonify(CreditCards=result_list)


    #funciona hazlo en el argument search
    def getCreditCardByExpDate(self, exp_date):
        data = CreditCardData()
        credit_card_list = data.getCreditCardByExpDate(exp_date)
        result_list = []
        for row in credit_card_list:
            result = self.build_creditcard_dict(row)
            result_list.append(result)
        return jsonify(CreditCards=result_list)

    #funciona hazlo en el argument search
    def getCreditCardByCVS(self, cvs):
        data = CreditCardData()
        row = data.getCreditCardByCVS(cvs)
        if not row:
            return jsonify(Error="Credit Card Not Found")
        else:
            credit_card = self.build_creditcard_dict(row)
        return jsonify(CreditCard=credit_card)

    #funciona
    def getCreditCardByVictimId(self, victim_id):
        data = CreditCardData()
        credit_card_list = data.getCreditCardByVictimId(victim_id)
        result_list = []
        for row in credit_card_list:
            result = self.build_creditcard_dict(row)
            result_list.append(result)
        return jsonify(CreditCards=result_list)


    #getting the victims that own credit cards

    #funciona
    def getVictimByCreditCardNumber(self,credit_card_number):
        data = CreditCardData()
        if not data.getCreditCardByCreditCardNumber(credit_card_number):
            return jsonify(Error="Credit Card Not Found"), 404
        row = data.getVictimByCreditCardNumber(credit_card_number)
        victim = self.build_victim_dict(row)
        return jsonify(Victim=victim)

    #funciona
    def getVictimByCreditCardId(self,credit_card_id):
        data = CreditCardData()
        if not data.getCreditCardById(credit_card_id):
            return jsonify(Error="Credit Card Not Found"),404
        row = data.getVictimByCreditCardId(credit_card_id)
        victim = self.build_victim_dict(row)
        return jsonify(Victim=victim)

    #funciona
    def getVictimByCreditCardCVS(self,cvs):
        data = CreditCardData()
        row = data.getVictimByCreditCardCVS(cvs)
        if not row:
            return jsonify(Error="Victim not found")
        else:
            victim = self.build_victim_dict(row)
        return jsonify(Victim=victim)

    #funciona
    def getVictimByNameOnCard(self,name_on_card):
        data = CreditCardData()
        row = data.getVictimByNameOnCard(name_on_card)
        if not row:
            return jsonify(Error="Victim not found")
        else:
            victim = self.build_victim_dict(row)
        return jsonify(Victim=victim)

    #funciona
    def getVictimsByCreditCardExpDate(self,exp_date):
        data = CreditCardData()
        if not data.getCreditCardByExpDate(exp_date):
            return jsonify(Error="Credit Card Not Found"),404
        credit_card_list = data.getVictimsByCreditCardExpDate(exp_date)
        result_list = []
        for row in credit_card_list:
            result = self.build_victim_dict(row)
            result_list.append(result)
        return jsonify(Victims=result_list)



