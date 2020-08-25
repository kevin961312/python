emails = ('a@example.com','b@example.com')
message = {
    'subject': ' You Have Email',
    'message': "Here's some mail for you!"
}
template ="""
From: <{0[0]}>
To: <{0[1]}>
Subject: {message[subject]}
{message[message]}
"""
print(template.format(emails, message= message))


emails = ("a@example.com", "b@example.com")
message = {
    'emails': emails,
    'subject': "You Have Mail!",
    'message': "Here's some mail for you!"
}
template = """
From: <{0[emails][0]}>
To: <{0[emails][1]}>
Subject: {0[subject]}
{0[message]}"""
print(template.format(message))