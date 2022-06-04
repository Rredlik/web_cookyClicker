BOOST_TYPE_NAME_TO_NUMBER = {
    'casual': 0,
    'auto': 1,
}

BOOST_TYPE_CHOICES = {
    (BOOST_TYPE_NAME_TO_NUMBER['casual'], 'casual'),
    (BOOST_TYPE_NAME_TO_NUMBER['auto'], 'auto'),
}

BOOST_TYPE_VALUES = {
    BOOST_TYPE_NAME_TO_NUMBER['casual']: {
        'click_power_scale': 1,
        'auto_click_power_scale': 0,
        'price_scale': 5,

    },
    BOOST_TYPE_NAME_TO_NUMBER['auto']: {
        'click_power_scale': 0,
        'auto_click_power_scale': 1,
        'price_scale': 25,
    },
}

CASUAL_BOOST_TYPE_VALUES = {
    1: {
        'need_level': 2,
        'base_click_power': 1,
        'base_price': 13,
        'price_scale': 1.35,
    },
    2: {
        'need_level': 3,
        'base_click_power': 8,
        'base_price': 100,
        'price_scale': 1.7,
    },
    3: {
        'need_level': 4,
        'click_power_scale': 50,
        'base_price': 11000,
        'price_scale': 1.25,
    },
    4: {
        'need_level': 5,
        'click_power_scale': 300,
        'base_price': 10,
        'price_scale': 1.3,
    },
    5: {
        'need_level': 6,
        'click_power_scale': 1500,
        'base_price': 1300000,
        'price_scale': 1.3,
    },
    6: {
        'click_power_scale': 32,
        'base_price': 10,
    },
    7: {
        'click_power_scale': 32,
        'base_price': 10,
    },
    8: {
        'click_power_scale': 32,
        'base_price': 10,
    },
    9: {
        'click_power_scale': 32,
        'base_price': 10,
    },
    10: {
        'click_power_scale': 32,
        'base_price': 10,
    },
}