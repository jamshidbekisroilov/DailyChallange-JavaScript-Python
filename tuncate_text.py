def truncate_text(text):
    if len(text) > 20:
        return text[0:17] + '...'
    return text
#Demo test
print(truncate_text("This string should get truncated."))
