def mad_lid():
  try:
    adj1:str=input('Enter an Adjective: ').lower()
    adj2:str=input('Enter another Adjective: ').lower()
    adj3:str=input('Enter another Adjective: ').lower()
    verb1:str=input('Enter a verb: ').lower()
    verb2:str=input('Enter another Verb: ').lower()
    verb3:str=input('Enter another Verb: ').lower()
    noun1:str=input('Enter a noun: ').lower()
    noun2:str=input('Enter another noun: ').lower()
    noun3:str=input('Enter another noun: ').lower()
    madlid=f"""The {adj1} {noun1} {verb1} to the {noun2}, where his {adj2} {noun3}
    {verb2} and {verb3} near a bench, while a {adj3} {noun3} reads a book quietly."""
    print(madlid)
  except Exception as e:
    print(f'Ooo you got a {e}')
if __name__=='__main__':
     mad_lid()