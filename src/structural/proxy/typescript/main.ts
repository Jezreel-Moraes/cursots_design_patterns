import { AdminUser } from './classes/AdminUser';
import { UserProxy } from './classes/UserProxy';

const withProxyAsCache = async () => {
  const user = new UserProxy('John', 'Doe');
  console.log('That`s gonna  take 2 seconds:');
  console.log(await user.getAddresses(), '\n');

  console.log('This`s gonna repeat 5 times:');
  for (let index = 0; index < 5; index++)
    console.log(await user.getAddresses());
};

const withoutProxy = async () => {
  const user = new AdminUser('John', 'Doe');
  console.log('That`s gonna  take 2 seconds:');
  console.log(await user.getAddresses(), '\n');

  console.log('This`s gonna repeat 5 times:');
  for (let index = 0; index < 5; index++)
    console.log(await user.getAddresses());
};

const main = async () => {
  console.log('With proxy as cache:\n');
  await withProxyAsCache();
  console.log('\nWithout proxy:\n');
  await withoutProxy();
};

main();
