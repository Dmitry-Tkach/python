# Importing a module: the guard in simple_message.py stops it printing on import.
import simple_message as msg

# the import printed nothing; now call the function on purpose
print("Module imported, now calling its function:")
msg.simple_message()
