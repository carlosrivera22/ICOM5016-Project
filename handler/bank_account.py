from flask import jsonify
from dao.bank_account import BankAccountDAO


class BankAccountHandler:

    def build__bank_account_dict(self, row):
        result = {}
        result['bank_account_id'] = row[0]
        result['supplier_id'] = row[1]
        result['bank_account_no'] = row[2]
        result['bank_account_type'] = row[3]
        result['amount'] = row[4]

        return result

    def build_supplier_dict(self, row):
        result = {}
        result['supplier_id'] = row[0]
        result['user_id'] = row[1]
        result['address_id'] = row[2]
        result['company_name'] = row[3]
        return result

    def build_part_attributes(self, bank_account_id, supplier_id, bank_account_no, bank_account_type, amount, ):
        result = {}
        result['bank_account_id'] = bank_account_id
        result['supplier_id'] = supplier_id
        result['bank_account_no'] = bank_account_no
        result['bank_account_type'] = bank_account_type
        result['amount'] = amount

        return result

    def getAllBankAccounts(self):
        dao = BankAccountDAO()
        bank_accounts_list = dao.getAllBankAccount()
        result_list = []
        for row in bank_accounts_list:
            result = self.build__bank_account_dict(row)
            result_list.append(result)
        return jsonify(BankAccounts=result_list)

    def getBankAccountById(self, bank_account_id):
        dao = BankAccountDAO()
        row = dao.getBankAccountById(bank_account_id)
        if not row:
            return jsonify(Error="Bank Account Not Found"), 404
        else:
            bank_account = self.build__bank_account_dict(row)
            return jsonify(BankAccount=bank_account)

    def searchBankAccounts(self, args):
        bank_account_no = args.get("bank_account_no")
        bank_account_type = args.get("bank_account_type")
        amount = args.get("amount")
        dao = BankAccountDAO()
        bank_accounts_list = []

        if(len(args) == 1) and bank_account_no:
            bank_accounts_list = dao.getBankAccountByBankAccountNo(bank_account_no)
        elif (len(args) == 1) and bank_account_type:
            bank_accounts_list = dao.getBankAccountByAccountType(bank_account_type)
        elif (len(args) == 1) and amount:
            bank_accounts_list = dao.getBankAccountByAmount(amount)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []

        for row in bank_accounts_list:
            result = self.build__bank_account_dict(row)
            result_list.append(result)
        return jsonify(Bankaccounts=result_list)

    def getSuppliersByBankAccountId(self, bank_account_id):
        dao = BankAccountDAO()
        if not dao.getBankAccountById(bank_account_id):
            return jsonify(Error="Bank Account Not Found"), 404
        suppliers_list = dao.getSupplierByBankAccountId(bank_account_id)
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Supplier=result_list)
