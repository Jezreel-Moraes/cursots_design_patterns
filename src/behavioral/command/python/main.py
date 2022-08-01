from classes.light_intensity_command import LightIntensityCommand
from classes.light_power_command import LightPowerCommand
from classes.smart_house_app import SmartHouseApp
from classes.smart_house_light import SmartHouseLight

main_home_light = SmartHouseLight('Main Home Light')
bedroom_light = SmartHouseLight('Bedroom Light')

main_home_light_power_command = LightPowerCommand(main_home_light)
main_home_light_intensity_command = LightIntensityCommand(main_home_light)
bedroom_light_power_command = LightPowerCommand(bedroom_light)

smart_house_app = SmartHouseApp()

smart_house_app.add_command('MH_power', main_home_light_power_command)
smart_house_app.add_command('MH_intensity', main_home_light_intensity_command)
smart_house_app.add_command('BR_power', main_home_light_power_command)

smart_house_app.execute_command('MH_power')
smart_house_app.undo_command('MH_power')

smart_house_app.execute_command('BR_power')
smart_house_app.undo_command('BR_power')

for _ in range(5):
    smart_house_app.execute_command('MH_intensity')
for _ in range(3):
    smart_house_app.undo_command('MH_intensity')
