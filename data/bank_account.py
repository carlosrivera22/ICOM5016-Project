class BankAccountData:
    bankAccount = [

        {
            'bank_account_id': 1,
            'bank_account_no': 100000001,
            'bank_account_type': 'checking',
            'amount': 500.50,
            'supplier_id': 1
        },

        {
            'bank_account_id': 2,
            'bank_account_no': 100000002,
            'bank_account_type': 'saving',
            'amount': 5200.23,
            'supplier_id': 2
        },

        {
            'bank_account_id': 3,
            'bank_account_no': 100000003,
            'bank_account_type': 'checking',
            'amount': 90.32,
            'supplier_id': 3
        },

        {
            'bank_account_id': 4,
            'bank_account_no': 100000004,
            'bank_account_type': 'checking',
            'amount': 5839.49,
            'supplier_id': 1
        },

        {
            'bank_account_id': 5,
            'bank_account_no': 100000005,
            'bank_account_type': 'saving',
            'amount': 32983.23,
            'supplier_id': 2
        },

        {
            'bank_account_id': 6,
            'bank_account_no': 100000006,
            'bank_account_type': 'checking',
            'amount': 3872.67,
            'supplier_id': 3
        },

        {
            'bank_account_id': 7,
            'bank_account_no': 100000007,
            'bank_account_type': 'saving',
            'amount': 9348.57,
            'supplier_id': 1
        },

        {
            'bank_account_id': 8,
            'bank_account_no': 100000008,
            'bank_account_type': 'checking',
            'amount': 464.32,
            'supplier_id': 2
        },


    ]

    def getAllBankAccount(self):
        return self.bankAccount

    def getBankAccountByID(self, bank_account_id):
        for b in self.bankAccount:
            if b['bank_account_id'] == bank_account_id:
                return b
        return 'No Bank Account Found'

    def getBankAccountByAccountNo(self, bank_account_no):
        for b in self.bankAccount:
            if b['bank_account_no'] == bank_account_no:
                return b
        return 'No Bank Account Found'

    def getBankAccountByAccountType(self, bank_account_type):
        for b in self.bankAccount:
            if b['bank_account_type'] == bank_account_type:
                return b
        return 'No Bank Account Found'

    def getBankAccountByAmount(self, amount):
        for b in self.bankAccount:
            if b['amount'] == amount:
                return b
        return 'No Bank Account Found'

    def getBankAccountBySupplierId(self, supplier_id):
        results = []
        for b in self.bankAccount:
            if b['supplier_id'] == supplier_id:
                results.append(b)
        return results

    def getBankAccountByAccountTypeAndSupplierID(self, bank_account_type, supplier_id):
        for b in self.bankAccount:
            if b['bank_account_type'] == bank_account_type and b['supplier_id'] == supplier_id:
                return b
        return 'No Bank Account found'