import configparser

config = configparser.ConfigParser()    # config = {}

config['Default'] = {
    'name' = 'liulili',
    'age' = 34
}

with open('config.ini', 'w') as f:
    config.write(f)

