from delivery import DeliveryFactory, deliveryContext

factory = DeliveryFactory()
deliveryContext(factory, 'John', '12345', 'Main Street', 'New York')
deliveryContext(factory, 'Ana', '145', 'Main Street', 'New York')
deliveryContext(factory, 'Jez', '1565', 'Street', 'Russia')
print()

print(factory.get_locations())