# Original code causing TypeError:
wrong_type = 'abc' + 123

# Fixed code:
wrong_type = 'abc' + str(123)  # or 'abc' + '123'
