const OBJECT = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
    'key4': 'value4'
};

const value = 'value2';

const key = Object.keys(OBJECT)[Object.values(OBJECT).indexOf(value)];

window.console.log(key);