
def global_variables(request):
    """
      The context processor must return a dictionary.
    """
    return {
        'domain_name': 'SuperCasa',
        'domain': "https://supercasa.tornode.org",
    }
