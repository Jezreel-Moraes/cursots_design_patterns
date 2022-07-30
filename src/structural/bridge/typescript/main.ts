import { Radio, TV } from './classes/Devices';
import { RemoteControl } from './classes/RemoteControl';
import { RemoteControlWithVolume } from './classes/RemoteControlWithVolume';

const testDevice = (control: RemoteControl | RemoteControlWithVolume) => {
  console.log('Device name: ', control.deviceName);
  console.log('Device volume:', control.deviceVolume);
  console.log('Device powerStatus: ', control.devicePower);
  control.togglePower();
  console.log('Device powerStatus: ', control.devicePower);

  if (!(control instanceof RemoteControlWithVolume)) return;

  console.log('Device volume:', control.deviceVolume);
  control.volumeUp();
  console.log('Device volume:', control.deviceVolume);
  control.volumeDown();
  console.log('Device volume:', control.deviceVolume);
};

const main = () => {
  const radio = new Radio();
  const tv = new TV();

  const remoteControl = new RemoteControl(radio);
  const remoteControlWithVolume = new RemoteControlWithVolume(tv);

  testDevice(remoteControl);
  console.log();
  testDevice(remoteControlWithVolume);
};

main();
