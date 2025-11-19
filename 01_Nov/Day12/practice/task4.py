#!/usr/bin/env python3
#Task-4

import logging

logging.basicConfig(
        filename="age.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s -%(message)s"
        )

class AgeOutOfRange(Exception):
    pass

def get_user_age():
    try:
        age=int(input("Enter your age:"))
        if not 1 <= age <= 120:
            raise AgeOutOfRange("Age must be between 1 and 20")

        logging.info(f"Valid age entered: {age}")
        return age

    except ValueError:
        logging.error(f"Invalid number entered")

    except AgeOutOfRange as e:
        logging.error(str(e))



age= get_user_age()
print("Age processed:", age)
