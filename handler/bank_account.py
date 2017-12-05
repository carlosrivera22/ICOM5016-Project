from flask import jsonify
from data.bank_account import BankAccountData

class BankAccountHandler:

    def getAllBankAccount(self):
        bankAccount = BankAccountData()
        return jsonify(bankAccount.getAllBankAccount())

    def getBankAccountById(self, bank_account_id):
        bankAccount = BankAccountData()
        result = bankAccount.getBankAccountByID()
        return jsonify(result)

    def getBankAccountByAccountNo(self, bank_account_no):
        bankAccount = BankAccountData()
        result = bankAccount.getBankAccountByAccountNo(self, bank_account_no)
        return jsonify(result)

    def getBankAccountByAccountType(self, bank_account_type):
        bankAccount = BankAccountData()
        result = bankAccount.getBankAccountByAccountType(self, bank_account_type)
        return jsonify(result)

    def getBankAccountByAmount(self, amount):
        bankAccount = BankAccountData()
        result = bankAccount.getBankAccountByAmount(self, amount)
        return jsonify(result)

    def getBankAccountBySupplierId(self, supplier_id):
        bankAccount = BankAccountData()
        result = bankAccount.getBankAccountBySupplierId(supplier_id)
        return jsonify(result)

    def getBankAccountByBankAccountTypeAndSupplierId(self, bank_account_type, supplier_id):
        bankAccount = BankAccountData()
        result = bankAccount.getBankAccountByAccountTypeAndSupplierID(bank_account_type, supplier_id)
        return jsonify(result)


    def searchBankAccount(self, args):
        bank_account_id = args.get('bank_account_id')
        bank_account_no = args.get('bank_account_no')
        bank_account_type = args.get('bank_account_type')
        amount = args.get('amount')
        supplier_id = args.get('supplier_id')

        if len(args) == 1 and bank_account_id:
            if bank_account_id:
                return self.getBankAccountById(int(bank_account_id))
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and bank_account_no:
            if bank_account_no:
                return self.getBankAccountByAccountNo(int(bank_account_no))
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and bank_account_type:
            if bank_account_type:
                return self.getBankAccountByAccountType(bank_account_type)
            else:
                return jsonify(Error="Malformed search string."), 400

        elif len(args) == 1 and amount:
            if amount:
                return self.getBankAccountByAmount(int(amount))
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and supplier_id:
            if supplier_id:
                return self.getBankAccountBySupplierId(int(supplier_id))
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 2 and bank_account_type and supplier_id:
                return self.getBankAccountByBankAccountTypeAndSupplierId(bank_account_type, supplier_id)
        else:
            return jsonify(Error="Malformed search string"), 400

