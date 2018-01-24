from flask import jsonify
from dao.credit_card import CreditCardData
from dao.user import UserDAO
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

    def build_card_attributes(self,credit_card_id,victim_id,credit_card_number,name_on_card,exp_date,cvs):
        result = {}
        result['credit_card_id'] = credit_card_id
        result['victim_id'] = victim_id
        result['credit_card_number'] = credit_card_number
        result['name_on_card'] = name_on_card
        result['exp_date'] = exp_date
        result['cvs'] = cvs
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

    #Phase3
    def insertCreditCard(self, form):
        #sacar nombre de la victima basado en su id
        if len(form) != 5:
            return jsonify(Error="Malformed post request"),400
        else:
            victim_id = form['victim_id']
            credit_card_number = form['credit_card_number']
            name_on_card = form['name_on_card']
            exp_date = form['exp_date']
            cvs = form['cvs']
            if victim_id and credit_card_number and name_on_card and exp_date and cvs:
                user_data = UserDAO()
                data = CreditCardData()
                if not user_data.getUserByVictimId(victim_id):
                    return jsonify(Error="Victim Not Found")
                else:
                    credit_card_id = data.insertCreditCard()








    def updateCreditCard(self,credit_card_id,fields):
        dao =  CreditCardData()
        if not dao.getCreditCardById(credit_card_id):
            return jsonify(Error="Credit Card Not Found."),404
        else:
            if len(fields) != 5:
                return jsonify(Error="Malformed update request"),400
            else:
                victim_id = fields['victim_id']
                card_number = fields['credit_card_number']
                name_on_card = fields['name_on_card']
                exp_date = fields['exp_date']
                cvs = fields['cvs']
                if victim_id and card_number and name_on_card and exp_date and cvs:
                    dao.updateCreditCard(credit_card_id,victim_id,card_number,name_on_card,exp_date,cvs)
                    result = self.build_card_attributes(credit_card_id,victim_id,card_number,name_on_card,exp_date,cvs)
                    return jsonify(CreditCard=result),200
                else:
                    return jsonify(Error="Unexpected attributes in update request"),400






