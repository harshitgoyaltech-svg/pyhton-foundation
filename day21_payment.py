class upi:
    def pay(self):
         print("payment done by upi")

class card:
     def pay(self):
          print("payment done by card")

class cash:
     def pay(self):
          print("payment done by cash")

payments =[upi(),card(),cash()]
for payment in payments:
     payment.pay()
