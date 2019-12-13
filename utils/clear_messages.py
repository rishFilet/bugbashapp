import django.contrib.messages as messages


def clear_msgs(request):
    system_messages = messages.get_messages(request)
    for message in system_messages:
        # This iteration is necessary
        pass
    system_messages.used = True
