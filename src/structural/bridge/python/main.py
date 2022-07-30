from classes.devices.radio import Radio
from classes.devices.tv import TV
from classes.remote_controls.remote_control import RemoteControl
from classes.remote_controls.remote_control_with_volume import \
    RemoteControlWithVolume


def test_device(remote_control: RemoteControl | RemoteControlWithVolume):
    print(remote_control.device.get_name())

    print(remote_control.device.get_power())
    remote_control.toggle_power()
    print(remote_control.device.get_power())

    if not isinstance(remote_control, RemoteControlWithVolume):
        return

    print(remote_control.device.get_volume())
    remote_control.volume_up()
    print(remote_control.device.get_volume())
    remote_control.volume_down()
    print(remote_control.device.get_volume())


def main():
    tv = TV()
    radio = Radio()

    remote_control = RemoteControl(tv)
    remote_control_with_volume = RemoteControlWithVolume(radio)

    test_device(remote_control)
    print()
    test_device(remote_control_with_volume)


if __name__ == '__main__':
    main()
