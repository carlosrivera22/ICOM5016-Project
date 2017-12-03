class UserData:
    users = [
        {
            'user_id':1,
            'first_name':'Fernando',
            'last_name':'mercado',
            'email':'fmercado@email.com',
            'phone':'7870001111',
            'password':'pwd',
        },
        {
            'user_id':2,
            'first_name':'',
            'last_name':'',
            'email':'',
            'phone':'',
            'password':'',
        },
        {
            'user_id':3,
            'first_name':'',
            'last_name':'',
            'email':'',
            'phone':'',
            'password':'',
        }
    ]

    def getAllUsers(self):
        return self.users

    def getUserById(self,sid):
        for s in self.users:
            if s['user_id'] == sid:
                return s
        return 'No user found'
