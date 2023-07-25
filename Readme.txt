Data folder:
    config.py  - The main url
    test_data.py - test data which will be needed 

Lib folder:
    custom_logger.py - Customing the logger, so that it can be used to log messages
    general_lib.py - Main functions, that will be needed 

Page folder:
    favorite_page.py: Getting 'Please Login' form, using corresponding locators and functions
    main_page.py: Opening the main page and choosing the choosing the language 
    search_page.py: Getting the prices, using corresponding locators and functions

Tests folder:
    test_favorite.py: Testing whether the 'Please Login' form is opened or not
    test_prices.py: Testing whether prices are within a selected range or not

    conftest.py: The pytest fixtures(driver,logger) that will be needed


