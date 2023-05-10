from numericnormalizer import normalizer

if __name__ == "__main__":
    test_cases = [
        (("I have 4 apples and five oranges.", "en"), "I have four (4) apples and five (5) oranges."),
        (("I have -4 apples and -five oranges.", "en"), "I have -four (-4) apples and -five (-5) oranges."),
        (("I have 10 pets", "en"), "I have ten (10) pets"),
        (("I have 11 pets", "en"), "I have 11 pets"),
        (("What are the 6 principles of intercultural adaption?", "en"), "What are the six (6) principles of intercultural adaption?"),
        (("What are the six principles of intercultural adaption?", "en"), "What are the six (6) principles of intercultural adaption?"),
    ]
    num_test_cases = len(test_cases)
    for i, ((input, lang), expected_result) in enumerate(test_cases, start=1):
        print(f"Running test {i}/{num_test_cases}")
        print(f"    input=`{input}`")
        print(f"    lang=`{lang}`")
        print(f"    excepted_result=`{expected_result}`")
        actual_result = normalizer.format_sentence(
            sentence=input,
            lang=lang,
        )
        print(f"    actual_result=`{actual_result}`")
        if expected_result == actual_result:
            print(f"PASS")
        else:
            print(f"FAIL")
