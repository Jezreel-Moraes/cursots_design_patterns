from .shopping_order_state import ShoppingOrderState


class OrderApproved(ShoppingOrderState):
   def __init__(self, order) -> None:
      self.name = 'OrderApproved'
      self.order = order
      
   def get_name(self): return self.name
   
   def approve_payment(self): 
      print('Payment has already been approved.')
   
   def reject_payment(self):
      self.order.set_state(OrderRejected(self.order))
   
   def wait_payment(self):
      self.order.set_state(OrderPending(self.order))
   
   def ship_order(self):
      print('Sending the order to the customer...')
      
   
class OrderRejected(ShoppingOrderState):
   def __init__(self, order) -> None:
      self.name = 'OrderRejected'
      self.order = order
      
   def get_name(self): return self.name
   
   def approve_payment(self): 
      print('Payment has been Rejected.')
   
   def reject_payment(self):
      print('Payment has already been Rejected.')
   
   def wait_payment(self): 
      print('Payment has been Rejected.')
   
   def ship_order(self):
      print('Unable to send order with rejected payment!')
      
      
class OrderPending(ShoppingOrderState):
   def __init__(self, order) -> None:
      self.name = 'OrderPending'
      self.order = order
      
   def get_name(self): return self.name
   
   def approve_payment(self):
      self.order.set_state(OrderApproved(self.order))
      
   def reject_payment(self):
      self.order.set_state(OrderRejected(self.order))

   def wait_payment(self):
      print('Payment has already pending.')
   
   def ship_order(self):
      print('Unable to send order with pending payment!')