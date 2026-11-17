try:
    x = 10;
    if x > 5:
        raise Exception(f"x should not be greater than {x}");
except Exception as e:
    print(f"an error occurred: {e}");

finally:
    print("This block will always execute, regardless of whether an exception occurred or not.");