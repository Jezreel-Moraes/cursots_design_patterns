from classes.factories.customer_vehicle_factory import CustomerVehicleFactory
from classes.factories.enterprise_vehicle_factory import \
    EnterpriseVehicleFactory

customer_factory = CustomerVehicleFactory()
customer = customer_factory.create_user('João', 'Joinville')
customer_vehicle = customer_factory.create_vehicle('Volvo')

print(customer)
customer_vehicle.pick_up(customer.get_name())
print(customer_vehicle)

print()

enterprise_factory = EnterpriseVehicleFactory()
enterprise = enterprise_factory.create_user('Jonas', 'Cubatão')
enterprise_vehicle = enterprise_factory.create_vehicle('Vasco')

print(enterprise)
enterprise_vehicle.pick_up(enterprise.get_name())
print(enterprise_vehicle)
